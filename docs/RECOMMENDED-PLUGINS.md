# 🔌 Recommended Obsidian Plugins for JEE Advanced Solutions Vault

> Install these from **Settings → Community Plugins → Browse** in Obsidian.

> [!warning] 📱 On a phone or tablet?
> Four plugins in this vault are **desktop-only** (`molren`, `ketcher`, `plot-vectors-graphs`,
> `circuit-sketcher`) — Obsidian will show *“This plugin does not support your device”*. That is a
> deliberate flag by the plugin author, not a problem with your device.
> See **[MOBILE-GUIDE.md](MOBILE-GUIDE.md)** for the mobile-compatible alternatives, a ready-made
> `.obsidian-mobile` config folder, and copy-paste snippets.

**Legend:** 🖥️📱 = Desktop + Mobile · 🖥️ = Desktop only

---

## 🧪 Chemistry — Molecular Structures & Reactions

| Plugin | Platforms | What It Does | Use Case in This Vault |
|--------|-----------|-------------|----------------------|
| **[ChemEdit Universal](https://github.com/ruzx/ChemEdit-Universal)** | 🖥️📱 | Draw/edit SMILES & MOL structures offline (OpenChemLib — no wasm/iframe). Touch-friendly editor, property calculator. | **Best mobile choice.** Draw organic molecules, show reaction intermediates, display structures inline |
| **[Molren](https://github.com/quiachonj/molren)** | 🖥️ only | Render SMILES → SVG from fenced code blocks using RDKit.js (wasm inlined, ~7 MB). Offline. | Quick inline molecule rendering: `` ```smiles CC(=O)O `` ` |
| **[Chem](https://github.com/Acylation/obsidian-chem)** | 🖥️📱 | SMILES → structure (SmilesDrawer / optional RDKit). Copy/export PNG, Dataview support. | Mobile-friendly alternative to Molren |
| **[Ketcher](https://github.com/yulei-chen/obsidian-ketcher)** | 🖥️ only | Full molecule/reaction editor embedded in Obsidian, `.ket` files | Draw complex reaction mechanisms — use the [Ketcher web app](https://lifescience.opensource.epam.com/ketcher/) on mobile instead, then drop the SVG/MOL into the vault |
| **[TikZJax](https://github.com/artisticat1/obsidian-tikzjax)** (chemfig) | 🖥️📱 (heavy) | Render chemical structures via LaTeX `chemfig` | Precise bond-angle diagrams, Fischer projections, Haworth projections |

> [!tip] Enable only **one** SMILES renderer per device
> Molren, ChemEdit Universal and Chem all claim the ` ```smiles ` block. Two at once = every structure
> drawn twice.

### Example — Rendering Aspirin
````markdown
```smiles
CC(=O)Oc1ccccc1C(=O)O Aspirin (Acetylsalicylic acid)
```
````

### Example — Drawing a Reaction with TikZJax
````markdown
```tikz
\usepackage{chemfig}
\begin{document}
\chemfig{C(-[2]H)(-[4]H)(-[6]H)-C(=[1]O)-[7]OH}
\end{document}
```
````

---

## 📊 Math — Graphs, Equations & Function Plots

| Plugin | Platforms | What It Does | Use Case in This Vault |
|--------|-----------|-------------|----------------------|
| **[LaTeX Suite](https://github.com/artisticat1/obsidian-latex-suite)** | 🖥️📱 | Snippet-based LaTeX typing. Tab through placeholders. Auto-fraction. | Write math equations at handwriting speed: `@a` → `\alpha`, `//` → `\frac{}{}` |
| **[Desmos](https://github.com/Nigecat/obsidian-desmos)** | 🖥️📱 | Embed interactive Desmos graphs in notes. | Plot `y = x^3 - 3x + c`, visualise tangents, show roots |
| **[Numerals](https://github.com/gtg922r/obsidian-numerals)** | 🖥️📱 | Calculate expressions in `math` blocks or inline code; units, currency, TeX output. | Verify calculations: `` `#: 3 * 4.5` `` → `13.5` |
| **[Calctex](https://github.com/developer-mike/obsidian-calctex)** | 🖥️📱 | Calculate LaTeX formulas. | Numerals alternative |
| **[Plot Vectors & Graphs](https://github.com/nicoletanyt/obsidian-plugin-graphs)** | 🖥️ only | Generate function plots/vectors from LaTeX via FunctionPlot. | Static graphs of $f(x)$, vector diagrams |
| **[Kroki](https://github.com/gregzuro/obsidian-kroki)** | 🖥️📱 | Server-side rendering of TikZ, GraphViz, Vega, Mermaid, PlantUML… | **Mobile route to TikZ/pgfplots/vega graphs.** Needs internet; source is sent to `kroki.io` (self-hostable) |
| **[TikZJax](https://github.com/artisticat1/obsidian-tikzjax)** (pgfplots) | 🖥️📱 (heavy) | Publication-quality plots, coordinate geometry, number lines. | Complex geometric figures, locus problems, coordinate transformations |

> **No-plugin option:** Obsidian's built-in **Mermaid** supports `xychart-beta` (line + bar charts) and
> works on every device — see [MOBILE-GUIDE.md](MOBILE-GUIDE.md#41-graphs--mermaid-xychart-beta-core-obsidian-no-plugin-no-internet).

### Example — Desmos Graph
````markdown
```desmos-graph
---
bounds:
  x: [-5, 5]
  y: [-5, 5]
grid: true
---
y = x^3 - 3x + 1
y = 0 | hidden | dashed | red
```
````

### Example — LaTeX Suite Snippets (add to Settings)
```json
{"trigger": "@a", "replacement": "\\alpha"},
{"trigger": "@b", "replacement": "\\beta"},
{"trigger": "//", "replacement": "\\frac{$0}{$1}", "options": "mA"},
{"trigger": "sq", "replacement": "\\sqrt{$0}", "options": "mA"},
{"trigger": "**", "replacement": "^{$0}", "options": "mA"}
```

---

## ⚡ Physics — Circuits, Diagrams & Mechanics

| Plugin | Platforms | What It Does | Use Case in This Vault |
|--------|-----------|-------------|----------------------|
| **[TikZJax](https://github.com/artisticat1/obsidian-tikzjax)** (circuitikz) | 🖥️📱 (heavy) | Draw circuit diagrams with resistors, capacitors, batteries, etc. | RC circuits, Wheatstone bridges, cube networks |
| **[Kroki](https://github.com/gregzuro/obsidian-kroki)** (`tikz` block) | 🖥️📱 | Renders circuitikz/pgfplots **on a server** — light on the device. | **Mobile replacement for Circuit Sketcher.** Needs internet |
| **[Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin)** | 🖥️📱 | Freehand drawing canvas embedded in notes (finger/stylus on mobile). | Sketch force diagrams, ray optics, field lines, free-body diagrams |
| **[Circuit Sketcher](https://github.com/code-forge-temple/circuit-sketcher-obsidian-plugin)** | 🖥️ only | Mouse-driven circuit canvas, `.circuit-sketcher` files. | Simple series/parallel circuits (desktop) |
| **[Desmos](https://github.com/Nigecat/obsidian-desmos)** | 🖥️📱 | Interactive function plots. | Orbital mechanics graphs, SHM displacement-time, wave functions |

### Example — Circuit with TikZJax (desktop)
````markdown
```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american, scale=1]
\draw (0,0) to[battery1, l=$V=24V$] (0,3)
      to[R, l=$R_1=60k\Omega$] (3,3)
      to[R, l=$R_2=40k\Omega$] (3,0)
      -- (0,0);
\draw (3,3) -- (5,3)
      to[R, l=$R_3=120k\Omega$] (5,0)
      -- (3,0);
\draw (3,3) to[C, l=$C=10\mu F$] (3,0);
\end{circuitikz}
\end{document}
```
````

### Example — The same circuit, mobile-friendly (Kroki)
````markdown
```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}
\draw (0,0) to[battery1, l=$24\,\mathrm{V}$] (0,2)
      to[R, l=$R_1$] (3,2)
      to[R, l={$R_2=40k\Omega$}] (3,0) -- (0,0);
\end{circuitikz}
\end{document}
```
````

> [!warning] Kroki + labels with a second `=`
> `l=$R_1=60k\Omega$` fails server-side (*Extra }, or forgotten $*). Wrap the label: `l={$R_1=60k\Omega$}`.

### Example — Excalidraw Freehand
Use `![[drawing.excalidraw]]` to embed hand-drawn force body diagrams, ray tracing, or vector decompositions.

---

## 📝 Writing & Organization

| Plugin | Platforms | What It Does | Use Case in This Vault |
|--------|-----------|-------------|----------------------|
| **[Templater](https://github.com/SilentVoid13/Templater)** | 🖥️📱 (needs Obsidian 1.13+) | Powerful template engine with JavaScript. | Auto-generate solution file headers, question templates |
| **[Dataview](https://github.com/blacksmithgu/obsidian-dataview)** | 🖥️📱 | Query vault as a database. | Dashboard showing all papers solved, progress tracking |
| **[Linter](https://github.com/platers/obsidian-linter)** | 🖥️📱 (needs Obsidian 1.13+) | Auto-format markdown on save. | Keep all solution files uniformly formatted |
| **[Callout Manager](https://github.com/eth-p/obsidian-callout-manager)** | 🖥️📱 (needs Obsidian 1.13+) | Custom callout boxes with colors and icons. | Highlight key concepts, tricks, common mistakes |
| **[Columns](https://github.com/tnichols217/obsidian-columns)** | 🖥️📱 | Side-by-side content in notes. | Show approach comparison, before/after solutions |
| **[Table Editor](https://github.com/tgrosinger/advanced-tables-obsidian)** | 🖥️📱 | Excel-like table editing in markdown. | Answer key tables, comparison tables |
| **[Mind Map](https://github.com/lynchjames/obsidian-mind-map)** | 🖥️📱 | Auto-generate mind maps from headings. | Topic overview for each paper, theory connections |

---

## 📐 Diagram Decision Tree

```
What do you need to draw?
│
├── Chemical structure / molecule
│   ├── Mobile or desktop, offline  → ChemEdit Universal (```smiles)
│   ├── Desktop, RDKit-quality      → Molren
│   ├── Desktop, full editor        → Ketcher  (on mobile: Ketcher web app → export SVG)
│   └── Fischer/Haworth/precise     → TikZJax + chemfig (or Kroki tikz)
│
├── Circuit diagram
│   ├── Mobile (online)             → Kroki + ```tikz circuitikz
│   ├── Mobile (offline)            → Excalidraw / Canvas + photo of paper sketch
│   ├── Desktop, quick sketch       → Circuit Sketcher
│   └── Publication quality         → TikZJax + circuitikz
│
├── Math function graph
│   ├── Interactive                 → Desmos (desktop + mobile)
│   ├── No plugin at all            → Mermaid xychart-beta (built in)
│   ├── Static / vectors            → Plot Vectors & Graphs (desktop only)
│   └── Publication quality         → TikZJax + pgfplots, or Kroki tikz
│
├── Freehand / sketch
│   └── Excalidraw (desktop + mobile)
│
├── Flowchart / mind map
│   ├── Auto from headings          → Mind Map plugin
│   └── Custom                      → Excalidraw or Mermaid (built-in)
│
└── Math equations
    ├── Fast typing                 → LaTeX Suite
    ├── Inline calculation          → Numerals / Calctex
    └── Display only                → Built-in MathJax ($$...$$)
```

---

## ⚙️ Installation Order

**Desktop**

1. **LaTeX Suite** — immediate productivity boost for math typing
2. **Templater** — automate solution file creation
3. **TikZJax** — circuits, chemistry, geometry all in one
4. **Desmos** — instant function visualization
5. **Molren** *or* **ChemEdit Universal** — chemistry structures (not both)
6. **Excalidraw** — freehand diagrams
7. **Dataview** — progress tracking dashboard
8. **Callout Manager** — beautiful callouts for concepts/tricks
9. **Linter** — keep formatting consistent
10. **Mind Map** — topic visualization

**Mobile (phone/tablet)**

1. **LaTeX Suite** — math typing
2. **ChemEdit Universal** — structures, offline, touch editor
3. **Desmos** — graphs
4. **Kroki** — when you need TikZ/circuitikz quality and have internet
5. **Excalidraw** — freehand
6. **Numerals** — inline calculations
7. **Dataview** — progress dashboard

*Skip on mobile:* Molren, Ketcher, Plot Vectors & Graphs, Circuit Sketcher (desktop-only); TikZJax
(works but heavy on a phone CPU).

See **[MOBILE-GUIDE.md](MOBILE-GUIDE.md)** for the why, the snippets, and the `.obsidian-mobile`
config folder.
