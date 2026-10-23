#!/usr/bin/env python3
"""Publish each existing code-journey TXT as a browsable GitHub file.

Reads an already-audited Shopizer-Code-Journey.zip (source of truth), retains
parent and child filenames and exact bytes, groups by contiguous task number,
and builds deterministic, verified navigation indexes. No source modifications.
"""
from __future__ import annotations
import argparse,collections,csv,hashlib,io,json,re,shutil,zipfile
from pathlib import Path

def csv_bytes(rows,headers):
    out=io.StringIO(newline='');writer=csv.DictWriter(out,fieldnames=headers)
    writer.writeheader();writer.writerows(rows);return out.getvalue().encode('utf-8')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--zip',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--group-size',type=int,default=100)
    args=parser.parse_args()
    assert 1<=args.group_size<=250
    steps=args.output/'steps';steps.mkdir(parents=True,exist_ok=True)
    # Only replace the generated step directory, never unrelated folders.
    for p in steps.iterdir():
        if p.is_dir() and re.fullmatch(r'\d+-to-\d+',p.name):shutil.rmtree(p)
    with zipfile.ZipFile(args.zip) as z:
        audit=json.loads(z.read('code-journey/AUDIT.json'))
        rows=list(csv.DictReader(io.StringIO(z.read('code-journey/MASTER_INDEX.csv').decode('utf-8'))))
        assert audit['status']=='PASS' and len(rows)==audit['parent_tasks']
        assert audit['source_text_byte_for_byte_reconstruction']=='PASS'
        entries=[];seen=set();folders=collections.defaultdict(list)
        for row in rows:
            seq=int(row['sequence']);scope=((seq-1)//args.group_size)*args.group_size+1
            grouping=f'{scope}-to-{scope+args.group_size-1}'
            folder=steps/grouping;folder.mkdir(parents=True,exist_ok=True)
            items=[('parent',row['sequence'],row['filename'])]
            items.extend(('child',name.split('_',1)[0],name) for name in (row['children'].split('|') if row['children'] else []))
            assert len(items)-1==int(row['child_count'])
            parent_payload=z.read('code-journey/blocks/'+row['filename'])
            assert hashlib.sha256(parent_payload).hexdigest()==row['sha256']
            pieces=[]
            for kind,tid,filename in items:
                assert filename not in seen and '/' not in filename and '\\' not in filename,filename
                seen.add(filename)
                assert filename.startswith(tid+'_')
                part=z.read('code-journey/blocks/'+filename)
                (folder/filename).write_bytes(part)
                assert (folder/filename).read_bytes()==part
                rng=re.search(r'_lines-(\d+)-to-(\d+)\.txt$',filename)
                assert rng,filename
                start,end=map(int,rng.groups())
                if kind=='child':
                    assert 1<=end-start+1<=8,(filename,start,end)
                    pieces.append(part)
                else:
                    assert start==int(row['source_start']) and end==int(row['source_end'])
                published=f'code-journey/steps/{grouping}/{filename}'
                record=dict(sequence=tid,kind=kind,parent=row['sequence'],folder=grouping,
                            filename=filename,github_path=published,source_path=row['source_path'],
                            source_start=start,source_end=end,sha256=hashlib.sha256(part).hexdigest())
                entries.append(record)
                if kind=='parent':folders[grouping].append(record)
            if pieces:assert b''.join(pieces)==parent_payload,row['sequence']
        assert len(entries)==audit['generated_txt_files'],(len(entries),audit['generated_txt_files'])
        assert len(seen)==len(entries)
    # Folder README navigates parents in strictly numeric order; filename supplies
    # the exact technical description, original file and source line range.
    for group,parent_items in folders.items():
        md=['# Shopizer developer tasks '+group,'',
            'Open parent files to see the complete task code. For any task with children,',
            'choose **either** its parent or its 1.1 / 1.2 / ... children, never both.',
            'Each file preserves the original code bytes and source line range.','',
            '| Task | Parent file | Original source |','|---:|---|---|']
        for e in parent_items:
            md.append(f"| {e['sequence']} | [{e['filename']}]({e['filename']}) | `{e['source_path']}` |")
        (steps/group/'README.md').write_text('\n'.join(md)+'\n',encoding='utf8')
    group_list=sorted(folders,key=lambda name:int(name.split('-')[0]))
    page=['# Shopizer Code Journey — Browse All 29,283 TXT Files','',
          'Full source is split into **14,552 numbered parent tasks**, with children',
          'where a logical block exceeds eight original source lines.',
          'Each directory includes parent tasks and their children.','',
          '**Follow the main task numbers globally**, even when the same Java file',
          'appears in several separate tasks. Folder names show ranges of main IDs.','',
          '| Parent ID range | Open folder | Number of parent tasks |','|---:|---|---:|']
    for group in group_list:
        page.append(f'| {group} | [{group}]({group}/) | {len(folders[group])} |')
    (steps/'README.md').write_text('\n'.join(page)+'\n',encoding='utf8')
    headers=['sequence','kind','parent','folder','filename','github_path','source_path','source_start','source_end','sha256']
    (args.output/'BROWSE_INDEX.csv').write_bytes(csv_bytes(entries,headers))
    result={
        'status':'PASS','github_browsable_source':'code-journey/steps/',
        'folders':len(folders),'folder_size_in_parent_tasks':args.group_size,
        'parents':len(rows),'children':len(entries)-len(rows),
        'published_txt_files':len(entries),'unique_txt_filenames':len(seen),
        'child_lines_maximum':8,'every_txt_matches_zip_bytes':True,
        'all_parent_children_concatenate_to_parent_exactly':True,
        'source_byte_exact_reconstruction':audit['source_text_byte_for_byte_reconstruction'],
        'source_commit':audit['source_commit']
    }
    # The archive is the only required flat blocks/ store. GitHub exposes the
    # organized steps/ copies instead of 29,283 extra unbrowsable flat files.
    # This runs ONLY after every nested TXT is checked against ZIP bytes.
    flat_blocks=args.output/'blocks'
    if flat_blocks.is_dir():
        shutil.rmtree(flat_blocks)
    result['redundant_flat_blocks_removed']=not flat_blocks.exists()
    with (args.output/'README.md').open('a',encoding='utf8') as readme:
        readme.write('\n## Browse individual TXT files on GitHub\n\n'
                     'Open [`steps/`](steps/) for the numbered project journey '
                     'split into 100-parent-task folders, or use '
                     '[`BROWSE_INDEX.csv`](BROWSE_INDEX.csv) to locate any task. '
                     'The individual original source lines are preserved exactly, '
                     'and the ZIP still contains the complete original flat source blocks.\n\n'
                     'See `BROWSE_AUDIT.json` for folder and file-count verification.\n')
    (args.output/'BROWSE_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
