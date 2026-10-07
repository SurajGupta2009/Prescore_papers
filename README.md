# Prescore Papers — JEE Advanced Solutions Vault

> **Target Rank:** Top 100 | **Format:** Obsidian Vault | **Approach:** Multi-method solutions with complete theory

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

## 📱 Works On Any Device (Phones Included)

This vault used to advertise chemistry/graph/circuit figures through plugins that **cannot
run on Android or iOS** — Molren, Ketcher, Plot Vectors and Graphs and Circuit Sketcher are
all published as desktop-only, so Obsidian refuses to enable them on a phone.

That is fixed, in two ways:

1. **Figures are pre-rendered into plain SVG** by [`tools/render_figures.py`](tools/render_figures.py).
   Every client — Android, iOS, Windows, macOS, Linux — displays an SVG natively. No
   community plugin involved, works offline, works in PDF exports and on GitHub.
2. **The plugin list only contains mobile-capable plugins**, with correct IDs
   (e.g. `numerals`, not `obsidian-numerals`).

| Write this | Get this | Replaces (desktop-only) |
|---|---|---|
| ```` ```smiles ```` | RDKit molecule drawing | Molren, Ketcher, chemfig |
| ```` ```plot ```` | matplotlib function graph | Plot Vectors and Graphs, Desmos (static) |
| ```` ```circuit ```` | schemdraw circuit / vector diagram | Circuit Sketcher, circuitikz |

- **Why the plugins fail:** [docs/PLUGIN-COMPATIBILITY.md](docs/PLUGIN-COMPATIBILITY.md)
- **What to use instead:** [docs/DIAGRAMS-WITHOUT-PLUGINS.md](docs/DIAGRAMS-WITHOUT-PLUGINS.md)
- **See it rendered now:** [examples/figures-demo.md](examples/figures-demo.md)
- **Plugin list with a mobile column:** [docs/RECOMMENDED-PLUGINS.md](docs/RECOMMENDED-PLUGINS.md)

## 🔌 Obsidian Vault

This repository is an **Obsidian vault**. Open the folder in Obsidian to get:

- ✏️ **Excalidraw** — freehand diagrams (mobile ✅)
- 📈 **Dataview** — progress dashboards
- 🧪 **Molecules & graphs** — via committed SVG, no plugin needed
- ⚡ **Circuits** — schematic SVG, or TikZJax for light cases (mobile ✅)
- 📝 **LaTeX Suite** — fast math typing

See [docs/RECOMMENDED-PLUGINS.md](docs/RECOMMENDED-PLUGINS.md) — every plugin row states
whether it actually runs on a phone.

## 📁 Directory Structure

```
├── solutions/          ← Solved papers (Markdown)
├── examples/           ← figures-demo.md: the figure pipeline, rendered
├── templates/          ← Templater templates for new solutions
├── docs/               ← Guides and documentation
│   ├── VAULT-GUIDE.md
│   ├── PLUGIN-COMPATIBILITY.md      ← why desktop-only plugins fail
│   ├── DIAGRAMS-WITHOUT-PLUGINS.md  ← the alternatives playbook
│   └── RECOMMENDED-PLUGINS.md
├── tools/              ← render_figures.py (fences → SVG)
├── assets/diagrams/    ← generated + hand-made figures (committed)
├── *.pdf               ← Original question papers
└── .obsidian/          ← Vault configuration (mobile-safe plugin list)
```

## 🎯 How to Use

1. **Clone** this repository
2. **Open** the folder in Obsidian (File → Open Vault → Open folder as vault)
3. Install plugins from [docs/RECOMMENDED-PLUGINS.md](docs/RECOMMENDED-PLUGINS.md) —
   on a phone the list is already trimmed to what works
4. **Navigate** using the graph view or the index in [docs/VAULT-GUIDE.md](docs/VAULT-GUIDE.md)

## 🔧 Rebuilding figures

```bash
pip install -r tools/requirements.txt
python3 tools/render_figures.py     # fences → SVG (rewrites the notes in place)
make check                          # fail if a committed figure is stale
```

Figures can also be rendered by CI: **Actions → Render vault figures → Run workflow**.

---

*Built for JEE Advanced 2027 preparation — aiming for Top 100*
