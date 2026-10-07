#!/usr/bin/env python3
"""Report draft-narrative left inside the solution bodies.

The solutions were written incrementally and some paragraphs still carry the
"Wait ... let me recheck" scaffolding of a scratch pad. That wording is a useful
signal: wherever it appears, the derivation either has a loose end or the answer
was taken from the key without the step being reproduced.

Usage:
    python3 tools/check_prose.py            # report only, always exits 0
    python3 tools/check_prose.py --strict   # exit 1 if anything is found
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS = ROOT / "solutions"

PATTERNS = [
    r"\bWait\b",
    r"\bHmm\b",
    r"\blet me\b",
    r"\bLet me\b",
    r"no wait",
    r"\brecheck\b",
    r"\bActually, I think\b",
    r"\bI think the\b",
    r"getting complex",
    r"getting messy",
    r"this isn't working",
    r"just trust the answer",
]
UNRESOLVED = [
    r"but the answer is",
    r"but the answer key",
    r"the paper says",
    r"just trust the answer",
]


def scan(path: Path):
    heading = "(top of file)"
    out = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("#"):
            heading = line.lstrip("# ").strip() or heading
        hit = next((p for p in PATTERNS if re.search(p, line)), None)
        if hit:
            out.append((heading, i, line.strip(), any(re.search(u, line) for u in UNRESOLVED)))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    total = 0
    open_items = 0
    for path in sorted(SOLUTIONS.glob("*.md")):
        rows = scan(path)
        if not rows:
            continue
        by_heading: dict[str, int] = {}
        for heading, _line, _text, unresolved in rows:
            by_heading[heading] = by_heading.get(heading, 0) + 1
            open_items += unresolved
        total += len(rows)
        print("%-34s %2d note(s) in %d section(s)" % (path.name, len(rows), len(by_heading)))
        for heading, n in by_heading.items():
            print("    %-60s x%d" % (heading[:60], n))

    print()
    print("draft-narrative lines: %d   (of which unresolved vs. the key: %d)" % (total, open_items))
    if total:
        print("Sections above still read like a scratch pad - see docs/OPEN-ITEMS.md.")
    if args.strict and total:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
