# Figure Pipeline — demo & reference

> [!info] What this note is
> This note is the **proof and the manual** for `tools/render_figures.py`, the plugin-free
> replacement for Molren, Ketcher, Plot Vectors & Graphs, Circuit Sketcher and Numerals.
> Open it on your phone: every figure below is a plain `.svg` file committed to the repo, so it
> renders without a single community plugin.

---

## 1. Chemistry — `smiles` blocks

WRITE THIS:

````markdown
```smiles
CC(=O)Oc1ccccc1C(=O)O Aspirin (acetylsalicylic acid)
```
````

GET THIS (rendered by RDKit at build time, stored in `assets/diagrams/`):

![[assets/diagrams/smiles-fe9a034e22.svg]]

More than one structure per block works; each line is `SMILES<space>Label`:

![[assets/diagrams/smiles-457c5fbcb2.svg]]

A reaction can be written as one SMILES with `>>`, exactly like RDKit reactions:

![[assets/diagrams/smiles-a7b0556015.svg]]

> [!info] Which chemistry engine draws this?
> **RDKit** if it is installed (the same engine family Molren uses in the browser via
> WASM); otherwise the pipeline falls back to **Indigo**, the engine behind Ketcher. Both
> are offline and produce self-contained SVG. Check which one ran:
> `python3 -c "import tools.render_figures as r; print(r._chemistry_backend()[0])"`.

> [!tip] Why this beats Molren/Ketcher here
> Molren and Ketcher both ship `"isDesktopOnly": true` — Obsidian refuses to enable them on
> Android/iOS. The SVG above has no runtime at all, so it works on any device, and it also
> shows up in PDF exports, GitHub previews and plain markdown viewers.

---

## 2. Graphs — `plot` blocks

WRITE THIS:

````markdown
```plot
y = x^3 - 3x + 1
y = 3x - 3    @ tangent at x = 2
x: [-4, 4]
y: [-8, 8]
title: Cubic and its tangent
```
````

GET THIS:

![[assets/diagrams/plot-ed93f61736.svg]]

Physics-flavoured example — SHM displacement and velocity:

![[assets/diagrams/plot-2a127c5b91.svg]]

Syntax inside a `plot` block:

- `y = <expression>` — one line per curve (`=` before the expression is optional).
- `@ caption` — optional label for that curve (shows up in the legend).
- `# comment` — ignored.
- `x: [a, b]` / `y: [a, b]` — axis ranges (y is auto-scaled if omitted), `grid: true|false`,
  `title: ...`, `width: 900`, `height: 470`, `samples: 1200`.

The parser understands `^`, implicit products (`3x`, `2sin(x)`), `|x|`, `ln`, `exp`,
`H(x)` (Heaviside), and gives each curve its own colour and line style.

> [!warning] What `plot` does **not** replace
> It is a static renderer: you cannot drag a slider like in Desmos. For interactive
> exploration open [desmos.com](https://www.desmos.com/calculator) in the phone browser —
> that needs no plugin either.

---

## 3. Circuits and vector diagrams — `circuit` blocks

WRITE THIS (the body is ordinary schemdraw code — deliberately close to circuitikz):

````markdown
```circuit width=620
d += elm.SourceV().up().at((0, 0)).length(2.5).label('12 V')
d += elm.Resistor().right().label('R₁ = 2 Ω')
d += elm.Resistor().right().label('R₂ = 4 Ω')
d += elm.MeterA().down().length(2.5).label('2 A')
d += elm.Line().left().length(6)
```
````

GET THIS — a series loop with an ammeter in it:

![[assets/diagrams/circuit-f24cfb1885.svg|620]]

And a Wheatstone bridge with a galvanometer between the mid-nodes — the kind of
figure that used to need circuitikz or Circuit Sketcher:

![[assets/diagrams/circuit-f68b47a5f3.svg|760]]

An RC charging circuit, drawn left to right:

![[assets/diagrams/circuit-662653c049.svg|680]]

> [!tip] Drawing vocabulary
> `elm.*` mirrors circuitikz: `elm.Resistor`, `elm.Capacitor`, `elm.Inductor`,
> `elm.Battery`, `elm.SourceV`, `elm.SourceI`, `elm.SourceSin`, `elm.Diode`,
> `elm.Lamp`, `elm.Switch`, `elm.Ground`, `elm.MeterA` (ammeter),
> `elm.MeterV` (voltmeter), `elm.MeterI` (galvanometer), `elm.Opamp`, `elm.Motor`.
> Elements chain with `.right()/.up()/.down()/.left()`, `.label('...')`,
> `.label('...', loc='bottom')`, `.at((x, y))`, `.length(n)`, `.color('red')`,
> `.dot()` for junction nodes, and `d.push()` / `d.pop()` to branch.

Vector diagrams work too — arrows are just lines with arrowheads:

![[assets/diagrams/circuit-5e163617dd.svg|620]]

---

## 4. Quick arithmetic (what Numerals used to do)

Numerals **is** mobile-compatible — it just has the wrong ID in this vault's config
(`obsidian-numerals` instead of `numerals`). Until you install it, keep one-liners in a
plain code block:

```text
R_eq   = 6·3/(6+3) + 4·2/(4+2) = 2 + 1.333 = 3.333 Ω
τ      = R·C = 3.333e3 × 10e-6 = 33.3 ms
v(τ)   = 24(1 − e⁻¹) = 24 × 0.6321 = 15.17 V
```

---

## 5. Rebuilding the figures

```bash
pip install -r tools/requirements.txt
python3 tools/render_figures.py            # fences -> SVG, edits the notes in place
python3 tools/render_figures.py --check    # CI guard: exit 1 if a figure is stale
python3 tools/render_figures.py --restore  # put the code blocks back
make figures                               # same thing via make
```

Every generated file is tracked in git, so a phone that pulls the repo gets finished
pictures — it never has to compile anything.
