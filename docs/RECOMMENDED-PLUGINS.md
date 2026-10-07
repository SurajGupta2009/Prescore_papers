# 🔌 Recommended Obsidian Plugins for JEE Advanced Solutions Vault

> Install these from **Settings → Community Plugins → Browse** in Obsidian.
> This list is curated for **maximum cross-platform device compatibility (Desktop, Tablet, iOS, Android)** using native Obsidian renderers.

---

## 🧪 Chemistry — Molecular Structures & Reactions

| Plugin | Rendering Engine | Why It Works on Your Device | Use Case in This Vault |
|--------|------------------|-----------------------------|------------------------|
| **[TikZJax](https://github.com)** (`chemfig`) | Client WebAssembly LaTeX compiler | **100% vector accuracy**, native sharp fonts, zero external browser or iframe dependencies. | Fischer projections, bond angles, stereochemistry, polymers, mechanisms |
| **[ChemEdit Universal](https://github.com)** | OpenChemLib & SmilesDrawer | Lightweight, built specifically for Mobile + Desktop offline support. | Visual chemical structure drawing, property inspection, SMILES editing |
| **[Chemtrails](https://github.com)** or **[Obsidian Chem](https://github.com)** | SmilesDrawer | Lightweight pure-JS SVG vector rendering of ```` ```smiles ```` without heavy desktop WASM crashes. | Clean, fast inline SMILES molecular rendering |

*(Replaces unsupported Molren and Ketcher)*

### Example — Reaction / Polymer with TikZJax (`chemfig`)
````markdown
```tikz
\usepackage{chemfig}
\begin{document}
\chemfig{C(-[2]H)(-[4]H)(-[6]H)-C(=[1]O)-[7]OH}
\end{document}
```
````

### Example — Inline Structure with Chemtrails / Chem
````markdown
```smiles
CC(=O)Oc1ccccc1C(=O)O
```
````

---

## ⚡ Physics — Circuits, Diagrams & Mechanics

| Plugin | Rendering Engine | Why It Works on Your Device | Use Case in This Vault |
|--------|------------------|-----------------------------|------------------------|
| **[TikZJax](https://github.com)** (`circuitikz`) | LaTeX PGF / TikZ | Pure code-based vector graphics. Generates exact IEEE/IEC schematic components at native resolution. | RC circuits, bridge networks, switches, cube/3D capacitor ladders |
| **[Excalidraw](https://github.com)** | Native Obsidian Canvas | Full stylus / touch / mouse support across mobile, tablet, and desktop. | Free-body diagrams, ray optics, equipotential lines, field lines |
| **[CircuitJS](https://github.com)** | Falstad Simulator | Interactive circuit simulation inside Obsidian notes. | Dynamic RC/RLC transient response analysis |

*(Replaces unsupported Circuit Sketcher)*

### Example — RC Circuit with TikZJax (`circuitikz`)
````markdown
```tikz
\usepackage{circuitikz}
\begin{document}
\begin{tikzpicture}[scale=1.0]
  \draw (0,0) to[battery1, l=$\mathcal{E}=24\text{ V}$] (0,3)
        to[nos, l=$S_1$] (1.8,3)
        to[R, l=$R_1=60\text{ k}\Omega$] (3.6,3)
        to[short] (4.5,3);
  \draw (4.5,3) to[C, l=$C=10\,\mu\text{F}$] (4.5,0) -- (0,0);
  \draw (4.5,3) to[nos, l=$S_2$] (6.0,3)
        to[R, l=$R_2=40\text{ k}\Omega$] (6.0,1.5)
        to[R, l=$R_3=120\text{ k}\Omega$] (6.0,0) -- (4.5,0);
\end{tikzpicture}
\end{document}
```
````

---

## 📊 Math — Coordinate Geometry, Functions & Plots

| Plugin | Rendering Engine | Why It Works on Your Device | Use Case in This Vault |
|--------|------------------|-----------------------------|------------------------|
| **[TikZJax](https://github.com)** (`pgfplots`) | LaTeX PGF | Precise coordinate axes, locus diagrams, complex plane circles, tangents. | Locus of complex numbers, Argand plane geometry, conic sections |
| **[Desmos](https://github.com)** | Desmos Graphing Engine | Native touch pinch-to-zoom, pan, parameter sliders, mobile responsive. | Interactive calculus curves, roots, tangents, wave packets |
| **[LaTeX Suite](https://github.com)** | CodeMirror extension | Universal keyboard shortcut engine for writing math at typing speed. | Matrix algebra, integrals, calculus notations |

*(Replaces unsupported Plot Vectors and Graphs)*

### Example — Complex Plane Geometry with TikZJax (`pgfplots`)
````markdown
```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}[scale=0.9]
  \draw[->, >=stealth, gray!70] (-1.5,0) -- (5.5,0) node[right, black] {$\text{Re}$};
  \draw[->, >=stealth, gray!70] (0,-0.8) -- (0,5.5) node[above, black] {$\text{Im}$};
  \draw[blue, thick] (0,3) circle (2);
  \filldraw[red] (4,0) circle (2pt) node[below] {$4+0i$};
  \draw[dashed, red!80] (0,3) -- (4,0);
  \filldraw[teal] (1.6, 1.8) circle (2.5pt) node[above right] {$z_{\text{min}}$};
\end{tikzpicture}
\end{document}
```
````

### Example — Interactive Function with Desmos
````markdown
```desmos-graph
---
bounds: [-5, 5, -5, 5]
grid: true
---
y = x^3 - 3x + 1
y = 0 | hidden | dashed | red
```
````

---

## 🔢 Math Calculations & Numerals Alternative

| Plugin | Why It Works on Your Device | Use Case in This Vault |
|--------|-----------------------------|------------------------|
| **[Calculator Pro](https://github.com)** | Scientific calculator built for Obsidian Mobile & Desktop with direct LaTeX export. | Numerical verification, trigonometry, scientific constants |
| **[Calculite](https://github.com)** | Compact, lightweight floating calculator sidebar. | Fast scratchpad arithmetic |
| **Dataview Inline Math** (`$= ... $`) | Core Javascript engine, zero extra background AST threads. | Inline formula checks |

*(Replaces unsupported Numerals)*

---

## 📐 Diagram Decision Tree (Cross-Platform)

```
What do you need to draw?
│
├── Chemical Structure / Polymer
│   ├── Exact bonds / Stereochemistry / Rings → TikZJax (\chemfig)
│   ├── Quick inline SMILES → Chemtrails / Chem (```smiles)
│   └── Visual touch editor → ChemEdit Universal
│
├── Physics Circuit
│   ├── Publication-quality schematic → TikZJax (\circuitikz)
│   ├── Interactive simulation → CircuitJS
│   └── Freehand sketch / Optics / Mechanics → Excalidraw
│
├── Math Function / Geometry
│   ├── Coordinate locus / Argand plane → TikZJax (pgfplots / tikzpicture)
│   └── Curve plotting / Maxima-Minima → Desmos (```desmos-graph)
│
└── Calculations & Math Typing
    ├── Fast typing → LaTeX Suite
    ├── Scratchpad calculation → Calculator Pro / Calculite
    └── Formatted formulas → Built-in MathJax ($$...$$)
```
