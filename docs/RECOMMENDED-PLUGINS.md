# 🔌 Recommended Plugins — With Device Support On Every Row

> **Settings → Community plugins → Browse → search the ID in the first column.**
>
> This list is **phone-first**: the *Mobile* column is checked against each plugin's live
> `manifest.json` (`isDesktopOnly`), not against marketing copy. Anything that cannot run
> on a phone is either listed as ❌ and given a replacement, or left out entirely.
> The story behind the ❌ rows: [PLUGIN-COMPATIBILITY.md](PLUGIN-COMPATIBILITY.md).

Legend: ✅ mobile-capable · ❌ desktop-only (store hides it on phones) · ⭐ enabled by default in this vault

---

## 🟢 Tier 1 — install these first

| Install ID | Plugin | Mobile | Why it earns a slot |
|---|---|---|---|
| `obsidian-latex-suite` | ⭐ **Latex Suite** | ✅ | Type math at handwriting speed: `@a` → `\alpha`, `//` → `\frac{}{}`, `sq` → `\sqrt{}` |
| `dataview` | ⭐ **Dataview** | ✅ | Query the vault like a database — progress dashboards, answer keys |
| `templater-obsidian` | ⭐ **Templater** | ✅ | Note scaffolding used by `templates/new-solution.md` |
| `obsidian-excalidraw-plugin` | ⭐ **Excalidraw** | ✅ | Freehand force diagrams, ray optics — works with a finger |
| `obsidian-tikzjax` | ⭐ **TikZJax** | ✅ | TikZ/chemfig/circuitikz/pgfplots in notes. Light diagrams on a phone; heavy ones are slow — prefer `smiles`/`plot`/`circuit` fences for those |
| `obsidian-desmos` | ⭐ **Desmos** | ✅ | Interactive `desmos-graph` blocks, online and offline |
| `numerals` | ⭐ **Numerals** | ✅ | Inline calculator code blocks. **The ID is `numerals`** (this vault previously wrote `obsidian-numerals` and so it never installed) |
| `callout-manager` | ⭐ **Callout Manager** | ✅ | Custom callout colours/icons. **The ID is `callout-manager`** (previously `obsidian-callout-manager`) |

---

## 🧪 Chemistry

| Install ID | Plugin | Mobile | Verdict |
|---|---|---|---|
| `chemedit-universal` | ⭐ **ChemEdit Universal** | ✅ | Editor + viewer, offline, PubChem lookup. The best mobile pick |
| `chem` | **Chem** | ✅ | Renders `chem`/`smiles` code blocks, 100+ stars, actively maintained |
| `chemtrails` | **Chemtrails** | ✅ | Lightweight SMILES → crisp SVG |
| `chemical-structure-renderer` | **Chemical Structure Renderer** | ✅ | SMILES → PNG/SVG (Indigo service needed for full features) |
| `molren` | **Molren** | ❌ | Desktop-only (RDKit WASM design) — use `chem`/`chemedit-universal`, or this repo's ```` ```smiles ```` pipeline |
| `ketcher` | **Ketcher** | ❌ | Desktop-only (registry ID is `ketcher`, not `obsidian-ketcher` — the old README used the repo name). Use the [online Ketcher demo](https://lifescience.opensource.epam.com/KetcherDemoSA/index.html) in the phone browser, or the ```` ```smiles ```` pipeline |
| `chemedit` | **ChemEdit** (the older one) | ❌ | Superseded by `chemedit-universal` |

### Molecule without any plugin — the pipeline in this repo

````markdown
```smiles
CC(=O)Oc1ccccc1C(=O)O Aspirin (acetylsalicylic acid)
C[C@H](N)C(=O)O L-Alanine (wedge shown)
```
````

renders to a committed SVG that any device displays:

![[assets/diagrams/smiles-2763fbacc5.svg]]

---

## 📊 Maths — graphs, plots, vectors

| Install ID | Plugin | Mobile | Verdict |
|---|---|---|---|
| `obsidian-desmos` | ⭐ **Desmos** | ✅ | The interactive plotter — sliders, tangents, roots |
| `obsidian-plotly` | **Plotly** | ✅ | `plotly` blocks: interactive charts inside the note |
| `obsidian-latex-suite` | ⭐ **Latex Suite** | ✅ | Non-negotiable for JEE-speed typing |
| `numerals` | ⭐ **Numerals** | ✅ | Calculator blocks — see Tier 1 |
| `plot-vectors-graphs` | **Plot Vectors and Graphs** | ❌ | Desktop-only. Use the ```` ```plot ```` fence here, GeoGebra for vectors, or Desmos when you want sliders |
| `math-plotter` | **Math Plotter** | ❌ | Desktop-only despite the name |
| `live-plots` | **Live Plots** | ❌ | Desktop-only |

### Static graph without any plugin

````markdown
```plot
y = x^3 - 3x + 1
y = 3x - 3   @ tangent at x = 2
x: [-4, 4]
y: [-8, 8]
title: Cubic and its tangent
```
````

![[assets/diagrams/plot-dbd764a532.svg]]

For vectors and coordinate geometry, GeoGebra in the browser is the power tool:
[geogebra.org/classic](https://www.geogebra.org/classic) → export PNG → embed.

---

## ⚡ Physics — circuits and field diagrams

| Install ID | Plugin | Mobile | Verdict |
|---|---|---|---|
| `obsidian-tikzjax` | ⭐ **TikZJax** | ✅ | `circuitikz` on mobile for small circuits; keep one diagram per note |
| `obsidian-excalidraw-plugin` | ⭐ **Excalidraw** | ✅ | Freehand: force diagrams, ray tracing, field lines |
| `desmos` (`obsidian-desmos`) | ⭐ **Desmos** | ✅ | SHM, orbital mechanics, I–V curves |
| `circuit-sketcher` | **Circuit Sketcher** | ❌ | Desktop-only canvas editor. Use the ```` ```circuit ```` fence, or [Falstad CircuitJS](https://www.falstad.com/circuit/circuitjs.html) in the browser (it *simulates*) |
| `obsidian-circuitjs` | **CircuitJS** | ❌ | Desktop-only. Browser version linked above |

### Circuit or vector diagram without any plugin

````markdown
```circuit width=680
d += elm.SourceV().up().at((0, 0)).length(2.5).label('V = 12 V')
d += elm.Resistor().right().label('R = 1 kΩ')
d += elm.Capacitor().down().length(2.5).label('C = 10 µF')
d += elm.Line().left().length(3)
```
````

![[assets/diagrams/circuit-662653c049.svg|680]]

---

## 🗂 Writing, organisation, revision

| Install ID | Plugin | Mobile | Verdict |
|---|---|---|---|
| `dataview` | ⭐ **Dataview** | ✅ | Progress tables, per-topic indexes |
| `templater-obsidian` | ⭐ **Templater** | ✅ | Question/approach templates |
| `obsidian-linter` | ⭐ **Linter** | ✅ | Uniform formatting across 8 paper files |
| `table-editor-obsidian` | ⭐ **Advanced Tables** | ✅ | Answer-key tables without tears |
| `obsidian-columns` | ⭐ **Columns** | ✅ | Side-by-side approach comparisons |
| `obsidian-mind-map` | ⭐ **Mind Map** | ✅ | Topic overview per paper |
| `callout-manager` | ⭐ **Callout Manager** | ✅ | See Tier 1 (ID fixed) |

---

## 🚫 Not recommended on a phone, and what to use instead

| Blocked plugin | Use instead |
|---|---|
| Molren, Ketcher | `chem` / `chemedit-universal`, or [Ketcher online](https://lifescience.opensource.epam.com/KetcherDemoSA/index.html) / [PubChem editor](https://pubchem.ncbi.nlm.nih.gov/edit3/index.html) |
| Plot Vectors and Graphs | ```` ```plot ```` fence, Desmos, [GeoGebra](https://www.geogebra.org/classic) |
| Circuit Sketcher, CircuitJS | ```` ```circuit ```` fence, [Falstad CircuitJS](https://www.falstad.com/circuit/circuitjs.html) |
| Any heavy TikZ block | Render once on desktop → commit the SVG/PNG → read it anywhere |

---

## 🧭 Diagram decision tree (phone-first)

```
What do you need to draw?
│
├── Molecule
│   ├── in the vault, offline  → ```smiles fence  (this repo renders it)
│   └── draw/eyeball it now    → Ketcher or PubChem editor in the browser
│
├── Function graph
│   ├── static, offline        → ```plot fence
│   └── sliders / exploration  → Desmos (plugin or web)
│
├── Circuit
│   ├── static                 → ```circuit fence  (or TikZJax circuitikz)
│   └── simulate it            → Falstad CircuitJS in the browser
│
├── Vectors / coordinate geometry
│   ├── static                 → ```circuit fence with elm.Arrow, or ```plot
│   └── interactive            → GeoGebra Classic in the browser
│
├── Freehand (ray optics, FBD) → Canvas (core) or Excalidraw (✅ mobile)
│
├── Flowchart / reaction scheme → Mermaid (core plugin, ✅) or Mind Map
│
└── Arithmetic on the fly
    ├── in a note              → Numerals (id: numerals, ✅)
    └── no plugin              → MathJax $\frac{}{}$ and a plain text block
```

---

## ⚙️ Install order for a phone

1. **Enable the core plugins** — *Settings → Core plugins* → **Mermaid** and **Canvas**
   (already enabled in this vault's config).
2. **Numerals** (`numerals`) — calculators everywhere.
3. **Latex Suite** (`obsidian-latex-suite`) — typing speed.
4. **Desmos** (`obsidian-desmos`) — instant graph checks.
5. **ChemEdit Universal** (`chemedit-universal`) — molecules in-app.
6. **Excalidraw** (`obsidian-excalidraw-plugin`) — freehand figures.
7. **TikZJax** (`obsidian-tikzjax`) — when you need real LaTeX drawing.
8. **Dataview** + **Templater** + **Linter** — keep the vault tidy.
9. **Plotly** (`obsidian-plotly`) — if you want interactive charts in-note.
10. Leave Molren, Ketcher, Plot Vectors & Graphs, Circuit Sketcher **off on mobile** —
    set them up on a desktop-only config folder if you want them there.
    See [PLUGIN-COMPATIBILITY.md § Desktop vs mobile config](PLUGIN-COMPATIBILITY.md).

---

## Related

- [PLUGIN-COMPATIBILITY.md](PLUGIN-COMPATIBILITY.md) — why the desktop-only ones fail, with evidence
- [DIAGRAMS-WITHOUT-PLUGINS.md](DIAGRAMS-WITHOUT-PLUGINS.md) — the full alternatives playbook
- [`examples/figures-demo.md`](../examples/figures-demo.md) — the three fences, rendered
