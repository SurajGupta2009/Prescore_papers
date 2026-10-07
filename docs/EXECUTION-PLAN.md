# 📋 Master Plan: Complete JEE Advanced Solutions Overhaul (Tests 1–4)

> **Objective:** Upgrade and complete all solution papers (`1-paper1` through `4-paper2`) into comprehensive, top-rank JEE Advanced study guides. Each paper must feature multiple smart approaches, BSc/MSc-level shortcuts in concise callouts, rigorous end-of-file theory compilations, and device-compatible Obsidian plugins (`TikZJax` for ChemFig/Circuits/PGFPlots, `Desmos`, `Chemtrails`, and Obsidian Callouts).

---

## 🏗 Standard Specification for Every Solution Note

Each file in `solutions/` must adhere strictly to this schema:

### 1. Frontmatter & Header
```yaml
---
test: [1|2|3|4]
paper: [1|2]
subjects: [Mathematics, Physics, Chemistry]
status: complete
tags: [solutions, jee-advanced, test-X]
---
```

### 2. Per Question Schema
- **Question Statement & Metadata:** Clear question definition and final answer in bold.
- **Approach 1 — Standard / JEE Exam Method:** Direct, robust method following JEE syllabus.
- **Approach 2 — Exam Hack / Elimination / Symmetry / Dimensional Analysis:** Rapid 30-second inspection techniques, symmetry shortcuts, or graphical checks.
- **Approach 3 (Where Applicable) — Advanced BSc/MSc Insight:** High-level mathematical or physical machinery presented concisely (e.g., Contour Integration, Residue Theorem, Green's Functions, Operator Formalism, Group Theory/Symmetry, Perturbation Analysis, MO Theory).
- **Embedded Obsidian Diagram / Plugin:**
  - *Circuits:* ```` ```tikz \usepackage{circuitikz} ... ``` ````
  - *Chemistry (Organic / Mechanisms):* ```` ```tikz \usepackage{chemfig} ... ``` ```` or ```` ```smiles ... ``` ````
  - *Coordinate Geometry & Curves:* ```` ```tikz \usepackage{pgfplots} ... ``` ```` or ```` ```desmos-graph ... ``` ````
- **Callout Summary:**
  - `> [!tip] Exam Shortcut`
  - `> [!warning] Trap & Common Pitfall`
  - `> [!success] Key Takeaway`

### 3. End-of-File Comprehensive Theory Vault
- Complete theory summary for Math, Physics, and Chemistry tested in that paper.
- Master formula sheet and reaction mechanism reference tables.

---

## 🗂 Division of Work by Test (Ready for Parallel Agent Execution)

---

### 🟢 Phase 1: Test 1 (`solutions/1-paper1-solutions.md` & `1-paper2-solutions.md`)
*Focus: Deepen existing content, ensure 100% diagram coverage, and verify high-level BSc/MSc insights.*

#### File: `1-paper1-solutions.md`
- **Math:**
  - Roots of unity, polynomial decomposition, binomial sums with complex roots.
  - *BSc/MSc Insight:* Rouche's Theorem, Vieta's symmetric polynomials in $\mathbb{C}$.
  - *TikZ/PGFPlots:* Argand plane circle locus and closest distance vector (Q4).
- **Physics:**
  - RC circuits with multiple switches, potentiometer balancing, infinite honeycomb resistor grid.
  - *BSc/MSc Insight:* Laplace transform $s$-domain impedance, lattice Green's functions for infinite 2D networks.
  - *Circuitikz:* Dual-switch transient RC circuit (Q19), potentiometer multi-balancing schematic (Q34), cube network equipotential shorting (Q24).
- **Chemistry:**
  - Nylon-610 polymerization, Dumas nitrogen quantification, non-reducing disaccharides.
  - *ChemFig:* Condensation polymerization of hexamethylenediamine + sebacic acid (Q47), sucrose glycosidic $(1\to 2)$ bridge (Q48).

#### File: `1-paper2-solutions.md`
- **Math:**
  - Octahedron resistor symmetry, complex geometry, binomial identities.
- **Physics:**
  - Five-bulb non-linear circuit bridge (Q23), dual-switch capacitor network (Q24), sliding dielectric forces.
  - *Circuitikz:* Five-bulb bridge topology, switched capacitor network.
- **Chemistry:**
  - Coordination isomerism, organic reaction cascades, amino acid electro-migration.
  - *ChemFig:* Zwitterionic forms at varying pH, octahedral crystal field splitting ($\Delta_o$).

---

### 🟡 Phase 2: Test 2 (`solutions/2-paper1-solutions.md` & `2-paper2-solutions.md`)
*Focus: Expand abbreviated drafts into full-scale solutions with all approaches and diagrams.*

#### File: `2-paper1-solutions.md`
- **Math:**
  - Combinatorics ($S_1, S_2, S_3$ cardinalities), inverse trigonometric identities, calculus limits.
  - *BSc/MSc Insight:* Generating functions for constrained integer partitions, Taylor asymptotic expansions.
  - *Desmos/PGFPlots:* Inverse trigonometric piecewise domain transformations ($y = \sin^{-1}(\sin x)$).
- **Physics:**
  - Optics lens-mirror combinations, dynamic image acceleration $a_i = d^2v/dt^2$, error analysis in screw gauge/Vernier.
  - *TikZ:* Ray tracing through convex/concave lens systems, transverse image motion geometry.
- **Chemistry:**
  - Coordination chemistry Werner valencies, synergic $\pi$-backbonding in carbonyls, ambidentate ligand isomerism.
  - *ChemFig:* $d$-orbital overlap with CO $\pi^*$ antibonding orbital, cis/trans and fac/mer complex isomers.

#### File: `2-paper2-solutions.md`
- **Math:**
  - Differential equations, functional equations, conic sections (parabola tangents, normals).
  - *Desmos:* Parabola focal chord envelope, locus of orthogonal tangents.
- **Physics:**
  - Magnetic forces, Biot-Savart law for coaxial loops, electromagnetic induction and LR transients.
  - *Circuitikz:* LR transient circuit with decay switches, coaxial current ring flux configuration.
- **Chemistry:**
  - Qualitative inorganic analysis (cation salt analysis), Aldol and Cannizzaro mechanisms.
  - *ChemFig:* Step-by-step enolate carbanion attack and aldol condensation mechanism.

---

### 🟠 Phase 3: Test 3 (`solutions/3-paper1-solutions.md` & `3-paper2-solutions.md`)
*Focus: Upgrade pending/abbreviated files to comprehensive format.*

#### File: `3-paper1-solutions.md`
- **Math:**
  - Definite integration with King's property, Leibniz integral rule, matrix eigenvalues & Cayley-Hamilton.
  - *BSc/MSc Insight:* Spectral decomposition, residue integration over semicircular contours.
  - *PGFPlots:* Area bounded between intersecting curves with integration strips.
- **Physics:**
  - Rotational dynamics (pure rolling on inclined surfaces, instantaneous center of rotation), LC oscillations.
  - *TikZ / Circuitikz:* Free body diagram with friction vectors, undamped LC tank circuit with energy conservation plots.
- **Chemistry:**
  - Thermodynamics (free energy $\Delta G^\circ$, chemical potential, phase equilibria), aromatic electrophilic substitution ($S_E\text{Ar}$).
  - *ChemFig:* Arenium ion ($\sigma$-complex) resonance contributors, ortho/para directing group energy profiles.

#### File: `3-paper2-solutions.md`
- **Math:**
  - Probability distributions (Bayes' Theorem, binomial expectation, Markov chains in discrete states).
  - *BSc/MSc Insight:* Transition probability matrices and stationary distributions.
- **Physics:**
  - Thermodynamics (Carnot, Otto, Diesel cycles on $P$-$V$ and $T$-$S$ planes), sound waves, Doppler effect.
  - *TikZ / PGFPlots:* Reversible cyclic processes on $P$-$V$ diagram with work area shading.
- **Chemistry:**
  - Electrochemistry (Nernst equation, concentration cells, Debye-Hückel limit), carbohydrate Fischer/Haworth projections.
  - *ChemFig:* Haworth projection of $\alpha$-D-glucopyranose and $\beta$-D-fructofuranose.

---

### 🔴 Phase 4: Test 4 (`solutions/4-paper1-solutions.md` & `4-paper2-solutions.md`)
*Focus: Full completion of advanced mock papers with high-difficulty multi-concept problems.*

#### File: `4-paper1-solutions.md`
- **Math:**
  - 3D Vector geometry (shortest distance between skew lines, plane intersections), extreme value problems in multivariable calculus.
  - *BSc/MSc Insight:* Lagrange multipliers, exterior product / cross-ratio in affine 3D space.
  - *TikZ:* 3D spatial representation of skew lines and mutual perpendicular vector $\vec{u} \times \vec{v}$.
- **Physics:**
  - Modern physics (Bohr-Sommerfeld quantization, photoelectric work function with stopping potential graphs, radioactive decay chains).
  - *PGFPlots:* Stopping potential $V_0$ vs frequency $\nu$ graph indicating Planck's constant slope and threshold frequency.
- **Chemistry:**
  - Reaction kinetics (consecutive first-order reactions $A \to B \to C$, steady-state approximation), pericyclic Diels-Alder reactions.
  - *ChemFig:* Diels-Alder [4+2] cycloaddition showing endo/exo transition state geometry.

#### File: `4-paper2-solutions.md`
- **Math:**
  - Definite integral inequalities (Cauchy-Schwarz, Chebyshev, Jensen), family of circles and radical axes.
  - *Desmos/PGFPlots:* Radical axis orthogonal circle networks.
- **Physics:**
  - Fluid mechanics (Bernoulli equation, viscous drag, terminal velocity, surface tension excess pressure), alternating currents (LCR resonance, phasor diagrams).
  - *Circuitikz / TikZ:* AC RLC phasor diagram showing $\vec{V}_L, \vec{V}_C, \vec{V}_R$ impedance vectors.
- **Chemistry:**
  - Bio-molecules (amino acid sequencing, peptide bond geometry), polymer stereochemistry (isotactic, syndiotactic, atactic).
  - *ChemFig:* Tripeptide backbone showing planar trans amide bonds.

---

## 🛠 Plugin Checklist for Parallel Agents

Every agent must ensure:
1. **Never use Molren or Ketcher:** Use ```` ```tikz \usepackage{chemfig} ... ``` ```` or ```` ```smiles ... ``` ```` via Chemtrails.
2. **Never use Circuit Sketcher:** Use ```` ```tikz \usepackage{circuitikz} ... ``` ````.
3. **Never use Plot Vectors and Graphs:** Use ```` ```tikz \usepackage{pgfplots} ... ``` ```` or ```` ```desmos-graph ... ``` ````.
4. **Never rely on Numerals:** Use clear step-by-step MathJax evaluation blocks `$$ ... $$`.
5. **Always include full end-of-file theory compilation** covering all three subjects.
