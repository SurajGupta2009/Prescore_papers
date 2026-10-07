# assets/

Everything the notes embed. Everything here is committed, so a phone that pulls the repo
gets finished pictures and never has to render or compile anything.

```
assets/
├── diagrams/            ← figures (mostly generated)
│   ├── smiles-*.svg     ← rendered from ```smiles fences by tools/render_figures.py
│   ├── plot-*.svg       ← rendered from ```plot fences
│   ├── circuit-*.svg    ← rendered from ```circuit fences
│   ├── figures.json     ← registry: source text + notes for every generated figure
│   └── *.png / *.svg    ← hand-made or exported images (left untouched by the pipeline)
└── chemistry/           ← optional: molecule images exported from a browser editor
```

## Adding a figure

**Option A — a fence (recommended).** Write the source in a note, then:

```bash
python3 tools/render_figures.py     # or: make figures
```

The fence is replaced by `![[assets/diagrams/<kind>-<hash>.svg]]` and the SVG is written
here. The original text is kept in `figures.json`, so nothing is lost and
`--restore` can put the fences back.

**Option B — drop a file in.** Export PNG/SVG from Ketcher, PubChem, GeoGebra, Falstad or
Desmos and save it in `assets/diagrams/`. Embed it with
`![[assets/diagrams/my-figure.png]]`. The pipeline ignores files it did not generate.

## Rules of thumb

- Prefer **SVG** (crisp at any zoom, small, theme-independent because the pipeline forces a
  white background). Use PNG for screenshots and hand-drawn exports.
- Keep the file name descriptive for hand-made files, hashed for generated ones — the hash
  **is** the identity: change the fence, get a new file, and `--prune` removes the old one.
- Never edit a generated `.svg` by hand: the next build overwrites it. Edit the fence.
