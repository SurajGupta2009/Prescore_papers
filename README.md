# Prescore Papers — JEE Advanced Solutions Vault

> **Target Rank:** Top 100 | **Format:** Obsidian Vault | **Approach:** Multi-method solutions with complete theory

---

## 📋 Papers Available

| Test | Paper 1 | Paper 2 |
|------|---------|---------|
| **Test 1** | ⏳ 48/51 — [Solutions](solutions/1-paper1-solutions.md) | ⏳ 47/51 — [Solutions](solutions/1-paper2-solutions.md) |
| **Test 2** | ✅ 54/54 — [Solutions](solutions/2-paper1-solutions.md) | ✅ 54/54 — [Solutions](solutions/2-paper2-solutions.md) |
| **Test 3** | ✅ 48/48 — [Solutions](solutions/3-paper1-solutions.md) | ✅ 48/48 — [Solutions](solutions/3-paper2-solutions.md) |
| **Test 4** | ⏳ 38/57 — [Solutions](solutions/4-paper1-solutions.md) | ⏳ 43/57 — [Solutions](solutions/4-paper2-solutions.md) |

**Status key:** ✅ complete = every question of the paper written up with a derivation, the exam shortcut and a concept callout, plus the COMPLETE THEORY REFERENCE section. ⏳ in progress = remaining question numbers are listed at the top of each file.

## 🏗️ Solution Format

Each question includes:
- **Multiple approaches** (2-3 per question)
- **Step-by-step derivations** (formulas derived, not just stated)
- **Concept explanations** (general statements for understanding)
- **JEE tricks** (shortcuts, including out-of-syllabus ones)
- **Complete theory** at the end of each paper

## 🔌 Obsidian Vault

This repository is configured as an **Obsidian vault**. Open the folder in Obsidian to get:

- 📊 **Desmos graphs** — Interactive function plots *(desktop + mobile)*
- 🧪 **Chemical structures** — SMILES rendering via ChemEdit Universal (mobile) / Molren (desktop)
- ⚡ **Circuit diagrams** — TikZ circuitikz integration *(desktop)* or Kroki *(mobile, server-side)*
- ✏️ **Excalidraw** — Freehand diagrams for ray optics, force diagrams *(desktop + mobile)*
- 📝 **LaTeX Suite** — Fast math typing with snippets *(desktop + mobile)*
- 📈 **Dataview** — Progress tracking and dashboards *(desktop + mobile)*

> [!note] Reading on a phone or tablet?
> Nothing in the solution notes needs a plugin — they are plain Markdown + MathJax (core).
> But **Molren, Ketcher, Plot Vectors & Graphs and Circuit Sketcher are desktop-only** by design, so
> Obsidian mobile shows *“This plugin does not support your device.”* Every capability has a
> mobile-compatible replacement, and this repo ships a ready-made mobile config folder.
> → **[docs/MOBILE-GUIDE.md](docs/MOBILE-GUIDE.md)**

See [docs/RECOMMENDED-PLUGINS.md](docs/RECOMMENDED-PLUGINS.md) for the installation guide with
platform (desktop/mobile) support for every plugin.

## 📁 Directory Structure

```
├── solutions/          ← Solved papers (Markdown)
├── templates/          ← Templater templates for new solutions
├── docs/               ← Guides and documentation
│   ├── VAULT-GUIDE.md
│   ├── RECOMMENDED-PLUGINS.md
│   ├── MOBILE-GUIDE.md        ← Why some plugins won't run on phones + alternatives
│   └── SOLUTION-TEMPLATE.md
├── assets/             ← Diagrams and images
│   ├── diagrams/       ←    pre-rendered SVG/PNG (works on every device)
│   └── chemistry/      ←    exported molecule SVGs
├── *.pdf               ← Original question papers
├── .obsidian/          ← Vault configuration (desktop)
└── .obsidian-mobile/   ← Vault configuration (phone/tablet only)
```

## 🎯 How to Use

1. **Clone** this repository
2. **Open** the folder in Obsidian (File → Open Vault → Open folder as vault)
3. **Install** recommended plugins from docs/RECOMMENDED-PLUGINS.md
   *(plugin code is deliberately not committed — install each plugin once per device)*
4. **On mobile**, optionally point *Settings → About → Override config folder* at `.obsidian-mobile`
   so the desktop-only plugins never error — see docs/MOBILE-GUIDE.md
5. **Navigate** using the graph view or the index in docs/VAULT-GUIDE.md

---

*Built for JEE Advanced 2027 preparation — aiming for Top 100*