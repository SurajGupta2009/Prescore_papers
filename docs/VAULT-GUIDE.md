# 🏠 Prescore Papers — Obsidian Vault Guide

> [!success] Welcome!
> This vault contains JEE Advanced rank improvement solutions with multiple approaches, theory, and visual explanations.

---

## 📁 Vault Structure

```
Prescore_papers/
├── 📂 solutions/              ← All solution files live here
│   ├── 1-paper1-solutions.md
│   ├── 1-paper2-solutions.md
│   ├── 2-paper1-solutions.md
│   ├── 2-paper2-solutions.md
│   ├── 3-paper1-solutions.md
│   ├── 3-paper2-solutions.md
│   ├── 4-paper1-solutions.md
│   └── 4-paper2-solutions.md
│
├── 📂 templates/              ← Templater templates
│   └── new-solution.md
│
├── 📂 docs/                   ← Documentation & guides
│   ├── VAULT-GUIDE.md               ← You are here
│   ├── PLUGIN-FIGURES.md            ← tikz / desmos / smiles / math syntax
│   ├── PLUGIN-COMPATIBILITY.md      ← why desktop-only plugins fail on phones
│   ├── RECOMMENDED-PLUGINS.md       ← plugin list, mobile support on every row
│   └── SOLUTION-TEMPLATE.md         ← Full solution template
│
├── 📂 tools/                  ← check_figures.py, check_plugin_ids.py
├── 📂 assets/                 ← hand-made exports (Excalidraw, screenshots)
│   ├── diagrams/
│   └── chemistry/
│
├── 📂 .obsidian/              ← Vault configuration
│   ├── app.json
│   ├── core-plugins.json
│   └── community-plugins.json
│
├── 📄 1-paper1.pdf            ← Original papers
├── 📄 1-paper2.pdf
├── ... (8 papers total)
│
└── 📄 README.md               ← Repository description
```

---

## 🎯 Quick Navigation

### By Test
- [[1-paper1-solutions|Test 1 — Paper 1]]
- [[1-paper2-solutions|Test 1 — Paper 2]]
- [[2-paper1-solutions|Test 2 — Paper 1]]
- [[2-paper2-solutions|Test 2 — Paper 2]]
- [[4-paper1-solutions|Test 4 — Paper 1]]
- [[4-paper2-solutions|Test 4 — Paper 2]]

### By Subject
- Use Dataview queries or the graph view to explore connections

### By Topic
- **Mathematics:** Complex numbers, combinatorics, calculus, coordinate geometry
- **Physics:** Electrostatics, circuits, optics, mechanics, modern physics
- **Chemistry:** Organic reactions, coordination chemistry, polymers, biomolecules

---

## ✍️ Solution File Format

Each solution file follows this structure:

1. **Header** — Paper identification and metadata
2. **Per Question:**
   - Question statement
   - **Multiple approaches** (2-3 per question)
   - Step-by-step derivations
   - Key concepts highlighted in callouts
3. **Theory Reference** — Complete theory needed for the paper

### Callout Types Used

| Callout | Purpose |
|---------|---------|
| `> [!question]` | Original question text |
| `> [!tip]` | Tricks, shortcuts, exam hacks |
| `> [!example]` | Full worked solutions |
| `> [!success]` | Concepts and key results |
| `> [!warning]` | Common mistakes to avoid |
| `> [!danger]` | Advanced/out-of-syllabus tricks |
| `> [!note]` | Formulas and quick reference |
| `> [!info]` | Background information |

---

## 🔌 Essential Plugins

Install these from **Settings → Community plugins → Browse** (IDs in brackets). All are
mobile-capable — verified by `tools/check_plugin_ids.py`, explained in [[PLUGIN-COMPATIBILITY]].

**Required for the figures to show up at all:**

1. **TikZJax** (`obsidian-tikzjax`) — circuits, molecules, pgfplots, geometry
2. **Desmos** (`obsidian-desmos`) — function graphs
3. **ChemEdit Universal** (`chemedit-universal`) — chemical structures (or `chem` / `chemtrails`)
4. **Numerals** (`numerals`) — calculation blocks

**Recommended for working the papers:**

5. **Latex Suite** (`obsidian-latex-suite`) — type math at handwriting speed
6. **Excalidraw** (`obsidian-excalidraw-plugin`) — freehand force/ray diagrams
7. **Dataview** + **Templater** + **Linter** — dashboards, templates, tidy formatting

> [!tip] Figures are code, not images
> Every diagram in the solutions is a `tikz`, `desmos-graph`, `smiles` or `math` block that
> the plugin draws live. Nothing is exported, so you can change a resistor value and the
> circuit redraws. Syntax reference: [[PLUGIN-FIGURES]].

### For Creating Diagrams
- **Circuits / vectors / ray optics / geometry:** a ` ```tikz ` block (circuitikz or plain TikZ)
- **Molecules:** a ` ```smiles ` block — one SMILES per line, no trailing name
- **Graphs:** a ` ```desmos-graph ` block — settings, `---`, then one equation per line
- **Arithmetic checks:** a ` ```math ` block (Numerals), units included
- **Freehand:** Canvas (core) or Excalidraw
- **Flowcharts:** Mermaid (core plugin, enabled)

Before committing a note, run:

```bash
python3 tools/check_figures.py     # or: make check
```

It validates every block (balanced environments, allowed packages, one SMILES per line, …)
so a typo cannot turn into an empty box on your phone.
