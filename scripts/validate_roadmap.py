#!/usr/bin/env python3
"""Validate stable task IDs, phase ranges, extension questions and progress.

Stdlib only; run: python scripts/validate_roadmap.py
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COUNTS = [12, 20, 26, 32, 25, 25, 35, 43, 37, 49, 45, 32, 42, 34,
          36, 40, 34, 32, 30, 42, 48, 42, 27, 24, 65, 65, 45, 38]
QUESTION_RE = re.compile(r"^- \[([ xX])\] \*\*(Q\d{4,})\s+[—-]", re.M)
STATUSES = {"NOT_STARTED", "IN_PROGRESS", "BLOCKED", "VERIFIED", "RETIRED", "SPLIT"}
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def questions(path: Path) -> list[tuple[str, bool]]:
    return [(qid, checked.lower() == "x") for checked, qid
            in QUESTION_RE.findall(path.read_text(encoding="utf-8"))]


def main() -> int:
    if sum(COUNTS) != 1025:
        fail("Unexpected baseline task total")

    registry: dict[str, tuple[str, bool]] = {}
    # Baseline IDs are permanent, but membership and order may change through
    # an approved change request. Do not enforce the original per-phase counts.
    for phase in range(len(COUNTS)):
        path = ROOT / "questions" / f"phase-{phase:02d}.md"
        if not path.is_file():
            fail(f"Missing phase file: {path}")
            continue
        for qid, checked in questions(path):
            if int(qid[1:]) > 1025:
                fail(f"New IDs belong in questions/extensions/: {qid}")
            if qid in registry:
                fail(f"Duplicate question ID: {qid}")
            registry[qid] = (f"{phase:02d}", checked)

    expected_baseline = {f"Q{n:04d}" for n in range(1, 1026)}
    actual_baseline = {qid for qid in registry if int(qid[1:]) <= 1025}
    if actual_baseline != expected_baseline:
        missing = sorted(expected_baseline - actual_baseline)
        extra = sorted(actual_baseline - expected_baseline)
        fail(f"Baseline identity mismatch, missing={missing[:12]}, extra={extra[:12]}")

    ext_dir = ROOT / "questions" / "extensions"
    extension_ids: list[str] = []
    for path in sorted(ext_dir.glob("Q*.md")) if ext_dir.exists() else []:
        entries = questions(path)
        if len(entries) != 1:
            fail(f"Extension must have exactly one question: {path}")
            continue
        qid, checked = entries[0]
        if path.stem != qid:
            fail(f"Filename/ID mismatch: {path} vs {qid}")
        if int(qid[1:]) <= 1025:
            fail(f"Extension ID must be above Q1025: {qid}")
        if qid in registry:
            fail(f"Duplicate question ID: {qid}")
        content = path.read_text(encoding="utf-8")
        found = re.search(r"(?m)^\s*-?\s*\*\*Phase:\*\*\s*(\d{2})\s*$", content)
        if not found or not 0 <= int(found.group(1)) < 28:
            fail(f"Extension missing valid **Phase:** 00–27: {path}")
            continue
        registry[qid] = (found.group(1), checked)
        extension_ids.append(qid)

    extra_ids = sorted((int(x[1:]) for x in extension_ids))
    if extra_ids != list(range(1026, 1026 + len(extra_ids))):
        fail("Extension IDs must be allocated contiguously starting Q1026")

    csv_path = ROOT / "tracking" / "PROGRESS.csv"
    if not csv_path.is_file():
        fail("Missing tracking/PROGRESS.csv")
        return show_result(len(registry))

    with csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        required = {"id", "phase", "status", "priority", "depends_on",
                    "lesson_path", "implementation_paths",
                    "test_evidence", "commit_sha", "notes"}
        if not required.issubset(set(reader.fieldnames or [])):
            fail("Progress CSV is missing required columns")
        records = list(reader)

    seen = Counter(row.get("id", "") for row in records)
    for qid, qty in seen.items():
        if qty != 1:
            fail(f"Progress CSV ID occurs {qty} times: {qid}")
    if set(seen) != set(registry):
        missing = sorted(set(registry) - set(seen))
        extra = sorted(set(seen) - set(registry))
        fail(f"Progress register mismatch; missing={missing[:8]}, unexpected={extra[:8]}")

    for row in records:
        qid = row.get("id", "")
        if qid not in registry:
            continue
        phase, checked = registry[qid]
        if row.get("phase") != phase:
            fail(f"{qid}: phase mismatch: tracker={row.get('phase')} actual={phase}")
        status = row.get("status")
        if status not in STATUSES:
            fail(f"{qid}: unknown status {status!r}")
        if checked != (status == "VERIFIED"):
            fail(f"{qid}: checkbox and VERIFIED status disagree")
        if status == "VERIFIED" and (not row.get("commit_sha") or not row.get("test_evidence")):
            fail(f"{qid}: VERIFIED requires commit SHA and test evidence")
        for dep in filter(None, re.split(r"[;\s]+", row.get("depends_on", ""))):
            if dep not in registry:
                fail(f"{qid}: unknown prerequisite {dep}")
            if dep == qid:
                fail(f"{qid}: self-dependency")

    return show_result(len(registry))


def show_result(size: int) -> int:
    if ERRORS:
        print(f"FAILED ({len(ERRORS)} errors)")
        for issue in ERRORS:
            print(" - " + issue)
        return 1
    print(f"PASS: 28 phase files, 1025 baseline questions, "
          f"{size - 1025} extensions, {size} unique IDs and matching tracker rows.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
