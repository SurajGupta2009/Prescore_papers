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
FIGURES - all rendered live by plugins, no exported images.

    ```tikz           circuits (circuitikz), molecules (chemfig), plots, geometry
    ```desmos-graph    function graphs (settings, ---, then equations)
    ```smiles          one SMILES per line (ChemEdit Universal / Chem / Chemtrails)
    ```math            unit-aware calculation checks (Numerals)

Validate before committing:  python3 tools/check_figures.py
Syntax reference: docs/PLUGIN-FIGURES.md
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
> ```tikz
> \usepackage{circuitikz}
> \begin{document}
> \begin{circuitikz}[american]
>   \draw (0,0) to[battery1, l=$V$] (0,2.5) to[R, l=$R$] (3,2.5) to[C, l=$C$] (3,0) -- (0,0);
> \end{circuitikz}
> \end{document}
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