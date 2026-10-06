# 📱 Mobile & Low-End Device Guide

> **Short answer:** those plugins aren't blocked by *your* device — the plugin authors marked them
> **desktop-only** (`"isDesktopOnly": true` in each plugin's `manifest.json`), so the Obsidian app on
> Android/iOS refuses to enable them and shows **“This plugin does not support your device.”**
> Nothing in this vault's solution notes actually needs them. Everything below is a workaround or a
> mobile-friendly replacement.

---

## 1. Why Obsidian says “not supported on this device”

A community plugin is just a folder with a `manifest.json`. That file contains one field that decides
whether a phone can ever run it:

```json
{
  "id": "molren",
  "name": "Molren",
  "version": "1.0.4",
  "minAppVersion": "1.4.0",
  "isDesktopOnly": true      // ← this line is why it won't install on a phone
}
```

When `isDesktopOnly` is `true`, Obsidian Mobile hides/refuses the plugin. There is no hardware check
going on — it is a promise the author makes about where the code can run.

**Why authors set that flag** (all four desktop-only plugins in this vault do, for real reasons):

| Reason | Example in this vault |
|---|---|
| Uses **Node.js / Electron APIs** that don't exist in the mobile WebView (`fs`, `child_process`, `electron`, native dialogs) | Plugins that spawn a LaTeX/binary process |
| Ships **heavy native/WebAssembly code** that is painful on a phone | **Molren** inlines the ~7 MB RDKit WebAssembly as base64 inside `main.js` (~9 MB of JS to parse at startup) |
| Bundles a **desktop-sized UI framework** | **Ketcher** embeds the full Ketcher molecule editor |
| UX is built around **mouse gestures** (right-click menus, scroll-wheel pan, drag-and-drop with hover) | **Circuit Sketcher** (right-click canvas → Create Node → Add Port…) |
| Opens **desktop-style views/windows** | **Plot Vectors and Graphs** (generates a new page with the FunctionPlot renderer) |

### The three different error messages (know which one you got)

| What you see | Real cause | Fix |
|---|---|---|
| “This plugin **does not support your device**” | `isDesktopOnly: true` | Use an alternative (§3) or the hack (§5a) |
| “Requires a **newer version of Obsidian**” | Plugin's `minAppVersion` > your Obsidian version | Update the app (Play Store / App Store / APK) |
| “**Failed to load** plugin” | Plugin launched but crashed (often a Node API called at startup, or a broken build on that WebView) | Reinstall/update the plugin; report upstream |

> **Right now, `minAppVersion` is a real trap:** Templater, Linter and Callout Manager currently
> require **Obsidian 1.13.0+**. If your phone can't update Obsidian any more, those three are also
> unavailable to you — with the *“newer version of Obsidian”* message, not the device message.

---

## 2. This vault's plugin stack — verified platform status

Read directly from each plugin's `manifest.json` (checked **October 2025**). ✔ = runs on
Android/iOS, ✖ = desktop-only.

| Plugin | `isDesktopOnly` | Mobile | What you lose on a phone |
|---|---|---|---|
| Molren (SMILES → SVG) | `true` | ✖ | Molecule rendering |
| Ketcher (molecule editor) | `true` | ✖ | Drawing/editing structures |
| Plot Vectors and Graphs | `true` | ✖ | LaTeX → function/vector plots |
| Circuit Sketcher | `true` | ✖ | Circuit-diagram canvas |
| TikZJax (tikz / chemfig / circuitikz / pgfplots) | `false` | ✔* | *Works, but compiles LaTeX in WebAssembly on-device — slow/heavy on phones |
| ChemEdit Universal | `false` | ✔ | — (offline SMILES/MOL renderer **and** editor) |
| Chem (Acylation) | `false` | ✔ | — |
| Desmos | `false` | ✔ | — |
| Kroki (server-side diagrams, incl. TikZ) | `false` | ✔ | — |
| Excalidraw | `false` | ✔ | Some desktop-only extras (PDF export, files outside the vault) |
| LaTeX Suite | `false` | ✔ | — |
| Numerals | `false` | ✔ | — |
| Calctex | `false` | ✔ | — |
| Dataview | `false` | ✔ | — |
| Templater | `false` | ✔ | Needs Obsidian **1.13+** |
| Linter | `false` | ✔ | Needs Obsidian **1.13+** |
| Table Editor | `false` | ✔ | — |
| Columns | `false` | ✔ | — |
| Mind Map | `false` | ✔ | — |
| callout-manager (Callout Manager) | `false` | ✔ | Needs Obsidian **1.13+** |

### ⚠️ About Numerals

**Numerals is officially Desktop + Mobile** — it is *not* a desktop-only plugin. If it refuses to
load on your device, the cause is one of these (not the platform gate):

1. **Wrong plugin ID in this vault's config (this was a real bug here — now fixed).**
   `.obsidian/community-plugins.json` listed `obsidian-numerals`, `obsidian-ketcher` and
   `obsidian-callout-manager`, but the real IDs are `numerals`, `ketcher` and `callout-manager`.
   Obsidian enables plugins **by ID**, so those three never switched on, on *any* device.
2. **The plugin files were never downloaded on that device** — see §7.
3. Obsidian older than **0.16.0** (Numerals' minimum).

---

## 3. Mobile-friendly alternatives (capability by capability)

| I want to… | Desktop-only plugin you tried | Use instead (mobile-compatible) |
|---|---|---|
| Render a molecule from SMILES | Molren | **ChemEdit Universal** (`smiles` code block, offline, no wasm) or **Chem** by Acylation. Both are `isDesktopOnly: false`. |
| Draw / edit a molecule or reaction | Ketcher | **ChemEdit Universal**'s touch-friendly editor, *or* open the **Ketcher web app** in your phone browser → export **SVG/MOL** → drop the file into the vault (`![[benzene.svg]]`) |
| Plot a function / vector | Plot Vectors and Graphs | **Desmos** plugin (`desmos-graph` block, Desktop+Mobile), **Mermaid `xychart-beta`** (built into Obsidian — zero plugins), **Kroki** (server-side vega/graphviz), or a pre-rendered SVG/PNG |
| Draw a circuit | Circuit Sketcher | **Kroki + `tikz`/`circuitikz`** (renders on their server, Desktop+Mobile — verified below), **Excalidraw** (Desktop+Mobile), Obsidian **Canvas** (core plugin) with a photo/PNG of your sketch |
| Inline calculation | Numerals | Numerals itself (mobile-supported) or **Calctex** (Desktop+Mobile) |
| Freehand: ray diagrams, FBDs | — | **Excalidraw** (works with finger/stylus on Android & iOS) |

### Don't double up

Molren, ChemEdit Universal and Chem **all** claim the ` ```smiles ` code block. Enable only **one**
of them per device, otherwise you get duplicate drawings under each block.

---

## 4. Snippets that work on a phone (copy-paste)

### 4.1 Graphs — Mermaid `xychart-beta` (core Obsidian, no plugin, no internet)

````markdown
```mermaid
xychart-beta
    title "y = x^3 - 3x + 1"
    x-axis [-3, -2, -1, 0, 1, 2, 3]
    y-axis "y" -25 --> 25
    line [1, 3, 5, 1, -1, 3, 19]
```
````

### 4.2 Graphs — Desmos plugin (`isDesktopOnly: false`)

````markdown
```desmos-graph
left=-5; right=5;
top=5; bottom=-5;
---
y=x^3-3x+1
y=0 | hidden | dashed | red
```
````

### 4.3 Molecules — ChemEdit Universal / Chem (`isDesktopOnly: false`)

````markdown
```smiles
CC(=O)Oc1ccccc1C(=O)O Aspirin
```
````

### 4.4 Circuits — Kroki plugin, TikZ/circuitikz rendered server-side (verified)

The **Kroki** plugin is `isDesktopOnly: false` and its README explicitly handles mobile (it loads the
result as an `<img>`). It supports the `tikz` block, and I verified a circuitikz circuit renders:

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

**Gotcha found while testing:** Kroki's LaTeX rejects a label that contains a **second `=` outside
braces** (`l=$R_1=60k\Omega$` → `400 ! Extra }, or forgotten $`). Wrap the whole label in braces —
`l={$R_1=60k\Omega$}` — and it compiles.

**Trade-off:** Kroki sends the diagram source to `kroki.io` (or your own self-hosted Kroki) and needs
internet. For exam notes that's fine; for privacy-sensitive content, self-host or pre-render (see §5b).

### 4.5 Paper-style sketches — Excalidraw / Canvas

- **Excalidraw:** create a drawing, embed with `![[ray-diagram.excalidraw]]` — works with finger/stylus
  on Android and iOS.
- **Canvas (core):** put PNGs/SVGs of a circuit next to text annotations; Canvas is a core plugin, so it
  works everywhere.

---

## 5. If you *really* want a desktop-only plugin on the phone

### 5a. Flip the manifest flag (hack — expect breakage)

1. On a computer, open `.obsidian/plugins/<plugin>/manifest.json`.
2. Change `"isDesktopOnly": true` → `false`.
3. Sync the vault to the phone, restart Obsidian mobile, enable the plugin.

Reality check: this **only** works for plugins that were merely *untested* on mobile. Molren,
Ketcher, Plot Vectors and Circuit Sketcher are flagged for structural reasons (7 MB wasm, Node calls,
mouse-only UI) — they will likely show a blank view or “Failed to load”. The flag also resets on every
plugin update. Don't report bugs to the authors if you do this.

### 5b. Render once on a computer, read everywhere (recommended — no plugins needed)

This is the bullet-proof route for a phone-only reader:

1. On any desktop (or a free GitHub Action / Overleaf), render the figure to **SVG**:
   - `smiles` → `rdkit` / ChemEdit → export SVG
   - `tikz`/circuitikz/pgfplots → `pdflatex` + `dvisvgm` (or Kroki)
   - `desmos` → use Desmos' own **Export image** button
2. Save it under `assets/diagrams/` or `assets/chemistry/` and commit it.
3. Embed it: `![[assets/diagrams/rc-circuit.svg]]`

Images render on every device, in Obsidian Sync, and in PDF export — no plugin, no WebAssembly, no
internet. For a revision vault aimed at a phone, this is usually the right trade.

### 5c. Server-side rendering

Keep the readable source in the note (`tikz`, `mermaid`, `vega`) and let a server do the heavy work:
**Kroki** (plugin or self-hosted), or a GitHub Action that renders diagrams on push and commits the
SVGs. Best of both worlds: the note stays searchable text, the phone only downloads an image.

---

## 6. Mobile setup for *this* vault — `.obsidian-mobile`

Obsidian can use a **different config folder per device** (Settings → About → *Override config
folder*). This repo now ships a ready-made one:

```
.obsidian-mobile/
├── app.json                 ← same editor settings as desktop
├── core-plugins.json        ← same core plugin set
└── community-plugins.json   ← only the mobile-safe plugins
```

**Steps**

1. Sync/clone the repo to the phone.
2. Obsidian → **Settings → About → Override config folder** → type `.obsidian-mobile`.
3. Restart Obsidian. The desktop-only plugins are simply absent, so there are no “not supported”
   errors and a faster startup.
4. Install only the ones you want from **Settings → Community plugins → Browse** (the vault config
   lists IDs, it can't download code — see §7).

Enabled in `.obsidian-mobile` by default: Excalidraw, ChemEdit Universal, Desmos, Kroki, LaTeX Suite,
Numerals, Dataview, Templater, Linter, Table Editor, Columns, Mind Map.

Left out on purpose: `molren`, `ketcher`, `plot-vectors-graphs`, `circuit-sketcher` (desktop-only),
`obsidian-tikzjax` (works on mobile but heavy — turn it on yourself if your phone handles it),
`chem` (would double-render every `smiles` block alongside ChemEdit Universal).

---

## 7. Troubleshooting checklist for phones/tablets

1. **“Failed to load community plugins” / the Browse list is empty.**
   Usually **not** your device: some ISPs (several Indian providers included) block or poison the
   `raw.githubusercontent.com` domain Obsidian uses for the plugin index. Change DNS to
   `1.1.1.1` / `8.8.8.8` (or use a VPN), restart Obsidian. This is a known, well-documented issue.
2. **Plugins listed in the vault config but nothing happens.**
   Check the IDs match the real plugin IDs. `obsidian-numerals` → **`numerals`**,
   `obsidian-ketcher` → **`ketcher`**, `obsidian-callout-manager` → **`callout-manager`**. (Fixed in
   this repo; if you have a local copy, apply the same fix.)
3. **The plugin folder is empty.**
   `.gitignore` in this repo excludes `main.js` / `manifest.json` / `styles.css` on purpose, so a git
   clone gives you *settings* but not the *code*. Install each plugin once per device from
   **Settings → Community plugins → Browse** (or copy the files over manually).
4. **“This plugin does not support your device.”**
   It is the `isDesktopOnly` gate — no setting, version or workaround will change it, except §5a.
5. **“Requires a newer version of Obsidian.”**
   Update the app. If the device can no longer update Obsidian, pick a plugin with a lower
   `minAppVersion` (check the plugin page's *Compatible with* line).
6. **Renders but crawls / battery drains.**
   TikZJax and Desmos are the CPU-heavy ones. Move those figures to pre-rendered SVGs (§5b) and keep
   text/Mermaid live.

---

## 8. Why this vault is fine on a phone *today*

I checked all eight solution files: they contain **zero** fenced code blocks — no `tikz`, no `smiles`,
no `desmos-graph`. Everything is standard Markdown plus MathJax (`$…$`, `$$…$$`) and Obsidian
callouts, both of which are **core** features that work identically on desktop and mobile.

So on your device, right now:

- ✅ All 8 solution files render, with every equation, callout and table
- ✅ Reading, search, graph view, PDF export — all core
- ⚠️ Only these are missing: the *optional extras* (molecule pictures, interactive plots, circuit
  drawings) — and §3/§4 covers each one with a mobile-compatible route

**Bottom line:** the four plugins that refuse to install are desktop-only by design and are
replacements-in-progress, not a broken setup. If you write notes on the phone, use Mermaid + Desmos +
ChemEdit Universal; if you need TikZ-quality figures, render them once and commit the SVG.

---

*Last verified: October 2025 — platform flags read straight from each plugin's `manifest.json`;
the Kroki circuitikz example was rendered successfully server-side while writing this guide.*
