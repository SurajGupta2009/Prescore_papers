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
│   ├── PLUGIN-COMPATIBILITY.md      ← why desktop-only plugins fail on phones
│   ├── DIAGRAMS-WITHOUT-PLUGINS.md  ← the alternatives playbook
│   ├── RECOMMENDED-PLUGINS.md       ← plugin list, mobile support on every row
│   └── SOLUTION-TEMPLATE.md         ← Full solution template
│
├── 📂 examples/               ← figures-demo.md: the figure pipeline, rendered
├── 📂 tools/                  ← render_figures.py (fences → SVG)
├── 📂 assets/                 ← Diagrams & images (all committed, phone-readable)
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

Everything in this list is **mobile-capable** (verified against each plugin's manifest).
The desktop-only plugins that used to be recommended here — Molren, Ketcher, Plot Vectors &
Graphs, Circuit Sketcher — cannot run on Android/iOS; see
[[PLUGIN-COMPATIBILITY]] for the evidence and [[DIAGRAMS-WITHOUT-PLUGINS]] for what to use
instead.

1. **Latex Suite** (`obsidian-latex-suite`) — type math 10x faster
2. **Desmos** (`obsidian-desmos`) — interactive function plots
3. **Numerals** (`numerals`) — calculators in a code block (the ID matters!)
4. **ChemEdit Universal** (`chemedit-universal`) — molecules, offline
5. **Excalidraw** (`obsidian-excalidraw-plugin`) — freehand diagrams
6. **TikZJax** (`obsidian-tikzjax`) — LaTeX/circuitikz/chemfig diagrams
7. **Templater** + **Dataview** + **Linter** — keep the vault tidy

> [!tip] Figures that need no plugin at all
> Molecules, graphs and circuits in this vault are pre-rendered into SVG
> (`assets/diagrams/`) by `tools/render_figures.py` — see
> [[DIAGRAMS-WITHOUT-PLUGINS]] and open `examples/figures-demo.md` on the phone.

---

## 📊 Progress Tracking

Use Dataview to track which papers are solved:

```dataview
TABLE file.name AS "Paper", 
      length(file.name) AS "Size (chars)"
FROM "solutions"
SORT file.name ASC
```

---

## 🧠 How to Use This Vault

### For Revision
1. Open a solution file
2. Read the question, try solving yourself first
3. Check against the multiple approaches provided
4. Note the **concept callout** for the underlying theory
5. Review the **theory section** at the end of each paper

### For Adding New Solutions
1. Use the template from [[SOLUTION-TEMPLATE]]
2. Follow the callout format for consistency
3. Include at least 2 approaches per question
4. Add theory at the end of the file

### For Creating Diagrams
- **Chemistry:** a ` ```smiles ` fence (RDKit renders it) — see [[DIAGRAMS-WITHOUT-PLUGINS]]
- **Circuits / vectors:** a ` ```circuit ` fence (schemdraw), or `\circuitikz` with TikZJax
- **Graphs:** a ` ```plot ` fence for a static graph, ` ```desmos-graph ` when you want sliders
- **Freehand:** Canvas (core) or Excalidraw for ray diagrams, force diagrams, etc.
- **Flowcharts:** Mermaid (core plugin, now enabled)

Then rebuild the pictures and they appear on every device — including the phone:

```bash
python3 tools/render_figures.py     # or: make figures
```