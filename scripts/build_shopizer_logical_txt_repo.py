#!/usr/bin/env python3
"""Fix split boundaries for original Shopizer TXT journey.

Source: existing pinned Shopizer ZIP/MASTER_INDEX. Produces ONLY numbered .txt files.
Guarantees byte-exact coverage, no cuts inside protected XML/JSON/Java constructs,
no child starting with a detached closing tag/brace, and no cut mid-expression.
"""
from __future__ import annotations
import sys,io,re,json,csv,time,hashlib,zipfile,collections,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'scripts'
spec=importlib.util.spec_from_file_location('old',WORK/'semantic_support_repo.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
SOURCE=ROOT/'code-journey/Shopizer-Code-Journey.zip'
DEST=ROOT/'code-journey/Shopizer-Code-Journey-Logical-Fixed.zip'

# A protected span (a,b) forbids cuts after each line a..b-1.
def mask_xml(lines):
    s=b''.join(lines).decode('utf-8')
    spans=[]
    # XML tokens, CDATA, XML/HTML comments, processing instructions; protect multiline tags.
    token=re.compile(r'<!--[\s\S]*?-->|<!\[CDATA\[[\s\S]*?\]\]>|<\?[\s\S]*?\?>|</?[\w:.-]+(?:\s+(?:[^>"\']|"[^"]*"|\'[^\']*\')*)?\s*/?>',re.M)
    stack=[]
    for m in token.finditer(s):
        l=s.count('\n',0,m.start())+1;r=s.count('\n',0,m.end())+1
        if r>l:spans.append((l,r,'xml-token'))
        t=m.group()
        if t.startswith(('<!--','<![CDATA[','<?')):continue
        close=re.match(r'</([\w:.-]+)',t)
        opening=re.match(r'<([\w:.-]+)',t)
        if close:
            tag=close[1];which=next((i for i in range(len(stack)-1,-1,-1) if stack[i][0]==tag),None)
            if which is None:continue
            start=stack[which][1];stack=stack[:which]
            # Protect modest complete XML units (nested nodes cannot have their tail in later child).
            # Longer container units can be split BETWEEN complete children instead.
            if r-start+1<=125:spans.append((start,r,'xml-element'))
        elif opening and not t.rstrip().endswith('/>'):
            stack.append((opening[1],l))
    return spans

def mask_braces(lines):
    """Bracket/string/comment aware scan of braces and control blocks."""
    txt=b''.join(lines).decode('utf-8')
    spans=old.comment_spans(lines)
    stack=[];line=1;i=0;state='code';triple=False
    while i<len(txt):
        c=txt[i];n=txt[i+1] if i+1<len(txt) else ''
        if c=='\n':line+=1
        if state=='block':
            if c=='*' and n=='/':state='code';i+=2;continue
        elif state=='lc':
            if c=='\n':state='code'
        elif state in ('str','char','triple'):
            if state=='triple' and txt.startswith('"""',i):state='code';i+=3;continue
            if c=='\\':i+=2;continue
            if state=='str' and c=='"':state='code'
            if state=='char' and c=="'":state='code'
        else:
            if c=='/' and n=='*':state='block';i+=2;continue
            if c=='/' and n=='/':state='lc';i+=2;continue
            if txt.startswith('"""',i):state='triple';i+=3;continue
            if c=='"':state='str'
            elif c=="'":state='char'
            elif c=='{':stack.append((line,i))
            elif c=='}' and stack:
                beg,at=stack.pop();width=line-beg+1
                # Protect complete, modest control/method/interface/anonymous blocks.
                # Do not lock an entire large class that spans thousands of lines.
                prefix=txt[max(0,at-320):at]
                prefix=prefix[prefix.rfind(';')+1:]
                prefix=prefix[prefix.rfind('}')+1:].strip()
                is_class=bool(re.search(r'\b(class|interface|enum|record)\s+\w+',prefix))
                is_control=bool(re.search(r'\b(if|else|for|while|try|catch|finally|switch|synchronized|do)\b',prefix))
                is_method=bool(re.search(r'\([^;]*\)\s*(?:throws\s+[\w\s,.<>]+)?\s*$',prefix))
                threshold=(90 if (is_control or is_method or not is_class) else 55)
                if 2<=width<=threshold:spans.append((beg,line,'java-brace-pair'))
        i+=1
    for m in re.finditer(r'"""[\s\S]*?"""',txt):
        a=txt.count('\n',0,m.start())+1;b=txt.count('\n',0,m.end())+1
        if b>a:spans.append((a,b,'java-text-block'))
    return spans

def mask_json(lines):
    txt=b''.join(lines).decode('utf-8');spans=[];stack=[];line=1;quote=False;esc=False
    for c in txt:
        if c=='\n':line+=1
        if quote:
            if esc:esc=False
            elif c=='\\':esc=True
            elif c=='"':quote=False
            continue
        if c=='"':quote=True
        elif c in '{[':stack.append((c,line))
        elif c in '}]' and stack:
            kind,a=stack.pop()
            if (kind=='{' and c=='}') or (kind=='[' and c==']'):
                if 1<line-a+1<=150:spans.append((a,line,'json-struct'))
    return spans

def shell_spans(lines):
    """Protect complete shell if/fi and case/esac and loop/done groups."""
    spans=[]; stack=[]
    for ix,raw in enumerate(lines,1):
        text=raw.decode('utf-8',errors='replace').strip()
        if not text or text.startswith('#'):continue
        # Shell wrapper scripts use standalone 'if', 'else', 'elif', 'fi' etc.
        if re.match(r'^if\b',text):stack.append(('if',ix))
        elif re.match(r'^case\b',text):stack.append(('case',ix))
        elif re.match(r'^(?:for|while|until)\b',text):stack.append(('loop',ix))
        elif re.match(r'^(fi|esac|done)\b',text):
            target={'fi':'if','esac':'case','done':'loop'}[text.split()[0]]
            match=next((j for j in range(len(stack)-1,-1,-1) if stack[j][0]==target),None)
            if match is not None:
                start=stack[match][1];stack=stack[:match]
                if ix-start+1<=250:spans.append((start,ix,'shell-'+target))
    return spans

def css_rule_spans(lines):
    """Keep CSS declarations enclosed by matching braces, including in FreeMarker HTML."""
    text=b''.join(lines).decode('utf-8');spans=[];stack=[];i=0;line=1;quote=None;comment=False
    while i<len(text):
        c=text[i];n=text[i+1] if i+1<len(text) else ''
        if c=='\n':line+=1
        if comment:
            if c=='*' and n=='/':comment=False;i+=2;continue
        elif quote:
            if c=='\\':i+=2;continue
            if c==quote:quote=None
        elif c=='/' and n=='*':comment=True;i+=2;continue
        elif c in ('"',"'"):quote=c
        elif c=='{':stack.append(line)
        elif c=='}' and stack:
            start=stack.pop()
            if 2<=line-start+1<=200:spans.append((start,line,'css-block'))
        i+=1
    return spans

def spans_for(lines,path):
    ext=Path(path).suffix.lower()
    if ext in ('.xml','.html','.xhtml','.svg','.jsp','.jspx') or path.endswith('pom.xml'):return mask_xml(lines)
    if ext=='.ftl':return mask_xml(lines)+css_rule_spans(lines)
    if ext in ('.java','.js','.ts','.drl','.css','.scss'):return mask_braces(lines)
    if ext in ('.json','.jsonc'):return mask_json(lines)
    if Path(path).name in ('mvnw', 'mvnw.cmd') or ext in ('.sh','.bash','.zsh'):return shell_spans(lines)
    return old.comment_spans(lines) if ext in ('.md','.txt') else []

def forbidden(lines,path):
    n=len(lines);deny=old.banned_cuts(spans_for(lines,path),n)
    ext=Path(path).suffix.lower()
    if ext in ('.java','.js','.ts','.drl'):
        old.prevent_partial_java_statements(lines,deny)
    # Protect multiline shell/config statements/continuation characters.
    if ext in ('.sh','.cmd','.bat','.properties','.yml','.yaml','.sql','.ftl') or Path(path).name in ('mvnw','mvnw.cmd'):
        for j in range(n-1):
            s=lines[j].decode('utf-8').rstrip();tail=lines[j+1].decode('utf-8').lstrip()
            if s.endswith(('\\','^','&&','||','|','->')):deny[j+1]=True
            if ext=='.sql' and s.strip() and not s.rstrip().endswith((';','--','*/')) and not tail.startswith(('--','/*')):deny[j+1]=True
    # Never let the *next* child start with an orphan closing suffix, or continuation marker.
    # Keep a closing suffix with the preceding child, even if it increases child size.
    for j in range(1,n):
        left=lines[j-1].decode('utf-8',errors='replace').strip()
        right=lines[j].decode('utf-8',errors='replace').strip()
        if not right:
            k=j+1
            while k<n and not lines[k].decode('utf-8',errors='replace').strip():k+=1
            if k<n:right=lines[k].decode('utf-8',errors='replace').strip()
            else:continue
        if ext in ('.java','.js','.ts','.drl','.css','.scss'):
            if right.startswith(('}',');',');',';', '.', '->', '&&','||','),', 'catch ', 'finally ', 'else ', 'while (')) or right in (')',']','};'):
                deny[j]=True
            # A control header or method declaration may span lines without any parens open.
            if left.endswith(('{','(',',','.','=',':','->')) or (left.startswith('@') and right.startswith(('public ','private ','protected ','class '))):deny[j]=True
            if left and not left.startswith('//') and not left.endswith((';','{','}',':', '*/', ',')) and not right.startswith(('@','//','/*','*')):
                # An expression ending without a terminating token is not a safe seam.
                if not left.endswith((')',']')):deny[j]=True
        elif ext in ('.xml','.html','.xhtml','.svg','.ftl','.jsp','.jspx') or path.endswith('pom.xml'):
            if right.startswith(('</','/>','-->','<\/')) or left.endswith(('<','<!--')):deny[j]=True
        elif ext in ('.json','.jsonc'):
            if right.startswith(('}',']',',',':')) or left.endswith((':','{','[')):deny[j]=True
    return deny

def choose_blocks(lines,first,last,deny,target=8,cap=140):
    if not first:return [(0,0)]
    if last-first+1<=target:return [(first,last)]
    result=[];pos=first
    while pos<=last:
        if last-pos+1<=target:result.append((pos,last));break
        legal=[k for k in range(pos,min(last,pos+cap)+1) if (k==last or not deny[k])]
        # Avoid one-line 'stub' children when they are not a standalone unit.
        legal=[k for k in legal if k==last or k>=pos+1]
        if legal:
            # Prefer a legal boundary near 8; a longer block is preferable to splitting a statement.
            def score(k):
                a=k-pos+1;end=lines[k-1].decode('utf-8',errors='replace').strip()
                if k<last and last-k<=2:tail_pen=5
                else:tail_pen=0
                suffix= -2 if end.endswith((';','}',']','</dependency>','</parent>','</license>','</licenses>')) else 0
                return (abs(a-target)+(max(0,a-target)*0.5)+tail_pen+suffix,k)
            step=min(legal,key=score)
        else:
            # A single protected unit exceeds cap. Extend until the first safe boundary.
            step=pos+cap-1
            while step<last and deny[step]:step+=1
            step=min(last,step)
        assert step>=pos and (step==last or not deny[step])
        result.append((pos,step));pos=step+1
    assert result[0][0]==first and result[-1][1]==last
    return result

def build():
    begin=time.monotonic()
    with zipfile.ZipFile(SOURCE) as z:
        originals,history=old.load_source(z)
    assert len(originals)==1325,len(originals)
    jobs=[];pre_stats=collections.Counter();denies={};rawlines={};linecovers={}
    for path,raw in originals.items():
        lines=raw.splitlines(keepends=True); n=len(lines); rawlines[path]=lines
        deny=forbidden(lines,path);denies[path]=deny
        old_tasks=history[path]
        if not n:
            parents=[(0,0)]
        else:
            parents=[];pos=1
            for _,e,_,_ in old_tasks:
                if pos>n:break
                k=min(e,n)
                while k<n and deny[k]:k+=1
                if k<pos:continue
                # Prevent tiny leading or trailing fragment when possible.
                if k-pos+1<=2 and k<n and parents:
                    pre_stats['tiny_pieces_merged']+=1;continue
                parents.append((pos,k));pos=k+1
            if pos<=n:parents.append((pos,n))
        if n:
            assert parents[0][0]==1 and parents[-1][1]==n,(path,parents)
            for p in parents:
                if p[1]<n:assert not deny[p[1]],(path,p)
            assert all(parents[i][1]+1==parents[i+1][0] for i in range(len(parents)-1)),path
        for s,e in parents:
            parent_idx=next((v[3] for v in old_tasks if v[0]<=s<=v[1]),old_tasks[0][3])
            jobs.append((parent_idx,s,e,path))
        pre_stats['sources']+=1
    jobs.sort(key=lambda x:(x[0],x[1],x[3]))
    count=collections.Counter();unique=set();byfile=collections.defaultdict(list);split_flags=collections.Counter();exceptions=[];index_rows=[]
    with zipfile.ZipFile(DEST,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as out:
        for tasknum,(_,s,e,path) in enumerate(jobs,1):
            prefix=f'{((tasknum-1)//100)*100+1}-to-{((tasknum-1)//100+1)*100}'
            lines=rawlines[path];deny=denies[path];raw=b''.join(lines[s-1:e]) if s else b''
            title=old.title_of(raw, originals[path],path,s,e,Path(path).stem)
            pfilename=old.shortname(f'{tasknum}.0',title,path,s,e)
            key=f'{prefix}/{pfilename}';assert key.lower() not in unique,key
            unique.add(key.lower());out.writestr(key,raw)
            byfile[path].append((s,e,key));count['parents']+=1
            index_rows.append({'sequence':tasknum,'original_path':path,'source_start':s,'source_end':e,'parent_filename':key,'sha256':hashlib.sha256(raw).hexdigest()})
            if s and e-s+1>8:
                child_parts=choose_blocks(lines,s,e,deny)
                # If indivisible, do not introduce a child identical to the parent.
                if len(child_parts)==1:
                    count['atomic_parents_without_redundant_child']+=1
                    if e-s+1>30:exceptions.append((path,s,e,e-s+1))
                else:
                    chunks=[]
                    for j,(a,b) in enumerate(child_parts,1):
                        assert b==e or not deny[b],(path,a,b)
                        blob=b''.join(lines[a-1:b]);chunks.append(blob)
                        name=old.shortname(f'{tasknum}.{j}',old.title_of(blob,originals[path],path,a,b,title),path,a,b)
                        full=f'{prefix}/{name}';assert full.lower() not in unique,full
                        unique.add(full.lower());out.writestr(full,blob)
                        count['children']+=1
                        ln=b-a+1
                        count['max_child_lines']=max(count['max_child_lines'],ln)
                        if ln>8:count['necessary_children_over_8_lines']+=1
                        text=blob.decode('utf-8',errors='replace').lstrip('\r\n\t ')
                        ext=Path(path).suffix.lower()
                        if j>1 and ((ext in ('.java','.js','.ts','.drl','.css','.scss') and text.startswith(('}',');','else ','catch ','finally ','.'))) or
                            ((ext in ('.xml','.html','.xhtml','.svg','.ftl') or path.endswith('pom.xml')) and text.startswith('</')) or
                            (ext=='.json' and text.startswith(('}',']')))):
                            split_flags['orphan_child_head']+=1
                            if split_flags['orphan_child_head']<=15:print('ORPHAN',path,a,b,repr(text[:80]),flush=True)
                    assert b''.join(chunks)==raw,(path,s,e)
            if tasknum%4000==0:print('generated',tasknum,'parent tasks',count['children'],'child files',flush=True)
    assert not split_flags,split_flags
    with zipfile.ZipFile(DEST) as z:
        entries=z.namelist()
        assert all(x.endswith('.txt') for x in entries)
        assert len(entries)==len(unique)==count['parents']+count['children']
        assert z.testzip() is None
        assert all(len(Path(x).name)<=132 and len(x)<=153 for x in entries)
        total=0
        for p,source in originals.items():
            pieces=sorted(byfile[p]);last=0;parts=[]
            for a,b,name in pieces:
                assert a==last+1 or (a,b)==(0,0),('coverage',p,a,last)
                parts.append(z.read(name));last=b
            assert b''.join(parts)==source,('byte-mismatch',p)
            total+=len(source.splitlines(keepends=True))
        assert total==132076,total
    with (ROOT/'code-journey/MASTER_INDEX.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['sequence','original_path','source_start','source_end','parent_filename','sha256']);w.writeheader();w.writerows(index_rows)
    with (ROOT/'code-journey/BROWSE_INDEX.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['sequence','parent_filename','original_path']);w.writeheader();w.writerows([{k:r[k] for k in ['sequence','parent_filename','original_path']} for r in index_rows])
    print('AUDIT PASS',dict(count),'TXT',len(unique),'sources',len(originals),'lines',total,'size',DEST.stat().st_size,'orphan heads',dict(split_flags),'time',int(time.monotonic()-begin),flush=True)
    print('atomic_large_examples',exceptions[:7])
    audit={'status':'PASS','text_files':len(unique),'parents':count['parents'],'children':count['children'],'exact_source_files':len(originals),'source_lines':total,'necessary_children_over_8_lines':count['necessary_children_over_8_lines'],'max_child_lines':count['max_child_lines'],'atomic_parents_without_redundant_child':count['atomic_parents_without_redundant_child'],'no_detached_child_closers':'PASS','no_protected_construct_cut':'PASS','zip_crc':'PASS','rebuild_byte_for_byte':'PASS','original_tabs_and_newlines':'PRESERVED','only_txt_files':'YES'}
    (ROOT/'code-journey/LOGICAL_AUDIT.json').write_text(json.dumps(audit,indent=2))
if __name__=='__main__':build()
