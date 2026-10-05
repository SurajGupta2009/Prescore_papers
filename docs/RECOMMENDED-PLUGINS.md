# 🔌 Recommended Obsidian Plugins for JEE Advanced Solutions Vault

> Install these from **Settings → Community Plugins → Browse** in Obsidian.

---

## 🧪 Chemistry — Molecular Structures & Reactions

| Plugin | What It Does | Use Case in This Vault |
|--------|-------------|----------------------|
| **[ChemEdit Universal](https://github.com)** | Draw/edit SMILES, MOL structures. Offline. Mobile+Desktop. PubChem integration. | Draw organic molecules, show reaction intermediates, display IUPAC structures inline |
| **[Molren](https://github.com)** | Render SMILES → SVG from fenced code blocks using RDKit.js. Fully offline. | Quick inline molecule rendering: ` ```smiles CC(=O)O ``` ` |
| **[Ketcher](https://github.com)** | Full molecule editor embedded in Obsidian. Draw reactions, export .ket files. | Draw complex reaction mechanisms, arrow-pushing diagrams |
| **[TikZJax](https://github.com)** (chemfig) | Render chemical structures via LaTeX `chemfig` package. | Precise bond-angle diagrams, Fischer projections, Haworth projections |

### Example — Rendering Aspirin with Molren
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

| Plugin | What It Does | Use Case in This Vault |
|--------|-------------|----------------------|
| **[LaTeX Suite](https://github.com)** | Snippet-based LaTeX typing. Tab through placeholders. Auto-fraction. | Write math equations at handwriting speed: `@a` → `\alpha`, `//` → `\frac{}{}` |
| **[Desmos](https://github.com)** | Embed interactive Desmos graphs in notes. Online+offline. | Plot functions like `y = x^3 - 3x + c`, visualize tangent lines, show roots |
| **[Plot Vectors & Graphs](https://github.com)** | Generate function plots from LaTeX equations using FunctionPlot. | Quick static graphs of $f(x)$, vector diagrams for physics |
| **[Numerals](https://github.com)** | Calculate LaTeX expressions inline. Shows results next to equations. | Verify calculations: `3 \times 4.5 =` → shows `13.5` |
| **[TikZJax](https://github.com)** (pgfplots) | Render publication-quality plots, coordinate geometry, number lines. | Complex geometric figures, locus problems, coordinate transformations |

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

| Plugin | What It Does | Use Case in This Vault |
|--------|-------------|----------------------|
| **[TikZJax](https://github.com)** (circuitikz) | Draw circuit diagrams with resistors, capacitors, batteries, etc. | RC circuits, Wheatstone bridges, cube networks |
| **[Excalidraw](https://github.com)** | Freehand drawing canvas embedded in notes. | Sketch force diagrams, ray optics, field lines, free-body diagrams |
| **[Circuit Sketcher](https://github.com)** | Quick circuit diagram editor for Obsidian. | Simple series/parallel circuits |
| **[Desmos](https://github.com)** | Interactive function plots. | Orbital mechanics graphs, SHM displacement-time, wave functions |

### Example — Circuit with TikZJax
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

### Example — Excalidraw Freehand
Use `![[drawing.excalidraw]]` to embed hand-drawn force body diagrams, ray tracing, or vector decompositions.

---

## 📝 Writing & Organization

| Plugin | What It Does | Use Case in This Vault |
|--------|-------------|----------------------|
| **[Templater](https://github.com)** | Powerful template engine with JavaScript. Auto-fill dates, create notes from templates. | Auto-generate solution file headers, question templates |
| **[Dataview](https://github.com)** | Query vault as a database. List notes by tag, filter by properties. | Dashboard showing all papers solved, progress tracking |
| **[Linter](https://github.com)** | Auto-format markdown on save. Consistent headings, lists, spacing. | Keep all solution files uniformly formatted |
| **[Callout Manager](https://github.com)** | Custom callout boxes with colors and icons. | Highlight key concepts, tricks, common mistakes |
| **[Columns](https://github.com)** | Side-by-side content in notes. | Show approach comparison, before/after solutions |
| **[Table Editor](https://github.com)** | Excel-like table editing in markdown. | Answer key tables, comparison tables |
| **[Mind Map](https://github.com)** | Auto-generate mind maps from headings. | Topic overview for each paper, theory connections |

---

## 📐 Diagram Decision Tree

```
What do you need to draw?
│
├── Chemical structure / molecule
│   ├── Simple/inline → Molren (```smiles)
│   ├── Full editor → ChemEdit Universal or Ketcher
│   └── Fischer/Haworth/precise → TikZJax + chemfig
│
├── Circuit diagram
│   ├── Quick sketch → Circuit Sketcher
│   └── Publication quality → TikZJax + circuitikz
│
├── Math function graph
│   ├── Interactive → Desmos
│   ├── Static → Plot Vectors & Graphs
│   └── Publication quality → TikZJax + pgfplots
│
├── Freehand / sketch
│   └── Excalidraw
│
├── Flowchart / mind map
│   ├── Auto from headings → Mind Map plugin
│   └── Custom → Excalidraw or Mermaid (built-in)
│
└── Math equations
    ├── Fast typing → LaTeX Suite
    ├── Inline calculation → Numerals
    └── Display only → Built-in MathJax ($$...$$)
```

---

## ⚙️ Installation Order (Recommended)

1. **LaTeX Suite** — immediate productivity boost for math typing
2. **Templater** — automate solution file creation
3. **TikZJax** — circuits, chemistry, geometry all in one
4. **Desmos** — instant function visualization
5. **ChemEdit Universal** or **Molren** — chemistry structures
6. **Excalidraw** — freehand diagrams
7. **Dataview** — progress tracking dashboard
8. **Callout Manager** — beautiful callouts for concepts/tricks
9. **Linter** — keep formatting consistent
10. **Mind Map** — topic visualization