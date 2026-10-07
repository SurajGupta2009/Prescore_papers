# 🔍 Why 5 Plugins Say "This Plugin Does Not Support Your Device"

> **Short answer:** those five plugins ship with `"isDesktopOnly": true` in their
> `manifest.json`. Obsidian treats that flag as a hard block: on Android and iOS the
> plugin is **hidden from the community-plugin browser** and, if it is already listed as
> enabled, it is **skipped at load** — the app shows *"This plugin does not support your
> device"*. It is not a bug in your phone, your Obsidian version or your vault. The
> author has to decide to support mobile; four of these five did not (yet).

**Four of the five are genuinely desktop-only. The fifth — Numerals — works fine on
mobile; this vault just had the wrong plugin ID for it.**

---

## 1. Verified status of every figure plugin in this vault

Checked against the live `obsidianmd/obsidian-releases` registry and each project's own
`manifest.json` (October 2026).

| Vault references… | Real plugin & repo | Latest | `isDesktopOnly` | On Android/iOS |
|---|---|---|---|---|
| `molren` | **Molren** — [quiachonj/molren](https://github.com/quiachonj/molren) | 1.0.4 | **`true`** | ❌ blocked |
| `obsidian-ketcher` | **Ketcher** — [yulei-chen/obsidian-ketcher](https://github.com/yulei-chen/obsidian-ketcher) | 0.2.3 | **`true`** | ❌ blocked |
| `plot-vectors-graphs` | **Plot Vectors and Graphs** — [nicoletanyt/obsidian-plugin-graphs](https://github.com/nicoletanyt/obsidian-plugin-graphs) | 1.0.2 | **`true`** | ❌ blocked |
| `circuit-sketcher` | **Circuit Sketcher** — [code-forge-temple/circuit-sketcher-obsidian-plugin](https://github.com/code-forge-temple/circuit-sketcher-obsidian-plugin) | 1.4.0 | **`true`** | ❌ blocked |
| `obsidian-numerals` | **Numerals** — [gtg922r/obsidian-numerals](https://github.com/gtg922r/obsidian-numerals) | 1.10.2 | `false` | ✅ **works** — wrong ID in this vault |

The real plugin ID is `numerals`, not `obsidian-numerals`. With the correct ID, Numerals
installs on mobile like any other plugin (no crash, no "unsupported device" prompt —
the option that used to be desktop-only, *in-block TeX rendering*, is simply off by
default and can stay off).

### Why each author marked it desktop-only

| Plugin | Author's own reason (from the project's README / code) |
|---|---|
| **Molren** | README: *"Molren is desktop-only"*. The RDKit `.wasm` (~7 MB) is inlined into `main.js` as base64 and decoded at load; that design and testing target the desktop app. |
| **Ketcher** | README: *"An Obsidian desktop plugin for viewing and drawing chemical structures … with Ketcher"*. Ketcher is a large React bundle; the project targets the desktop app. |
| **Plot Vectors and Graphs** | Marked `isDesktopOnly: true` in its manifest — no mobile build published. |
| **Circuit Sketcher** | A canvas editor driven by mouse context menus, drag-and-drop ports and `right-click`; the manifest declares desktop-only. |

> [!warning] Don't "fix" it by editing `main.js`/`manifest.json`
> You *can* hand-edit `isDesktopOnly` to `false` on desktop and sync the file to the
> phone. It usually fails: these plugins call Node/desktop APIs (`require('fs')`,
> `child_process`, native Cairo/WASM bindings) that do not exist in Obsidian Mobile, so
> the plugin errors or crashes on enable. A plugin cannot gain a capability by editing a
> flag.

### 30-second confirmation test (on the phone)

1. **Settings → Community plugins → Browse**.
2. Search `molren`. If it does not appear in the list at all, the mobile app is filtering
   it out — that is the flag at work.
3. **Show installed plugins** → the four desktop-only ones are listed as *not supported on
   this device*, and are skipped even when the vault's config enables them.

---

## 2. What the vault looked like before the fix

`.obsidian/community-plugins.json` used to enable all 17 plugins on every device,
including the four desktop-only ones and the two wrong IDs. On a phone that produced:

- 4 plugins silently skipped → every ```` ```smiles ````, ```` ```plot ```` and
  ```` ```circuit ```` fence fell back to a **plain grey code block**;
- **Numerals** never installed (wrong ID) → arithmetic blocks stayed raw text;
- **Callout Manager** never installed (ID `obsidian-callout-manager` vs real
  `callout-manager`) → custom callouts fell back to the built-in set, which is cosmetic
  but looks like a "broken theme";

Meanwhile the README advertised "📊 Desmos graphs, 🧪 chemical structures, ⚡ circuit
diagrams" as vault features. That mismatch is the bug this repo now fixes.

### What changed

| Area | Now |
|---|---|
| `.obsidian/community-plugins.json` | Only **mobile-capable** plugins are enabled by default; IDs corrected (`numerals`, `callout-manager`). |
| `.obsidian/core-plugins.json` | Added the built-in **Mermaid** and **Canvas** core plugins — diagrams with *zero* community plugins. |
| Chemistry, graphs, circuits | Rendered **live** by four mobile-capable plugins — TikZJax (tikz), Desmos, ChemEdit Universal (smiles), Numerals (math). See **[PLUGIN-FIGURES.md](PLUGIN-FIGURES.md)**. |
| Plugins that *do* support mobile | Documented in the rewritten **[RECOMMENDED-PLUGINS.md](RECOMMENDED-PLUGINS.md)**, with a device-support column on every row. |

---

## 3. Reproduce this audit yourself

```bash
# every plugin ID this vault enables, resolved against the official registry
curl -s https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugins.json \
  | python3 - <<'PY'
import json, sys, urllib.request
reg = {p["id"]: p for p in json.load(sys.stdin)}
vault = json.load(open(".obsidian/community-plugins.json"))
for pid in vault:
    p = reg.get(pid)
    if not p:
        print(f"{pid:28} NOT IN REGISTRY (wrong id?)")
        continue
    url = f"https://raw.githubusercontent.com/{p['repo']}/HEAD/manifest.json"
    m = json.load(urllib.request.urlopen(url))
    print(f"{pid:28} desktopOnly={m.get('isDesktopOnly')!s:5} v{m.get('version')}  {p['name']}")
PY
```

The same data lives, pre-computed and annotated, in the tables above — no internet needed
to read it.

---

## 4. Desktop vs mobile config (how to keep desktop-only plugins *and* a phone)

Obsidian reads plugin enablement from the vault's config folder (`.obsidian` by default).
The clean way to run desktop-only plugins without breaking the phone is a **separate config
folder per device** — no syncing fights, no "unsupported device" prompts:

1. Copy `.obsidian/` to `.obsidian-desktop/` **on the desktop**.
2. Desktop: *Settings → Files and links → Override config folder* → `.obsidian-desktop`.
3. Install/enable Molren, Ketcher, Circuit Sketcher, Plot Vectors & Graphs there.
4. Phone keeps this repo's `.obsidian/`, which now enables only mobile-capable plugins.
5. When syncing, exclude `workspace.json`, `workspace-mobile.json`, `graph.json`,
   `starred.json` and the plugin `data.json` files (already in this repo's `.gitignore`).

The figures those desktop plugins draw are still worth sharing: export them to
`assets/diagrams/` and embed the PNG/SVG, or redraw them as `tikz` / `smiles` blocks so
they render on both devices — see [PLUGIN-FIGURES.md](PLUGIN-FIGURES.md).

---

## 5. Where to go next

| You want | Read |
|---|---|
| The syntax of every figure block (tikz / desmos / smiles / math) | [PLUGIN-FIGURES.md](PLUGIN-FIGURES.md) |
| A plugin list that is honest about device support | [RECOMMENDED-PLUGINS.md](RECOMMENDED-PLUGINS.md) |
| To see it working end-to-end | open `solutions/1-paper1-solutions.md` on the phone |
| To validate every figure block before committing | `python3 tools/check_figures.py` |
