#!/usr/bin/env python3
"""Audit question coverage per paper against the official answer keys.

For every solution note this reports

  * which question numbers of that paper are missing entirely,
  * which ones are present but "thin" (answer letter only, no working),

so a half-finished paper cannot pass unnoticed.

Usage:
    python3 tools/check_coverage.py            # table + gaps
    python3 tools/check_coverage.py --thin 14  # use a different thin threshold
    python3 tools/check_coverage.py --strict   # exit 1 if anything is missing
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS = ROOT / "solutions"

# question count per paper, straight off the printed answer keys
TOTALS = {
    "1-paper1": 51, "1-paper2": 51,
    "2-paper1": 54, "2-paper2": 54,
    "3-paper1": 48, "3-paper2": 48,
    "4-paper1": 57, "4-paper2": 57,
}

HEADING = re.compile(r"^#{2,4}\s+Q\.?\s*(\d+)\s*(?:[–\-—]\s*Q?\.?\s*(\d+))?")


def parse(path: Path):
    """Return {question_number: (heading, body_line_count)}."""
    lines = path.read_text(encoding="utf-8").splitlines()
    marks = []
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m:
            a = int(m.group(1))
            b = int(m.group(2)) if m.group(2) else a
            marks.append((i, a, b, line.strip()))
    out = {}
    for idx, (i, a, b, head) in enumerate(marks):
        end = marks[idx + 1][0] if idx + 1 < len(marks) else len(lines)
        body = [l for l in lines[i + 1:end] if l.strip() and not l.startswith("> [!")]
        for q in range(a, b + 1):
            out[q] = (head, len(body))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--thin", type=int, default=12,
                    help="a section with fewer non-blank body lines is 'thin'")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    missing_total = 0
    thin_total = 0
    print("%-22s %6s %8s %8s" % ("note", "Q total", "missing", "thin"))
    print("-" * 48)
    for name, total in TOTALS.items():
        path = SOLUTIONS / ("%s-solutions.md" % name)
        if not path.exists():
            print("%-22s %6d %8s %8s" % (name, total, "FILE", "-"))
            missing_total += total
            continue
        present = parse(path)
        missing = [q for q in range(1, total + 1) if q not in present]
        thin = [q for q, (_h, n) in sorted(present.items()) if q <= total and n < args.thin]
        missing_total += len(missing)
        thin_total += len(thin)
        print("%-22s %6d %8d %8d" % (name, total, len(missing), len(thin)))
        if missing:
            print("    missing: %s" % ",".join(map(str, missing)))
        if thin:
            print("    thin:    %s" % ",".join(map(str, thin)))

    print()
    print("questions not written at all : %d" % missing_total)
    print("questions with answer only  : %d" % thin_total)
    if missing_total:
        print("\nSee docs/OPEN-ITEMS.md for the plan; run make check after filling them in.")
    if args.strict and (missing_total or thin_total):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
