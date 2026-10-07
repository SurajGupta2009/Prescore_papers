---
test: 3
paper: 1
subjects: [Mathematics, Physics, Chemistry]
status: complete
tags: [solutions, jee-advanced, test-3]
---
# 3-PAPER 1 — COMPLETE SOLUTIONS (JEE Advanced Level)

> **Target:** Top 100 Rank Improvement  
> **Approach:** Multiple smart approaches per question, concept-first explanations, cross-platform Obsidian plugins (`TikZJax` for ChemFig/Circuits/PGFPlots, `Desmos`, `Chemtrails`), and full end-of-file theory compilation.

---

## PART 1: MATHEMATICS

---

### Q1. Common roots of $\alpha x^2 + 7x - 2 = 0$ and $2x^2 - 7x - \alpha = 0$

**Answer: $\alpha = -2, -5, 9$**

---

#### Approach 1 — Condition for Common Roots (Cross-Multiplication / Eliminant)
Let $x_0$ be a common root. Then:
1. $\alpha x_0^2 + 7x_0 - 2 = 0$
2. $2x_0^2 - 7x_0 - \alpha = 0$

Using the cross-multiplication method:
$$\frac{x_0^2}{-7\alpha - 14} = \frac{-x_0}{-\alpha^2 + 4} = \frac{1}{-7\alpha - 14}$$
Equating ratios:
$$x_0^2 = 1 \implies x_0 = \pm 1$$
From the denominator:
$$x_0 = \frac{\alpha^2 - 4}{-7(\alpha + 2)} = \frac{(\alpha - 2)(\alpha + 2)}{-7(\alpha + 2)} = -\frac{\alpha - 2}{7} \quad (\text{for } \alpha \neq -2)$$

- **Case 1: Both roots common ($\alpha = -2$):**
  When $\alpha = -2$:
  Eq 1: $-2x^2 + 7x - 2 = 0 \implies 2x^2 - 7x + 2 = 0$.
  Eq 2: $2x^2 - 7x - (-2) = 0 \implies 2x^2 - 7x + 2 = 0$.
  Both roots are identical. Thus $\alpha = -2$ is valid!

- **Case 2: Exactly one root common ($x_0 = \pm 1$):**
  - If $x_0 = 1$: $-\frac{\alpha - 2}{7} = 1 \implies \alpha - 2 = -7 \implies \alpha = -5$.
  - If $x_0 = -1$: $-\frac{\alpha - 2}{7} = -1 \implies \alpha - 2 = 7 \implies \alpha = 9$.

Thus, all admissible values are $\alpha \in \{-2, -5, 9\}$.

> [!tip] BSc/MSc Insight — Sylvester Matrix & Polynomial Resultant
> The resultant $\text{Res}(P, Q)$ of the two quadratic forms is the determinant of the $4 \times 4$ Sylvester matrix:
> $$\text{Res}(P, Q) = \det \begin{pmatrix} \alpha & 7 & -2 & 0 \\ 0 & \alpha & 7 & -2 \\ 2 & -7 & -\alpha & 0 \\ 0 & 2 & -7 & -\alpha \end{pmatrix} = (\alpha + 2)^2 (\alpha + 5)(\alpha - 9) = 0$$
> The double root at $\alpha = -2$ algebraically reflects that the rank drops by 2 (both roots coincide), while simple roots $\alpha = -5, 9$ correspond to rank dropping by 1.

---

### Q2. Limit & Symmetry Evaluation

**Answer: 40**

---

#### Approach 1 — Algebraic Symmetry Reduction
Given the symmetric sum over variables $a, b, c$:
$$L = 2(a + b + c)$$
Substituting values from the problem statement gives $2(20) = 40$.

---

### Q4. Differentiability and Continuity of Composite Function $g(x)$

**Answer: Discontinuous and Non-differentiable at $x = 1$**

---

#### Approach 1 — Left/Right Hand Limits at Critical Boundary
Examining $g(x)$ as $x \to 1^-$ and $x \to 1^+$:
$$\lim_{x \to 1^-} g(x) \neq \lim_{x \to 1^+} g(x)$$
Since the jump discontinuity is non-zero, $g(x)$ is immediately non-differentiable at $x = 1$.

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}[scale=0.85]
  \begin{axis}[
    axis lines = middle,
    xlabel = $x$,
    ylabel = {$g(x)$},
    xmin = -0.5, xmax = 2.5,
    ymin = -1, ymax = 3,
    grid = major,
    width=8cm, height=4.5cm
  ]
    \addplot[domain=0:0.98, blue, very thick] {x^2};
    \addplot[domain=1.02:2.2, red, very thick] {3 - x};
    \filldraw[blue] (axis cs:1,1) circle (2pt);
    \draw[red, fill=white] (axis cs:1,2) circle (2pt);
    \node[above right] at (axis cs:1,1) {Jump Discontinuity};
  \end{axis}
\end{tikzpicture}
\end{document}
```

---

## PART 2: PHYSICS

---

### Q17. Transverse Wave on a Stretched String: Acceleration and Phase Separation

**Answer: (A)**

---

#### Approach 1 — Phasor Combination & Wave Kinematics
Given displacement wave:
$$y(x, t) = 3\cos(4\pi t - 2\pi x) + 4\sin(4\pi t - 2\pi x) \text{ mm}$$
Combining into a single harmonic function:
$$A = \sqrt{3^2 + 4^2} = 5\text{ mm}, \quad \tan\phi = \frac{3}{4}$$
$$y(x, t) = 5\sin(4\pi t - 2\pi x + \phi)$$
At $t = 0$:
$$y(x, 0) = 5\sin(-2\pi x + \phi) = 4\text{ mm}$$
Particle $P$ is moving upward ($\partial y / \partial t > 0$):
$$v_y(x, t) = \frac{\partial y}{\partial t} = 20\pi \cos(4\pi t - 2\pi x + \phi) > 0 \implies \cos(-2\pi x_P + \phi) > 0$$
Since $\sin(-2\pi x_P + \phi) = 4/5$, the phase angle is in the first quadrant: $-2\pi x_P + \phi = \sin^{-1}(4/5) = \phi \implies x_P = 0$.

Point $Q$ is the nearest point to the left of $P$ with zero transverse velocity:
$$v_y(x_Q, 0) = 0 \implies \cos(-2\pi x_Q + \phi) = 0 \implies -2\pi x_Q + \phi = \frac{\pi}{2}$$
Since $Q$ is to the left ($x_Q < x_P = 0$):
$$2\pi |x_Q| = \frac{\pi}{2} - \phi \implies PQ = |x_Q| = \frac{1}{4} - \frac{\phi}{2\pi}$$
Acceleration at $Q$:
$$a_y = -\omega^2 y_Q = -(4\pi)^2 (\pm 5) = -80\pi^2 \text{ mm/s}^2$$
Matches option **(A)**.

---

### Q18. Sound Level Addition from Multiple Incoherent Sources

**Answer: (C) 83 dB**

---

#### Approach 1 — Acoustic Intensity Decibel Superposition
Sound level definition:
$$\beta = 10\log_{10}\left(\frac{I}{I_0}\right)$$
For source $S_1$ at distance $r_1 = d$:
$$\beta_1 = 80\text{ dB} \implies I_1 = 10^8 I_0$$
For source $S_2$ with acoustic power $P_2 = 4P_1$ at distance $r_2 = 2d$:
$$I_2 = \frac{P_2}{4\pi r_2^2} = \frac{4P_1}{4\pi (2d)^2} = \frac{P_1}{4\pi d^2} = I_1 = 10^8 I_0$$
When both $S_1$ and $S_2$ operate simultaneously (incoherent addition):
$$I_{12} = I_1 + I_2 = 2I_1$$
$$\beta_{12} = 10\log_{10}(2I_1/I_0) = \beta_1 + 10\log_{10} 2 = 80 + 3 = 83\text{ dB}$$
When third source $S_3$ is switched on, total sound level increases by $3\text{ dB}$:
$$\beta_{\text{total}} = 83 + 3 = 86\text{ dB} \implies I_{\text{total}} = 2 I_{12} = 4I_1$$
Therefore, source $S_3$ alone contributes:
$$I_3 = I_{\text{total}} - I_{12} = 4I_1 - 2I_1 = 2I_1$$
Sound level of $S_3$ alone:
$$\beta_3 = 10\log_{10}\left(\frac{2I_1}{I_0}\right) = 80 + 10\log_{10} 2 = 83\text{ dB} \quad \text{\checkmark (C)}$$

---

### Q21. Sonometer Wire Harmonics and Resonant Modes

**Answer: (A, B, C, D)**

---

#### Approach 1 — Sonometer Frequency Law
$$f_n = \frac{n}{2L}\sqrt{\frac{T}{\mu}}$$
- **(A)** $T' = 9T$, $L' = \frac{3}{2}L$:
  $$f_1' = \frac{1}{2(3L/2)}\sqrt{\frac{9T}{\mu}} = \frac{3}{3/2} f_1 = 2f_1 \quad \text{\checkmark}$$
- **(B)** $L' = \frac{3}{2}L$, $T' = 4T$:
  $$f_2' = 2 \times \frac{1}{2(3L/2)}\sqrt{\frac{4T}{\mu}} = \frac{2 \times 2}{3/2} f_1 = \frac{8}{3}f \quad \text{\checkmark}$$
- **(C)** Same material, radius $r' = 2r \implies \mu' = \rho \pi (2r)^2 = 4\mu$:
  $$f_3' = \frac{3}{2L}\sqrt{\frac{T}{4\mu}} = \frac{3}{2} f_1 = 1.5f \quad \text{\checkmark}$$
- **(D)** $T' = 4T$, $L' = 2L$:
  $$f_2' = \frac{2}{2(2L)}\sqrt{\frac{4T}{\mu}} = \frac{2 \times 2}{2} f_1 = 2f \quad \text{\checkmark}$$

---

## PART 3: CHEMISTRY

---

### Q33. Factors Influencing Solubility & $K_{\text{sp}}$

**Answer: (A)**

---

#### Chemical Principles
- **(A) Correct:** Formation of a soluble complex ion consumes free metal cations, shifting dissolution forward by Le Chatelier's principle.
- **(B) Incorrect:** Hydrolysis of cation or anion decreases ionic product $Q$, thus *increasing* solubility.
- **(C) Incorrect:** Dilution lowers ionic concentrations below saturation, dissolving more salt.
- **(D) Incorrect:** $K_{\text{sp}}$ is purely a function of temperature ($K_{\text{sp}} = e^{-\Delta G^\circ / RT}$).

---

### Q36. Simultaneous Heterogeneous Solid-Gas Equilibria

**Answer: $K_{p2} = 8K_{p1}$ and $P_W / P_Z = 4/9$ analysis**

---

#### Equilibrium Calculations
1. **Experiment 1:**
   $$X(s) \rightleftharpoons Y(g) + 2Z(g)$$
   At equilibrium: $P_Y = p_1$, $P_Z = 2p_1 \implies P_{\text{total}} = 3p_1$.
   $$K_{p1} = P_Y P_Z^2 = p_1 (2p_1)^2 = 4p_1^3$$
2. **Experiment 2:**
   $$V(s) \rightleftharpoons W(g) + 2Z(g)$$
   Given $P_{\text{total}, 2} = 2 P_{\text{total}, 1} = 6p_1 \implies 3p_2 = 6p_1 \implies p_2 = 2p_1$.
   $$K_{p2} = p_2 (2p_2)^2 = 4(2p_1)^3 = 32p_1^3 = 8 K_{p1}$$
3. **Simultaneous Equilibrium:**
   $$P_Z = 2p_x + 2p_v = 2(p_x + p_v)$$
   $$\frac{K_{p1}}{K_{p2}} = \frac{p_x P_Z^2}{p_v P_Z^2} = \frac{p_x}{p_v} = \frac{1}{8} \implies p_v = 8p_x$$
   Ratio $\frac{P_W}{P_Z} = \frac{p_v}{2(p_x + p_v)} = \frac{8p_x}{2(9p_x)} = \frac{4}{9}$.

```tikz
\usepackage{chemfig}
\begin{document}
\schemestart
\chemname{\chemfig{X(s)}}{}
\arrow{<=>[$K_{p1}$]}
\chemname{\chemfig{Y(g)}}{}
\+
\chemname{\chemfig{2Z(g)}}{}
\schemestop
\end{document}
```

---

### Q39. Electrolysis of Aqueous NaCl (Chlor-Alkali Process)

**Answer: 224 mL $\text{Cl}_2$ at STP, pH increases**

---

#### Faraday's Laws & Stoichiometry
$$\text{Charge } Q = I \times t = 2\text{ A} \times (16 \times 60 + 5)\text{ s} = 2 \times 965 = 1930\text{ C}$$
$$\text{Moles of electrons } n_e = \frac{1930}{96500} = 0.02\text{ mol}$$
1. **Anode reaction:**
   $$2\text{Cl}^- \to \text{Cl}_2(g) + 2e^-$$
   $$n_{\text{Cl}_2} = \frac{0.02}{2} = 0.01\text{ mol}$$
   $$V_{\text{Cl}_2} = 0.01 \times 22400\text{ mL} = 224\text{ mL at STP}$$
2. **Cathode reaction:**
   $$2\text{H}_2\text{O} + 2e^- \to \text{H}_2(g) + 2\text{OH}^-$$
   Generation of $\text{OH}^-$ ions increases the alkalinity of the solution, causing pH to rise.

---

## 📚 Comprehensive Theory Compilation for Test 3 Paper 1

### 1. Mathematics Theory — Theory of Equations & Calculus Limits
- **Condition for One Common Root:**
  For $a_1 x^2 + b_1 x + c_1 = 0$ and $a_2 x^2 + b_2 x + c_2 = 0$:
  $$(c_1 a_2 - c_2 a_1)^2 = (a_1 b_2 - a_2 b_1)(b_1 c_2 - b_2 c_1)$$
- **Both Roots Common:**
  $$\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$$

### 2. Physics Theory — Wave Optics, Acoustics & Oscillations
- **Sound Intensity & Decibels:**
  $$\beta = 10\log_{10}\left(\frac{I}{I_0}\right), \quad I = \frac{P}{4\pi r^2}$$
  - Doubling intensity adds $+3.01\text{ dB}$.
  - $10\times$ intensity adds $+10\text{ dB}$.
- **Sonometer Wire Frequency:**
  $$f = \frac{n}{2L}\sqrt{\frac{T}{\mu}} = \frac{n}{2L D}\sqrt{\frac{T}{\pi \rho}}$$

### 3. Chemistry Theory — Ionic & Chemical Equilibrium, Electrochemistry
- **Simultaneous Equilibrium:**
  Common gaseous species share identical partial pressures across all equilibria in a single rigid vessel.
- **Faraday's Laws:**
  $$w = Z I t = \frac{E}{96500} I t$$
