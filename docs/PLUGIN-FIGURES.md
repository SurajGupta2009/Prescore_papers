# 🧩 Figures & Graphs — the plugin syntax reference

Every figure in this vault is drawn **live inside Obsidian by a community plugin**. Type the
block, the plugin renders it — nothing is pre-rendered, nothing is exported to an image
file, and editing the numbers updates the picture the moment you leave the block.

All of the plugins below are **mobile-capable** (`isDesktopOnly: false`), so the same note
renders on a phone and on a desktop.

| Block | Plugin (install ID) | Use it for | Notes |
|---|---|---|---|
| ```` ```tikz ```` | **TikZJax** (`obsidian-tikzjax`) | circuits, molecules, plots, geometry, every free-body/ray diagram | needs Obsidian **1.8.7+** — required for the φ↔π buttons and printing |
| ```` ```desmos-graph ```` | **Desmos** (`obsidian-desmos`) | function graphs, V–I characteristics, SHM, tangent lines | fully offline once the plugin is installed |
| ```` ```smiles ```` | **ChemEdit Universal** (`chemedit-universal`), or **Chem** (`chem`), or **Chemtrails** (`chemtrails`) | structures from SMILES | all three read the same `smiles` fence — pick any one |
| ```` ```math ```` | **Numerals** (`numerals`) | unit-aware calculations and checks | the ID is `numerals` (not `obsidian-numerals`) |

> [!warning] Install order matters
> Obsidian reads plugin enablement from this vault's config, so all four are already listed —
> you only have to install them: **Settings → Community plugins → Browse**, search the ID,
> *Install*, then toggle on. `tools/check_plugin_ids.py` verifies they exist and are
> mobile-capable.

---

## 1. TikZ / circuitikz — `tikz` blocks

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american, line width=0.8pt]
  \draw (0,0) to[battery1, l=$V$] (0,2.5)
        to[R, l=$R_1$] (3,2.5)
        to[C, l=$C$] (3,0)
        -- (0,0);
  \draw (3,2.5) to[R, l=$R_2$] (6,2.5) to[L, l=$L$] (6,0) -- (3,0);
\end{circuitikz}
\end{document}
```

**Rules the plugin enforces**

- `\begin{document}` … `\end{document}` are mandatory (TikZJax uses the `standalone` class).
- `\usepackage{...}` must come *before* `\begin{document}`.
- Packages that ship with TikZJax: `tikz`, `circuitikz`, `chemfig`, `pgfplots`, `tikz-cd`,
  `tikz-3dplot`, `amsmath`, `amstext`, `amsfonts`, `amssymb`, `array`, `xcolor`.
- `\input`, `\include`, `\write18` are blocked. (Since v0.5.x the TeX engine is bundled
  inside `main.js`, so rendering is offline — no CDN call.)
- Compilation is WASM: a phone renders a small circuit instantly, a 200-line pgfplots axis
  in a few seconds. Split giant figures into several blocks.

**Element vocabulary (circuitikz):** `[R]` resistor, `[C]` capacitor, `[L]` inductor,
`[battery1]`/`[battery2]` cell, `[sourceV]`/`[sourceI]`, `[sV]`/`[sI]` sinusoidal source,
`[D]`/`[D*]` diode, `[lamp]`, `[switch]`/`[nos]`, `[ammeter]`, `[voltmeter]`, `[Rvariable]`,
`[potentiometer]`, `[op amp]` (or the `op amp` node shape), `[ground]`, `[tlground]`.
Labels: `l=`, `l_=`, `a=`, `v=`, `i=`. Coordinates: `to[...] (x,y)` plus `--` for plain wire.

**Recipes copied out of the solutions in this vault**

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
% galvanometer as a circle (fill=white so it masks the wire behind it)
\draw (0,0) -- (1.4,0);
\node at (2.1,0) [circle, draw, fill=white, inner sep=1pt, minimum size=7mm]{$G$};
\draw (2.8,0) -- (4.6,0);
% a bridge arm drawn with an explicit resistance value
\draw (0,-1.5) to[R, a=$8\,\Omega$] (2.5,-1.5);
% current arrow
\draw[->, >=stealth, thick] (4.0,-0.4) -- (4.0,-1.1) node[midway,right]{$i(t)$};
% dots at nodes
\node at (0,-1.5) [circle, fill, inner sep=1.4pt]{};
\end{circuitikz}
\end{document}
```

**Other packages in the same fence**

```tikz
\usepackage{chemfig}
\begin{document}
\chemfig{H_3C-C(=[:60]O)-[:300]O-CH_2-CH_3}
\end{document}
```

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[width=9cm, height=6cm, grid=both, xlabel=$t$ (s), ylabel=$i$ (A)]
\addplot[thick, blue, domain=0:5, samples=120]{2*exp(-x)*sin(3*x r)};
\end{axis}
\end{tikzpicture}
\end{document}
```

Plain TikZ (no package needed beyond `tikz`) covers geometry, vectors, orbits, ray optics:

```tikz
\begin{document}
\begin{tikzpicture}[line width=0.9pt]
\draw[->, thick] (0,0) -- (3,0) node[right]{$\vec F_1$};
\draw[->, thick] (0,0) -- (0,2) node[above]{$\vec F_2$};
\draw[->, very thick, red] (0,0) -- (3,2) node[above right]{$\vec R$};
\draw[dashed] (3,0) -- (3,2);
\draw[dashed] (0,2) -- (3,2);
\end{tikzpicture}
\end{document}
```

---

## 2. Desmos — `desmos-graph` blocks

````markdown
```desmos-graph
left=-4; right=4
bottom=-8; top=8
width=800; height=420
grid=true
---
y=x^3-3x+1
y=3x-3|dashed|red|label:tangent at x=2
(1,-1)|open
```
````

```desmos-graph
left=-4; right=4
bottom=-8; top=8
height=420
grid=true
---
y=x^3-3x+1
y=3x-3|dashed|red
(1,-1)|open
```

- Everything **before** the `---` is settings: `left`, `right`, `top`, `bottom`, `width`,
  `height`, `grid`, `degreeMode`, `defaultColor` (separate pairs with `;` or newlines).
- Everything **after** is one equation per line, in Desmos/LaTeX syntax. Flags go after `|`
  in any order: a colour (`red`, `#c1440e`, …), a style (`solid`, `dashed`, `dotted`,
  `point`, `open`, `cross`), `hidden`, `label:text`, or a restriction (`y>0`).
- To graph a derivative, define the function on a hidden line and use `f'(x)` on the next.
- **`|` is the flag separator.** An absolute value cannot be written `\left|x\right|` —
  the plugin would read everything after the first pipe as flags. Use `\sqrt{x^2}`.

**V–I characteristic (used in the nonlinear-element questions):**

```desmos-graph
left=0; right=6
bottom=0; top=0.6
height=360
---
y=x^2/20
y=x^3/60
y=0.05x
```

---

## 3. Chemistry — `smiles` blocks

```smiles
CC(=O)Oc1ccccc1C(=O)O
```

- **Exactly one SMILES per line.** Do not append the compound name — `CC(=O)O Aspirin`
  fails to parse. Put the name in the sentence or an italic line above/below the block.
- Stereochemistry comes from `@`/`@@` (wedges appear automatically); charges as `[N+]`,
  `[O-]`; salts as separate lines.
- A reaction is not expressed in one line — draw the species on separate lines and write
  `→` in the text, or use `chemfig` arrows inside a `tikz` block.

Verified examples live throughout `solutions/` — e.g. `Nc1ccccc1` (aniline),
`Cc1cc(Cl)c(O)cc1C` (chloroxylenol), `CNC(=O)c1ccccc1` (N-methylbenzamide),
`C([C@@H]1[C@@H](...)...)O` (sucralose, 3 Cl).

> [!tip] Generating SMILES
> **ChemEdit Universal** has a ribbon icon (*Draw new molecule*) with a touch-friendly
> editor; press *Save* and it inserts the fence for you. On desktop, the Ketcher plugin
> does the same. Both round-trip through the same `smiles` block, so a structure drawn on a
> computer renders on the phone.

---

## 4. Calculations — `math` blocks (Numerals)

```math
# units are first-class; '=>' highlights the result, '#' starts a comment
eps0 = 9e-12 F/m
wdt = 0.32 m
len = 0.40 m
sep = 3 mm
thick = 2 mm
Kslab = 4
deff = thick/Kslab + (sep - thick) =>
c_ins = eps0 * wdt / deff =>
c_air = eps0 * wdt / sep =>
x0 = 0.10 m
cap0 = c_ins*x0 + c_air*(len - x0) =>
charge = cap0 * 6000 V =>
x = 0.20 m
cap = c_ins*x + c_air*(len - x) =>
force = charge^2/(2*cap^2)*(c_ins - c_air) =>
```

Numerals uses mathjs, so you also get `sqrt()`, `sin()`, `log()`, fractions, bases
(`0xff`), unit conversion (`72 degF to degC`) and **note-wide variables** via `$varname`.
Inline form inside a sentence: `` `#: 20 mi / 4 hr` ``.

> [!note] Why this is in the solutions
> Numerals is the honest replacement for "I did the arithmetic in my head and wrote the
> number down": the block shows the inputs, the unit handling and the result, and it
> re-checks itself if you change an input.

---

## 5. Freehand and diagrams without LaTeX

| Need | Use |
|---|---|
| Hand-drawn ray/force diagram on a phone | **Excalidraw** (`obsidian-excalidraw-plugin`) — `![[diagram.excalidraw]]` |
| Flowchart of a reaction scheme | **Mermaid** (core plugin, already enabled) |
| Whiteboard of the whole paper | **Canvas** (core plugin, already enabled) |
| Mind map of a topic | **Mind Map** (`obsidian-mind-map`) |

---

## 6. Checks

```bash
python3 tools/check_figures.py     # validates every tikz/desmos/smiles/math block
python3 tools/check_plugin_ids.py  # validates plugin IDs + mobile support
make check                         # both
```

`check_figures.py` catches the mistakes that silently produce an empty box in Obsidian:
a missing `\end{document}`, a `\begin{}` without its `\end{}`, an unbalanced brace, a
`\usepackage` TikZJax does not ship, a Desmos settings key that does not exist, two SMILES
on one line, or a SMILES with a stray space.
