#!/usr/bin/env python3
"""Render vault figures to plain SVG - no Obsidian plugin required.

WHY THIS EXISTS
---------------
Molren, Ketcher, Plot Vectors and Graphs, Circuit Sketcher (and friends) are
published with `"isDesktopOnly": true`.  Obsidian's community-plugin browser
hides them on Android/iOS and refuses to enable them, reporting
"This plugin does not support your device".

This script removes the dependency completely: figures are rendered **ahead of
time** into plain `.svg` files that are committed to the vault.  Every Obsidian
client (Android, iOS, Windows, macOS, Linux) displays SVG natively, in Live
Preview and Reading view, with zero community plugins - and the same files work
in PDF exports, on GitHub and in any Markdown viewer.

WHAT IT DOES
------------
It scans the vault for three fenced block types and replaces each one with an
embed of a generated SVG:

    ```smiles     RDKit (or Indigo) draws the molecule
                  replaces: Molren, Ketcher
    ```plot       matplotlib plots y = f(x)
                  replaces: Plot Vectors and Graphs, Desmos (static), pgfplots
    ```circuit    schemdraw draws a circuit or vector diagram
                  replaces: Circuit Sketcher, circuitikz

    Before:                            After:
    ```smiles                          ![[assets/diagrams/smiles-1a2b3c4d5e.svg]]
    CC(=O)Oc1ccccc1C(=O)O Aspirin
    ```

The original source text is kept in `assets/diagrams/figures.json`, so the build
is idempotent, re-runnable and reversible (`--restore`).

USAGE
-----
    python3 tools/render_figures.py              # build all figures
    python3 tools/render_figures.py --check      # CI: exit 1 if figures are stale
    python3 tools/render_figures.py --restore    # put the code blocks back
    python3 tools/render_figures.py --prune      # delete orphaned SVG files
    python3 tools/render_figures.py --force      # re-render everything

Requires: matplotlib + schemdraw, and RDKit or epam.indigo for chemistry
(see tools/requirements.txt).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

KINDS = ("smiles", "plot", "circuit")

FIGURE_DIR = Path("assets/diagrams")
REGISTRY = FIGURE_DIR / "figures.json"

# Directories that never contain vault notes we should rewrite.
SKIP_DIRS = {".git", ".obsidian", ".obsidian-mobile", "node_modules",
             "tools", "templates", ".github"}

CELL_W, CELL_H, LABEL_H = 440, 330, 34
LABEL_FONT = "DejaVu Sans, Helvetica Neue, Arial, sans-serif"


# --------------------------------------------------------------------------- #
# Small SVG helpers
# --------------------------------------------------------------------------- #

SVG_OPEN_RE = re.compile(r"<svg[^>]*>", re.DOTALL)


def _svg_open(svg: str) -> str:
    m = SVG_OPEN_RE.search(svg)
    if not m:
        raise ValueError("not an SVG document")
    return m.group(0)


def _svg_inner(svg: str) -> str:
    m = SVG_OPEN_RE.search(svg)
    return svg[m.end():svg.rindex("</svg>")]


def _svg_size(svg: str) -> tuple[float, float]:
    head = _svg_open(svg)
    vb = re.search(r'viewBox="\s*([\d.eE+-]+)[ ,]+([\d.eE+-]+)[ ,]+([\d.eE+-]+)[ ,]+([\d.eE+-]+)', head)
    if vb:
        return float(vb.group(3)), float(vb.group(4))
    w = re.search(r'width="([\d.]+)', head)
    h = re.search(r'height="([\d.]+)', head)
    return float(w.group(1)) if w else 400.0, float(h.group(1)) if h else 300.0


def _prefix_ids(svg: str, prefix: str) -> str:
    """Namespace every id so several molecule SVGs can live in one document."""
    for ident in sorted(set(re.findall(r'id="([^"]+)"', svg)), key=len, reverse=True):
        safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in ident)
        svg = svg.replace('id="%s"' % ident, 'id="%s%s"' % (prefix, safe))
        svg = svg.replace('href="#%s"' % ident, 'href="#%s%s"' % (prefix, safe))
        svg = svg.replace('url(#%s)' % ident, 'url(#%s%s)' % (prefix, safe))
    return svg


def _escape(text: str) -> str:
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _normalize_svg(path: Path) -> None:
    """Strip volatile metadata so a re-render is byte-identical (CI `--check`).

    matplotlib stamps every SVG with a creation timestamp; without this every
    build would look like a change to git even when the figure is identical.
    """
    svg = path.read_text(encoding="utf-8")
    svg = re.sub(r"[ \t]*<dc:date>[^<]*</dc:date>\n?", "", svg)
    svg = re.sub(r"[ \t]*<dc:creator>[^<]*</dc:creator>\n?", "", svg)
    svg = re.sub(r"<!--[^>]*?Generator[^>]*?-->\n?", "", svg)
    path.write_text(svg, encoding="utf-8")


def _white_background(svg: str) -> str:
    """Force an opaque white background so figures read well in dark themes."""
    head = _svg_open(svg)
    if re.search(r"<rect[^>]*(?:width=[\"']100%[\"']|class=[\"']bg[\"'])[^>]*>", svg):
        return svg
    w, h = _svg_size(svg)
    rect = '<rect x="0" y="0" width="%g" height="%g" fill="#ffffff"/>' % (w, h)
    m = SVG_OPEN_RE.search(svg)
    return svg[:m.end()] + rect + svg[m.end():]


def _arrow(cx: float, cy: float, half: float = 26.0) -> str:
    """A font-independent right arrow (no glyph dependency)."""
    return (
        '<g stroke="#1a1a1a" stroke-width="2.2" fill="#1a1a1a">'
        '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
        '<polygon stroke="none" points="%.1f,%.1f %.1f,%.1f %.1f,%.1f"/></g>'
        % (cx - half, cy, cx + half - 9, cy,
           cx + half, cy, cx + half - 9, cy - 6, cx + half - 9, cy + 6)
    )


def _plus(cx: float, cy: float, half: float = 9.0) -> str:
    """A font-independent plus sign."""
    return (
        '<g stroke="#1a1a1a" stroke-width="2.2">'
        '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
        '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/></g>'
        % (cx - half, cy, cx + half, cy, cx, cy - half, cx, cy + half)
    )


def _compose_rows(rows, out: Path, cell_w: int = 340, cell_h: int = 300,
                  label_h: int = 34, gap_w: int = 86) -> None:
    """Stack one source line per row; a row may mix molecules, + signs and arrows.

    rows: list of rows; each row is a list of (kind, payload, label) where kind is
    "mol" | "arrow" | "plus".  The caption of a row is taken from its first item.
    """
    def row_width(row):
        return sum(cell_w if item[0] == "mol" else gap_w for item in row)

    width = max(row_width(row) for row in rows) + 24
    height = 12
    for row in rows:
        height += cell_h + (label_h if row[0][2] else 0) + 6

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        'width="%d" height="%d" viewBox="0 0 %d %d">' % (width, height, width, height),
        '<rect x="0" y="0" width="%d" height="%d" fill="#ffffff"/>' % (width, height),
    ]
    y = 12
    tag = 0
    for row in rows:
        rw = row_width(row)
        x = (width - rw) / 2
        caption = row[0][2]
        cy = y + cell_h / 2
        for kind, payload, _label in row:
            if kind == "mol":
                vb_w, vb_h = _svg_size(payload)
                scale = min(cell_w / vb_w, cell_h / vb_h)
                tx = x + (cell_w - vb_w * scale) / 2
                ty = y + (cell_h - vb_h * scale) / 2
                inner = _prefix_ids(_svg_inner(payload), "c%d-" % tag)
                tag += 1
                parts.append('<g transform="translate(%.2f,%.2f) scale(%.4f)">%s</g>'
                             % (tx, ty, scale, inner))
                x += cell_w
            elif kind == "arrow":
                parts.append(_arrow(x + gap_w / 2, cy))
                x += gap_w
            elif kind == "plus":
                parts.append(_plus(x + gap_w / 2, cy))
                x += gap_w
        if caption:
            parts.append(
                '<text x="%.1f" y="%.1f" text-anchor="middle" font-family="%s" '
                'font-size="17" fill="#111111">%s</text>'
                % (width / 2, y + cell_h + label_h * 0.7, LABEL_FONT, _escape(caption))
            )
        y += cell_h + (label_h if caption else 0) + 6
    parts.append("</svg>")
    out.write_text("\n".join(parts), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Chemistry:  ```smiles  ->  one molecule per line, optional label
# --------------------------------------------------------------------------- #

_CHEM_CACHE = {}


def _chemistry_backend():
    """Pick the chemistry engine, deterministically.

    **Indigo first** (the engine behind Ketcher): it installs as a plain wheel with no
    system libraries, so a laptop, a CI runner and a container all produce
    *byte-identical* molecules - which is what `--check` depends on. RDKit is the
    fallback, preferred only when Indigo is absent, because on Linux RDKit's SVG
    renderer needs libXrender.

    Force one with PRESCORE_CHEM=rdkit (or =indigo), e.g. when migrating the vault.
    """
    if _CHEM_CACHE:
        return _CHEM_CACHE["name"], _CHEM_CACHE["draw"]

    import os
    forced = os.environ.get("PRESCORE_CHEM", "").strip().lower()

    def try_indigo():
        from indigo import Indigo
        from indigo.renderer import IndigoRenderer

        indigo = Indigo()
        renderer = IndigoRenderer(indigo)
        indigo.setOption("render-background-color", "255,255,255")
        indigo.setOption("render-atom-ids-visible", "false")
        indigo.setOption("render-implicit-hydrogens-visible", "true")
        # wedges already convey stereochemistry; without this Indigo stamps a
        # "Chiral" flag over every stereocentre
        for opt in ("render-stereo-style", "render-stereo-style-old"):
            try:
                indigo.setOption(opt, "none")
            except Exception:  # noqa: BLE001 - option name varies by Indigo version
                pass

        def draw(smiles: str, w: int, h: int) -> str:
            import tempfile as _tf

            indigo.setOption("render-image-width", str(w))
            indigo.setOption("render-image-height", str(h))
            mol = indigo.loadMolecule(smiles)
            with _tf.NamedTemporaryFile(suffix=".svg", delete=False) as fh:
                tmp = fh.name
            try:
                renderer.renderToFile(mol, tmp)
                return Path(tmp).read_text(encoding="utf-8")
            finally:
                Path(tmp).unlink(missing_ok=True)

        draw("C", 60, 60)                      # prove it really works
        return draw

    def try_rdkit():
        from rdkit import Chem
        from rdkit.Chem import AllChem
        from rdkit.Chem.Draw import rdMolDraw2D

        def draw(smiles: str, w: int, h: int) -> str:
            mol = Chem.MolFromSmiles(smiles)
            if mol is None:
                raise ValueError("RDKit cannot parse SMILES %r" % smiles)
            AllChem.Compute2DCoords(mol)
            drawer = rdMolDraw2D.MolDraw2DSVG(w, h)
            opts = drawer.drawOptions()
            opts.addStereoAnnotation = False   # wedges carry the stereo info
            opts.bondLineWidth = 2
            opts.minFontSize = 13
            opts.maxFontSize = 20
            opts.padding = 0.08
            drawer.DrawMolecule(mol)
            drawer.FinishDrawing()
            return drawer.GetDrawingText()

        draw("C", 60, 60)
        return draw

    candidates = {"indigo": try_indigo, "rdkit": try_rdkit}
    order = [forced] if forced in candidates else ["indigo", "rdkit"]
    for name in order:
        try:
            draw = candidates[name]()
        except Exception:  # noqa: BLE001 - move on to the next engine
            continue
        _CHEM_CACHE.update(name=name, draw=draw)
        return name, draw
    raise RuntimeError("no chemistry engine available: "
                       "pip install epam.indigo (preferred) or rdkit")


def chemistry_backend_name():
    """Name of the engine that will draw molecules, or None if none is installed."""
    try:
        return _chemistry_backend()[0]
    except Exception:  # noqa: BLE001
        return None


def render_smiles(source: str, out: Path, width: int, height: int) -> None:
    """One line per entry: `SMILES caption` or `A.B>>C+D caption` for a reaction."""
    _backend, draw = _chemistry_backend()
    rows = []
    for raw in source.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(None, 1)
        smiles, caption = parts[0], (parts[1] if len(parts) > 1 else "")
        left_species, right_species = None, None
        if ">>" in smiles:
            left, right = smiles.split(">>", 1)
            left_species = [p for p in left.split(".") if p]
            right_species = [p for p in right.split(".") if p]
            species = left_species + right_species
        else:
            species = [smiles]

        row = []
        for i, smi in enumerate(species):
            if left_species is not None and i == len(left_species):
                row.append(("arrow", None, None))
            elif i > 0:
                row.append(("plus", None, None))
            row.append(("mol", draw(smi, CELL_W, CELL_H), None))
        row[0] = (row[0][0], row[0][1], caption)
        rows.append(row)
    if not rows:
        raise ValueError("empty smiles block")
    _compose_rows(rows, out, cell_w=CELL_W, cell_h=CELL_H)


# --------------------------------------------------------------------------- #
# Maths:  ```plot  -> y = f(x) curves
# --------------------------------------------------------------------------- #

FUNCTION_NAMES = {
    "sin", "cos", "tan", "arcsin", "arccos", "arctan", "sinh", "cosh", "tanh",
    "exp", "log", "log10", "sqrt", "abs", "floor", "ceil", "sign",
    "min", "max", "H", "heaviside",
}

TOKEN_RE = re.compile(
    r"\*\*"                                    # power
    r"|\d+\.\d*(?:[eE][+-]?\d+)?|\d+(?:[eE][+-]?\d+)?"   # 12, 1.5, 1e-3
    r"|\.\d+"                                  # .5
    r"|[A-Za-z_]\w*"                           # names
    r"|[()+\-*/,]"                             # operators
    r"|\."                                     # attribute access
    r"|\s+"                                    # whitespace
)


def pythonize(expr: str) -> str:
    """Textbook notation -> a Python/numpy expression.

    `x^3 - 3x + 1` -> `x**3 - 3*x + 1`, `2sin(x)` -> `2*sin(x)`,
    `ln(x)` -> `log(x)`, `|x|` -> `abs(x)`.

    Implicit multiplication is inserted token by token, so `**` is never
    mangled (the bug that turned `x^3` into a constant in the first release).
    """
    e = expr.strip()
    e = e.replace("\u2212", "-")                 # unicode minus
    e = e.replace("\u00b7", "*").replace("\u00d7", "*")
    e = e.replace("^", "**")
    e = re.sub(r"\|([^|]+)\|", r"abs(\1)", e)    # |x| -> abs(x)
    e = re.sub(r"\bln\s*\(", "log(", e)
    e = re.sub(r"\basin\b", "arcsin", e)
    e = re.sub(r"\bacos\b", "arccos", e)
    e = re.sub(r"\batan\b", "arctan", e)

    out = []
    prev = None            # "num" | "name" | "close" | "op" | "open"
    last_name = None
    for m in TOKEN_RE.finditer(e):
        tok = m.group(0)
        if tok.isspace():
            out.append(" ")
            continue
        if tok == "**":
            cur = "op"
        elif tok[0].isdigit() or (tok[0] == "." and len(tok) > 1):
            cur = "num"
        elif tok[0].isalpha() or tok[0] == "_":
            cur = "name"
        elif tok == "(":
            cur = "open"
        elif tok == ")":
            cur = "close"
        else:
            cur = "op"

        implicit = (
            (prev in ("num", "close") and cur in ("num", "name", "open"))
            or (prev == "name" and cur in ("num", "open") and last_name not in FUNCTION_NAMES)
        )
        if implicit:
            out.append("*")
        out.append(tok)
        if cur == "name":
            last_name = tok
        elif cur != "open":
            last_name = None
        prev = cur
    return "".join(out).strip()


def make_namespace():
    """A tiny namespace for evaluating plot expressions (no builtins)."""
    import numpy as np

    return {
        "__builtins__": {},
        "x": None, "np": np,
        "sin": np.sin, "cos": np.cos, "tan": np.tan,
        "arcsin": np.arcsin, "arccos": np.arccos, "arctan": np.arctan,
        "sinh": np.sinh, "cosh": np.cosh, "tanh": np.tanh,
        "exp": np.exp, "log": np.log, "log10": np.log10, "sqrt": np.sqrt,
        "abs": np.abs, "floor": np.floor, "ceil": np.ceil, "sign": np.sign,
        "pi": np.pi, "e": np.e, "min": np.minimum, "max": np.maximum,
        "H": np.heaviside, "heaviside": np.heaviside,
    }


def render_plot(source: str, out: Path, width: int, height: int) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    matplotlib.rcParams["svg.fonttype"] = "path"      # identical on every device
    matplotlib.rcParams["svg.hashsalt"] = "prescore"  # deterministic output
    matplotlib.rcParams["font.family"] = "DejaVu Sans"
    matplotlib.rcParams["mathtext.fontset"] = "dejavusans"

    x_min, x_max, y_min, y_max = -5.0, 5.0, None, None
    grid, title, samples = True, None, 1200
    curves = []

    colours = ["#0b5fa5", "#c1440e", "#1b7f4d", "#7b2d8b", "#8a6d00"]
    styles = ["-", "--", ":", "-."]

    for raw in source.splitlines():
        line = raw.split("#", 1)[0].strip() if not raw.strip().startswith("#") else ""
        if not line:
            continue
        m = re.match(r"^(x|y)\s*:\s*\[\s*([-0-9.eE+]+)\s*,\s*([-0-9.eE+]+)\s*\]$", line, re.I)
        if m:
            lo, hi = float(m.group(2)), float(m.group(3))
            if m.group(1).lower() == "x":
                x_min, x_max = lo, hi
            else:
                y_min, y_max = lo, hi
            continue
        m = re.match(r"^(grid|title|samples|points|width|height)\s*:\s*(.+)$", line, re.I)
        if m:
            key, value = m.group(1).lower(), m.group(2).strip().strip('"\'')
            if key == "grid":
                grid = value.lower() in ("true", "yes", "on", "1")
            elif key == "title":
                title = value
            elif key in ("samples", "points"):
                samples = max(50, int(float(value)))
            elif key == "width":
                width = max(240, int(float(value)))
            elif key == "height":
                height = max(160, int(float(value)))
            continue
        label = None
        if "@" in line:
            line, label = line.split("@", 1)
            label = label.strip()
        expr = line.strip()
        m = re.match(r"^(?:y\s*=\s*)?(.+)$", expr)
        if m:
            curves.append((label, m.group(1).strip()))
    if not curves:
        raise ValueError("plot block has no equations (write e.g. `y = x^2 - 1`)")

    fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=100)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    xs = np.linspace(x_min, x_max, samples)
    ns = make_namespace()
    ns["x"] = xs
    for i, (label, expr) in enumerate(curves):
        try:
            ys = eval(pythonize(expr), ns)  # noqa: S307 - vault-local, no builtins
        except Exception as exc:  # noqa: BLE001
            raise ValueError("cannot evaluate %r (%s)" % (expr, exc)) from exc
        ys = np.broadcast_to(np.asarray(ys, dtype=float), xs.shape).astype(float)
        ax.plot(xs, np.where(np.isfinite(ys), ys, np.nan),
                styles[i % len(styles)], color=colours[i % len(colours)],
                linewidth=2.0, label=label or ("y = " + expr), zorder=3)

    ax.set_xlim(x_min, x_max)
    if y_min is not None and y_max is not None:
        ax.set_ylim(y_min, y_max)
    ax.axhline(0, color="#444444", linewidth=1.0, zorder=2)
    ax.axvline(0, color="#444444", linewidth=1.0, zorder=2)
    ax.grid(grid, color="#c9d3dd", linewidth=0.8, zorder=1)
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color("#444444")
    ax.tick_params(colors="#333333", labelsize=11)
    ax.set_xlabel("x", color="#222222", fontsize=13)
    ax.set_ylabel("y", color="#222222", fontsize=13)
    if title:
        ax.set_title(title, color="#111111", fontsize=14)
    if len(curves) > 1 or any(label for label, _ in curves):
        leg = ax.legend(loc="best", fontsize=10, framealpha=0.9)
        for text in leg.get_texts():
            text.set_color("#111111")

    fig.tight_layout()
    fig.savefig(out, format="svg", facecolor="white",
                metadata={"Date": None, "Creator": None})
    plt.close(fig)
    _normalize_svg(out)


# --------------------------------------------------------------------------- #
# Physics:  ```circuit  -> schemdraw code (circuitikz-flavoured)
# --------------------------------------------------------------------------- #

def render_circuit(source: str, out: Path, width: int, height: int) -> None:
    import matplotlib
    matplotlib.use("Agg")
    matplotlib.rcParams["svg.fonttype"] = "path"
    matplotlib.rcParams["svg.hashsalt"] = "prescore"
    matplotlib.rcParams["font.family"] = "DejaVu Sans"

    import schemdraw
    import schemdraw.elements as elm

    body = _dedent(source).strip("\n")
    if not body.strip():
        raise ValueError("empty circuit block")

    schemdraw.use("matplotlib")
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=13, lw=1.6)
        env = {"d": d, "elm": elm, "schemdraw": schemdraw,
               "__builtins__": __builtins__, "print": print}
        try:
            exec(compile(body, "<circuit>", "exec"), env)  # noqa: S102
        except Exception as exc:  # noqa: BLE001
            raise ValueError("circuit code failed: %s" % exc) from exc
        d.save(str(out), dpi=110, transparent=False)
    out.write_text(_white_background(out.read_text(encoding="utf-8")), encoding="utf-8")
    _normalize_svg(out)


def _dedent(text: str) -> str:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return text
    pad = min(len(ln) - len(ln.lstrip()) for ln in lines)
    return "\n".join(ln[pad:] if ln.strip() else ln for ln in text.splitlines())


RENDERERS = {"smiles": render_smiles, "plot": render_plot, "circuit": render_circuit}


# --------------------------------------------------------------------------- #
# Vault scanning
# --------------------------------------------------------------------------- #

FENCE_OPEN_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<ticks>`{3,})(?P<kind>[A-Za-z0-9_-]*)[ \t]*(?P<spec>[^\n]*)$")


def scan_fences(text: str):
    """Yield fenced blocks, correctly ignoring fences nested in longer fences.

    A ````markdown block that *documents* a ```smiles block must not be touched,
    so the closing fence has to be at least as long as the opening one.
    """
    lines = text.splitlines(keepends=True)
    i = 0
    while i < len(lines):
        m = FENCE_OPEN_RE.match(lines[i].rstrip("\n"))
        if not m:
            i += 1
            continue
        ticks = len(m.group("ticks"))
        closing = re.compile(r"^[ \t]*`{%d,}[ \t]*$" % ticks)
        j = i + 1
        while j < len(lines) and not closing.match(lines[j].rstrip("\n")):
            j += 1
        if j >= len(lines):        # unterminated fence - ignore
            break
        yield {
            "kind": m.group("kind"),
            "spec": m.group("spec").strip(),
            "indent": m.group("indent"),
            "ticks": m.group("ticks"),
            "body": "".join(lines[i + 1:j]),
            "start": i,
            "end": j,               # index of the closing line
        }
        i = j + 1


def iter_notes(root: Path):
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts[:-1]):
            continue
        yield path


def figure_id(kind: str, source: str) -> str:
    digest = hashlib.sha1(("%s\0%s" % (kind, source.strip())).encode("utf-8")).hexdigest()
    return "%s-%s" % (kind, digest[:10])


def load_registry(root: Path) -> dict:
    path = root / REGISTRY
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"version": 1, "figures": {}}


def save_registry(root: Path, reg: dict) -> None:
    path = root / REGISTRY
    path.parent.mkdir(parents=True, exist_ok=True)
    figures = reg.setdefault("figures", {})
    reg["figures"] = {k: figures[k] for k in sorted(figures)}
    path.write_text(json.dumps(reg, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def render_one(root: Path, record: dict, out_path: Path, quiet: bool = False) -> bool:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        RENDERERS[record["kind"]](record["source"], out_path, 900, 470)
    except Exception as exc:  # noqa: BLE001
        print("  FAILED  %s: %s" % (record.get("file", out_path.name), exc), file=sys.stderr)
        return False
    if not quiet:
        print("  render  %s" % record.get("file", out_path.name))
    return True


# --------------------------------------------------------------------------- #
# Commands
# --------------------------------------------------------------------------- #

def cmd_build(root: Path, args) -> int:
    reg = load_registry(root)
    figures = reg.setdefault("figures", {})

    by_file = {Path(r["file"]).name: fid for fid, r in figures.items()}
    referenced = set()

    # The molecules are drawn by Indigo or RDKit, and the two never agree pixel for
    # pixel. Record which engine produced the committed files; when it changes, the
    # molecules are re-rendered so the vault stays self-consistent.
    backend = chemistry_backend_name()
    recorded = reg.get("chemistry_backend")
    rerender_smiles = False
    if backend and recorded and recorded != backend:
        print("  note    chemistry engine changed: %s -> %s; re-rendering molecules"
              % (recorded, backend))
        rerender_smiles = True
    if backend:
        reg["chemistry_backend"] = backend

    # ---- phase 1: discover fences, register figures ----------------------- #
    plan = []          # (note_path, blocks, [figure ids in order])
    for note in iter_notes(root):
        text = note.read_text(encoding="utf-8")
        rel = note.relative_to(root).as_posix()

        # figures that are already embedded in this note stay referenced
        for m in re.finditer(r"!\[\[([^\]|]+)", text):
            fid = by_file.get(Path(m.group(1).strip()).name)
            if fid:
                referenced.add(fid)
                notes = figures[fid].setdefault("notes", [])
                if rel not in notes:
                    notes.append(rel)
                    notes.sort()

        blocks = [b for b in scan_fences(text) if b["kind"] in KINDS]
        if not blocks:
            continue
        ids = []
        for block in blocks:
            fid = figure_id(block["kind"], block["body"])
            ids.append(fid)
            referenced.add(fid)
            record = figures.get(fid)
            if record is None:
                record = {
                    "kind": block["kind"],
                    "source": block["body"].rstrip("\n"),
                    "spec": block["spec"],
                    "file": "%s/%s.svg" % (FIGURE_DIR.as_posix(), fid),
                }
                figures[fid] = record
            if block["spec"]:
                record["spec"] = block["spec"]
            notes = record.setdefault("notes", [])
            if rel not in notes:
                notes.append(rel)
                notes.sort()
        plan.append((note, text, blocks, ids))

    for fid in sorted(set(figures) - referenced):
        record = figures.pop(fid)
        print("  drop    %s (no longer referenced by any note)" % record["file"])

    # ---- phase 2: render every registered figure --------------------------- #
    ok = {}
    tmp_ctx = tempfile.TemporaryDirectory() if args.check else None
    tmp_root = Path(tmp_ctx.name) if tmp_ctx else None

    for fid, record in sorted(figures.items()):
        target = root / record["file"]
        if args.check:
            ok[fid] = render_one(root, record, tmp_root / record["file"], quiet=True)
        elif args.force or not target.exists() or (rerender_smiles and record["kind"] == "smiles"):
            ok[fid] = render_one(root, record, target)
        else:
            ok[fid] = True

    # ---- phase 3: rewrite notes (only blocks that rendered) ---------------- #
    edits = 0
    for note, text, blocks, ids in plan:
        if args.restore:
            continue
        lines = text.splitlines(keepends=True)
        # replace from the bottom so earlier offsets stay valid
        for block, fid in sorted(zip(blocks, ids), key=lambda p: p[0]["start"], reverse=True):
            if not ok.get(fid):
                continue
            record = figures[fid]
            width = ""
            m = re.search(r"width\s*[=:]\s*(\d+)", block["spec"], re.I)
            if m:
                width = "|" + m.group(1)
            embed = "![[%s%s]]\n" % (record["file"], width)
            lines[block["start"]:block["end"] + 1] = [embed]
            edits += 1
        new_text = "".join(lines)
        if new_text != text:
            if not args.dry_run:
                note.write_text(new_text, encoding="utf-8")
            print("  notes   %s" % note.relative_to(root).as_posix())

    # ---- phase 4: staleness report (CI) ------------------------------------ #
    stale = []
    if args.check and tmp_root is not None:
        engine_ok = (backend is None or recorded is None or backend == recorded)
        if not engine_ok:
            print("\nWARNING: the committed molecules were drawn with %r but this machine\n"
                  "         has %r; skipping the molecule comparison (cosmetic difference).\n"
                  "         Install the recorded engine or run without --check to migrate."
                  % (recorded, backend))
        for fid, record in sorted(figures.items()):
            committed = root / record["file"]
            if record["kind"] == "smiles" and not engine_ok:
                continue
            if not ok.get(fid) or not committed.exists():
                stale.append(record["file"])
            elif committed.read_bytes() != (tmp_root / record["file"]).read_bytes():
                stale.append(record["file"])
        tmp_ctx.cleanup()

    pending = sum(1 for fid in figures if not (root / figures[fid]["file"]).exists())

    if not args.dry_run:
        save_registry(root, reg)

    print("\n%d figure(s) in registry, %d block(s) rewritten, %d still missing"
          % (len(figures), edits, pending))
    if stale:
        print("\nSTALE figures - run `python3 tools/render_figures.py`:")
        for s in stale:
            print("  " + s)
    if pending and not args.check:
        print("\n%d figure(s) could not be rendered (see errors above)" % pending, file=sys.stderr)
        return 1
    if args.check and stale:
        return 1
    return 0


def cmd_restore(root: Path, args) -> int:
    """Put the original source fences back in place of the embeds."""
    figures = load_registry(root).get("figures", {})
    if not figures:
        print("nothing to restore (registry is empty)")
        return 0
    by_name = {}
    for record in figures.values():
        by_name[Path(record["file"]).name] = record
        by_name[Path(record["file"]).stem] = record

    embed_re = re.compile(r"^[ \t]*!\[\[(?P<path>[^\]|]+)(?:\|[^\]]*)?\]\][ \t]*\n?", re.MULTILINE)
    touched = 0
    for note in iter_notes(root):
        text = note.read_text(encoding="utf-8")

        def repl(match):
            name = Path(match.group("path").strip()).name
            record = by_name.get(name) or by_name.get(Path(name).stem)
            if not record:
                return match.group(0)
            spec = (" " + record["spec"]) if record.get("spec") else ""
            return "```%s%s\n%s\n```\n" % (record["kind"], spec, record["source"])

        new_text = embed_re.sub(repl, text)
        if new_text != text:
            touched += 1
            if not args.dry_run:
                note.write_text(new_text, encoding="utf-8")
            print("  restored %s" % note.relative_to(root).as_posix())
    print("\n%d note(s) restored" % touched)
    return 0


def cmd_prune(root: Path, args) -> int:
    figures = load_registry(root).get("figures", {})
    keep = {Path(r["file"]).name for r in figures.values()}
    removed = 0
    fdir = root / FIGURE_DIR
    if fdir.exists():
        for svg in sorted(fdir.glob("*.svg")):
            if svg.name not in keep:
                removed += 1
                if not args.dry_run:
                    svg.unlink()
                print("  remove %s" % svg.relative_to(root).as_posix())
    print("\n%d orphaned file(s) removed" % removed)
    return 0


# --------------------------------------------------------------------------- #

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Render vault figures to plugin-free SVG.",
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=None, help="vault root (default: repo root)")
    p.add_argument("--check", action="store_true",
                   help="render to a temp dir; exit 1 if the committed SVGs differ")
    p.add_argument("--restore", action="store_true", help="re-insert the source fences")
    p.add_argument("--prune", action="store_true", help="delete unreferenced SVG files")
    p.add_argument("--force", action="store_true", help="re-render every figure")
    p.add_argument("--dry-run", action="store_true", help="show changes without writing")
    args = p.parse_args(argv)

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    print("vault: %s" % root)
    engine = chemistry_backend_name()
    print("chemistry engine: %s\n" % (engine or "none installed (smiles figures will fail)"))

    if args.restore:
        return cmd_restore(root, args)
    if args.prune:
        return cmd_prune(root, args)
    return cmd_build(root, args)


if __name__ == "__main__":
    sys.exit(main())
