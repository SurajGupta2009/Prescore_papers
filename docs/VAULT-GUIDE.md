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
│   ├── 3-paper1-solutions.md  ← (pending)
│   ├── 3-paper2-solutions.md  ← (pending)
│   ├── 4-paper1-solutions.md
│   └── 4-paper2-solutions.md
│
├── 📂 templates/              ← Templater templates
│   └── new-solution.md
│
├── 📂 docs/                   ← Documentation & guides
│   ├── VAULT-GUIDE.md         ← You are here
│   ├── RECOMMENDED-PLUGINS.md ← Plugin installation guide
│   └── SOLUTION-TEMPLATE.md   ← Full solution template
│
├── 📂 assets/                 ← Diagrams & images
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

See [[RECOMMENDED-PLUGINS]] for the complete list. Quick install priority:

1. **LaTeX Suite** — Type math 10x faster
2. **Templater** — Auto-generate solution files
3. **TikZJax** — Circuits, chemistry, geometry
4. **Desmos** — Interactive function plots
5. **Molren/ChemEdit** — Chemical structures
6. **Excalidraw** — Freehand diagrams

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
- **Chemistry:** Use ` ```smiles ` code blocks with Molren, or `\chemfig` with TikZJax
- **Circuits:** Use `\circuitikz` inside ` ```tikz ` blocks
- **Graphs:** Use ` ```desmos-graph ` for interactive plots
- **Freehand:** Use Excalidraw for ray diagrams, force diagrams, etc.