#!/usr/bin/env python3
"""Build a TXT-only Shopizer journey with hard 11-line maximum for every child.

Input: the checked-in semantic ZIP with 10,044 numbered parent tasks. Its
parents are the source of truth. Source byte content, paths, line numbers and
parent order stay unchanged. Children are recomputed at semantically favorable
boundaries (never over 11 lines) and their filenames describe source context.
"""
from __future__ import annotations

import argparse
import csv
import collections
import hashlib
import json
import re
import zipfile
from pathlib import Path

PAR_RE = re.compile(r'^(\d+)\.0_(.+)_lines-(\d+)-to-(\d+)\.txt$')
CH_RE = re.compile(r'^(\d+)\.(\d+)_(.+)_lines-(\d+)-to-(\d+)\.txt$')
REF_RE = re.compile(r'_(.+?)_lines-\d+-to-\d+\.txt$')
IDENT = re.compile(r'\b(?:public|protected|private)\s+(?:static\s+|final\s+|synchronized\s+|abstract\s+)*[\w<>?,. \[\]]+\s+(\w+)\s*\(')


def lines_exact(data: bytes) -> list[bytes]:
    return data.splitlines(keepends=True)


def protected_small_xml_constructs(lines: list[bytes]) -> set[int]:
    """Avoid putting a closing XML element in another child if <=11 lines."""
    stack=[]
    protected=set()
    tag=re.compile(r'<(/?)([A-Za-z_][\w:.-]*)(?:\s[^<>]*?)?\s*(/?)>')
    for idx, raw in enumerate(lines):
        s=raw.decode('utf-8',errors='replace')
        s=re.sub(r'<!--.*?-->','',s)
        for m in tag.finditer(s):
            closing, name, self_closing=m.group(1), m.group(2), m.group(3)
            if closing:
                for j in range(len(stack)-1,-1,-1):
                    if stack[j][0]==name:
                        _,start=stack[j]
                        del stack[j:]
                        if idx-start+1<=11:
                            protected.update(range(start+1,idx+1))
                        break
            elif not self_closing and name not in ('xml','DOCTYPE'):
                stack.append((name,idx))
    return protected


def score_split(lines: list[bytes], k: int, preferred: set[int], protected: set[int]) -> float:
    """Smaller scores indicate a less confusing boundary after line k."""
    try:
        prev = lines[k-1].decode('utf-8', errors='replace').strip()
        nxt = lines[k].decode('utf-8', errors='replace').strip()
    except IndexError:
        return -20
    penalty = 0.0
    if k in preferred:
        penalty -= 2.0
    if k in protected:
        penalty += 75.0
    if not prev:
        penalty -= 2.2
    if not nxt:
        penalty -= 1.1
    if re.match(r'^(?:</[\w:.-]+\s*>|\}|\]\s*[,;]?|\)\s*;|else\b|catch\b|finally\b)', nxt):
        penalty += 28  # avoid next child inheriting the end of previous statement/tag
    if re.match(r'^\s*(?:[.).,+*/]|&&|\|\||\?|:)', nxt):
        penalty += 15
    if re.search(r'(?:</[\w:.-]+>|/\s*>|-->)[;,]?$', prev):
        penalty -= 3.5
    if prev.endswith(';') or prev.endswith('}') or prev.endswith('};'):
        penalty -= 3.4
    if re.match(r'^\s*(?:<\?|<!--|<\w+\b)', nxt):
        penalty -= 0.6
    if re.search(r'[.,=+*/&|({\\-]$',prev):
        penalty += 12
    if prev.startswith(('/*','/**','*','//','#')) and nxt.startswith(('*','//','#')):
        penalty += 2.0
    if re.match(r'^<\w+[^>]*>$',prev):
        penalty += 8
    if re.search(r'\b(?:if|while|for|switch|catch)\s*\(.*\)\s*\{$',prev):
        penalty += 12
    return penalty


def choose_breaks(raw: list[bytes], original_ends: set[int]) -> list[tuple[int,int]]:
    n=len(raw)
    if n<=8:
        return []
    # 9–11 lines may remain one child rather than force a nonsensical cut.
    if n<=11:
        return [(0,n)]
    # Dynamic program, globally balancing ~8 lines with cleaner end points.
    protected=protected_small_xml_constructs(raw)
    costs=[float('inf')]*(n+1)
    picks=[None]*(n+1)
    costs[0]=0
    for end in range(1,n+1):
        for start in range(max(0,end-11),end):
            size=end-start
            if size>11:continue
            if end<n:
                boundary=score_split(raw,end,original_ends,protected)
            else:
                boundary=-6
            # Allow 9-11 if this keeps logical units intact.
            length_penalty=(size-8)**2*.48
            if size<=3:
                length_penalty+=11+(4-size)*2
            if size==11:
                length_penalty+=1
            candidate=costs[start]+length_penalty+boundary
            if candidate<costs[end]:
                costs[end]=candidate
                picks[end]=start
    segs=[]
    i=n
    while i>0:
        start=picks[i]
        if start is None:
            raise ValueError('unsplittable line range')
        segs.append((start,i))
        i=start
    segs.reverse()
    assert segs[0][0]==0 and segs[-1][1]==n
    # Guardrail: avoid tiny trailing blocks where feasible without exceeding 11.
    return segs


def slug(s: str, maxlen: int = 93) -> str:
    s=re.sub(r'[^a-zA-Z0-9-]+','-',s.strip().lower()).strip('-')
    s=re.sub('-+','-',s)
    return s[:maxlen].rstrip('-') or 'examine-source-lines'


def context_label(buf: list[bytes], fallback: str) -> str:
    raw='\n'.join(x.decode('utf-8', errors='replace') for x in buf)
    src=[x.strip() for x in raw.splitlines() if x.strip()]
    if not src:return fallback
    # A license or documentation comment must never be misread as a function call.
    commentlike=sum(bool(re.match(r'^(?:#|\*|/\*|//|@|\*/)',p)) for p in src)
    if commentlike>=max(1,len(src)*.65):return fallback
    # Prefer an exact method signature or Java field if visible.
    for x in src:
        m=IDENT.search(x)
        if m:
            return 'declare-or-update-'+m.group(1)+'-method-and-related-logic'
    # XML/HTML element and property names.
    tags=[]
    for m in re.finditer(r'<([a-zA-Z][\w:.-]*)(?:\s|>)',raw):
        tag=m.group(1)
        if tag not in ('project','properties','dependencies','plugins','configuration','modules') and tag not in tags:
            tags.append(tag)
        if len(tags)>=2:break
    if tags:
        return 'configure-'+'-and-'.join(tags)+'-elements-and-values'
    for x in src:
        # Java method calls: prefer specific calls over generic descriptions
        calls=re.findall(r'\b([a-zA-Z_$][\w$]*)\s*\(',x)
        calls=[c for c in calls if c not in ('if','while','for','switch','new','catch','return','throw','super','this')]
        if calls:
            return 'invoke-'+calls[0]+'-and-process-related-source-logic'
    for x in src:
        m=re.search(r'([a-zA-Z][\w.-]*)\s*[:=]',x)
        if m:
            return 'define-or-process-'+m.group(1)+'-value-in-current-block'
    return fallback


def normalize_context(older_desc: str, block: list[bytes], fallback: str) -> str:
    # The prior instructional label remains the reference explanation.
    # When a large old child is re-split, distinguish newly visible methods,
    # config tags and statement calls instead of repeating a generic label.
    specific=context_label(block, '')
    if specific and not specific.startswith('define-or-process-'):
        return slug(specific, 92)
    return slug(older_desc or fallback, 92)


def generate(source: Path, output: Path, audit_out: Path|None=None, manifest: Path|None=None) -> dict:
    output.parent.mkdir(parents=True,exist_ok=True)
    parent_count=child_count=old_oversized=0
    original_input_total=0
    parent_bytes=0
    source_children_by_parent=collections.defaultdict(list)
    original_filenames=[]
    if manifest:
        with manifest.open(encoding='utf-8',newline='') as fh:
            original_filenames=sorted({Path(row['source_path']).name for row in csv.DictReader(fh)},key=len,reverse=True)
    source_parents=[]
    with zipfile.ZipFile(source) as zi:
        assert zi.testzip() is None, 'Input ZIP failed CRC'
        for name in zi.namelist():
            if not name.endswith('.txt'):raise ValueError('Non TXT input: '+name)
            root=Path(name).name
            par=PAR_RE.match(root)
            ch=CH_RE.match(root)
            if par:
                source_parents.append((name,par))
            elif ch and int(ch.group(2))>0:
                source_children_by_parent[int(ch.group(1))].append((name,ch))
            else:
                raise ValueError('Unrecognized filename '+name)
        produced=set(); folder_ids=set(); child_line_lengths=collections.Counter()
        with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6,allowZip64=True) as zo:
            for name,m in source_parents:
                parent_count+=1
                seq=int(m.group(1))
                folder=name.split('/')[0]
                folder_ids.add(folder)
                data=zi.read(name)
                orig=lines_exact(data)
                oldrange=(int(m.group(3)),int(m.group(4)))
                assert len(orig)==oldrange[1]-oldrange[0]+1 or (len(orig)==0), (name,len(orig),oldrange)
                if name.lower() in produced:raise ValueError('Duplicate parent '+name)
                zo.writestr(name,data)
                produced.add(name.lower())
                parent_bytes+=len(data)
                oldchildren=[]
                off=0
                for old_name,c in source_children_by_parent.pop(seq,[]):
                    old_data=zi.read(old_name)
                    old_l=lines_exact(old_data)
                    old_start=int(c.group(4));old_end=int(c.group(5))
                    assert len(old_l)==old_end-old_start+1 or not old_l
                    offset_start=old_start-oldrange[0]
                    offset_end=old_end-oldrange[0]+1
                    assert b''.join(orig[offset_start:offset_end])==old_data,old_name
                    oldchildren.append((offset_start,offset_end,old_name))
                    if len(old_l)>11:old_oversized+=1
                oldchildren.sort()
                if oldchildren:
                    assert b''.join(b''.join(orig[a:b]) for a,b,_ in oldchildren)==data, name
                preferred={b for a,b,_ in oldchildren}
                pieces=choose_breaks(orig,preferred)
                if not pieces:
                    assert len(orig)<=8
                else:
                    assert b''.join(b''.join(orig[a:b]) for a,b in pieces)==data
                    assert all(1<=b-a<=11 for a,b in pieces)
                # Pull original filename from prior parent, important for rebuild.
                basename_parent=Path(name).name
                filename_mid=m.group(2)
                # Source suffix = longest trailing filename portion present in old desc.
                # Preserve the _File.java convention from all existing source filenames.
                source_suffix=None
                for candidate in original_filenames:
                    if basename_parent.endswith('_'+candidate+'_lines-'+str(oldrange[0])+'-to-'+str(oldrange[1])+'.txt'):
                        source_suffix=candidate
                        break
                if source_suffix is None:
                    # Fallback for offline use without a manifest. Choose the source
                    # filename from a well-defined extension (never the full label).
                    stem=basename_parent[:basename_parent.rfind('_lines-')]
                    mbase=re.search(r'_([^_]+\.(?:java|xml|json|ftl|yml|yaml|properties|cmd|bat|sh|py|sql|txt|js|ts|drl|md|html|css))$',stem)
                    source_suffix=mbase.group(1) if mbase else stem.split('_')[-1]
                prefix_source='_'+source_suffix+'_lines-'
                assert prefix_source in basename_parent, (source_suffix,basename_parent)
                for i,(a,b) in enumerate(pieces,1):
                    begin=oldrange[0]+a;end=oldrange[0]+b-1
                    matched=max(oldchildren, key=lambda x:max(0,min(b,x[1])-max(a,x[0])),default=None)
                    description='study-original-source-lines-for-'+source_suffix
                    if matched:
                        oldbase=Path(matched[2]).name
                        cut=oldbase.rfind('_'+source_suffix+'_lines-')
                        if cut>0:
                            description=oldbase[oldbase.index('_')+1:cut]
                    content=orig[a:b]
                    if matched and a==matched[0] and b==matched[1]:
                        label=slug(description,92)
                    else:
                        label=normalize_context(description,content,filename_mid)
                    suffix=f'_{source_suffix}_lines-{begin}-to-{end}.txt'
                    child_name=f'{seq}.{i}_{label}{suffix}'
                    # Windows file/path budget: full extracted path below 180 chars.
                    if len(child_name)>155:
                        available=155-len(f'{seq}.{i}_')-len(suffix)
                        label=slug(label,max(16,available))
                        child_name=f'{seq}.{i}_{label}{suffix}'
                    full=folder+'/'+child_name
                    if full.lower() in produced:raise ValueError('Duplicate child: '+full)
                    produced.add(full.lower())
                    block=b''.join(content)
                    assert block and 1<=len(content)<=11
                    assert len(content)==end-begin+1
                    zo.writestr(full,block)
                    child_count+=1
                    child_line_lengths[len(content)]+=1
        if source_children_by_parent:
            raise ValueError('Orphan source children '+str(list(source_children_by_parent)[:3]))
    with zipfile.ZipFile(output) as z:
        names=z.namelist()
        assert z.testzip() is None
        assert len(names)==parent_count+child_count
        assert len(names)==len(produced)
        assert all(x.endswith('.txt') for x in names)
        assert max(len(Path(x).name) for x in names)<=155
        # Second independent reconstruction from this archive, for all parents.
        for name,m in source_parents:
            seq=int(m.group(1))
            data=z.read(name)
            folder=name.split('/')[0]+'/'
            children=[x for x in names if x.startswith(folder+str(seq)+'.') and not x.startswith(folder+str(seq)+'.0_')]
            # Numeric ordering, NOT alphabetical (1.10 must follow 1.9).
            children.sort(key=lambda x:int(Path(x).name.split('.',1)[1].split('_',1)[0]))
            if children:
                assert b''.join(z.read(c) for c in children)==data,name
            else:
                assert len(lines_exact(data))<=8,name
    summary={
        'status':'PASS',
        'only_txt_files':True,
        'source_zip':source.name,
        'parents':parent_count,
        'children':child_count,
        'total_txt_files':parent_count+child_count,
        'child_min_lines':min(child_line_lengths),
        'child_max_lines':max(child_line_lengths),
        'child_over_eight':sum(n for s,n in child_line_lengths.items() if s>8),
        'child_over_eleven':sum(n for s,n in child_line_lengths.items() if s>11),
        'previous_oversized_children_corrected':old_oversized,
        'parent_child_content_exact':'PASS',
        'original_parent_bytes_preserved':'PASS',
        'parent_tasks_without_children_only_at_most_eight_lines':'PASS',
        'all_filename_unique_case_insensitively':True,
        'max_filename_characters':max(map(lambda s:len(Path(s).name),names)),
        'zip_integrity':'PASS',
        'source_commit':'6a4a0a65a3408ee8f62597b51d1b3aac24b77dee',
        'largest_child_line_distribution':dict(sorted(child_line_lengths.items())),
        'note':'Long methods spanning more than 11 lines must cross child boundaries; this hard cap takes priority over keeping entire methods in one child.',
    }
    if audit_out:
        audit_out.write_text(json.dumps(summary,indent=2)+'\n',encoding='utf8')
    return summary


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--source',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--audit',type=Path)
    ap.add_argument('--manifest',type=Path)
    a=ap.parse_args()
    print(json.dumps(generate(a.source,a.output,a.audit,a.manifest),indent=2))
