<%*
const test = await tp.system.prompt("Test number (1-4):");
const paper = await tp.system.prompt("Paper number (1-2):");
const date = tp.date.now("YYYY-MM-DD");
-%>---
test: <% test %>
paper: <% paper %>
date: <% date %>
subjects: [Mathematics, Physics, Chemistry]
status: in-progress
tags: [solutions, jee-advanced, test-<% test %>]
---

# <% test %>-PAPER <% paper %> — COMPLETE SOLUTIONS (JEE Advanced Level)

<!--
FIGURES — no desktop-only plugin needed
Leave a fence unquoted (not inside a callout) and the build draws it into a committed SVG
that renders on every device, Obsidian Mobile included:

    ```smiles      molecule          e.g.  CC(=O)O Aspirin
    ```plot        function graph    e.g.  y = x^3 - 3x + 1
    ```circuit     circuit / vectors e.g.  d += elm.Resistor().right()

then run:  python3 tools/render_figures.py      (or: make figures)

Live examples: examples/figures-demo.md  |  Why plugins fail on phones: docs/PLUGIN-COMPATIBILITY.md
-->

> [!info] Paper Details
> **Target:** Top 100 Rank Improvement
> **Date:** <% date %>
> **Approach:** Multiple smart approaches per question, concept-first explanations, and full theory at the end.

---

## PART 1: MATHEMATICS

---

### Q1. 

> [!question] Question
> 

**Answer: ()** 

---

#### Approach 1 — 

> [!example]- Full Solution
> 

> [!success] Concept Used
> 

#### Approach 2 — 

---

## PART 2: PHYSICS

---

### Q20. 

> [!question] Question
> 

**Answer: ()** 

---

#### Solution

> [!abstract]- Diagram
> ```circuit
> d += elm.SourceV().up().label('12 V')
> d += elm.Resistor().right().label('R = 4 Ω')
> d += elm.Line().down()
> d += elm.Line().left()
> ```

> [!example]- Step-by-Step
> 

---

## PART 3: CHEMISTRY

---

### Q39. 

> [!question] Question
> 

**Answer: ()** 

---

#### Solution

> [!abstract]- Structure
> ```smiles
> C[C@H](N)C(=O)O Alanine
> ```

> [!example]- Mechanism / Analysis
> 

---

## 📚 COMPLETE THEORY REFERENCE

### Topic Name

> [!note] Key Formulas
> - 

> [!tip] JEE Tricks
> - 