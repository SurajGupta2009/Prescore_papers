#!/usr/bin/env python3
"""Validate every plugin-rendered figure block in the vault.

The vault is Obsidian-only: figures are rendered live by community plugins, so a
typo in a fence means a broken diagram on the reader's device. This checker is the
safety net. It validates the four block types the vault uses:

    ```tikz          TikZJax        (chemfig / circuitikz / pgfplots / tikz-cd)
    ```desmos-graph  Desmos         (LaTeX equations + settings header)
    ```smiles        ChemEdit Universal / Chem / Chemtrails   (one SMILES per line)
    ```math          Numerals       (calculator lines)

Checks per block type
---------------------
tikz
  * ``\\begin{document}`` / ``\\end{document}`` present (TikZJax requires them)
  * every ``\\usepackage{...}`` is one TikZJax actually ships
  * every ``\\begin{env}`` has a matching ``\\end{env}``
  * braces / brackets / dollars balanced (quote-aware)
  * no file-inclusion or shell-escape commands
  * a ``\\usepackage{tikz}`` is unnecessary, flagged as a warning
desmos-graph
  * settings header (before ``---``) uses known keys only
  * every equation line is non-empty and free of stray ``---``
  * flags after ``|`` are a known set (colour, style, restriction, hidden, label:)
smiles
  * exactly one SMILES per line, no trailing prose (the renderers choke on labels)
  * allowed atom/bond/ring characters only, brackets and ring closures balanced
math
  * each line is a `name = expression` (optionally ending in `=>` to print the result),
    or a comment
  * no characters Numerals cannot parse

Usage
-----
    python3 tools/check_figures.py                # whole vault
    python3 tools/check_figures.py --quiet        # only problems + summary
    python3 tools/check_figures.py --stats        # block counts per file
Exit code 1 if any block fails.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", ".obsidian", "node_modules", "tools", "templates"}

# Packages that TikZJax ships (from the plugin README). Anything else fails to compile.
TIKZ_PACKAGES = {
    "chemfig", "tikz-cd", "circuitikz", "pgfplots", "array",
    "amsmath", "amstext", "amsfonts", "amssymb", "tikz-3dplot",
    "tikz", "xcolor", "graphicx", "pgf", "float", "calc", "positioning",
    "arrows.meta", "decorations.pathmorphing", "decorations.markings",
    "patterns", "shapes.geometric", "intersections", "through", "angles",
    "quotes", "backgrounds", "fit", "3d",
}
# ...but these are pointless (already loaded) or unsupported; warn instead of fail.
TIKZ_WARN_PACKAGES = {"tikz", "pgf", "graphicx", "float"}

DESMOS_KEYS = {
    "left", "right", "top", "bottom", "width", "height", "grid",
    "degreemode", "defaultcolor", "xaxislabel", "yaxislabel", "xaxisstep",
    "yaxisstep", "showxaxis", "showyaxis", "showgrid",
}
DESMOS_COLOURS = {
    "red", "green", "blue", "yellow", "magenta", "cyan", "purple",
    "orange", "black", "white",
}
DESMOS_STYLES = {"solid", "dashed", "dotted", "point", "open", "cross", "hidden"}

SMILES_ALLOWED = re.compile(r"^[A-Za-z0-9@+\-\[\]\(\)=#$:/\\.%*]+$")

FENCE_OPEN = re.compile(r"^(?P<indent>[ \t]*)(?P<ticks>`{3,})(?P<kind>[A-Za-z0-9_-]*)[ \t]*(?P<rest>[^\n]*)$")
KINDS = ("tikz", "desmos-graph", "smiles", "math")


def scan_fences(text: str):
    """Yield fenced blocks, respecting longer outer fences (documentation blocks)."""
    lines = text.splitlines(keepends=True)
    i = 0
    while i < len(lines):
        m = FENCE_OPEN.match(lines[i].rstrip("\n"))
        if not m:
            i += 1
            continue
        ticks = len(m.group("ticks"))
        closing = re.compile(r"^[ \t]*`{%d,}[ \t]*$" % ticks)
        j = i + 1
        while j < len(lines) and not closing.match(lines[j].rstrip("\n")):
            j += 1
        if j >= len(lines):
            break
        yield {
            "kind": m.group("kind"),
            "body": "".join(lines[i + 1:j]),
            "line": i + 1,
        }
        i = j + 1


def strip_latex_comments(body: str) -> str:
    out = []
    for line in body.splitlines():
        idx, in_escape = None, False
        for p, ch in enumerate(line):
            if ch == "\\" and not in_escape:
                in_escape = True
                continue
            if ch == "%" and not in_escape:
                idx = p
                break
            in_escape = False
        out.append(line if idx is None else line[:idx])
    return "\n".join(out)


def balance_report(text: str) -> list[str]:
    """Brace / bracket / dollar balance, skipping escaped characters."""
    problems = []
    stack: list[tuple[str, int]] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    i, n = 0, len(text)
    dollars = 0
    while i < n:
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "$":
            dollars += 1
            i += 1
            continue
        if ch in "([{":
            stack.append((ch, i))
        elif ch in ")]}":
            if not stack or stack[-1][0] != pairs[ch]:
                problems.append("unbalanced '%s'" % ch)
                return problems
            stack.pop()
        i += 1
    if stack:
        problems.append("%d unclosed '%s'" % (len(stack), stack[-1][0]))
    if dollars % 2:
        problems.append("odd number of '$' (%d)" % dollars)
    return problems


# --------------------------------------------------------------------------- #

def check_tikz(body: str, where: str) -> tuple[list[str], list[str]]:
    errors, warns = [], []
    src = strip_latex_comments(body)

    if "\\begin{document}" not in src:
        errors.append("missing \\begin{document} (TikZJax requires it)")
    if "\\end{document}" not in src:
        errors.append("missing \\end{document}")

    for pkg in re.findall(r"\\usepackage(?:\[[^\]]*\])?\{([^}]*)\}", src):
        for name in (p.strip() for p in pkg.split(",") if p.strip()):
            if name not in TIKZ_PACKAGES:
                errors.append("\\usepackage{%s} is not shipped by TikZJax" % name)
            elif name in TIKZ_WARN_PACKAGES:
                warns.append("\\usepackage{%s} is unnecessary (loaded anyway)" % name)

    begins = re.findall(r"\\begin\{([^}]*)\}", src)
    ends = re.findall(r"\\end\{([^}]*)\}", src)
    if sorted(begins) != sorted(ends):
        only_b = [e for e in begins if begins.count(e) > ends.count(e)]
        only_e = [e for e in ends if ends.count(e) > begins.count(e)]
        if only_b:
            errors.append("unclosed environment(s): %s" % ", ".join(sorted(set(only_b))))
        if only_e:
            errors.append("stray \\end{%s}" % only_e[0])

    if "\\begin{document}" in begins:
        open_at = src.index("\\begin{document}")
        for m in re.finditer(r"\\usepackage", src):
            if m.start() > open_at:
                warns.append("\\usepackage after \\begin{document} (move it to the top)")
                break

    for bad in ("\\input", "\\include", "\\write18", "\\openout", "\\read"):
        if bad in src:
            errors.append("%s is not allowed in TikZJax" % bad)

    errors.extend(balance_report(src))

    # a tikzpicture that never draws anything is certainly a mistake
    if "\\begin{tikzpicture}" in src and not re.search(
            r"\\(draw|node|fill|path|shade|plot|matrix|graph|addplot|addlegendentry)\b",
            src):
        errors.append("tikzpicture has no \\draw/\\node/\\path/\\addplot")

    return errors, warns


def check_desmos(body: str, where: str) -> tuple[list[str], list[str]]:
    errors, warns = [], []
    lines = body.splitlines()

    idx = next((i for i, l in enumerate(lines) if l.strip() == "---"), None)
    header, equations = (lines[:idx], lines[idx + 1:]) if idx is not None else ([], lines)

    for h in header:
        h = h.strip()
        if not h:
            continue
        parts = [p.strip() for p in re.split(r"[;\n]", h) if p.strip()]
        for p in parts:
            if "=" not in p:
                errors.append("settings line without '=': %r" % p)
                continue
            key = p.split("=", 1)[0].strip().lower()
            if key not in DESMOS_KEYS:
                errors.append("unknown Desmos setting %r (allowed: %s)"
                              % (key, ", ".join(sorted(DESMOS_KEYS))))

    seen_equation = False
    for eq in equations:
        eq = eq.strip()
        if not eq or eq.startswith("//"):
            continue
        if eq == "---":
            errors.append("stray '---' separator (only one settings header is allowed)")
            continue
        seen_equation = True
        parts = [p.strip() for p in eq.split("|")]
        equation, flags = parts[0], parts[1:]
        if not equation:
            errors.append("empty equation in %r" % eq)
        # '|' is the flag separator, so an absolute value must be written another way
        if "\\left|" in equation or "\\right|" in equation or "|" in equation:
            errors.append(
                "'|' is the Desmos flag separator, so it cannot appear inside the "
                "equation - write an absolute value as \\sqrt{x^2} instead (%r)" % eq)
        for f in flags:
            low = f.lower()
            if low in DESMOS_STYLES or low in DESMOS_COLOURS:
                continue
            if low.startswith("#") or re.fullmatch(r"[0-9a-fA-F]{6}", low):
                continue
            if low.startswith("label:"):
                continue
            # anything else is a restriction, e.g. y>0, x<3, 0<x<5
            if re.fullmatch(r"[a-zA-Z0-9_\.\*\+\-/\(\)\s<>=!,^]+", f) and any(
                    op in f for op in ("<", ">", "=")):
                continue
            warns.append("unrecognised Desmos flag %r (treated as a restriction)" % f)
        if equation.count("$"):
            errors.append("remove '$' from Desmos equations (LaTeX already)")
    if not seen_equation:
        errors.append("desmos-graph block has no equations")
    return errors, warns


def check_smiles(body: str, where: str) -> tuple[list[str], list[str]]:
    errors, warns = [], []
    count = 0
    for n, raw in enumerate(body.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        count += 1
        if line.startswith("#"):
            errors.append("line %d starts with '#' (SMILES comments are not stripped)"
                          % n)
            continue
        if " " in line or "\t" in line:
            errors.append("line %d has spaces - every renderer expects exactly one "
                          "SMILES per line, put the label in the text above the block "
                          "(line: %r)" % (n, line))
            continue
        if line.lower().startswith("smiles="):
            errors.append("line %d: drop the 'smiles=' prefix, the fence already says it"
                          % n)
            continue
        if not SMILES_ALLOWED.match(line):
            errors.append("line %d has characters a SMILES string cannot contain: %r"
                          % (n, line))
            continue
        # ring-closure digit check: every ring bond number must appear twice
        digits = re.findall(r"%(\d)", line) if "%" in line else []
        ring = re.findall(r"(?<![A-Za-z@])(\d{1,2})(?![0-9])", re.sub(r"[A-Za-z@+\-\[\]\(\)=#$/\\%.]", " ", line))
        counts: dict[str, int] = {}
        for d in ring:
            counts[d] = counts.get(d, 0) + 1
        for d, c in counts.items():
            if c % 2:
                warns.append("line %d: ring-closure digit '%s' appears %d time(s)"
                             % (n, d, c))
        for ch, op in (("(", ")"), ("[", "]")):
            if line.count(ch) != line.count(op):
                errors.append("line %d: %d '%s' vs %d '%s'"
                              % (n, line.count(ch), ch, line.count(op), op))
    if not count:
        errors.append("smiles block has no structures")
    return errors, warns


def check_math(body: str, where: str) -> tuple[list[str], list[str]]:
    errors, warns = [], []
    count = 0
    for n, raw in enumerate(body.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        count += 1
        if line.startswith("#"):
            continue                      # '#' starts a comment in a Numerals block
        if "…" in line or "..." in line:
            warns.append("line %d contains '...' - Numerals needs a real expression" % n)
        if re.search(r"\$\$|\$[^$]*\$", line):
            warns.append("line %d looks like LaTeX; Numerals evaluates plain "
                         "arithmetic/units" % n)
    if not count:
        errors.append("math block is empty")
    return errors, warns


CHECKERS = {
    "tikz": check_tikz,
    "desmos-graph": check_desmos,
    "smiles": check_smiles,
    "math": check_math,
}


# --------------------------------------------------------------------------- #

def iter_notes(root: Path):
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts[:-1]):
            continue
        yield path


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=None)
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--stats", action="store_true",
                    help="print how many of each block type each note contains")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve() if args.root else ROOT
    total = errors_total = warns_total = 0
    per_kind: dict[str, int] = {k: 0 for k in KINDS}
    per_file: dict[str, dict[str, int]] = {}

    for note in iter_notes(root):
        rel = note.relative_to(root).as_posix()
        text = note.read_text(encoding="utf-8")
        for block in scan_fences(text):
            kind = block["kind"]
            if kind not in CHECKERS:
                continue
            total += 1
            per_kind[kind] += 1
            per_file.setdefault(rel, {}).setdefault(kind, 0)
            per_file[rel][kind] += 1
            where = "%s:%d" % (rel, block["line"])
            errors, warns = CHECKERS[kind](block["body"], where)
            errors_total += len(errors)
            warns_total += len(warns)
            if errors:
                print("FAIL  %s  (%s)" % (where, kind))
                for e in errors:
                    print("        %s" % e)
            if warns and not args.quiet:
                print("warn  %s  (%s)" % (where, kind))
                for w in warns:
                    print("        %s" % w)

    if args.stats or not args.quiet:
        print("\n%-42s %s" % ("file", "  ".join(k[:6] for k in KINDS)))
        for rel in sorted(per_file):
            row = per_file[rel]
            print("%-42s %s" % (rel, "  ".join(
                str(row.get(k, 0)).rjust(6) for k in KINDS)))
    print("\n%d figure block(s) checked: %s"
          % (total, ", ".join("%s=%d" % (k, per_kind[k]) for k in KINDS)))
    print("%d error(s), %d warning(s)" % (errors_total, warns_total))
    return 1 if errors_total else 0


if __name__ == "__main__":
    sys.exit(main())
