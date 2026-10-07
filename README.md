# Prescore Papers — JEE Advanced Solutions Vault

> **Target Rank:** Top 100 | **Format:** Obsidian Vault | **Approach:** Multi-method solutions with complete theory and **live plugin figures**

---

## 📋 Papers Available

| Test | Paper 1 | Paper 2 |
|------|---------|---------|
| **Test 1** | ✅ [Solutions](solutions/1-paper1-solutions.md) | ✅ [Solutions](solutions/1-paper2-solutions.md) |
| **Test 2** | ✅ [Solutions](solutions/2-paper1-solutions.md) | ✅ [Solutions](solutions/2-paper2-solutions.md) |
| **Test 3** | ✅ [Solutions](solutions/3-paper1-solutions.md) | ✅ [Solutions](solutions/3-paper2-solutions.md) |
| **Test 4** | ✅ [Solutions](solutions/4-paper1-solutions.md) | ✅ [Solutions](solutions/4-paper2-solutions.md) |

## 🏗️ Solution Format

Each question includes:
- **Multiple approaches** (2-3 per question)
- **Step-by-step derivations** (formulas derived, not just stated)
- **Concept explanations** (general statements for understanding)
- **JEE tricks** (shortcuts, including out-of-syllabus ones)
- **Complete theory** at the end of each paper
- **Figures drawn live by plugins** — circuits, molecules, graphs (see below)

## 🧩 Figures Render Inside Obsidian

Nothing is exported to image files. Four mobile-capable plugins render four kinds of block:

| Block | Plugin (install ID) | Draws |
|---|---|---|
| ```` ```tikz ```` | TikZJax (`obsidian-tikzjax`) | circuits (circuitikz), molecules (chemfig), plots (pgfplots), geometry |
| ```` ```desmos-graph ```` | Desmos (`obsidian-desmos`) | function graphs, V–I curves, SHM, tangents |
| ```` ```smiles ```` | ChemEdit Universal (`chemedit-universal`), or Chem (`chem`), or Chemtrails (`chemtrails`) | structures from SMILES |
| ```` ```math ```` | Numerals (`numerals`) | unit-aware calculations that check the arithmetic |

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[american]
  \draw (0,0) to[battery1, l=$V$] (0,2.5) to[R, l=$R$] (3,2.5) to[C, l=$C$] (3,0) -- (0,0);
\end{circuitikz}
\end{document}
```

```smiles
CC(=O)Oc1ccccc1C(=O)O
```

```desmos-graph
left=-4; right=4
bottom=-8; top=8
height=300
---
y=x^3-3x+1
y=3x-3|dashed|red
```

> **Before you open a solution file:** install the four plugins above. Until then Obsidian
> shows the raw code instead of the picture. Full syntax reference:
> **[docs/PLUGIN-FIGURES.md](docs/PLUGIN-FIGURES.md)** · install table:
> **[docs/RECOMMENDED-PLUGINS.md](docs/RECOMMENDED-PLUGINS.md)**

## 📁 Directory Structure

```
├── solutions/          ← Solved papers (Markdown + live plugin figures)
├── docs/               ← Guides
│   ├── VAULT-GUIDE.md
│   ├── PLUGIN-FIGURES.md            ← tikz / desmos / smiles / math syntax
│   ├── PLUGIN-COMPATIBILITY.md      ← which plugins work on phones, with evidence
│   ├── RECOMMENDED-PLUGINS.md       ← install table (ID + mobile support)
│   ├── OPEN-ITEMS.md                ← known loose ends in the written solutions
│   └── SOLUTION-TEMPLATE.md
├── templates/          ← Templater template for new solutions
├── tools/              ← check_figures.py, check_plugin_ids.py, check_prose.py
├── assets/             ← hand-made exports (Excalidraw, screenshots)
├── *.pdf               ← Original question papers
└── .obsidian/          ← Vault configuration (mobile-safe plugin list)
```

## 🎯 How to Use

1. **Clone** this repository
2. **Open** the folder in Obsidian (File → Open Vault → Open folder as vault)
3. **Install the four figure plugins** (list above) — one-time, 5 minutes
4. **Navigate** using the graph view or the index in [docs/VAULT-GUIDE.md](docs/VAULT-GUIDE.md)

## 🔧 Checks

```bash
python3 tools/check_figures.py     # every tikz/desmos/smiles/math block parses
python3 tools/check_plugin_ids.py  # every plugin ID exists and is mobile-capable
python3 tools/check_prose.py       # scratch-pad wording still left in a solution body
make check                         # figures + plugin IDs, as CI runs them
make prose                         # the report behind docs/OPEN-ITEMS.md
```

---

*Built for JEE Advanced 2027 preparation — aiming for Top 100*
