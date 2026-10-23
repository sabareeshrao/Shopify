#!/usr/bin/env python3
"""Deterministically split a pinned Shopizer checkout into a reconstructible TXT journey.

Preserves every tracked text-file byte. Parent tasks each own one contiguous source
interval; children repeat only their parent's exact bytes in <=8-line pieces.
"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import zipfile

PIN = '6a4a0a65a3408ee8f62597b51d1b3aac24b77dee'
UPSTREAM = 'https://github.com/shopizer-ecommerce/shopizer'
BINARY_EXTENSIONS = {'.mmdb', '.db', '.dat', '.ods', '.xls', '.jpg', '.png', '.ico', '.gif', '.jpeg', '.pdf', '.zip', '.jar', '.class'}
TOPICS = ['bootstrap', 'customer', 'user', 'security', 'product', 'category', 'catalog',
          'shoppingcart', 'cart', 'order', 'payment', 'shipping', 'merchant', 'store',
          'inventory', 'content', 'promotion', 'search', 'pricing', 'configuration',
          'tax', 'integration', 'general']
PRIORITY = ['pom.xml', 'mvnw', '.mvn/', 'README.md']


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str, cwd: Path) -> bytes:
    return subprocess.check_output(['git', *args], cwd=cwd)


def exact_lines(b: bytes) -> list[bytes]:
    # splitlines(keepends=True) retains the original bytes of LF, CRLF, and CR.
    return b.splitlines(keepends=True)


def is_text(path: str, data: bytes) -> bool:
    if Path(path).suffix.lower() in BINARY_EXTENSIONS or b'\x00' in data:
        return False
    try:
        data.decode('utf-8', errors='strict')
        return True
    except UnicodeDecodeError:
        return False


def split_words(name: str) -> str:
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', name)
    s = re.sub(r'([A-Z])([A-Z][a-z])', r'\1-\2', s)
    s = re.sub('[^a-zA-Z0-9]+', '-', s).strip('-').lower()
    return s


def classify(path: str) -> tuple[str, int]:
    t = path.lower().replace('-', '').replace('_', '')
    if path in {'pom.xml', 'mvnw', 'mvnw.cmd'} or path.startswith(('.mvn/', '.circleci/')):
        return 'bootstrap', 0
    # Identify functional domain from the most relevant path segment.
    parts = [split_words(p).replace('-', '') for p in Path(path).parts]
    domain = next((d for d in TOPICS[1:-1] if any(d in x for x in parts)), 'general')
    p = path.lower()
    if '/model/' in p or '/entity/' in p or path.endswith('Model.java'):
        stage = 0
    elif '/repositories/' in p or '/repository/' in p or 'repository' in p:
        stage = 1
    elif '/services/' in p or '/service/' in p or 'service' in p:
        stage = 2
    elif '/facade/' in p or 'facade' in p:
        stage = 3
    elif '/api/' in p or '/controller/' in p or 'controller' in p:
        stage = 4
    elif '/test/' in p or '/tests/' in p:
        stage = 5
    else:
        stage = 2
    return domain, stage


def describe(lines: list[bytes], path: str, start: int, end: int) -> str:
    """Generate a grounded descriptor from the visible code rather than invented behavior."""
    piece = b''.join(lines[start-1:end]).decode('utf-8', errors='replace')
    plain = [x.strip() for x in piece.splitlines() if x.strip()]
    basename = Path(path).stem
    cls = split_words(basename) or 'source-file'
    sample = '\n'.join(plain[:18])
    method = re.search(r'\b(?:public|protected|private|static|final|synchronized|abstract|default|native|override|void|[A-Za-z_][\w<>?,.\[\]]*)[ \t]+(?:[\w<>?,.\[\]]+[ \t]+){0,7}([a-zA-Z_]\w*)[ \t]*\(', sample)
    if not method:
        method = re.search(r'^\s*(?:function\s+|def\s+)([A-Za-z_]\w*)\s*\(', sample, re.M)
    if method and method.group(1) not in {'if', 'while', 'for', 'switch', 'catch', 'return', 'throw', 'new'}:
        m = split_words(method.group(1))
        what = ('validate-conditions-and-handle-failures' if re.search(r'\b(if|throw|catch)\b', piece) else
                'process-the-associated-application-data')
        if re.search(r'\breturn\b', piece):
            what += '-then-return-the-result'
        elif re.search(r'\b(save|persist|update|delete)\w*\s*\(', piece, re.I):
            what += '-and-apply-the-changes'
        else:
            what += '-for-the-caller'
        return f'implement-{m}-to-{what}'
    c = re.search(r'\b(class|interface|enum|record)\s+([A-Za-z_]\w*)', sample)
    if c:
        return f'declare-{c.group(1)}-{split_words(c.group(2))}-and-its-associated-members'
    if any(s.startswith('package ') for s in plain):
        return f'declare-package-and-import-required-dependencies-for-{cls}'
    if any(s.startswith('import ') for s in plain):
        target = split_words(re.sub(r'.*\.', '', next(s for s in plain if s.startswith('import ')).rstrip(';')))
        return f'import-{target}-and-related-dependencies-required-by-{cls}'
    if Path(path).name == 'pom.xml':
        if '<dependency>' in piece or '<dependencies>' in piece:
            return 'configure-maven-dependencies-and-their-versions-for-shopizer-build'
        if '<plugin>' in piece or '<plugins>' in piece:
            return 'configure-maven-build-plugins-and-their-execution-settings'
        return 'define-maven-project-settings-properties-and-module-build-configuration'
    if path.endswith(('.properties', '.yml', '.yaml')):
        key = next((split_words(x.split('=')[0].split(':')[0]) for x in plain if '=' in x or ':' in x), cls)
        return f'configure-{key}-and-related-runtime-application-settings'
    if path.endswith(('.xml', '.ftl', '.html')):
        tag = re.search(r'<\s*([a-zA-Z][\w:.-]*)', sample)
        return f'define-{split_words(tag.group(1)) if tag else cls}-markup-and-related-template-settings'
    if path.endswith(('.md', '.txt')):
        heading = next((split_words(x.lstrip('# ')) for x in plain if x.startswith('#')), cls)
        return f'document-{heading}-with-the-corresponding-project-instructions'
    if path.endswith('.java'):
        # Ground operation names in identifiers actually present in the block.
        cond = re.search(r'\bif\s*\(\s*!?\s*([A-Za-z_]\w*)', sample)
        assignment = re.search(r'\b(?:this\.)?([A-Za-z_]\w*)\s*=\s*(?![=])([A-Za-z_]\w*)', sample)
        invoked = re.search(r'\b([A-Za-z_]\w*)\s*\(', sample)
        if cond and cond.group(1) not in {'if', 'true', 'false'}:
            return f'check-{split_words(cond.group(1))}-condition-and-execute-the-appropriate-branch-in-{cls}'
        if assignment and assignment.group(1) not in {'if', 'return'}:
            return f'assign-{split_words(assignment.group(1))}-from-{split_words(assignment.group(2))}-while-configuring-{cls}'
        if invoked and invoked.group(1) not in {'if', 'return', 'for', 'while', 'switch'}:
            return f'call-{split_words(invoked.group(1))}-and-process-the-related-code-path-in-{cls}'
        if re.search(r'\breturn\b', sample):
            return f'calculate-or-retrieve-the-result-and-return-it-from-{cls}'
        if re.search(r'\bif\s*\(', sample):
            return f'check-application-conditions-and-handle-matching-paths-in-{cls}'
        if re.search(r'\bthrow\b', sample):
            return f'handle-exceptional-conditions-and-report-failure-in-{cls}'
        if re.search(r'\b(private|protected|public)\b', sample):
            return f'declare-fields-methods-or-accessors-used-by-{cls}'
        if any(x in sample for x in ('//', '/*', '* ')):
            return f'preserve-original-code-comments-and-context-for-{cls}'
        return f'implement-the-next-application-statements-and-control-flow-in-{cls}'
    if not plain:
        return f'preserve-empty-or-whitespace-only-source-content-for-{cls}'
    return f'define-the-next-settings-statements-or-content-used-by-{cls}'


def boundaries(lines: list[bytes], path: str) -> list[tuple[int,int]]:
    """Contiguous logical regions; no line is discarded, re-ordered, or repeated."""
    n = len(lines)
    if not n:
        return [(0, 0)]
    pieces, start = [], 0
    extension = Path(path).suffix.lower()
    max_lines = 64 if extension in {'.java', '.js', '.ts'} else 36
    min_lines = 9 if extension in {'.java', '.js', '.ts'} else 12
    for i in range(n):
        text = lines[i].decode('utf-8', errors='replace').strip()
        nxt = lines[i+1].decode('utf-8', errors='replace').strip() if i+1<n else ''
        size = i - start + 1
        last = i == n-1
        is_end = (text in {'}', '};', '</dependency>', '</plugin>', '</project>'} or
                  (not text and not nxt) or
                  (not text and (nxt.startswith(('public ', 'private ', 'protected ', '@Override', 'class ', 'package ')))))
        # A standalone 1-8-line logical section is valid; limit tiny fragments
        # unless the next region is a distinct declaration.
        new_declaration = nxt.startswith(('public ', 'private ', 'protected ', 'import ', '@Override', 'package ',
                                           'class ', 'interface ', 'enum ', 'record ', '@GetMapping', '@PostMapping'))
        split_at_boundary = (not text and new_declaration and size >= 1) or (text in {'}', '};'} and size >= 3 and not nxt)
        if last or size >= max_lines or split_at_boundary or (size >= min_lines and is_end):
            pieces.append((start + 1, i + 1))
            start = i + 1
    assert start == n
    assert sum(e-s+1 for s,e in pieces) == n
    return pieces


def filename(num: str, desc: str, src: str, begin: int, end: int) -> str:
    suffix = f'_{Path(src).name}_lines-{begin}-to-{end}.txt'
    # Keep filename under 240 UTF-8 bytes, safe on most filesystems.
    maxdesc = max(28, 235 - len(num.encode()) - len(suffix.encode()) - 1)
    slug = re.sub('[^a-z0-9-]+', '-', desc.lower()).strip('-')[:maxdesc].rstrip('-')
    return f'{num}_{slug}{suffix}'


def write_csv(path: Path, names: list[str], rows: list[dict]):
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=names)
        w.writeheader(); w.writerows(rows)


def build(checkout: Path, output: Path, zipout: Path, expected_pin: str, full_binary_in_zip: bool):
    checkout = checkout.resolve(); output = output.resolve(); zipout = zipout.resolve()
    head = git('rev-parse','HEAD',cwd=checkout).decode().strip()
    if head != expected_pin:
        raise RuntimeError(f'Wrong source commit: expected {expected_pin}; checkout is {head}')
    output.mkdir(parents=True, exist_ok=True)
    blocks = output / 'blocks'
    if blocks.exists():
        shutil.rmtree(blocks)
    blocks.mkdir()
    tracked = [b.decode('utf-8') for b in git('ls-files','-z',cwd=checkout).split(b'\x00') if b]
    by_topic = collections.defaultdict(list)
    text_sources, binaries, source_records = {}, {}, []
    for path in tracked:
        data = (checkout/path).read_bytes()
        kind = 'text' if is_text(path, data) else 'binary'
        source_records.append(dict(source_path=path,kind=kind,size_bytes=len(data),sha256=sha(data),
                                   source_lines=len(exact_lines(data)) if kind=='text' else '',
                                   source_url=f'{UPSTREAM}/blob/{head}/{path}'))
        if kind == 'text':
            text_sources[path] = data
            dom, stage = classify(path)
            for start,end in boundaries(exact_lines(data),path):
                by_topic[dom].append(dict(path=path,start=start,end=end,stage=stage,domain=dom))
        else:
            binaries[path] = data
    # Topic-by-topic real-development narrative, navigating between files
    # in each feature; reopens are intentional. Never claim historical ordering.
    scheduled=[]
    for topic in TOPICS:
        entries=by_topic[topic]
        if not entries: continue
        by_file=collections.defaultdict(list)
        for e in entries: by_file[e['path']].append(e)
        files=sorted(by_file, key=lambda p:(classify(p)[1],p))
        if topic == 'bootstrap': files=sorted(files,key=lambda p:(next((i for i, prefix in enumerate(PRIORITY) if p==prefix or p.startswith(prefix)),99),p))
        # Rotate across files each step; choose next source block in each file.
        maxpass=max(map(len,by_file.values()))
        for k in range(maxpass):
            for p in files:
                if k<len(by_file[p]): scheduled.append(by_file[p][k])
    if len(scheduled)!=sum(len(v) for v in by_topic.values()):
        raise AssertionError('Scheduling omitted some code regions')
    index=[]; owned=collections.defaultdict(list); total_children=0
    for seq, item in enumerate(scheduled,1):
        src=item['path']; start=item['start']; end=item['end']
        original=text_sources[src]; lines=exact_lines(original)
        content=b''.join(lines[start-1:end]) if start else b''
        name=filename(str(seq),describe(lines,src,start,end),src,start,end)
        (blocks/name).write_bytes(content)
        kids=[]
        if end-start+1>8:
            child_index=0
            for offset in range(start-1,end,8):
                child_index+=1; a=offset+1; z=min(end,offset+8)
                segment=b''.join(lines[offset:z]); title=describe(lines,src,a,z)
                kid=filename(f'{seq}.{child_index}',title,src,a,z)
                (blocks/kid).write_bytes(segment)
                kids.append((kid,segment,a,z))
            if b''.join(k[1] for k in kids)!=content:
                raise AssertionError(f'Child reassembly failed for {src}:{start}-{end}')
            if not all(1<=k[3]-k[2]+1<=8 for k in kids):
                raise AssertionError('Child exceeds 8 lines')
        total_children+=len(kids)
        index.append(dict(sequence=seq,filename=name,source_path=src,source_start=start,
                          source_end=end,source_line_count=(end-start+1) if start else 0,
                          child_count=len(kids),children='|'.join(k[0] for k in kids),
                          sha256=sha(content),source_github_url=f'{UPSTREAM}/blob/{head}/{src}#L{start}-L{end}',
                          domain=item['domain'],stage=item['stage']))
        owned[src].append((start,end,content))
    # Exhaustive byte-for-byte audit for every text file, including empty files,
    # CRLF, trailing whitespace, and trailing-no-newline cases.
    for src,original in text_sources.items():
        pieces=sorted(owned[src], key=lambda p:p[0])
        expected=exact_lines(original)
        got=[]; expected_line=1
        for a,z,b in pieces:
            if a == 0 and z == 0 and not original: continue
            if a!=expected_line:
                raise AssertionError(f'Missing or duplicated source lines in {src} at {expected_line} -> {a}')
            got.append(b); expected_line=z+1
        if expected_line!=len(expected)+1 or b''.join(got)!=original:
            raise AssertionError(f'Byte-for-byte source reconstruction mismatch: {src}')
    csvnames=['sequence','filename','source_path','source_start','source_end','source_line_count',
              'child_count','children','sha256','source_github_url','domain','stage']
    write_csv(output/'MASTER_INDEX.csv',csvnames,index)
    write_csv(output/'SOURCE_MANIFEST.csv',['source_path','kind','size_bytes','sha256','source_lines','source_url'],source_records)
    validation={
        'status':'PASS', 'source_repo':UPSTREAM,'source_commit':head,
        'source_files_total':len(tracked), 'source_files_text':len(text_sources),
        'source_files_binary':len(binaries),
        'source_text_lines':sum(len(exact_lines(v)) for v in text_sources.values()),
        'parent_tasks':len(index),'child_tasks':total_children,
        'generated_txt_files':len(index)+total_children,
        'parent_source_line_coverage':'100%',
        'child_byte_exact_comparison':'PASS',
        'source_text_byte_for_byte_reconstruction':'PASS',
        'original_line_endings_and_tabs':'PRESERVED',
        'binary_assets':'INCLUDED_IN_ZIP' if full_binary_in_zip else 'LISTED_IN_MANIFEST_ONLY',
        'sequence_description':'Plausible heuristic developer journey, not recorded historical edit order',
        'zero_length_text_files':sum(v==b'' for v in text_sources.values())
    }
    (output/'AUDIT.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
    (output/'README.md').write_text(
        '# Shopizer Code Journey (immutable source snapshot)\n\n'
        f'Source: {UPSTREAM} at `{head}`.\n\n'
        'Walk through the parent TXT files in **numeric sequence order**, not lexicographic filename order.\n'
        'Each parent is a distinct, contiguous, exact range of the original source file; '
        'only parents should be used when reconstructing. Children are up-to-eight-line '
        'exact duplicates of a parent, for teaching purposes. Some tasks are only one line.\n\n'
        'Filenames contain grounded automated descriptors, but those descriptions are heuristics; '
        'refer to the source and index for exact intent. Some original code fragments are not '
        'standalone compilable until subsequent tasks are applied.\n\n'
        '## Rebuild and verification\n\n'
        'Use `python rebuild.py --journey path/to/code-journey --output rebuilt` '
        'after unzipping. This sorts parent ranges by original source line and verifies each '
        'text file SHA256. Original binary assets are stored under `original-binaries/` in '
        'the ZIP when available. No TXT headers, changed whitespace, or extra newlines.\n\n'
        'The historical task/edit order is **not** recoverable from a snapshot; the task sequence '
        'is a modeled educational development journey.\n\n'
        'Data files: `MASTER_INDEX.csv`, `SOURCE_MANIFEST.csv`, `AUDIT.json`.\n',encoding='utf-8')
    # Zip everything except raw binary assets in repository path; embed originals
    # in downloadable zip, allowing offline source-tree reconstruction.
    zipout.parent.mkdir(parents=True,exist_ok=True)
    if zipout.exists(): zipout.unlink()
    with zipfile.ZipFile(zipout,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
        for file in sorted(output.rglob('*')):
            if file.is_file() and file.resolve()!=zipout:
                z.write(file,arcname='code-journey/'+file.relative_to(output).as_posix())
        if full_binary_in_zip:
            for name,content in sorted(binaries.items()):
                z.writestr('code-journey/original-binaries/'+name,content,compress_type=zipfile.ZIP_STORED)
    with zipfile.ZipFile(zipout) as z:
        bad=z.testzip()
        if bad: raise RuntimeError(f'ZIP CRC validation failed: {bad}')
    validation['zip_bytes']=zipout.stat().st_size
    (output/'AUDIT.json').write_text(json.dumps(validation,indent=2)+'\n',encoding='utf-8')
    # Rewrite audit inside zip (zip initially had pre-size version; replace entry
    # via re-create would duplicate file; exclude size from inside manifest).
    print(json.dumps(validation,indent=2))


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--checkout',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--zip',dest='zipout',type=Path,required=True)
    p.add_argument('--pin',default=PIN)
    p.add_argument('--omit-binary-from-zip',action='store_true')
    a=p.parse_args()
    build(a.checkout,a.output,a.zipout,a.pin,not a.omit_binary_from_zip)


if __name__ == '__main__':
    main()
