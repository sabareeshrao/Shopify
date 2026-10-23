#!/usr/bin/env python3
"""Shift short child edges (at most 3 lines) to complete local constructs.

Invariant: parent code bytes untouched; each child's bytes join into its parent;
child contains 1-11 source lines; one-to-one original task ids preserved.
"""
import argparse
import collections
import json
import re
import zipfile
from pathlib import Path

MEMBER = re.compile(r'^([^/]+)/([1-9][0-9]*)\.([0-9]+)_(.+)_lines-([0-9]+)-to-([0-9]+)\.txt$')
TAG = re.compile(r'<(/?)([A-Za-z][\w.:-]*)(?:\s[^<>]*?)?\s*(/?)>')
BARE_CLOSE = re.compile(r'^\s*(?:\}\s*\)?\s*;?|\}\s*,?|\]\s*[,;]?|\)\s*[,;]?|\}\)\s*;?|</[A-Za-z][\w.:-]*\s*>)\s*(?://.*)?$')


def parse_entry(path):
    m = MEMBER.match(path)
    if not m: raise AssertionError(f'Unexpected member filename: {path}')
    return dict(path=path,folder=m[1],parent=int(m[2]),child=int(m[3]),desc=m[4],start=int(m[5]),end=int(m[6]))


def clean_line(line):
    return line.decode('utf-8','replace').strip()


def syntax_protection(lines, language):
    """Boundaries inside independently complete short constructs cost more to cut."""
    protected=collections.defaultdict(list)
    def protect(a,b,kind,weight=90):
        if 0 < b-a+1 <= 11:
            for pos in range(a+1,b+1):
                protected[pos].append((weight,kind,a,b))
    texts=[x.decode('utf-8','replace') for x in lines]
    n=len(texts)
    # A short block comment should remain in one file, not split header or license.
    comment_start=None
    for i,s in enumerate(texts):
        if comment_start is None and '/*' in s and '*/' not in s[s.index('/*')+2:]:
            comment_start=i
        elif comment_start is not None and '*/' in s:
            protect(comment_start,i,'complete-comment',105)
            comment_start=None
    if language in {'xml','html','jsp','xhtml','svg','pom'}:
        open_tags=[]
        for i,s in enumerate(texts):
            # Strip comments to avoid detecting examples as markup.
            for m in TAG.finditer(s):
                closing,name,self_close=m.groups()
                if self_close: continue
                if closing:
                    for j in range(len(open_tags)-1,-1,-1):
                        if open_tags[j][0]==name:
                            open_i=open_tags[j][1]
                            open_tags=open_tags[:j]
                            protect(open_i,i,f'complete-{name}-element',110)
                            break
                elif not s.lstrip().startswith(('<?','<!')):
                    open_tags.append((name,i))
        # XML opening tags sometimes span two or more lines and contain attributes.
        for i,s in enumerate(texts):
            if re.search(r'<[A-Za-z][^>]*$',s) and not re.search(r'/>\s*$',s):
                for j in range(i+1,min(i+11,n)):
                    if '>' in texts[j]:
                        protect(i,j,'complete-opening-tag',100)
                        break
    elif language in {'java','js','ts','jsx','tsx','json','css','scss','groovy','gradle','kt'}:
        # Parse delimiter pairs outside comments and quotes. Matchable short pairs
        # (including @Annotations / method invocations) should not be split.
        stack=[]
        insingle=indouble=False
        inblock=False
        triple=False
        pairs={')':'(',']':'[','}':'{'}
        for i,s in enumerate(texts):
            k=0
            while k<len(s):
                c=s[k]; nxt=s[k:k+2]
                if inblock:
                    if nxt=='*/':inblock=False;k+=2;continue
                    k+=1;continue
                if not (insingle or indouble) and nxt=='//':break
                if not (insingle or indouble) and nxt=='/*':inblock=True;k+=2;continue
                if (insingle or indouble):
                    if c=='\\':k+=2;continue
                    if insingle and c=="'": insingle=False
                    elif indouble and c=='"':indouble=False
                    k+=1;continue
                if c=="'":insingle=True;k+=1;continue
                if c=='"':indouble=True;k+=1;continue
                if c in '([{': stack.append((c,i))
                elif c in ')]}' and stack:
                    for j in range(len(stack)-1,-1,-1):
                        if stack[j][0]==pairs[c]:
                            start=stack[j][1]
                            del stack[j:]
                            protect(start,i,'complete-bracket-expression',90 if c!='}' else 55)
                            break
                k+=1
        # Protect short multi-line @annotations even when values contain awkward quotes.
        for i,s in enumerate(texts):
            if re.match(r'^\s*@[A-Za-z_$][\w.$]*\s*\(',s):
                depth=0
                for j in range(i,min(i+11,n)):
                    fragment=re.sub(r'"(?:\\.|[^"\\])*"','""',texts[j])
                    depth+=fragment.count('(')-fragment.count(')')
                    if depth<=0:
                        if j>i:protect(i,j,'complete-annotation',140)
                        break
    return protected


def language_for(parent):
    file=parent['desc'].rsplit('_',1)[-1].lower()  # Ends before _lines with source basename.
    return file.rsplit('.',1)[-1] if '.' in file else file


def boundary_penalty(texts,cut,protected):
    prev=texts[cut-1].strip() if cut else ''
    curr=texts[cut].strip() if cut<len(texts) else ''
    reasons=[]
    if cut in protected:
        # Penalize all protected intervals, with stronger weight for short @annotations and XML.
        strength=max(x[0] for x in protected[cut])
        reasons.append((strength,protected[cut][0][1]))
    if curr.startswith('</'):
        reasons.append((70,'detached-xml-closing-tag'))
    if curr.startswith(('})','));','}));',');','};')):
        reasons.append((50,'detached-expression-tail'))
    elif BARE_CLOSE.fullmatch(curr):
        reasons.append((24,'detached-closing-delimiter'))
    if re.match(r'^\s*(?:\+|\.|&&|\|\||\?|:|,)',curr):
        reasons.append((32,'continuation-at-child-start'))
    if prev.endswith(('+','&&','||','=',',','->','.', '?', ':')):
        reasons.append((29,'statement-continues-into-next-child'))
    if prev.endswith(('(', '[', '{')) and curr not in ('',):
        reasons.append((10,'opening-expression-at-child-end'))
    # Friendly endpoints: standalone complete statements, XML end tags or comment closers.
    if curr and prev and not reasons:
        if prev.endswith((';','}', '*/','>')):pass
        elif curr.startswith(('@','public ','private ','protected ','import ','package ','//','/*','<')):pass
        else:reasons.append((3,'mid-statement-uncertain'))
    return sum(w for w,_ in reasons),[name for _,name in reasons]


def adjust_parent(parent,children,record_bytes):
    pbytes=record_bytes[parent['path']]
    lines=pbytes.splitlines(keepends=True)
    count=len(lines)
    if len(children)<2:
        return [(x,x['start'],x['end'],record_bytes[x['path']]) for x in children],[],0,0
    # Previous audit guarantees that old children cover parent without gaps, so validate it.
    assert b''.join(record_bytes[ch['path']] for ch in children)==pbytes, parent['path']
    sizes=[len(record_bytes[ch['path']].splitlines(keepends=True)) for ch in children]
    assert all(1<=s<=11 for s in sizes),parent['path']
    old=[];acc=0
    for size in sizes[:-1]:acc+=size;old.append(acc)
    assert sum(sizes)==count,(parent['path'],sum(sizes),count)
    strings=[clean_line(x) for x in lines]
    protected=syntax_protection(lines,language_for(parent))
    old_total=sum(boundary_penalty(strings,c,protected)[0] for c in old)
    # Dynamic programming over original cut positions ±3. Every child remains <=11.
    levels=[{0:(0,[],[])}]
    for j,original in enumerate(old):
        states={}
        for cut in range(max(1,original-3),min(count-1,original+3)+1):
            if (cut <= j) or count-cut<len(old)-j: continue
            penalty,reasons=boundary_penalty(strings,cut,protected)
            for prior,(cost,prev_cuts,prev_reasons) in levels[-1].items():
                length=cut-prior
                if not 1<=length<=11: continue
                # A conservative preference for original cut keeps movement localized.
                candidate=cost+penalty+(max(0,cut-original)*3.0)+(max(0,original-cut)*9.0)
                if cut not in states or candidate<states[cut][0]:
                    states[cut]=(candidate,prev_cuts+[cut],prev_reasons+[(penalty,reasons)])
        if not states:raise AssertionError('No feasible boundary '+parent['path'])
        levels.append(states)
    viable=[x for start,x in levels[-1].items() if 1<=count-start<=11]
    if not viable:raise AssertionError('No valid final slice '+parent['path'])
    best=min(viable,key=lambda r:r[0]);cuts=best[1]
    new_total=sum(boundary_penalty(strings,c,protected)[0] for c in cuts)
    # Never make an objective worse just to tweak line positions.
    if new_total>=old_total or cuts==old:
        cuts=old;new_total=old_total
    partitions=[0]+cuts+[count]
    output=[];movements=[]
    for i,ch in enumerate(children):
        a,b=partitions[i],partitions[i+1]
        assert 1<=b-a<=11
        body=b''.join(lines[a:b])
        begin=parent['start']+a if parent['start'] else 0
        end=parent['start']+b-1 if parent['start'] else 0
        output.append((ch,begin,end,body))
    for i,(was,now) in enumerate(zip(old,cuts)):
        if was!=now:
            movements.append({'parent':parent['parent'],'between':f'{children[i]["parent"]}.{children[i]["child"]} and {children[i+1]["parent"]}.{children[i+1]["child"]}',
                'from_line':parent['start']+was-1,'to_line':parent['start']+now-1,
                'lines_shifted':abs(now-was),
                'before_reasons':boundary_penalty(strings,was,protected)[1],
                'after_reasons':boundary_penalty(strings,now,protected)[1]})
    assert b''.join(data for _,_,_,data in output)==pbytes
    return output,movements,old_total,new_total


def run(source,target,audit_path):
    with zipfile.ZipFile(source) as z:
        original_paths=z.namelist()
        assert len(original_paths)==24055, len(original_paths)
        assert all(x.lower().endswith('.txt') for x in original_paths)
        data={n:z.read(n) for n in original_paths}
    parents={}; children=collections.defaultdict(list)
    for p in original_paths:
        r=parse_entry(p)
        if r['child']==0:parents[r['parent']]=r
        else:children[r['parent']].append(r)
    assert len(parents)==10044
    result=[];movements=[];total_old=total_new=0
    for num in sorted(parents):
        parent=parents[num]
        result.append((parent['path'],data[parent['path']]))
        kids=sorted(children[num],key=lambda x:x['child'])
        new,changed,before,after=adjust_parent(parent,kids,data)
        total_old+=before;total_new+=after
        movements.extend(changed)
        for r,a,b,body in new:
            newname=re.sub(r'_lines-[0-9]+-to-[0-9]+\.txt$',f'_lines-{a}-to-{b}.txt',r['path'])
            result.append((newname,body))
    assert len(result)==len(original_paths)
    result_names=[n for n,_ in result]
    assert len(set(n.casefold() for n in result_names))==len(result_names)
    assert all(len(n)<=220 for n in result_names)
    assert all(len(data.splitlines(keepends=True))<=11 for n,data in result if not re.search(r'/[0-9]+\.0_',n))
    target.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7,allowZip64=True) as z:
        for name,body in result:z.writestr(name,body)
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
        assert len(z.namelist())==24055
    # Find example lines in corrected result for the audit.
    preview={}
    for num in (196,351):
        preview[str(num)]=[name for name,body in result if re.search(rf'/{num}\.[1-9][0-9]*_',name)]
    report=dict(status='PASS',source_zip=source.name,output_zip=target.name,
        total_txt_files=len(result),parent_tasks=len(parents),children=sum(map(len,children.values())),
        boundary_shifts=len(movements),shifted_parent_tasks=len(set(x['parent'] for x in movements)),
        maximum_lines_shifted=max((x['lines_shifted'] for x in movements),default=0),
        child_max_lines=max((len(body.splitlines(keepends=True)) for name,body in result if not re.search(r'/[0-9]+\.0_',name)),default=0),
        protected_and_tail_boundary_penalty_before=total_old,protected_and_tail_boundary_penalty_after=total_new,
        exact_parent_child_reconstruction='PASS',original_parent_bytes_preserved='PASS',zip_only_txt='PASS',zip_integrity='PASS',
        changes=movements,examples=preview)
    audit_path.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('changes','examples')},indent=2))
    print('Sample moved child boundary details:',json.dumps([x for x in movements if x['parent'] in (196,351)],indent=2))
    return report

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--audit',type=Path,required=True)
    args=ap.parse_args()
    run(args.source,args.output,args.audit)
