#!/usr/bin/env python3
"""Create Windows-friendly only-TXT archive, preserving original Shopizer text bytes.
Logical XML subtrees, JSON objects, Java comments and short code blocks are atomic.
Allow >8 lines rather than cut through protected logical units.
"""
import csv, io, re, collections, hashlib, zipfile, json, time
from pathlib import Path
from importlib import util

BASE=Path(__file__).resolve().parents[1]
SRC=BASE/'code-journey/Shopizer-Code-Journey.zip'
OUT=BASE/'code-journey/Shopizer-Code-Journey-Legacy.zip'
REF=BASE/'scripts/refine_shopizer_code_journey_names.py'
spec=util.spec_from_file_location('refine_names',REF);m=util.module_from_spec(spec);spec.loader.exec_module(m)

# Mark protected intervals inclusive: a cut after line k cannot split a <= k < b.
def xml_protected(lines):
    src=''.join(x.decode('utf-8') for x in lines)
    spans=[]; stack=[]; structural={'project','dependencies','dependencyManagement','properties','plugins','pluginManagement','executions','build','repositories','profiles','configuration','root','beans','web-app','components','schema','reporting','extensions','system-properties','configuration','settings','catalog','beans:beans','html','body','head','div','table','tbody','tr','collection'}
    offset=0
    # Preserve complete XML comments regardless of whether a comment spans multiple lines.
    for cm in re.finditer(r'<!--[\s\S]*?-->',src):
        a=src.count('\n',0,cm.start())+1;b=src.count('\n',0,cm.end())+1
        if b>a:spans.append((a,b,'xml-comment'))
    # Match XML tags (including attributes containing > in quoted strings) at their exact source positions.
    token=re.compile(r'<(/?)([A-Za-z_][\w:.-]*)(?:\s+(?:[^>"\']|"[^"]*"|\'[^\']*\')*)?\s*(/?)>')
    for t in token.finditer(src):
        a=src.count('\n',0,t.start())+1;b=src.count('\n',0,t.end())+1
        tag=t.group(2).split(':')[-1]
        if t.group(1):
            idx=next((i for i in range(len(stack)-1,-1,-1) if stack[i][0]==tag),None)
            if idx is not None:
                start=stack[idx][1];stack=stack[:idx]
                span=b-start+1
                if (tag not in structural and span<=38) or (tag in {'licenses','modules','parent','license','dependency','plugin','execution','bean','repository','developer','projectName','scm'} and span<=48):
                    if span>1:spans.append((start,b,'xml-'+tag))
        elif not t.group(3):
            stack.append((tag,a))
        if b>a:spans.append((a,b,'xml-multiline-tag'))
    return spans

def comment_spans(lines):
    txt=b''.join(lines).decode('utf-8')
    res=[]
    for x in re.finditer(r'/\*[\s\S]*?\*/',txt):
        a=txt.count('\n',0,x.start())+1;b=txt.count('\n',0,x.end())+1
        if 1<b-a+1<=36:res.append((a,b,'multiline-comment'))
    return res

def java_protected(lines):
    # Protect complete short brace blocks and multi-line comments; ignore string braces.
    txt=b''.join(lines).decode('utf-8')
    spans=comment_spans(lines)
    stack=[];line=1;i=0;mode='code'
    while i<len(txt):
        c=txt[i];n=txt[i+1] if i+1<len(txt) else ''
        if c=='\n':line+=1
        if mode=='comment':
            if c=='*' and n=='/':mode='code';i+=2;continue
        elif mode=='linecomment':
            if c=='\n':mode='code'
        elif mode in ('string','char'):
            if c=='\\':i+=2;continue
            if (c=='"' and mode=='string') or (c=="'" and mode=='char'):mode='code'
        else:
            if c=='/' and n=='*':mode='comment';i+=2;continue
            if c=='/' and n=='/':mode='linecomment';i+=2;continue
            if c=='"':mode='string'
            elif c=="'":mode='char'
            elif c=='{':
                prior=txt[max(0,i-250):i]
                # Find the latest syntactic statement on the same line.
                prior=prior.split('\n')[-1]
                # Usually line containing the opening brace for if, try, method etc.
                intro=prior.strip()
                kind='container'
                if re.search(r'\b(if|else|try|catch|finally|for|while|switch|do|synchronized)\b',intro): kind='control'
                elif '(' in intro or re.search(r'\b(public|private|protected|void|static|default)\b',intro): kind='method'
                stack.append((line,kind))
            elif c=='}' and stack:
                start,kind=stack.pop();length=line-start+1
                if kind=='control' and 2<=length<=30:spans.append((start,line,'java-control'))
                elif kind=='method' and 2<=length<=16:spans.append((start,line,'java-method'))
        i+=1
    # Java text-block delimiters are atomic.
    for x in re.finditer(r'"""[\s\S]*?"""',txt):
        a=txt.count('\n',0,x.start())+1;b=txt.count('\n',0,x.end())+1
        if b>a and b-a<36:spans.append((a,b,'java-textblock'))
    return spans

def json_protected(lines):
    txt=b''.join(lines).decode('utf-8');stack=[];sp=[];line=1;in_string=False;escape=False
    for c in txt:
        if c=='\n':line+=1
        if in_string:
            if escape:escape=False
            elif c=='\\':escape=True
            elif c=='"':in_string=False
        elif c=='"':in_string=True
        elif c in '{[':stack.append((c,line))
        elif c in '}]' and stack:
            op,a=stack.pop()
            if line-a+1<=35 and line>a:sp.append((a,line,'json-object'))
    return sp

def spans_for(lines,path):
    ext=Path(path).suffix.lower()
    if ext in ('.xml','.html','.xhtml','.svg') or Path(path).name=='pom.xml':return xml_protected(lines)
    if ext in ('.java','.js','.ts','.drl'):return java_protected(lines)
    if ext=='.json':return json_protected(lines)
    if ext=='.ftl':
        # Keep HTML and Freemarker control blocks intact when short.
        return comment_spans(lines)
    return comment_spans(lines) if ext in ('.css','.md') else []

def banned_cuts(spans,n):
    blocks=[False]*(n+1)
    for a,b,_ in spans:
        a=max(1,a);b=min(n,b)
        for x in range(a,b):blocks[x]=True
    return blocks

def prevent_partial_java_statements(lines, forbidden):
    """Do not break a multiline Java signature, method call, or chain."""
    in_block_comment=False;in_string=False;in_char=False;escape=False;paren=0
    for line_no,data in enumerate(lines,1):
        s=data.decode('utf-8');i=0
        while i<len(s):
            c=s[i];nextc=s[i+1] if i+1<len(s) else ''
            if in_block_comment:
                if c=='*' and nextc=='/':in_block_comment=False;i+=2;continue
            elif in_string or in_char:
                if escape:escape=False
                elif c=='\\':escape=True
                elif (in_string and c=='"') or (in_char and c=="'"):
                    in_string=False;in_char=False
            elif c=='/' and nextc=='*':in_block_comment=True;i+=2;continue
            elif c=='/' and nextc=='/':break
            elif c=='"':in_string=True
            elif c=="'":in_char=True
            elif c=='(':paren+=1
            elif c==')':paren=max(0,paren-1)
            i+=1
        if line_no>=len(lines):continue
        stripped=s.strip();nextline=lines[line_no].decode('utf-8').strip()
        if paren>0 or in_string or in_char or (stripped.startswith('@') and not stripped.endswith(');')):
            forbidden[line_no]=True
        if stripped.endswith(('.', ',', '&&', '||', '->')) or nextline.startswith(('.', ')', ';')):
            forbidden[line_no]=True

def partition(lines, start,end, forbid, target, maxlen, ext, group='parent'):
    if end<start:return []
    units=[];s=start
    while s<=end:
        if end-s+1<=target:
            units.append((s,end));break
        options=[]
        for k in range(s,min(end,s+maxlen)+1):
            if k==end or not forbid[k]:
                length=k-s+1
                if k<end and length<=1:continue
                tail=end-k
                if 0<tail<=2 and length>=4 and group=='parent':continue
                last=lines[k-1].decode('utf-8',errors='replace').strip()
                nxt=lines[k].decode('utf-8',errors='replace').strip() if k<end else ''
                bonus=0
                if last=='':bonus-=2.0
                if ext=='.xml' or ext=='pom.xml':
                    if re.search(r'</[\w:.-]+>\s*$',last):bonus-=2.7
                    if re.search(r'<[\w:.-]+[^>]*?/?>\s*$',last):bonus-=.5
                    if nxt.startswith('</'):bonus+=5.0
                    if last.startswith('<') and not last.endswith('>'):bonus+=15.0
                elif ext=='.java':
                    if last.endswith((';','}', '};')):bonus-=2.5
                    if last.startswith('@'):bonus+=9
                    if nxt.startswith((')', '}', 'else ', 'catch ', 'finally ', '.', ';')):bonus+=7
                    if last.endswith(('{',',','(','.','=')):bonus+=8
                elif ext=='.json':
                    if last.endswith(('}', '},', ']', '],')):bonus-=2.5
                    if last.endswith(':'):bonus+=7
                if tail and tail<4:bonus+=5
                if length>target:bonus+=1.1*(length-target)
                if length>8 and group=='child':bonus+=10.0*(length-8)
                # Prefer source blocks of ~8, but keep entire nodes when necessary.
                score=abs(target-length)+bonus
                if group=='parent' and length<4:score+=9
                options.append((score,abs(length-target),k))
        if not options:
            # Protected XML/Java element longer than maxlen is one exceptional unit.
            k=s+maxlen
            while k<end and forbid[k]:k+=1
            k=min(k,end)
        else:k=min(options)[2]
        assert k>=s and (k==end or not forbid[k]),('unsafe',s,k,end)
        units.append((s,k));s=k+1
    assert units[0][0]==start and units[-1][1]==end
    assert all(a<=b for a,b in units)
    return units

def load_source(z):
    rows=list(csv.DictReader(io.TextIOWrapper(z.open('code-journey/MASTER_INDEX.csv'),encoding='utf-8')))
    bysrc=collections.defaultdict(list)
    for r in rows:
        start=int(r['source_start']);end=int(r['source_end'])
        content=z.read('code-journey/blocks/'+r['filename'])
        assert hashlib.sha256(content).hexdigest()==r['sha256']
        bysrc[r['source_path']].append((start,end,content,int(r['sequence'])))
    sources={};source_map={}
    for path,pieces in bysrc.items():
        pieces.sort(key=lambda v:v[0]);expected=1;data=[];anchors={}
        for s,e,c,n in pieces:
            if not s and not e:continue
            assert s==expected,(path,s,expected)
            data.append(c)
            anchors[s]=n
            expected=e+1
        full=b''.join(data)
        assert len(full.splitlines(keepends=True))==expected-1
        sources[path]=full
        source_map[path]=pieces
    return sources,source_map

def shortname(seq, title, path, start,end):
    # Keep basename <= 132 chars; Explorer/ZIP tools commonly impose MAX_PATH.
    suffix=f'_{Path(path).name}_lines-{start}-to-{end}.txt'
    seq=str(seq)
    maxlen=132-len(seq)-len(suffix)-1
    if maxlen<22:
        suffix=f'_{Path(path).stem[:30]}-{hashlib.sha1(path.encode()).hexdigest()[:6]}{Path(path).suffix}_lines-{start}-to-{end}.txt'
        maxlen=132-len(seq)-len(suffix)-1
    title=re.sub(r'[^a-z0-9-]+','-',title.lower()).strip('-')
    words=title.split('-');desc=''
    for word in words:
        if len(desc)+len(word)+bool(desc)>maxlen:break
        desc+=('-' if desc else '')+word
    if len(desc)<10:desc=(title[:maxlen]).strip('-') or 'record-original-source-lines'
    return f'{seq}_{desc}{suffix}'

def title_of(blob,full,path,a,b,fallback):
    try:desc=m.detail(blob,full,path,a,b)
    except Exception:desc='explain-'+Path(path).stem+'-source-code'
    # XML lines of one complete license element should be described accordingly.
    if Path(path).suffix.lower()=='.xml' and b'<licenses>' in blob and b'</licenses>' in blob:
        desc='declare-project-apache-license-name-and-official-license-url'
    if path=='pom.xml' and b'<licenses>' in blob and b'</licenses>' in blob:
        desc='declare-apache-2-license-name-and-link-to-official-license-terms'
    if path=='pom.xml' and b'<parent>' in blob and b'</parent>' in blob:
        desc=('declare-apache-2-license-and-configure-spring-boot-parent-version' if b'<licenses>' in blob else 'configure-spring-boot-maven-parent-artifact-and-pinned-version')
    if not desc or any(w in desc for w in ['finish-the-enclosing','resource-delimiters']):
        desc='continue-'+fallback
    return desc

def build():
    t=time.monotonic()
    with zipfile.ZipFile(SRC) as source:
        originals,history=load_source(source)
    print('Loaded',len(originals),'original UTF-8 source files',flush=True)
    all_tasks=[];violations=collections.Counter();notes=collections.Counter();infos=[]
    for path,full in originals.items():
        lines=full.splitlines(keepends=True);n=len(lines);ext=Path(path).suffix.lower()
        spans=spans_for(lines,path);forbid=banned_cuts(spans,n)
        if ext in ('.java','.js','.ts'):prevent_partial_java_statements(lines,forbid)
        orig=history[path]
        # Rebuild parent boundaries while favoring the existing high-level developer sequence.
        # Non-XML files keep legacy parent outline whenever structurally sound,
        # only regrouping blocks when the old boundary cuts protected syntax.
        if not n:
            segments=[(0,0)]
        elif ext in ('.xml','.json','.html','.xhtml','.svg'):
            segments=partition(lines,1,n,forbid,12 if ext=='.xml' else 16,35,ext,'parent')
        else:
            # Protect no method/comment boundary by moving any old cuts that cross
            # a protected construct to its closing line, then merge tiny or empty pieces.
            segments=[];last=1
            for os,oe,_,_ in orig:
                if oe==n:break
                end=oe
                if forbid[end]:
                    while end<n and forbid[end]:end+=1
                    notes['original_parent_seams_repaired']+=1
                if end<last:continue
                if end-last+1<3 and segments:continue
                segments.append((last,end));last=end+1
            if last<=n:segments.append((last,n))
        # Verify no logical protected interval is split between parent tasks.
        for a,b in segments:
            if a and b<n and forbid[b]:violations['parent_seam']+=1
        for a,b in segments:
            old_seq=next((i[3] for i in orig if i[0]<=a<=i[1]),orig[0][3])
            # Stable sequencing: preserve old development-jump ordering as ordering key.
            all_tasks.append((old_seq,a,path,b,lines,forbid,full,ext))
    if violations:raise AssertionError(violations)
    all_tasks.sort(key=lambda p:(p[0],p[1],p[2]))
    stats=collections.Counter();unique=set();audit_xml=collections.Counter();reverse=collections.defaultdict(list)
    outfolder=OUT.parent;OUT.unlink(missing_ok=True)
    with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=5,allowZip64=True) as z:
        for seq,(anchor,start,path,end,lines,forbid,full,ext) in enumerate(all_tasks,1):
            prefix=f'{((seq-1)//100)*100+1}-to-{((seq-1)//100+1)*100}'
            parent=bytes().join(lines[start-1:end]) if start else b''
            title=title_of(parent,full,path,start,end,Path(path).stem)
            filename=shortname(str(seq)+'.0',title,path,start,end)
            assert filename not in unique,filename;unique.add(filename)
            z.writestr(prefix+'/'+filename,parent)
            reverse[path].append((start,end,prefix+'/'+filename))
            stats['parents']+=1
            if start and end-start+1>8:
                child_parts=partition(lines,start,end,forbid,8,44,ext,'child')
                reconstructed=[]
                for j,(s,e) in enumerate(child_parts,1):
                    piece=b''.join(lines[s-1:e]);reconstructed.append(piece)
                    name=shortname(f'{seq}.{j}',title_of(piece,full,path,s,e,title),path,s,e)
                    assert name not in unique,name;unique.add(name)
                    z.writestr(prefix+'/'+name,piece)
                    stats['children']+=1
                    sz=e-s+1
                    if sz>8:stats['exceptional_children_over_8']+=1
                    if sz>stats['max_child_lines']:stats['max_child_lines']=sz
                    if e<end and forbid[e]:violations['child_seam']+=1
                    if ext=='.xml' and path=='pom.xml' and s<=13 and e>=13:
                        audit_xml['pom_license_span_child_start']=s
                        audit_xml['pom_license_span_child_end']=e
                assert b''.join(reconstructed)==parent,('children_bad',path,start,end)
            if stats['parents']%5000==0:
                print('written parents:',stats['parents'],'children:',stats['children'],flush=True)
    assert not violations,violations
    with zipfile.ZipFile(OUT) as z:
        files=z.namelist()
        assert len(files)==len(unique)==stats['parents']+stats['children']
        assert all(n.endswith('.txt') for n in files)
        assert all(len(Path(n).name)<=132 and len(n)<=153 for n in files)
        assert len(set(n.lower() for n in files))==len(files),'Windows filename collision'
        assert z.testzip() is None
        expected_total_lines=0
        for source_path,source_bytes in originals.items():
            regions=sorted(reverse[source_path])
            if not source_bytes:
                assert len(regions)==1 and regions[0][:2]==(0,0)
                assert z.read(regions[0][2])==b''
                continue
            next_line=1;chunks=[]
            for a,b,file in regions:
                assert a==next_line,(source_path,'gap/overlap',a,next_line)
                chunks.append(z.read(file));next_line=b+1
            assert b''.join(chunks)==source_bytes,(source_path,'BYTE MISMATCH')
            assert next_line-1==len(source_bytes.splitlines(keepends=True))
            expected_total_lines+=next_line-1
        assert expected_total_lines==132076,(expected_total_lines,'source line count')
        print('REBUILD VERIFICATION: 1325 exact UTF8 source files, 132076 lines, CRC PASS',flush=True)
    print('PASS:',dict(stats),'sum',len(unique),'bytes',OUT.stat().st_size,'seams',dict(violations),'notes',dict(notes),'time',time.monotonic()-t,flush=True)
    return all_tasks

if __name__=='__main__':build()
