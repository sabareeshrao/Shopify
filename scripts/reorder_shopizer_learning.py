#!/usr/bin/env python3
"""Reorder numbered Shopizer TXT exercises to dependency-informed teaching order.
Preserve exact source bytes, every parent/child interval, max-11 child cap.
The ZIP contains ONLY .txt files; audit/index/README are separate outputs.
"""
import argparse,collections,csv,hashlib,heapq,io,json,os,re,sys,zipfile
from pathlib import Path
import networkx as nx

NAME_RE=re.compile(r'^(\d+)\.(\d+)_(.*?)_lines-(\d+)-to-(\d+)\.txt$',re.I)
GENERIC=re.compile(r'process-related-source-logic|declare-or-update',re.I)
BANNED=re.compile(r'[<>:"/\\|?*\x00-\x1f]')
WORD=re.compile(r'[A-Za-z][A-Za-z0-9_]*')
JAVA_DCL=re.compile(r'\b(?:public|protected|private|static|final|abstract|default|synchronized|native|\s)*\s*(?:<[^>]+>\s*)?(?:[\w\[\]<>?,]+\s+)?([A-Za-z_$][\w$]*)\s*\(',re.M)
STOP=set('public private protected static final class interface enum record this super if else for while switch catch return throw new try synchronized assert String void int long boolean double float byte short char equals hashCode toString serialVersionUID true false null Override Nullable Param annotations methods'.lower().split())

def slug(t):
    t=re.sub(r'([a-z0-9])([A-Z])',r'\1-\2',str(t))
    t=re.sub(r'[^a-zA-Z0-9]+','-',t).strip('-').lower()
    return t[:110].rstrip('-') or 'source'

def meaningful(source,old='',kind='parent'):
    # Infer a specific code action from lexical facts, avoiding fabricated semantics.
    s=source.decode('utf-8','replace');a=[x.strip() for x in s.splitlines() if x.strip()]
    if not a:return 'preserve-empty-source-file'
    lines=[x for x in a if not x.startswith(('*','//','#','<!--')) and x not in ('{','}',');',')','};','*/')]
    if not lines: return 'document-'+slug(' '.join(a[:2])[:80])
    t='\n'.join(lines[:20]); low=t.lower()
    # Most informative anchors: annotated contracts / Java methods / query semantics / assignments.
    annotation=re.findall(r'(?<!\w)@([A-Z][A-Za-z0-9_]*)',t)
    meth=[]
    for line in lines:
        # A method DECLARATION needs a declaration keyword and/or a block/semicolon ending.
        # Reject constructor invocations, throws, and method calls.
        if not re.match(r'^(?:public|protected|private|static|final|abstract|default|synchronized|native|\w+(?:<[^>]+>)?\s+)',line):continue
        if line.startswith(('return ','throw ','new ','if ','for ','while ','catch ')):continue
        if not re.search(r'\)\s*(?:\{|;|throws\b)',line):continue
        m=JAVA_DCL.search(line)
        if m and m.group(1).lower() not in STOP:
            meth.append(m.group(1))
    calls=[x for x in re.findall(r'\b([A-Za-z_$][\w$]*)\s*\(',t) if x.lower() not in STOP and x not in meth]
    java_type=re.search(r'\b(class|interface|enum|record)\s+(\w+)',t)
    pkg=re.search(r'(?m)^\s*package\s+([\w.]+)\s*;',t)
    imports=re.findall(r'(?m)^\s*import\s+(?:static\s+)?([\w.*]+)\s*;',t)
    java_field=re.search(r'(?:private|protected|public)\s+(?:static\s+|final\s+|transient\s+)*([\w<>\[\], ?]+)\s+([A-Za-z_$][\w$]*)\s*(?:[;=])',t)
    if old.lower().endswith(('.xml','.pom','.xhtml','.html','.htm','.jsp')):
        tags=[x for x in re.findall(r'<(?!/|!|\?)([a-zA-Z][\w:.-]*)',t) if x not in ('project','configuration','properties','dependencies','build')]
        values=[x for x in re.findall(r'<([a-zA-Z][\w.-]*)>\s*([^<>\s][^<>]{0,45})\s*</\1>',t)]
        if values:
            return slug('set-'+values[0][0]+'-'+values[0][1]+('-and-'+values[1][0] if len(values)>1 else ''))
        if tags:return slug('configure-'+tags[0]+('-and-'+tags[1] if len(tags)>1 else '')+'-xml-elements')
    if old.lower().endswith('.json'):
        keys=re.findall(r'"([A-Za-z_][\w.-]{1,34})"\s*:',t)
        if keys:return slug('define-json-'+keys[0]+('-and-'+keys[1] if len(keys)>1 else '')+'-properties')
    if java_type:return slug('declare-'+java_type.group(1)+'-'+java_type.group(2)+('-with-'+annotation[0] if annotation else ''))
    if annotation and meth:return slug('apply-'+annotation[0]+'-to-'+meth[0]+'-method')
    if pkg:return slug('declare-java-package-'+pkg.group(1))
    if imports:return slug('import-'+imports[0].split('.')[-1]+('-and-'+imports[1].split('.')[-1] if len(imports)>1 else '')+'-dependencies')
    if meth:
        n=meth[0]
        if n.startswith('get') and len(n)>3:return slug('return-'+n[3:]+'-via-'+n+'-method')
        if n.startswith('set') and len(n)>3:return slug('update-'+n[3:]+'-via-'+n+'-method')
        if n.startswith('is') and len(n)>2:return slug('check-'+n[2:]+'-via-'+n+'-method')
        return slug('implement-'+n+'-method'+('-calling-'+calls[0] if calls else ''))
    if java_field:return slug('declare-'+java_field.group(2)+'-field-of-type-'+java_field.group(1).strip())
    if annotation:return slug('configure-'+annotation[0]+'-annotation'+('-for-'+calls[0] if calls else ''))
    sql=re.search(r'(?i)\b(select|insert|update|delete)\b.*?\b(from|into|set)\s+([\w.]+)',t,re.S)
    if sql:return slug('run-'+sql.group(1)+'-statement-on-'+sql.group(3))
    if re.search(r'\bthrow\s+new\b',t):
        e=re.search(r'throw\s+new\s+(\w+)',t)
        return slug('throw-'+(e.group(1) if e else 'exception')+('-when-'+calls[0] if calls else ''))
    if 'return ' in t:
        ret=re.search(r'\breturn\s+(?:this\.)?([\w.]+)',t)
        return slug('return-'+ret.group(1) if ret else 'computed-result'+('-after-'+calls[0] if calls else ''))
    if calls:return slug('call-'+calls[0]+('-then-'+calls[1] if len(calls)>1 else '-and-handle-result'))
    if 'if (' in t or 'if(' in t:
        m=re.search(r'\bif\s*\(\s*([^\s!=)]+)',t)
        return slug('check-condition-'+(m.group(1) if m else 'branch'))
    ass=re.search(r'\b([A-Za-z_$][\w$]*)\s*(?:\+=|-=|=(?!=))',t)
    if ass:return slug('assign-'+ass.group(1)+'-value')
    toks=[w for w in WORD.findall(' '.join(lines[:3])) if w.lower() not in STOP]
    if toks:return slug('define-'+toks[0]+('-and-'+toks[1] if len(toks)>1 else '')+'-source')
    return 'preserve-'+slug(old[:50])

def priority(path):
    p=path.lower();name=Path(p).name
    if name=='pom.xml':return (0, p.count('/'),p)
    if name in ('.gitignore','.editorconfig','mvnw','mvnw.cmd') or p.startswith('.mvn/') or p.startswith('.circleci/'):return (1, p.count('/'),p)
    if p.endswith('.java'):
        if '/test/' in p:return (11, p.count('/'),p)
        if 'constants/' in p or 'exception/' in p or 'generic/' in p or '/audit/' in p:return (2,p.count('/'),p)
        if 'sm-core-model/' in p:return (3,p.count('/'),p)
        if 'sm-shop-model/' in p:return (4,p.count('/'),p)
        if 'repositories/' in p:return (5,p.count('/'),p)
        if 'sm-core/' in p:return (6,p.count('/'),p)
        if 'sm-shop/' in p:return (7,p.count('/'),p)
        return (8,p.count('/'),p)
    if any(p.endswith(x) for x in ('.properties','.yml','.yaml','.xml')):return (9,p.count('/'),p)
    if p.endswith(('.js','.css','.html','.jsp','.json')):return (10,p.count('/'),p)
    return (12,p.count('/'),p)

def reline(data):return data.splitlines(keepends=True)

def source_map_from_index(index_rows,old_zip):
    # Current source mapping available from MASTER_INDEX.csv; used verbatim.
    result={}
    for r in index_rows:
        result[int(r['sequence'])]=dict(path=r['original_path'],start=int(r['source_start']),end=int(r['source_end']))
    return result

def load_zip(z,rows):
    groups=collections.defaultdict(dict)
    for n in z.namelist():
        if not n.endswith('.txt'):raise ValueError('Non TXT ZIP member '+n)
        m=NAME_RE.fullmatch(Path(n).name)
        if m is None:raise ValueError('Unexpected filename '+n)
        major,minor=int(m.group(1)),int(m.group(2))
        if minor in groups[major]:raise ValueError('Duplicate sequence '+n)
        groups[major][minor]=(n,z.read(n),int(m.group(4)),int(m.group(5)))
    assert len(groups)==len(rows)==10044,(len(groups),len(rows))
    srcgroups=collections.defaultdict(list)
    for id,bits in groups.items():
        assert 0 in bits and id in rows,id
        n,full,start,end=bits[0];r=rows[id]
        assert start==r['start'] and end==r['end'],(id,n,r)
        child=[bits[i] for i in sorted(bits) if i>0]
        if child:
            assert b''.join(x[1] for x in child)==full,(id,'child mismatch')
            assert all(len(reline(x[1]))<=11 for x in child)
        assert len(reline(full)) in (end-start+1,0) or (start==0 and end==0),id
        srcgroups[r['path']].append((start,end,id))
    for path,a in srcgroups.items():
        a.sort()
        pos=1
        for start,end,id in a:
            if start==0:continue
            assert start==pos,('gap or overlap',path,pos,start)
            pos=end+1
    return groups,srcgroups

def dependency_order(paths,source):
    java=[p for p in paths if p.endswith('.java') and ('/src/main/java/' in '/'+p or '/src/test/java/' in '/'+p)]
    fqn={};java_text={};cls={}
    for p in java:
        b=source[p]
        t=b.decode('utf-8','replace');java_text[p]=t
        package=re.search(r'(?m)^\s*package\s+([\w.]+)\s*;',t)
        if package:
            key=package.group(1)+'.'+Path(p).stem
            if key not in fqn:fqn[key]=p
        matches=list(re.finditer(r'\b(?:public|protected|private)?\s*(?:abstract|final|sealed|non-sealed)?\s*\b(?:class|interface|enum|record)\s+([A-Za-z_$][\w$]*)',t))
        cls[p]=matches[0].group(1) if matches else Path(p).stem
    g=nx.DiGraph();g.add_nodes_from(java);refs=[]
    for p,t in java_text.items():
        for match in re.finditer(r'(?m)^\s*import\s+(?:static\s+)?([\w.]+)\s*;',t):
            imp=match.group(1);target=fqn.get(imp)
            if not target and '.' in imp:target=fqn.get(imp.rsplit('.',1)[0])
            if target and target!=p:
                g.add_edge(target,p);refs.append((p,target))
    scc=list(nx.strongly_connected_components(g));cond=nx.condensation(g,scc)
    ready=[]
    for node in cond.nodes:
        if cond.in_degree(node)==0:
            members=cond.nodes[node]['members'];heapq.heappush(ready,(min(priority(x) for x in members),node))
    ordered=[]
    while ready:
        _,node=heapq.heappop(ready)
        members=set(cond.nodes[node]['members'])
        # Within unavoidable cycles, repeatedly choose the file with fewest unseen dependencies.
        while members:
            p=min(members,key=lambda x:(len(set(g.predecessors(x))&members),priority(x)))
            ordered.append(p);members.remove(p)
        for nxt in list(cond.successors(node)):
            cond.nodes[nxt]['remaining']=cond.nodes[nxt].get('remaining',cond.in_degree(nxt))-1
            if cond.nodes[nxt]['remaining']==0:
                heapq.heappush(ready,(min(priority(x) for x in cond.nodes[nxt]['members']),nxt))
    assert len(ordered)==len(java)
    order={p:i for i,p in enumerate(ordered)}
    inversion=sum(order[target]>order[importer] for importer,target in refs)
    old_order={p:i for i,p in enumerate(java)}
    return ordered,refs,inversion,scc

def produce(inp,source_root,index,out_zip,out_dir):
    out_dir.mkdir(parents=True,exist_ok=True)
    source_root=Path(source_root)
    rows={int(x['sequence']):dict(path=x['original_path'],start=int(x['source_start']),end=int(x['source_end'])) for x in csv.DictReader(open(index,encoding='utf-8',newline=''))}
    with zipfile.ZipFile(inp) as z:groups,srcgroups=load_zip(z,rows)
    orig={p:(source_root/p).read_bytes() for p in srcgroups}
    for p,pieces in srcgroups.items():
        constructed=b''.join(groups[id][0][1] for _,_,id in pieces)
        assert constructed==orig[p],('source mismatch',p)
    ordered_java,refs,inversions,scc=dependency_order(list(srcgroups),orig)
    main_java=[p for p in ordered_java if '/test/' not in p]
    test_java=[p for p in ordered_java if '/test/' in p]
    setup=sorted((p for p in srcgroups if p not in ordered_java and priority(p)[0]<=1),key=priority)
    other=sorted((p for p in srcgroups if p not in ordered_java and p not in setup),key=priority)
    files_order=setup+main_java+other+test_java
    assert len(files_order)==len(srcgroups)==1325 and len(set(files_order))==len(files_order)
    result=[];used=set();descs=collections.Counter()
    idx=0;old_to_new={};shortened=0
    with zipfile.ZipFile(out_zip,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as dest:
        for p in files_order:
            for start,end,oldid in sorted(srcgroups[p]):
                idx+=1;old_to_new[oldid]=idx
                items=groups[oldid];first_name=items[0][0];base=Path(p).name
                per_child={}
                for sub,(old_name,blob,a,b) in sorted(items.items()):
                    # all old generic names rewritten; all parent descriptions grounded in source.
                    old_desc=Path(old_name).name.split('_',1)[-1].rsplit('_'+base+'_lines-',1)[0]
                    if GENERIC.search(old_desc) or len(old_desc)>100 or sub==0:
                        d=meaningful(blob,base,kind='parent' if sub==0 else 'child')
                    else:d=old_desc
                    if len(d)>84:d=d[:84].rstrip('-')
                    # make filename lexical content meaningful, not just a unique counter
                    new_name=f'{idx}.{sub}_{d}_{base}_lines-{a}-to-{b}.txt'
                    if len(new_name)>165:
                        max_d=max(20,165-(len(new_name)-len(d)))
                        d=d[:max_d].rstrip('-')
                        new_name=f'{idx}.{sub}_{d}_{base}_lines-{a}-to-{b}.txt'
                        shortened+=1
                    folder=f'{((idx-1)//100)*100+1}-to-{((idx-1)//100+1)*100}'
                    rel=f'{folder}/{new_name}'
                    assert rel.lower() not in used,rel
                    used.add(rel.lower())
                    dest.writestr(rel,blob,compress_type=zipfile.ZIP_DEFLATED)
                    per_child[sub]=(rel,new_name,blob,a,b,d)
                full=per_child[0][2];child=[per_child[c] for c in sorted(per_child) if c]
                assert not child or full==b''.join(x[2] for x in child),(idx,p)
                result.append(dict(sequence=idx,old_sequence=oldid,original_path=p,source_start=start,source_end=end,parent_filename=per_child[0][0],parent_sha256=hashlib.sha256(full).hexdigest(),child_count=len(child),children='|'.join(c[0] for c in child),domain=priority(p)[0]))
    assert idx==len(groups)
    with open(out_dir/'MASTER_INDEX.csv','w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=result[0].keys());w.writeheader();w.writerows(result)
    with open(out_dir/'OLD_TO_NEW.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['old_sequence','new_sequence']);w.writerows(sorted(old_to_new.items()))
    with zipfile.ZipFile(out_zip) as z:
        names=z.namelist()
        assert len(names)==24055 and all(p.endswith('.txt') for p in names)
        assert z.testzip() is None
        for row in result:
            assert z.read(row['parent_filename'])==b''.join(z.read(c) for c in row['children'].split('|')) if row['children'] else True
        sample_bad=[p for p in names if len(p)>220]
        assert not sample_bad,sample_bad[:3]
    intro={p:i for i,p in enumerate(files_order)}
    source_inversions=sum(intro[t]>intro[s] for s,t in refs)
    new_generic=sum(bool(GENERIC.search(p)) for p in names)
    scc_cycle=[list(x) for x in scc if len(x)>1]
    audit=dict(status='PASS',total_txt=24055,parent_count=10044,child_count=14011,original_source_files=1325,original_source_lines=132076,source_sha256_exact=True,zip_only_txt=True,original_parent_bytes_unchanged=True,child_max_lines=11,child_over_11=0,duplicate_casefold_paths=0,source_file_line_order_preserved=True,numbering_contiguous=True,java_internal_import_references=len(refs),import_forward_references_after_reordering=source_inversions,unavoidable_sccs_with_multiple_files=len(scc_cycle),largest_dependency_cycle=max(map(len,scc_cycle),default=0),generic_phrases_remaining=new_generic,max_zip_member_path=max(map(len,names)),filename_shortened=shortened,source_files_buildable_step_by_step='NOT_VERIFIED',historical_edit_order='NOT_CLAIMED',github_lexicographic_numeric_sort='REQUIRES_INDEX_FOR_MULTIDIGIT_CHILDREN')
    (out_dir/'REORDER_AUDIT.json').write_text(json.dumps(audit,indent=2)+'\n')
    (out_dir/'README.md').write_text('# Shopizer Dependency-Informed TXT Learning Journey\n\n'
      'Follow the **numeric** task sequence. Every parent N.0 contains its whole original code block; '
      'children N.1, N.2, etc., are the source-order slices (1–11 lines). Use the parent **or** its children, not both.\n\n'
      'The ZIP contains only TXT files; mappings and audits are alongside the archive in GitHub. '
      'Files have been ordered with internal Java imports as prerequisites where possible. '
      'Circular dependencies cannot all appear before their dependants. '
      '**This is not the actual historical build sequence, and partial project compilation has not been verified.**\n\n'
      'GitHub sorts file names lexicographically, so `.10` may appear before `.2`; '
      'use the task index or numeric filename sorting locally.\n')
    print(json.dumps(audit,indent=2));return audit

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--zip',type=Path,required=True);ap.add_argument('--source-root',type=Path,required=True)
    ap.add_argument('--index',type=Path,required=True);ap.add_argument('--output-zip',type=Path,required=True);ap.add_argument('--outdir',type=Path,required=True)
    a=ap.parse_args();produce(a.zip,a.source_root,a.index,a.output_zip,a.outdir)
