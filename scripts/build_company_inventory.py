#!/usr/bin/env python3
"""Populate inventory-only Java companies from the pinned source without writing lessons."""
import json, re
from pathlib import Path
from collections import defaultdict
from tree_sitter import Language, Parser
import tree_sitter_java

TOP=Path(__file__).resolve().parents[1]
DOC=TOP/"docs/code-company-explorer"
SRC=TOP/".shopizer-pinned"
SHA="6a4a0a65a3408ee8f62597b51d1b3aac24b77dee"
BATCH=20

def main():
    old_data=json.loads((DOC/"companies.json").read_text())
    tree=json.loads((DOC/"repository-tree.json").read_text())
    old=old_data["companies"]
    assert old_data["reference"]["ref"]==tree["reference_commit"]==SHA
    assert len(old)==old_data["count"]==len({e["id"] for e in old})
    known=defaultdict(list)
    for entry in old: known[entry["source_path"]].append(entry)
    java=[entry for entry in tree["files"] if entry["path"].endswith(".java")]
    parser=Parser(Language(tree_sitter_java.language()))
    pending=[]; warnings=[]; matched=set(); empty=[]
    for f in java:
        path=f["path"]
        source=SRC/path
        if not source.is_file():
            warnings.append({"path":path,"issue":"Source absent from pinned checkout"}); continue
        raw=source.read_bytes()
        if b"\x00" in raw:
            warnings.append({"path":path,"issue":"Binary source"});continue
        root=parser.parse(raw).root_node
        if root.has_error: warnings.append({"path":path,"issue":"Syntax recovery; method details require review"})
        stack=[root];count=0
        while stack:
            node=stack.pop()
            stack.extend(reversed(node.named_children))
            if node.type not in ("method_declaration","constructor_declaration","compact_constructor_declaration","annotation_type_element_declaration"):continue
            n=node.child_by_field_name("name")
            if n is None: n=next((p for p in node.named_children if p.type=="identifier"),None)
            if n is None:
                warnings.append({"path":path,"issue":"Unnamed method at line "+str(node.start_point.row+1)});continue
            name=raw[n.start_byte:n.end_byte].decode("utf-8","replace")
            params=node.child_by_field_name("parameters")
            args=re.sub(r"\s+"," ",raw[params.start_byte:params.end_byte].decode("utf-8","replace")).strip() if params else "()"
            signature=(name+args)[:400]
            start=node.start_point.row+1
            declaration=n.start_point.row+1
            end=node.end_point.row+1
            matches=[x for x in known.get(path,[]) if x["method"].split("(")[0].strip()==name and start<=x.get("method_start_line",x["start_line"])<=end]
            if matches: matched.update(x["id"] for x in matches);continue
            pending.append({
                "id":None,"name":name,"method":signature,
                "kind":"constructor" if "constructor" in node.type else ("annotation_contract" if node.type=="annotation_type_element_declaration" else "method"),
                "source_path":path,"source_blob_sha":f["sha"],"start_line":start,"method_start_line":declaration,"end_line":end,
                "has_body":node.child_by_field_name("body") is not None,
                "source_scope":"test" if "/src/test/" in path or "/src/it/" in path else "main",
                "status":"INDEXED_AWAITING_LESSON_AND_QUESTION"
            })
            count+=1
        if not count and not known.get(path): empty.append(path)
    index=DOC/"company-inventory.json"
    prior=json.loads(index.read_text()) if index.exists() else {"reference_commit":SHA,"pending":[]}
    assert prior["reference_commit"]==SHA
    prev={(x["source_path"],x["method_start_line"],x["method"]):x["id"] for x in prior["pending"]}
    nextid=max([int(x["id"].split(".")[0]) for x in old]+[int(v) for v in prev.values()])+1
    pending.sort(key=lambda x:(x["source_path"],x["start_line"],x["method_start_line"],x["method"]))
    keys=set()
    for x in pending:
        key=(x["source_path"],x["method_start_line"],x["method"])
        assert key not in keys, "Duplicate declaration "+str(key)
        keys.add(key)
        x["id"]=prev.get(key)
        if x["id"] is None:x["id"]=str(nextid);nextid+=1
    pending.sort(key=lambda x:int(x["id"]))
    ids={x["id"] for x in pending}
    assert len(ids)==len(pending) and ids.isdisjoint(x["id"] for x in old)
    unmatched=[x["id"] for x in old if x["id"] not in matched]
    main_total=sum(x["source_scope"]=="main" for x in pending)
    test_total=len(pending)-main_total
    total=len(old)+len(pending)
    info={"schema_version":1,"reference_commit":SHA,
          "scope":"All Java methods, constructors and annotation declarations, including tests and interfaces",
          "source_java_files":len(java),"total_source_files":tree["file_count"],
          "mapped_taught_count":len(old),"pending_count":len(pending),
          "total_inventory_count":total,"main_pending_count":main_total,"test_pending_count":test_total,
          "parser_warnings":{"count":len(warnings),"details":warnings,
                             "unmatched_legacy_count":len(unmatched),"unmatched_legacy_ids":unmatched},
          "pending":pending}
    index.write_text(json.dumps(info,separators=(",",":"),ensure_ascii=False)+"\n")
    lines=["# Shopizer Complete Company Inventory and Checklist","",
           "Pinned reference SHA: "+SHA+". Reference repository remains read-only.","",
           "## Inventory completed","",
           f"- [x] Original Shopizer source: {tree['file_count']:,} tracked files, including {len(java):,} Java files.",
           f"- [x] Preserved taught companies and existing interview questions: {len(old):,}.",
           f"- [x] Newly numbered Java declarations: {len(pending):,}.",
           f"- [x] TOTAL NUMBERED COMPANIES: {total:,}.",
           f"- [x] New production or tooling declarations: {main_total:,}; new test and integration declarations: {test_total:,}.",
           "- [x] Original method names, signatures, file paths, line ranges and source blob hashes indexed.",
           f"- [x] All remaining batches of up to {BATCH} assigned permanent numeric IDs.",
           f"- [ ] YouTube-style explanations remaining: {len(pending):,}.",
           f"- [ ] Unique interview questions remaining: {len(pending):,}.",
           "- [ ] Manual company relationship mapping and semantic quality review remaining.",
           "- [ ] Live browser and mobile UI verification remaining.","",
           "INDEXED does not mean the method has been reviewed, taught, tested or approved.","",
           "## Known extraction limitations","",
           f"- Java files/parser locations raising warnings: {len(warnings):,}.",
           f"- Earlier curated company IDs not matched to parser methods: {len(unmatched):,}.",
           f"- Java files without discovered declarations or legacy mappings: {len(empty):,}.",
           "- Includes abstract/interface declarations and test methods; this is not a count of independent deployed microservices.","",
           "## Batch-by-batch status","",
           "| Batch | Company IDs | Source inventory | Mentor explanation | Interview question | Audit |",
           "|---:|---|---|---|---|---|"]
    for i in range(0,len(pending),BATCH):
        batch=pending[i:i+BATCH]
        lines.append(f"| {i//BATCH+1} | {batch[0]['id']}–{batch[-1]['id']} | Indexed ({len(batch)}) | Pending | Pending | Pending |")
    lines.extend(["","## Parser warning details (JSON)","",
                  json.dumps(info["parser_warnings"],indent=2)[:16000],""])
    (DOC/"BATCH-CHECKLIST.md").write_text("\n".join(lines))
    print(json.dumps({"total":total,"original":len(old),"new":len(pending),
                      "production_pending":main_total,"test_pending":test_total,
                      "batches":(len(pending)+BATCH-1)//BATCH,
                      "parser_warnings":len(warnings),"unmatched_legacy":len(unmatched)},indent=2))
if __name__=="__main__": main()
