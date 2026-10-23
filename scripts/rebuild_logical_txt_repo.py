#!/usr/bin/env python3
"""Rebuild Shopizer's original text sources from parent-only TXT tasks using MASTER_INDEX.csv.
Children are teaching slices and must NOT be pasted alongside parents.
"""
import argparse,csv,collections,hashlib
from pathlib import Path

def rebuild(journey,output):
    index=journey/'MASTER_INDEX.csv'
    if not index.exists(): raise FileNotFoundError(index)
    files=collections.defaultdict(list)
    with index.open(encoding='utf-8',newline='') as fh:
        for r in csv.DictReader(fh):
            src=Path(r['original_path'])
            if src.is_absolute() or '..' in src.parts:raise ValueError('Unsafe source path')
            files[str(src)].append(r)
    count=0
    for src,rows in files.items():
        rows.sort(key=lambda r:int(r['source_start']))
        expected=1;content=[]
        for r in rows:
            start,end=int(r['source_start']),int(r['source_end'])
            if start not in (expected,0): raise ValueError(f'Gap/overlap {src}: {start} expected {expected}')
            path=journey/'steps'/r['parent_filename']
            if not path.is_file():raise FileNotFoundError(path)
            data=path.read_bytes()
            if hashlib.sha256(data).hexdigest()!=r['sha256']:raise ValueError(f'Corrupted block {path}')
            if start==0 and end==0 and data:raise ValueError('Invalid empty file block')
            if start:expected=end+1
            content.append(data)
        out=output/src
        out.parent.mkdir(parents=True,exist_ok=True)
        out.write_bytes(b''.join(content));count+=1
    print(f'PASS: reconstructed {count} original text files from {index}')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--journey',type=Path,default=Path('code-journey'));p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();rebuild(a.journey,a.output)
