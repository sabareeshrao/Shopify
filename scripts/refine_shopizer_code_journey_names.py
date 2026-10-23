#!/usr/bin/env python3
"""Regenerate the pedagogical filenames from source-grounded evidence.

Does NOT touch source bytes. Handles a pre-existing journey ZIP and optionally
its extracted GitHub directory; verifies every block and parent-child range.
"""
from __future__ import annotations
import argparse,collections,csv,hashlib,io,json,os,re,tempfile,zipfile
from pathlib import Path

BAD={'declare-or-process','the-next','related-code-path','associated-application-data','for-the-caller','related-runtime-application-settings','corresponding-workflow-or-application-settings','and-its-associated-members','remaining-java-logic','process-the-related-code-path','continue-processing','handle-statement','define-the-next-settings','preserve-original-code-comments'}
KEYWORDS={'true','false','null','this','super','new','return','throw','throws','final','public','private','protected','static','class','interface','enum','if','else','while','for','var','int','long','short','void','string','list','set','map','boolean','object','override','try','catch','extends','implements','import','package','default','abstract','synchronized','instanceof','assert','char','float','double','byte','finally'}

def dash(s):
    s=re.sub(r'([a-z0-9])([A-Z])',r'\1-\2',s)
    s=re.sub(r'([A-Z])([A-Z][a-z])',r'\1-\2',s)
    s=re.sub(r'[^a-zA-Z0-9]+','-',s).strip('-').lower()
    return s

def snip(s,max_words=6):
    return '-'.join(dash(s).split('-')[:max_words])

def significant(s):
    return [x for x in dash(s).split('-') if len(x)>2 and x not in KEYWORDS]

def lex(code):
    return [x.strip() for x in code.splitlines() if x.strip()]

def clean_stmt(s):
    return re.sub(r'\s+', ' ', re.sub(r'//.*$','',s)).strip()

def function_context(full:str, start:int):
    """Find a nearby method/function signature before this code slice.
    Try to avoid mistaking call expressions for declarations."""
    lines=full.splitlines()
    for t in range(min(start,len(lines))-1,max(-1,start-145),-1):
        s=lines[t].strip()
        if s.startswith(('//','*','@','return','throw','if','for','while','switch','catch','new ','.')):continue
        m=re.search(r'\b(?:public|private|protected|static|final|synchronized|default|abstract|void|boolean|int|long|double|float|String|List|Set|Map|Optional|ResponseEntity|[A-Z][A-Za-z0-9_<>?,\[\]]*)\s+(?:<[^>]*>\s*)?(?:[\w<>?,\[\].]+\s+)?([a-zA-Z_$][\w$]*)\s*\(',s)
        if m and m.group(1) not in KEYWORDS and not s.endswith(';'):
            return m.group(1)
    return None

# Java behavior-specific actions, ordered by observable evidence.
def java_action(code:str,full:str,begin:int,path:str):
    plain=lex(code); base=Path(path).stem; base_slug=snip(base,6)
    # Documentation-only blocks carry useful meaning (licence, safety, APIs).
    uncommented=[x for x in plain if not x.startswith(('*','//','/*','*/'))]
    if plain and (not uncommented or (code.lstrip().startswith('/*') and not re.search(r'\b(?:class|interface|enum|public|private|protected)\s+[A-Za-z_]',code))):
        notes=' '.join(x.lstrip('/* ').strip() for x in plain)
        notes=re.sub(r'(?i)copyright|@author|licensed|http[s]?://\S+',' ',notes)
        words=[w for w in significant(notes) if len(w)>3 and w not in {'under','therefore','you','this','that','which','with','from','more','license','terms','conditions'}]
        if 'apache' in notes.lower() or 'license' in notes.lower():
            return f'document-apache-source-license-and-copyright-requirements-for-{base_slug}'
        return f'explain-{snip("-".join(words[:7]) or base,8)}-in-original-{base_slug}-code-comments'
    # Don't misinterpret package & import lines as methods.
    imports=re.findall(r'(?m)^\s*import\s+(?:static\s+)?([\w.]+\*?)\s*;',code)
    package=re.search(r'(?m)^\s*package\s+([\w.]+)\s*;',code)
    if package or (imports and len(imports)>=max(1,len(plain)//2)):
        pkg=snip(package.group(1).replace('.', '-'),11) if package else base_slug
        targets=[p.rstrip('.*') for p in imports]
        if not package:
            return f'import-{snip(targets[0].replace(".","-"),7)}-dependencies'+(f'-plus-{snip(targets[-1].replace(".","-"),7)}' if len(targets)>1 else '')+f'-for-{base_slug}'
        return f'declare-java-package-{pkg}-for-{base_slug}' + (f'-and-import-{snip(targets[0].split(".")[-1])}' if targets else '') +(f'-plus-{snip(targets[-1].split(".")[-1])}' if len(targets)>1 else '')
    clazz=re.search(r'\b(class|interface|enum|record|@interface)\s+([A-Za-z_]\w*)',code)
    if clazz:
        annotations=re.findall(r'(?m)^\s*@([\w.]+)',code)
        return f'declare-{clazz.group(1).strip("@")}--{snip(clazz.group(2))}-with-{snip(annotations[0])}-configuration' if annotations else f'declare-{clazz.group(1).strip("@")}--{snip(clazz.group(2))}-and-establish-its-type-definition'
    # Interfaces and abstract classes declare method contracts ending in ';'.
    # There is no implementation body in these lines, so say 'declare contract',
    # not that the operation has already been implemented.
    signatures=re.findall(r'(?m)^\s*(?:(?:public|protected|private|abstract|static|default)\s+)*(?:[A-Za-z_][\w<>?,.\[\]]*)\s+([a-zA-Z_$][\w$]*)\s*\([^;{}]*?\)\s*(?:throws\s+[\w,.\s]+)?;',code)
    signatures=[x for x in signatures if x not in KEYWORDS]
    if signatures:
        operations=[]
        for meth in signatures[:3]:
            if meth.startswith('get'): operations.append('retrieve-'+snip(meth[3:]))
            elif meth.startswith('set'): operations.append('accept-'+snip(meth[3:])+'-updates')
            elif meth.startswith('list'): operations.append('list-'+snip(meth[4:]))
            elif meth.startswith('find'): operations.append('find-'+snip(meth[4:]))
            elif meth.startswith('is'): operations.append('check-'+snip(meth[2:]))
            else: operations.append(snip(meth))
        return 'declare-'+('-and-'.join(operations))+'-interface-method-contract'+('-for-'+base_slug)
    # Find method/constructor signatures with an opening brace, allowing annotations.
    declaration=re.search(r'(?m)^\s*(?:(?:public|protected|private|static|final|synchronized|default|abstract|native)\s+)*(?:<[^>]+>\s+)?(?:[\w<>?,.\[\]]+\s+)?([A-Za-z_$][\w$]*)\s*\(([^;{}]*?)\)\s*(?:throws\s+[\w,.\s]+)?\s*\{',code)
    if declaration and declaration.group(1) in KEYWORDS: declaration=None
    if declaration:
        # A single original source region sometimes contains several related
        # accessors. Describe the additional methods rather than hiding them.
        all_methods=[m.group(1) for m in re.finditer(r'(?m)^\s*(?:(?:public|protected|private|static|final|synchronized)\s+)*(?:[\w<>?,.\[\]]+\s+)?([A-Za-z_$][\w$]*)\s*\([^;{}]*?\)\s*(?:throws\s+[\w,.\s]+)?\s*\{',code)]
        all_methods=[m for m in all_methods if m not in KEYWORDS]
        if len(all_methods)>1:
            operations=[]
            for meth in all_methods[:3]:
                if meth.startswith('get'):operations.append('return-'+snip(meth[3:]))
                elif meth.startswith('is'):operations.append('check-'+snip(meth[2:]))
                elif meth.startswith('set'):operations.append('update-'+snip(meth[3:]))
                else:operations.append('run-'+snip(meth))
            return '-then-'.join(operations)+'-through-'+base_slug+'-methods'
        m=declaration.group(1); slug=snip(m,7)
        tokens=significant(m)
        if m.startswith('get') and len(m)>3:
            return f'return-current-{snip(m[3:])}-field-value-through-{slug}-getter'
        if m.startswith('is') and len(m)>2:
            return f'report-whether-{snip(m[2:])}-flag-is-enabled-through-{slug}'
        if m.startswith('set') and len(m)>3:
            return f'accept-and-store-new-{snip(m[3:])}-value-through-{slug}-setter'
        if m==base:
            fields=re.findall(r'this\.([\w]+)\s*=',code)
            return f'initialize-{base_slug}-instance'+(f'-and-assign-{snip(fields[0])}-field' if fields else '-using-supplied-constructor-arguments')
        if m.startswith(('find','get','load','read','fetch','search')):
            return f'look-up-{snip("-".join(tokens[1:]) or base)}-and-provide-the-result-from-{slug}'
        if m.startswith(('create','build','make','new','save','add','insert','update','remove','delete')):
            return f'{snip(tokens[0])}-{snip("-".join(tokens[1:]) or base)}-using-{slug}-and-update-related-state'
        if m.startswith(('validate','verify','check','is','has','can','supports','authenticate','authorize')):
            return f'check-{snip("-".join(tokens[1:]) or base)}-conditions-and-control-result-in-{slug}'
        if m.startswith(('calculate','compute','sum','total','price','convert')):
            return f'calculate-{snip("-".join(tokens[1:]) or base)}-and-provide-computed-result-in-{slug}'
        if m in {'main','run','execute','start','init','initialize','configure'}:
            return f'run-{base_slug}-{slug}-entry-point-and-initialize-required-processing'
        # inspect observable body to avoid making unsupported promise
        methods=re.findall(r'(?:\w+\.)+([a-zA-Z_]\w*)\s*\(',code)
        if methods:
            return f'implement-{slug}-by-calling-{snip(methods[0])}' +(f'-and-{snip(methods[1])}' if len(methods)>1 else '-to-process-request')
        if re.search(r'\bthrow\s+new\b',code):return f'implement-{slug}-and-throw-exception-when-validation-fails'
        if re.search(r'\breturn\s+',code):return f'implement-{slug}-and-return-the-evaluated-expression'
        return f'implement-{slug}-method-using-declared-parameters-and-body'
    # Handle meaningful statements that are fragments within larger methods.
    context=function_context(full,begin)
    cx=f'-inside-{snip(context)}' if context else f'-in-{base_slug}'
    eq=re.search(r'\bif\s*\(\s*(!?)([\w.]+)\s*(==|!=|>=|<=|>|<)?\s*(null|true|false|\d+)?',code)
    if eq:
        a=eq.group(2).replace('this.',''); relation=eq.group(3) or ('is-not' if eq.group(1) else 'is');b=eq.group(4)
        cond='-'.join([snip(a),{'==':'equals','!=':'differs-from','>':'exceeds','<':'is-below','>=':'at-least','<=':'at-most'}.get(relation,relation),snip(b) if b else 'set'])
        throw=re.search(r'\bthrow\s+new\s+([A-Za-z_]\w*)',code)
        ret='return-null' if re.search(r'\breturn\s+null\s*;',code) else 'return-a-result' if re.search(r'\breturn\s+',code) else 'continue-the-matching-branch'
        return f'check-whether-{cond}-and-{snip("throw-"+throw.group(1)) if throw else ret}{cx}'
    loops=re.search(r'\bfor\s*\(\s*(?:[\w<>?,\[\]]+\s+)?([a-zA-Z_]\w*)\s*:\s*([\w.]+)',code)
    if loops:return f'iterate-through-{snip(loops.group(2))}-items-as-{snip(loops.group(1))}{cx}'
    if re.search(r'\btry\s*\{',code):
        calls=re.findall(r'\.([A-Za-z_]\w*)\s*\(',code)
        return f'execute-{snip(calls[0]) if calls else "service-operation"}-inside-try-block-and-handle-potential-failures{cx}'
    catch=re.search(r'\bcatch\s*\(\s*([\w.]+)',code)
    if catch:return f'catch-{snip(catch.group(1))}-and-handle-error-or-rethrow-as-required{cx}'
    constructs=re.findall(r'\b([A-Za-z_]\w*)\s*=\s*new\s+([A-Za-z_]\w*)',code)
    if constructs:
        if len(constructs)>1:
            return f'create-{snip(constructs[0][1])}-and-{snip(constructs[1][1])}-objects-and-initialize-their-fields{cx}'
        return f'create-{snip(constructs[0][1])}-instance-for-{snip(constructs[0][0])}-variable{cx}'
    assign=re.findall(r'(?:this\.)?([a-zA-Z_]\w*)\s*=\s*(?![=])\s*([\w.]+)',code)
    if assign:
        fields=[(a,b) for a,b in assign if a not in KEYWORDS]
        if fields:
            a,b=fields[0];return f'assign-{snip(a)}-from-{snip(b)}'+(f'-and-update-{snip(fields[1][0])}' if len(fields)>1 else '')+cx
    setters=re.findall(r'\.\s*(set[A-Z][\w]*)\s*\(',code)
    if setters:return f'populate-{snip(setters[0][3:])}-field'+(f'-and-{snip(setters[1][3:])}-field' if len(setters)>1 else '')+f'-on-target-object{cx}'
    standalone_call=re.search(r'(?m)^\s*([a-zA-Z_]\w*)\s*\(([^;\n]*)\)\s*;',code)
    if standalone_call:
        method=standalone_call.group(1);args=[x.strip() for x in standalone_call.group(2).split(',') if x.strip()]
        return f'call-{snip(method)}-operation'+(f'-with-{snip(args[0])}-argument' if args else '')+cx
    getters=re.findall(r'\.\s*((?:get|find|load|fetch|read|list)[A-Z][\w]*)\s*\(',code)
    if getters:return f'retrieve-{snip(getters[0][3:])}-data'+(f'-then-{snip(getters[1])}' if len(getters)>1 else '')+cx
    call=re.findall(r'\.\s*([A-Za-z_]\w*)\s*\(',code)
    if call:return f'invoke-{snip(call[0])}-operation'+(f'-followed-by-{snip(call[1])}' if len(call)>1 else '')+cx
    ret=re.search(r'\breturn\s+([^;\n]{1,65})',code)
    if ret:return f'return-{snip(ret.group(1),7)}-expression{cx}'
    throws=re.search(r'\bthrow\s+new\s+([A-Za-z_]\w*)',code)
    if throws:return f'raise-{snip(throws.group(1))}-when-processing-cannot-continue{cx}'
    fields=re.findall(r'\b(?:private|protected|public)\s+(?:(?:static|final|volatile|transient)\s+)*([\w<>?,.\[\]]+)\s+([a-zA-Z_]\w*)\s*[;=]',code)
    if fields:
        return f'declare-{snip(fields[0][0])}-typed-{snip(fields[0][1])}-member'+(f'-and-{snip(fields[1][1])}-member' if len(fields)>1 else '')+cx
    annot=re.findall(r'(?m)^\s*@([\w.]+)',code)
    if annot:return f'apply-{snip(annot[0])}-annotation'+(f'-together-with-{snip(annot[1])}' if len(annot)>1 else '')+f'-to-member{cx}'
    candidates=[]
    for s in plain:
        if s in {'}', '{', '};', ';', '*/', '/**','/*','*'} or s.startswith(('*','//','/*')):continue
        toks=[x for x in re.findall(r'[A-Za-z_][\w]{2,}',s) if x.lower() not in KEYWORDS]
        if toks:candidates.extend(toks[:3])
        if len(candidates)>3:break
    if candidates:return f'write-{snip(candidates[0])}-code-expression'+(f'-using-{snip(candidates[1])}' if len(candidates)>1 else '')+cx
    return f'close-{base_slug}-{snip(context) if context else "type"}-block-and-its-nested-scope'

def xml_action(code,path):
    base=snip(Path(path).stem)
    tags=[(m.group(1).split(':')[-1],re.sub(r'\s+',' ',m.group(2)).strip()) for m in re.finditer(r'<\s*([\w:.-]+)(?:\s[^>]*)?>([^<>\n]{1,110})</\1>',code)]
    fields={k: v for k,v in tags}
    if 'artifactId' in fields:
        name=fields['artifactId'];group=fields.get('groupId','')
        return f'declare-maven-{snip(name)}-artifact'+(f'-from-{snip(group)}-group' if group else '')+('-with-dependency-version' if 'version' in fields else '-and-link-its-dependencies')
    if 'module' in fields:return f'include-{snip(fields["module"])}-as-a-maven-build-module-for-shopizer'
    if 'name' in fields and 'value' in fields:return f'configure-{snip(fields["name"])}-entry-with-{snip(fields["value"])}-value-in-{base}'
    if tags:
        (a,b)=tags[0];last=tags[min(2,len(tags)-1)];return f'define-{snip(a)}-{snip(b)}-xml-property'+(f'-and-{snip(last[0])}-setting' if len(tags)>1 else f'-in-{base}')
    open_tags=re.findall(r'<\s*([A-Za-z][\w:.-]*)(?:\s|>|/)',code)
    if open_tags:return f'configure-{snip(open_tags[0])}-xml-element'+(f'-and-{snip(open_tags[-1])}-element' if len(open_tags)>1 else '')+f'-within-{base}'
    closing=re.findall(r'</\s*([\w:.-]+)>',code)
    if closing:return f'close-{snip(closing[0])}-xml-element-in-{base}-configuration'
    return f'declare-{base}-xml-namespace-document-root-and-schema-metadata'

def json_action(code,path,full,start):
    base=snip(Path(path).stem)
    # Detect actual JSON records such as zoneCode/zoneName and countryCode.
    names=re.findall(r'"(?:zoneName|countryName|name|description|code|zoneCode|countryCode|currencyCode)"\s*:\s*"([^"]+)"',code)
    zname=re.findall(r'"zoneName"\s*:\s*"([^"]+)"',code)
    zcode=re.findall(r'"zoneCode"\s*:\s*"([^"]+)"',code)
    if zname:
        return f'register-{len(zname)}-geographic-zones-including-{snip(zname[0],5)}'+(f'-through-{snip(zname[-1],5)}' if len(zname)>1 else '')+f'-using-{base}-reference-data'
    if zcode:return f'provide-zone-code-{snip(zcode[0])}-with-its-name-and-country-reference'
    if names:return f'define-{base}-reference-data-entries-for-{snip(names[0],5)}'+(f'-through-{snip(names[-1],5)}' if len(names)>1 else '')
    pairs=re.findall(r'"([\w.:-]+)"\s*:\s*(?:"([^"\n]{1,75})"|([^\s,}]+))',code)
    if pairs:
        first=pairs[0];last=pairs[-1]
        val=lambda x: snip(x[1] or x[2],5)
        return f'set-json-{snip(first[0])}-to-{val(first)}'+(f'-and-{snip(last[0])}-to-{val(last)}' if len(pairs)>1 else f'-in-{base}')
    if re.search(r'\]\s*\}?\s*$',code):return f'finish-{base}-json-array-and-close-its-record-collection'
    return f'open-{base}-json-record-and-establish-nested-field-containers'

def properties_action(code,path):
    keys=[]
    for x in code.splitlines():
        s=x.strip()
        if not s or s.startswith(('#','!')):continue
        m=re.match(r'([A-Za-z_][\w.:-]*)\s*[:=]',s)
        if m:keys.append(m.group(1))
    base=snip(Path(path).stem)
    if keys:
        return f'set-{snip(keys[0],10)}-property'+(f'-together-with-{snip(keys[-1],10)}-property' if len(keys)>1 else '')+f'-for-{base}-configuration'
    comments=[x.lstrip('#! ') for x in code.splitlines() if x.strip().startswith(('#','!'))]
    if comments:
        subject='-'.join(significant(comments[0])[:6])
        return f'document-{subject or base}-configuration-requirements-in-{base}'
    return f'preserve-{base}-configuration-file-structure-without-changing-values'

def other_action(code,path,full,start):
    ext=Path(path).suffix.lower();base=snip(Path(path).stem);plain=lex(code)
    if ext=='.java':return java_action(code,full,start,path)
    if ext=='.json':return json_action(code,path,full,start)
    if ext in {'.xml','.html','.xhtml','.svg'} or Path(path).name=='pom.xml':return xml_action(code,path)
    if ext=='.properties':return properties_action(code,path)
    if ext in {'.yml','.yaml'}:
        entries=re.findall(r'(?m)^\s*([\w.-]+)\s*:\s*([^#\n]*)',code)
        entries=[(a,b.strip()) for a,b in entries if a not in {'-'}]
        if entries:
            a,b=entries[0];e=entries[-1]
            return f'configure-{snip(a)}'+(f'-as-{snip(b,5)}' if b else '-mapping')+(f'-and-{snip(e[0])}-setting' if len(entries)>1 else '')+f'-in-{base}-yaml'
        return f'define-{base}-yaml-workflow-mapping-or-list-structure'
    if ext=='.ftl':
        variables=re.findall(r'\$\{\s*([\w.]+)',code)
        directives=re.findall(r'<#(if|list|assign|include|macro|else|elseif)',code)
        if variables:return f'render-template-value-from-{snip(variables[0])}'+(f'-and-{snip(variables[-1])}' if len(variables)>1 else '')+f'-in-{base}-freemarker'
        if directives:return f'apply-freemarker-{snip(directives[0])}-directive-to-conditionally-render-{base}-template'
        tags=re.findall(r'<\s*([\w]+)',code)
        if tags:return f'compose-{base}-email-html-content-using-{snip(tags[0])}-elements'
        return f'close-{base}-freemarker-template-block-and-preserve-output-spacing'
    if ext in {'.sql','.drl'}:
        statements=re.findall(r'\b(CREATE|ALTER|INSERT|UPDATE|DROP|DELETE|SELECT|RULE|WHEN|THEN)\s+(\w+)',code,re.I)
        if statements:
            a,b=statements[0];return f'execute-{snip(a)}-operation-for-{snip(b)}-in-{base}-script'
        return f'process-{base}-database-or-business-rule-statement-block'
    if ext in {'.md','.txt'}:
        headings=re.findall(r'(?m)^\s*#+\s+([^\n]{3,90})',code)
        if headings:return f'explain-{snip(headings[0],10)}-in-{base}-project-documentation'
        urls=re.findall(r'https?://[^\s)<>]+',code)
        if urls:return f'document-{base}-setup-and-reference-{snip(urls[0].split("/")[2])}-website'
        tokens=[x for x in plain if x and not x.startswith(('[',']'))]
        if tokens:return f'document-{snip(tokens[0],12)}-in-{base}-instructions'
    if ext in {'.cmd','.sh'} or Path(path).name in {'mvnw','mvnw.cmd'}:
        vars=re.findall(r'\b(?:export\s+|set\s+)?([A-Z][A-Z0-9_]{2,})=',code)
        if vars:return f'configure-{snip(vars[0])}-environment-variable'+(f'-and-{snip(vars[-1])}-value' if len(vars)>1 else '')+f'-in-{base}-startup-script'
        patterns=re.findall(r'\b(?:if|case|while|for|exit|exec|goto|shift|printf|echo|call)\b',code)
        if patterns:return f'evaluate-{snip(patterns[0])}-shell-flow'+(f'-then-{snip(patterns[-1])}-command' if len(patterns)>1 else '')+f'-when-launching-{base}'
        return f'define-shell-command-options-and-arguments-for-{base}-startup'
    # Generic resource file: extract concrete strings so nothing gets a meaningless description.
    keys=re.findall(r'\b([A-Za-z_][A-Za-z0-9_]{3,})\b',code)
    useful=[x for x in keys if x.lower() not in KEYWORDS and not x.lower().startswith(('https','http'))]
    if useful:
        return f'define-{snip(useful[0])}-resource-content'+(f'-with-{snip(useful[-1])}-values' if len(useful)>1 else '')+f'-for-{base}'
    if code.strip():return f'configure-{base}-resource-delimiters-and-declarations'
    return f'preserve-required-empty-{base}-file-content-for-reproducible-source-reconstruction'

def detail(code:bytes,full:bytes,path:str,start:int,end:int,parent_context:str=''):
    try: s=code.decode('utf-8');f=full.decode('utf-8')
    except UnicodeDecodeError:raise ValueError(f'Unexpected non-utf8 source: {path}')
    # Inside a multi-line Java comment, every fragment is documentation, not
    # an executable 'statement'. Distinguish license, warranty, and API docs.
    in_comment=False
    if path.endswith(('.java','.js','.ts')):
        line_prefix='\n'.join(f.splitlines()[:start-1])
        comment_open=line_prefix.rfind('/*')
        comment_close=line_prefix.rfind('*/')
        in_comment=comment_open>=0 and comment_open>comment_close
        # The source can contain an unmatched opener inside a Java string or a
        # mixed section. Executable semicolon-terminated statements win.
        if any(line.strip().endswith(';') and not line.strip().startswith(('//','*','/*')) for line in s.splitlines()):
            in_comment=False
    if in_comment:
        low=s.lower()
        base=snip(Path(path).stem)
        if 'warranty' in low or 'as is' in low:
            text=f'document-license-disclaimer-of-software-warranties-and-liability-for-{base}'
        elif 'apache' in low or 'http://www.apache.org' in low or 'license' in low:
            text=f'document-apache-license-terms-and-official-license-reference-for-{base}'
        elif '@param' in low or '@return' in low or '@throws' in low:
            tags=[x for x in ('param','return','throws') if '@'+x in low]
            text=f'document-{snip("-and-".join(tags))}-contract-for-{base}-method'
        else:
            terms=[w for w in significant(s) if len(w)>3 and w not in {'under','therefore','there','these','their','which','with','from','more','this','that'}]
            text=f'explain-{snip("-".join(terms[:6]) or base,7)}-in-{base}-code-documentation'
    else:
        text=other_action(s,path,f,start)
    text=dash(text)
    if parent_context:
        # If the 8-line child is only punctuation or has no independent explanatory
        # evidence, tie it back to the parent's concrete feature.
        tokens=significant(s)
        is_weak=not tokens or any(w in text for w in ('close-', 'preserve-required-empty-', 'resource-delimiters','configure--'))
        if is_weak:
            text='finish-'+dash(parent_context)[:125]+'-and-close-current-source-block'
    return text

def name_for(seq,title,source,start,end):
    suffix=f'_{Path(source).name}_lines-{start}-to-{end}.txt'
    max_title=234-len(str(seq).encode())-len(suffix.encode())-1
    if max_title<45: raise RuntimeError('Original basename too long for safe filename: '+source)
    title=dash(title)[:max_title].rstrip('-')
    return f'{seq}_{title}{suffix}'

def load_index(z):
    data=z.read('code-journey/MASTER_INDEX.csv').decode('utf-8')
    return list(csv.DictReader(io.StringIO(data)))

def csv_bytes(rows,cols):
    f=io.StringIO(newline='');w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
    return f.getvalue().encode('utf-8')

def generate(zip_src:Path,zip_dest:Path,folder:Path|None=None):
    with zipfile.ZipFile(zip_src) as z:
        old_index=load_index(z)
        assert len(old_index)>1000,'Not the full archive'
        all_parts=collections.defaultdict(list)
        for row in old_index:
            payload=z.read('code-journey/blocks/'+row['filename'])
            assert hashlib.sha256(payload).hexdigest()==row['sha256']
            all_parts[row['source_path']].append((int(row['source_start']),int(row['source_end']),payload))
        sources={}
        for src,parts in all_parts.items():
            parts=sorted(parts)
            assembled=b''.join(x[2] for x in parts)
            lines=assembled.splitlines(keepends=True)
            if assembled:
                expected=1
                for a,b,p in parts:
                    assert a==expected,(src,a,expected)
                    expected=b+1
                assert len(lines)==expected-1
            sources[src]=assembled
        rename={};seen=set();seen_desc=collections.defaultdict(set)
        generic=0;fallback=0;parent_names=[];child_names=[]
        for row in old_index:
            src=row['source_path'];a=int(row['source_start']);b=int(row['source_end']);seq=row['sequence']
            original=z.read('code-journey/blocks/'+row['filename'])
            title=detail(original,sources[src],src,a,b)
            # Genuine identical behavior is a valid repeated subject, but names
            # cannot all say the same thing. Add concrete nearest semantic context.
            if title in seen_desc[src]:
                lines=sources[src].splitlines()
                context=function_context(sources[src].decode('utf-8'),a)
                if context: title=f'{title}-within-{snip(context)}-method'
                if title in seen_desc[src]:
                    vocab=[x for x in re.findall(r'[A-Za-z][A-Za-z0-9_]{3,}',original.decode('utf8')) if x.lower() not in KEYWORDS]
                    if vocab: title=f'{title}-using-{snip(vocab[-1])}'
                if title in seen_desc[src]:
                    title=f'{title}-at-original-line-{a}'
                    fallback+=1
            seen_desc[src].add(title)
            if any(bad in title for bad in BAD):generic+=1
            new=name_for(seq,title,src,a,b)
            if new in seen:raise AssertionError('File collision '+new)
            rename['code-journey/blocks/'+row['filename']]='code-journey/blocks/'+new
            seen.add(new);parent_names.append(new)
            row['filename']=new
            kids=row['children'].split('|') if row['children'] else []
            renamed=[]
            for c in kids:
                m=re.match(r'^(\d+\.\d+)_.*_lines-(\d+)-to-(\d+)\.txt$',c)
                if not m:raise ValueError(c)
                n,ca,cb=m.group(1),int(m.group(2)),int(m.group(3))
                kid_payload=z.read('code-journey/blocks/'+c)
                line_slice=b''.join(sources[src].splitlines(keepends=True)[ca-1:cb])
                assert kid_payload==line_slice,(src,ca,cb,'child source bytes changed')
                title_child=detail(kid_payload,sources[src],src,ca,cb,parent_context=title)
                if any(bad in title_child for bad in BAD):generic+=1
                nc=name_for(n,title_child,src,ca,cb)
                if nc in seen:raise AssertionError('Child file collision '+nc)
                rename['code-journey/blocks/'+c]='code-journey/blocks/'+nc
                seen.add(nc);child_names.append(nc);renamed.append(nc)
            row['children']='|'.join(renamed)
            if renamed:
                assert b''.join(z.read('code-journey/blocks/'+c) for c in kids)==original,(src,'child reconstruction mismatch')
        assert generic==0,(generic,'Generic bad descriptions still present')
        assert len(rename)==len(parent_names)+len(child_names)
        assert sum(int(x['child_count']) for x in old_index)==len(child_names)
        for row in old_index:
            src=row['source_path'];a=int(row['source_start']);b=int(row['source_end']);
            parent=z.read(next(k for k,v in rename.items() if v=='code-journey/blocks/'+row['filename'])) if False else None
            # content hashing was already checked above; each child's byte-slice
            # must still be exactly the source slice. Only filenames are changed.
            if a and b:
                assert b<=len(sources[src].splitlines(keepends=True))
        columns=list(old_index[0])
        audit=json.loads(z.read('code-journey/AUDIT.json'))
        audit.update({'filename_quality_audit':'PASS','old_generic_description_templates_removed':'YES',
                      'generic_description_violations':generic,
                      'original_source_file_names_unchanged':'YES',
                      'filenames_unique':len(seen)==len(rename),
                      'parent_description_unique_within_each_source':'YES',
                      'same_source_description_collisions_resolved_with_line_context':fallback,
                      'filename_description_method':'Source-grounded static lexical and structural analysis; automated explanations may still require review'})
        index_bytes=csv_bytes(old_index,columns)
        audit.pop('zip_bytes',None)  # original archive size is no longer true after renaming
        audit['zip_bytes']='consult archive size: ZIP size changes when descriptive filenames change'
        audit_bytes=(json.dumps(audit,indent=2)+'\n').encode()
        oldreadme=z.read('code-journey/README.md').decode()
        readme=oldreadme.replace('Filenames contain grounded automated descriptors, but those descriptions are heuristics;',
          'Filenames explain code-specific operations, identifiers, keys and values wherever extractable.\nThey are machine-generated and should be reviewed against source;')
        readme+='\n## Filename quality audit\n\nAll generated TXT basenames and sequence identifiers are unique, and the old generic description templates are rejected. Source bytes are never rewritten by renaming.\n'
        replacement={'code-journey/MASTER_INDEX.csv':index_bytes,'code-journey/AUDIT.json':audit_bytes,'code-journey/README.md':readme.encode()}
        zip_dest.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(zip_dest,'w',allowZip64=True) as out:
            for item in z.infolist():
                origin=item.filename;name=rename.get(origin,origin)
                data=replacement.get(origin)
                if data is None:data=z.read(origin)
                out.writestr(name,data,compress_type=item.compress_type,compresslevel=6 if item.compress_type==zipfile.ZIP_DEFLATED else None)
    with zipfile.ZipFile(zip_dest) as z:
        assert z.testzip() is None
        assert len(z.namelist())==len(set(z.namelist()))
        assert len([n for n in z.namelist() if n.startswith('code-journey/blocks/')])==len(rename)
        assert z.read('code-journey/AUDIT.json')==audit_bytes
    if folder:
        bl=folder/'blocks'
        for old,new in rename.items():
            op=folder/old.removeprefix('code-journey/')
            np=folder/new.removeprefix('code-journey/')
            if op!=np:
                if not op.exists():raise FileNotFoundError(op)
                os.rename(op,np)
        for src,content in replacement.items():
            (folder/src.removeprefix('code-journey/')).write_bytes(content)
        if zip_src.resolve()==(folder/'Shopizer-Code-Journey.zip').resolve():
            os.replace(zip_dest,zip_src)
    print(json.dumps({'status':'PASS','parents':len(parent_names),'children':len(child_names),
        'filenames_unique':len(seen)==len(rename),'generic_violations':generic,
        'parent_description_repetitions_per_source':0,
        'duplicate_descriptors_resolved_using_line_context':fallback,
        'archive':str(zip_dest)},indent=2))

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--zip',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--folder',type=Path)
    a=p.parse_args()
    generate(a.zip,a.output,a.folder)
if __name__=='__main__':main()
