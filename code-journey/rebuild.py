#!/usr/bin/env python3
"""Reassemble all parent tasks by SOURCE line range, verify SHA256 of every file."""
from pathlib import Path
import argparse
import csv
import hashlib
import shutil


def rebuild(journey: Path, destination: Path):
    blocks=journey/'blocks'
    manifest=list(csv.DictReader((journey/'SOURCE_MANIFEST.csv').open(encoding='utf-8')))
    tasks=list(csv.DictReader((journey/'MASTER_INDEX.csv').open(encoding='utf-8')))
    grouped={}
    for row in tasks:
        grouped.setdefault(row['source_path'],[]).append(row)
    for row in manifest:
        src=row['source_path']; out=destination/src
        out.parent.mkdir(parents=True,exist_ok=True)
        if row['kind']=='binary':
            infile=journey/'original-binaries'/src
            if not infile.exists():
                raise FileNotFoundError(f'Missing binary asset {src}; use the full ZIP')
            shutil.copyfile(infile,out)
        else:
            ordered=sorted(grouped.get(src,[]),key=lambda x:int(x['source_start']))
            cur=1
            with out.open('wb') as w:
                for task in ordered:
                    a=int(task['source_start']); z=int(task['source_end'])
                    if a==0 and z==0: continue
                    if a!=cur: raise ValueError(f'Gap/overlap {src} line {cur} != {a}')
                    w.write((blocks/task['filename']).read_bytes())
                    cur=z+1
            if cur!=int(row['source_lines'])+1:
                raise ValueError(f'Final range incomplete for {src}: {cur}')
        digest=hashlib.sha256(out.read_bytes()).hexdigest()
        if digest!=row['sha256']: raise ValueError(f'SHA256 mismatch for {src}')
    print(f'PASS: Rebuilt and SHA256-verified {len(manifest)} original files in {destination}')

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--journey',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    rebuild(a.journey,a.output)
