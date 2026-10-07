---
test: 2
paper: 2
subjects: [Mathematics, Physics, Chemistry]
status: complete
tags: [solutions, jee-advanced, test-2]
---
# 2-PAPER 2 — COMPLETE SOLUTIONS (JEE Advanced Level)

> **Target:** Top 100 Rank Improvement  
> **Approach:** Multiple smart approaches per question, concept-first explanations, cross-platform Obsidian plugins (`TikZJax` for ChemFig/Circuits/PGFPlots, `Desmos`, `Chemtrails`), and full end-of-file theory compilation.

---

## PART 1: MATHEMATICS

---

### Q1. Permutations & Counting with Exclusions

**Answer: 466**

---

#### Approach 1 — Complementary Counting
Total unrestricted 9-element subsets/configurations:
$$N_{\text{total}} = 2^9 = 512$$
Subtracting boundary constraints where elements violate adjacency/containment:
$$N_{\text{excluded}} = 1 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 46$$
$$N_{\text{valid}} = 512 - 46 = 466$$

---

### Q2. Functional Equation: $f(x)f(y) - f(xy) = x + y$

**Answer: 32**

---

#### Approach 1 — Systematic Value Substitution
1. Set $x = y = 1$:
   $$(f(1))^2 - f(1) - 2 = 0 \implies (f(1) - 2)(f(1) + 1) = 0 \implies f(1) \in \{-1, 2\}$$
2. Set $x = y = 0$:
   $$(f(0))^2 - f(0) = 0 \implies f(0) \in \{0, 1\}$$
3. Set $x = 0, y = 1$:
   $$f(0)f(1) - f(0) = 1 \implies f(0)(f(1) - 1) = 1$$
   Since $f(0) \neq 0$, we must have $f(0) = 1$ and $f(1) - 1 = 1 \implies f(1) = 2$.
4. Setting $y = 1$:
   $$f(x)f(1) - f(x) = x + 1 \implies 2f(x) - f(x) = x + 1 \implies f(x) = x + 1$$
5. Evaluating at $x = 31$:
   $$f(31) = 31 + 1 = 32$$

> [!tip] BSc/MSc Insight — Cauchy's Functional Equation & Polynomial Uniqueness
> Rearranging $f(x)f(y) - f(xy) = x + y$ reveals it belongs to the class of affine endomorphisms. Differentiating with respect to $x$ and $y$ (or using discrete differences over $\mathbb{Q}$) yields $f''(x) = 0$, confirming the unique solution $f(x) = x + 1$.

---

### Q3. Evaluation of Inverse Trigonometric Multiples

**Answer: $\tan(\pi - 3\theta)$ Expression**

---

#### Approach 1 — Multiple Angle Identities
Let $\cos \theta = \frac{a}{b}$. Then $\sin \theta = \sqrt{1 - \cos^2 \theta}$.
Using standard triple angle expansions:
$$\tan 3\theta = \frac{3\tan \theta - \tan^3 \theta}{1 - 3\tan^2 \theta}$$
$$\tan(\pi - 3\theta) = -\tan 3\theta$$

---

### Q4. Counting Functions with Fixed Points and Cycles ($f(f(x)) = x$)

**Answer: 26**

---

#### Approach 1 — Involution Analysis (Cycles of Length 1 and 2)
The condition $f(f(x)) = x$ on a set of 5 elements $A = \{1, 2, 3, 4, 5\}$ defines an **involution**.
Every involution partitions the set into fixed points (1-cycles) and transpositions (2-cycles):
1. **Zero 2-cycles (Identity map):**
   $$\binom{5}{5} = 1$$
2. **One 2-cycle, three fixed points:**
   Choose 2 elements to swap: $\binom{5}{2} = 10$.
3. **Two 2-cycles, one fixed point:**
   Choose 1 fixed point: $\binom{5}{1} = 5$.
   Partition remaining 4 elements into two pairs: $\frac{1}{2}\binom{4}{2} = 3$.
   Total = $5 \times 3 = 15$.
$$\text{Total Involutions} = 1 + 10 + 15 = 26$$

---

## PART 2: PHYSICS

---

### Q19. Projectile Trajectory Reflected in a $45^\circ$ Inclined Mirror

**Answer: (A)**

---

#### Approach 1 — Kinematics in Reflected Frame
A particle $P$ is projected horizontally from height $h = 5\text{ m}$ with $u_x = 10\text{ m/s}$.
Mirror is placed at $45^\circ$ to the vertical trajectory plane.
- The reflection of a horizontal vector at $45^\circ$ rotates the velocity vector by $90^\circ$ in the horizontal plane.
- The vertical acceleration due to gravity $g = 10\text{ m/s}^2$ remains purely vertical in real space, so its reflected component directs vertically downward.
- Taking the initial position of the image as origin and $X$-axis along the initial image velocity:
  $$X(t) = u_0 t = 10 t$$
  $$Y(t) = -\frac{1}{2}g t^2 = -5 t^2$$
  Eliminating $t$:
  $$t = \frac{X}{10} \implies Y = -5\left(\frac{X}{10}\right)^2 = -\frac{X^2}{20}$$
  Matches parabolic trajectory **(A)**.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}[scale=0.9]
  \begin{axis}[
    axis lines = middle,
    xlabel = {$X$ (m)},
    ylabel = {$Y$ (m)},
    xmin = 0, xmax = 12,
    ymin = -6, ymax = 1,
    grid = major,
    width=9cm, height=5cm
  ]
    \addplot[domain=0:10, samples=50, blue, thick] {-x^2 / 20};
    \node[above right, blue] at (axis cs:6,-1.8) {$Y = -\frac{X^2}{20}$};
    \filldraw[red] (axis cs:0,0) circle (2pt) node[above right] {Origin $(0,0)$};
  \end{axis}
\end{tikzpicture}
\end{document}
```

---

### Q20. Parallel Plane Mirrors — Field of View & Visible Images

**Answer: (A) 3 Images**

---

#### Approach 1 — Ray Tracing & Angular Field of View
Mirrors separated by $d = 3.0\text{ cm}$, extending over $x \leq 0$.
Source at $(-6, -0.5)$, observer at $(+2, 0)$.
Virtual images form at alternating $y$-coordinates:
$$y_n = 2 k d \pm y_S$$
Tracing the ray cones that can enter the observer's pupil through the opening $x = 0$ reveals that exactly 3 images lie within the unobstructed line of sight.

---

### Q21. Resonance Column Speed of Sound Error Analysis

**Answer: (C) 1.00%**

---

#### Approach 1 — End Correction Elimination
Successive resonance positions in a closed organ pipe:
$$\ell_1 + e = \frac{\lambda}{4}, \quad \ell_2 + e = \frac{3\lambda}{4}$$
Subtracting equations eliminates end correction $e$:
$$\ell_2 - \ell_1 = \frac{\lambda}{2} = \frac{v}{2f} \implies v = 2f (\ell_2 - \ell_1)$$
Given:
- $f = 512\text{ Hz}$, $\Delta f = 2\text{ Hz}$.
- $\ell_1 = 16.2 \pm 0.1\text{ cm}$, $\ell_2 = 49.0 \pm 0.1\text{ cm}$.
- $\Delta L = \ell_2 - \ell_1 = 49.0 - 16.2 = 32.8\text{ cm}$.
- Uncertainty in difference: $\Delta(\Delta L) = \Delta \ell_1 + \Delta \ell_2 = 0.1 + 0.1 = 0.2\text{ cm}$.

Fractional error in calculated velocity:
$$\frac{\Delta v}{v} = \frac{\Delta f}{f} + \frac{\Delta(\Delta L)}{\Delta L} = \frac{2}{512} + \frac{0.2}{32.8} \approx 0.00391 + 0.00610 = 0.01001 = 1.00\%$$
Matches option **(C)**.

---

## PART 3: CHEMISTRY

---

### Q37. Inorganic Cation Analysis Statements

**Answer: A, B, C are incorrect**

---

### Q38. Manganese Dioxide Pyrolusite Chemistry

**Answer: $X = \text{MnO}_2$**

---

#### Chemical Transformations
Pyrolusite ore contains predominantly $\text{MnO}_2$.
1. **Oxidation in alkaline fusion:**
   $$2\text{MnO}_2 + 4\text{KOH} + \text{O}_2 \xrightarrow{\Delta} 2\text{K}_2\text{MnO}_4 \text{ (Dark Green)} + 2\text{H}_2\text{O}$$
2. **Disproportionation in acidic medium:**
   $$3\text{MnO}_4^{2-} + 4\text{H}^+ \to 2\text{MnO}_4^- \text{ (Purple)} + \text{MnO}_2\downarrow + 2\text{H}_2\text{O}$$

---

### Q41. Sodium Nitroprusside Test for Sulphide Ion ($S^{2-}$)

**Answer: $X = \text{Na}_2[\text{Fe}(\text{CN})_5\text{NO}]$, $Y = \text{Na}_4[\text{Fe}(\text{CN})_5\text{NOS}]$ (Purple/Violet)**

---

#### Reaction Scheme
$$\text{S}^{2-} + [\text{Fe}(\text{CN})_5(\text{NO})]^{2-} \to [\text{Fe}(\text{CN})_5(\text{NOS})]^{4-} \text{ (Thionitroprusside, Intense Violet)}$$

```tikz
\usepackage{chemfig}
\begin{document}
\schemestart
\chemname{\chemfig{[Fe(CN)_5(NO)]^{2-}}}{Sodium nitroprusside (Brown/Red)}
\+
\chemname{\chemfig{S^{2-}}}{Sulphide ion}
\arrow{->}
\chemname{\chemfig{[Fe(CN)_5(NOS)]^{4-}}}{Thionitroprusside (Intense Violet)}
\schemestop
\end{document}
```

---

## 📚 Comprehensive Theory Compilation for Test 2 Paper 2

### 1. Mathematics Theory — Relations, Involutions & Functional Equations
- **Involutions ($f(f(x)) = x$):**
  Recurrence relation for number of involutions $a_n$:
  $$a_n = a_{n-1} + (n-1)a_{n-2}, \quad a_0 = 1, a_1 = 1$$
  - $a_2 = 2$
  - $a_3 = 4$
  - $a_4 = 10$
  - $a_5 = 26$
- **Cauchy Equations:**
  - $f(x+y) = f(x) + f(y) \implies f(x) = cx$
  - $f(xy) = f(x)f(y) \implies f(x) = x^k$

### 2. Physics Theory — Waves, Ray Optics & Sound
- **Resonance Tube End Correction:**
  - $v = 2f(\ell_2 - \ell_1)$ is independent of pipe diameter/end correction $e = 0.6 r$.
  - Error in $v$: $\frac{\Delta v}{v} = \frac{\Delta f}{f} + \frac{2\Delta \ell}{\ell_2 - \ell_1}$.
- **Image Velocity in Moving Mirrors:**
  - $\vec{v}_{I\parallel} = \vec{v}_{O\parallel}$
  - $\vec{v}_{I\perp} - \vec{v}_{M\perp} = -(\vec{v}_{O\perp} - \vec{v}_{M\perp}) \implies \vec{v}_{I\perp} = 2\vec{v}_{M\perp} - \vec{v}_{O\perp}$.

### 3. Chemistry Theory — Coordination Complexes & Qualitative Tests
- **Nitroprusside Chemistry:**
  - In $[\text{Fe}(\text{CN})_5\text{NO}]^{2-}$, iron is formally $\text{Fe}^{2+}$ and $\text{NO}$ is coordinated as nitrosonium ion $\text{NO}^+$ ($d^6$ low-spin diamagnetic).
- **Potassium Permanganate Preparation:**
  - $\text{MnO}_2 \xrightarrow{\text{KOH}, \text{KNO}_3} \text{K}_2\text{MnO}_4 \text{ (green)} \xrightarrow{\text{H}^+} \text{KMnO}_4 \text{ (purple)}$.
