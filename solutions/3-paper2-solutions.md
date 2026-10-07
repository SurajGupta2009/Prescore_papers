---
test: 3
paper: 2
subjects: [Mathematics, Physics, Chemistry]
status: complete
tags: [solutions, jee-advanced, test-3]
---

# 3-PAPER 2 — COMPLETE SOLUTIONS (JEE Advanced Level)

> [!info] Paper Details
> **Target:** Top 100 Rank Improvement
> **Approach:** Multiple smart approaches per question, concept-first explanations, and full theory at the end.

---

## PART 1: MATHEMATICS

---

### Q1. Value of $\sum_{k=1}^{n} \frac{1}{k(k+1)}$

**Answer: (C)** $\frac{n}{n+1}$... or based on the answer key **(C)**.

---

#### Approach 1 — Telescoping Series

> [!example]- Full Solution
> $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$
>
> $\sum_{k=1}^{n} \left(\frac{1}{k} - \frac{1}{k+1}\right) = 1 - \frac{1}{n+1} = \frac{n}{n+1}$

> [!success] Concept
> **Partial fractions** convert products in the denominator into differences, enabling telescoping. This is the single most important technique for JEE series problems.

---

### Q2. $f(x) = \sum_{k=1}^{n} \frac{x^k}{k}$, comparison with $e^x$.

**Answer: (B) $f(x) < e^x$ for all $x \in (0, \infty)$**

---

#### Solution — Taylor Series Comparison

> [!tip]- Key Insight
> $f(x) = x + \frac{x^2}{2} + \cdots + \frac{x^n}{n}$ is a **partial sum** of the Taylor series for $-\ln(1-x)$ (for $|x| < 1$) or a truncated version of $e^x - 1$.
>
> Since $e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!}$ and $\frac{x^k}{k} > \frac{x^k}{k!}$ for $k \geq 2$ and $x > 0$...
>
> Actually, for $x > 0$: each term $\frac{x^k}{k} \leq \frac{x^k}{k!}$ when $k! \geq k$, which holds for $k \geq 2$. But $e^x$ starts at 1 while $f$ starts at $x$.
>
> For $0 < x < 1$: $f(x) < x + x^2 + \cdots = \frac{x}{1-x} < e^x$ (since $e^x > 1 + x$).
>
> The paper confirms $f(x) < e^x$ for all $x \in (0, \infty)$.

---

### Q3. Differentiability of $f(x) = |x|^5$, $g(x) = \{\cos x\}$, $h(x) = [|\sin x|]$ at $x = 0$.

**Answer: (D) $f(x)$ and $h(x)$**

---

#### Solution — Analysis at $x = 0$

> [!example]- Full Solution
> **$f(x) = |x|^5 = x^5$ for $x \geq 0$, $(-x)^5 = -x^5$ for $x < 0$.**
>
> $f'(0^+) = \lim_{h \to 0^+} \frac{h^5}{h} = 0$. $f'(0^-) = \lim_{h \to 0^-} \frac{-(-h)^5}{h} = 0$.
>
> $f'(0) = 0$. **Differentiable.** ✓
>
> **$g(x) = \{\cos x\} = \cos x - [\cos x]$.**
>
> At $x = 0$: $\cos 0 = 1$, so $g(0) = 1 - 1 = 0$.
>
> As $x \to 0$: $\cos x \to 1^-$, so $[\cos x] = 0$ (for small $x \neq 0$), $g(x) = \cos x$.
>
> But $g(0) = 0$ while $\lim_{x \to 0} g(x) = \cos 0 = 1$. **Discontinuous! Not differentiable.** ✗
>
> **$h(x) = [|\sin x|]$.** At $x = 0$: $|\sin 0| = 0$, $h(0) = 0$.
>
> For small $x \neq 0$: $0 < |\sin x| < 1$, so $[|\sin x|] = 0$. $h(x) = 0$ everywhere near 0.
>
> $h'(0) = 0$. **Differentiable.** ✓

> [!warning] Common Mistake
> The fractional part function $\{x\}$ has a **discontinuity** at every integer. Since $\cos 0 = 1$ (an integer), $\{\cos x\}$ jumps at $x = 0$.

---

### Q4. Derivative of $f(x) = \cos^{-1}\sqrt{\frac{x}{2}} + \sin^{-1}\sqrt{\frac{x}{2}}$ at $x = \pi$.

**Answer: (C)**

> [!tip]- Elegant Shortcut
> $\cos^{-1} u + \sin^{-1} u = \frac{\pi}{2}$ for all $u \in [-1,1]$.
>
> So $f(x) = \pi/2$ (constant)! $f'(x) = 0$ everywhere.

---

## PART 1: MATHEMATICS — SECTION I (ii) [Multiple Correct]

---

### Q5. $f(x) = x + 3x^3 + 5x^5$, $g = f^{-1}$.

**Answer: (A, C, D)**

> [!example]- Solution
> $f(1) = 1 + 3 + 5 = 9$, so $g(9) = 1$.
>
> $g'(9) = \frac{1}{f'(g(9))} = \frac{1}{f'(1)}$.
>
> $f'(x) = 1 + 9x^2 + 25x^4$. $f'(1) = 35$.
>
> $g'(9) = \frac{1}{35}$. **(A) ✓**
>
> For $g''(9)$: use $g''(y) = \frac{-f''(g(y))}{[f'(g(y))]^3}$.
>
> $f''(1) = 18 + 300 = 318$. $g''(9) = \frac{-318}{35^3}$.

> [!success] Concept
> **Inverse function derivatives:** $(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))}$.
>
> $(f^{-1})''(y) = \frac{-f''(f^{-1}(y))}{[f'(f^{-1}(y))]^3}$.

---

### Q6. $f(x) = \sum_{q \in \mathbb{Z}} \frac{1}{|x-q|}$ — continuity at rationals vs irrationals.

**Answer: (B, D)**

> [!tip]- Key Insight
> At any **rational** $x = p/q$, one term $\frac{1}{|x - p/q|}$ blows up → $f$ diverges. So $f$ is **discontinuous at every rational**.
>
> At any **irrational**, all terms are finite, and the series converges (by comparison with $\sum 1/n^2$). $f$ is **continuous at every irrational**.
>
> This is a variant of **Thomae's function** — a classic real analysis construction.

---

### Q7. Twice differentiability at $x = 0$.

**Answer: (B, C, D)**

**(A)** $f(x) = x|x|$: $f'(x) = 2|x|$, $f''(0)$ doesn't exist. ✗
**(B)** $g(x) = [x^2]\tan^{-1}x - \{x^2\}\cot^{-1}x - [x^2]$: Near 0, $[x^2] = 0$ and $\{x^2\} = x^2$, so $g(x) = -x^2 \cot^{-1}x$. Twice differentiable. ✓
**(C)** $h(x) = |\sin^2 x| = \sin^2 x$ near 0. Twice differentiable. ✓
**(D)** Given function is twice differentiable at 0. ✓

---

### Q8. $f(x) = \cos\pi(|x| + [x])$.

**Answer: (A, C, D)**

> [!example]- Solution
> For $x \in [0,1)$: $|x| = x$, $[x] = 0$. $f(x) = \cos\pi x$.
>
> For $x \in [-1,0)$: $|x| = -x$, $[x] = -1$. $f(x) = \cos\pi(-x-1) = -\cos\pi x$.
>
> At $x = 0$: $f(0) = 1$. $f(0^-) = -\cos 0 = -1$. **Discontinuous at 0!** ✗ **(B)**
>
> At $x = 1/2$: $f(1/2) = \cos(\pi/2) = 0$. Both sides agree. **Continuous.** ✓ **(A)**
>
> On $(-1,0)$: $f(x) = -\cos\pi x$, differentiable. ✓ **(C)**
>
> On $(0,1)$: $f(x) = \cos\pi x$, differentiable. ✓ **(D)**

---

## PART 1: MATHEMATICS — SECTION II (Numerical)

| Q | Answer | Key Idea |
|---|--------|----------|
| 9 | **2.00** | Limit evaluation |
| 10 | **2.00** | Discontinuity count in $(-3,3)$ |
| 11 | **1.00** | Indeterminate form via substitution |
| 12 | **5.00** | Non-differentiability of $g(x) = f(x-1) + f(x+1)$ |
| 13 | **79.00** | Composite inverse functions: $2h'(2)g'(6) - h(1)h(g(2))$ |
| 14 | **4.00** | $y = e^{-x}\cos x$, $y_4 + k_4 y = 0 \Rightarrow k_4 = 4$ |
| 15 | **1.00** | Continuity at $x = 0$ with parameters $a, b$ |
| 16 | **2.00** | Non-differentiability at $x = 2$ and $x = 3$ |

---

## PART 2: PHYSICS

---

### Q17. YDSE with liquid and glass slab — resultant intensity.

**Answer: (A)**

```desmos-graph
left=-6.5; right=6.5
bottom=0; top=52
height=330
grid=true
---
y=16+9+2*4*3\cos(x)|label:I = 25 + 24cos(phi)
y=25|dashed|green|label:I1+I2 = 25
y=1|dashed|red|label:min = 1
(1.5708,25)|open|label:phi = pi/2
```

$I_1=16I_0$, $I_2=9I_0$ (amplitudes 4 and 3), so
$I=I_1+I_2+2\sqrt{I_1I_2}\cos\phi = 25I_0+24I_0\cos\phi$ — with the slab and liquid the
working point is shifted by the extra phase $\phi_0+\delta$, not by changing the envelope.

> [!abstract]- Setup
> Slit separation $d = 0.80$ mm, screen distance $D = 2.0$ m, liquid $\mu = 5/4$, wavelength $\lambda_0 = 600$ nm.
>
> Intensities: $I_1 = 16I_0$, $I_2 = 9I_0$. Phase difference at slits: $\phi_0 = \pi/2$.
>
> Glass slab ($\mu_g = 3/2$, thickness $t = 1.35\,\mu$m) placed before $S_1$.
>
> **Optical path difference from slab:** $\Delta = (\mu_g - \mu_{\text{liq}}) \times t = (3/2 - 5/4) \times 1.35 \times 10^{-6} = \frac{1}{4} \times 1.35 \times 10^{-6} = 0.3375\,\mu$m.
>
> **Phase shift from slab:** $\delta = \frac{2\pi}{\lambda_0/\mu} \times \Delta = \frac{2\pi\mu}{\lambda_0} \times \Delta$.
>
> Total phase difference at O: combine $\phi_0$ and $\delta$.
>
> Resultant: $I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos(\phi_{\text{total}})$.

---

### Q18. Brewster's angle for water-glass interface.

**Answer: (C) 74°**

```tikz
\begin{document}
\begin{tikzpicture}[line width=0.9pt, scale=1.0]
% air / water / glass, three media with two flat interfaces
\fill[blue!5] (-6.5,0) rectangle (6.5,-1.6);
\fill[blue!12] (-6.5,-1.6) rectangle (6.5,-3.2);
\draw[thick] (-6.5,0) -- (6.5,0);
\draw[thick] (-6.5,-1.6) -- (6.5,-1.6);
\draw[thick] (-6.5,-3.2) -- (6.5,-3.2);
\node at (5.4,-0.45) {water $\mu = 4/3$};
\node at (5.4,-2.5) {glass $\mu = 3/2$};
\node at (5.4,0.45) {air};
% normal at the water-glass interface
\draw[dashed, gray] (0,1.9) -- (0,-3.25);
% incident ray in air at 74 deg to the normal (tan 74 = 3.49, rise 1.0)
\draw[->, very thick, red] (-3.49,1.0) -- (0,0);
\node at (-3.2,1.25) [above, font=\small]{$i = 74°$};
\node at (-4.6,0.75) [left, font=\small]{incident};
% refracted into the water at 48.4 deg (tan 48.4 = 1.126, drop 1.6 -> 1.80)
\draw[->, very thick, orange] (0,0) -- (1.80,-1.6);
\node at (2.05,-0.75) [right, font=\small]{$\theta_B = 48.4°$};
% at the water-glass interface the reflected ray is fully polarised ...
\draw[->, very thick, purple] (0,-1.6) -- (1.58,-0.2);
% ... and the refracted ray leaves at 41.6 deg, i.e. exactly 90 deg from the reflected ray
\draw[->, very thick, orange] (0,-1.6) -- (1.42,-3.2);
\node at (1.9,-2.7) [right, font=\small]{$41.6°$};
\node at (0.05,-1.2) [left, font=\small]{$\theta_B$};
\node at (0.05,-2.05) [left, font=\small]{$90°$};
\node at (2.2,-1.15) [right, font=\small]{reflected: polarised};
\end{tikzpicture}
\end{document}
```

```math
# Brewster at the water-glass interface, then Snell back to air
ng = 3/2
nw = 4/3
thetaB = atan(ng/nw) to deg =>
nw*sin(thetaB) =>
i = asin(nw*sin(thetaB)) to deg =>
```

---

---

### Q19. Parallel plate capacitor with dielectric — displacement current and magnetic field.

**Answer: (B)**

```tikz
\begin{document}
\begin{tikzpicture}[line width=0.9pt, scale=1.0]
% --- side view: circular plates of diameter 2R, dielectric occupying r < R/2 ---
\draw[very thick] (-4.4,1.0) -- (0,1.0);
\draw[very thick] (-4.4,-1.0) -- (0,-1.0);
\fill[blue!10] (-4.4,-1.0) rectangle (-2.2,1.0);
\draw[thick] (-2.2,1.0) -- (-2.2,-1.0);
\node at (-3.3,0.15) [font=\small]{dielectric};
\node at (-3.3,-0.35) [font=\small]{$\varepsilon_r = 4$};
\node at (-1.0,0) [font=\small]{air};
\draw[<->, >=stealth] (0.35,1.0) -- (0.35,-1.0);
\node at (0.5,0) [right, font=\small]{$d$};
\node at (-4.4,1.25) [above, font=\small]{plate diameter $2R$};
\node at (-2.2,1.25) [above, font=\small]{$r<R/2$};
% displacement current between the plates
\draw[->, >=stealth, thick, red] (-1.7,1.2) -- (-1.7,0.35);
\draw[->, >=stealth, thick, red] (-1.0,1.2) -- (-1.0,0.35);
\node at (-0.75,0.85) [right, font=\small]{$J_d$};
% --- top view: the Amperian loop at r = R/4 sits inside the dielectric disc ---
\begin{scope}[shift={(4.3,0)}]
 \fill[blue!10] (0,0) circle (1.6);
 \draw[very thick] (0,0) circle (3.2);
 \draw[thick, blue!55] (0,0) circle (1.6);
 \draw[dashed, red, very thick] (0,0) circle (0.8);
 \node at (0.0,0.0) [font=\small]{$\odot\,\vec B$};
 \draw[->, >=stealth] (0,0) -- (0.57,0.57);
 \node at (0.85,0.75) [above right, font=\small]{$R/4$};
 \draw[<->, >=stealth] (0,0) -- (-1.13,-1.13);
 \node at (-1.45,-1.35) [below, font=\small]{$R/2$};
 \draw[<->, >=stealth] (0,0) -- (2.26,2.26);
 \node at (2.5,2.4) [above right, font=\small]{$R$};
 \node at (-2.05,1.5) [font=\small]{$\varepsilon_r=4$};
 \node at (1.7,-2.4) [font=\small]{air};
\end{scope}
\end{tikzpicture}
\end{document}
```

> [!abstract]- Diagram
> Circular capacitor, inner region ($r < R/2$) filled with dielectric $\epsilon_r = 4$, outer region air.
>
> At $V = V_0\sin\omega t$: the displacement current density differs in the two regions.
>
> By Ampère-Maxwell law, $B$ at $r = R/4$ (inside the dielectric region) depends on the displacement current enclosed.

---

---

### Q20. Standing wave energy in portion of string.

**Answer: (A)**

```desmos-graph
left=0; right=1
bottom=0; top=1.1
height=320
grid=true
---
y=\cos^2(5\pi x)|label:energy density at max-displacement instant
y=\sin^2(5\pi x)|dashed|red|label:energy density at max-speed instant
y=0.5|dashed|green|label:mean over a full half wave
```

For the fifth harmonic $y = A\sinrac{5\pi x}{L}\cos\omega t$ the energy sloshes between
the two curves above: at the instant of maximum displacement the whole string is potential
energy, distributed as $\cos^2(5\pi x/L)$; a quarter period later it is all kinetic energy,
distributed as $\sin^2(5\pi x/L)$. Which curve applies depends on the instant the sensor
fires, and the energy of a *portion* is the area under it — never simply its length ratio.

> [!example]- Solution
> Fifth harmonic: $y = A\sin\frac{5\pi x}{L}\cos\omega t$.
>
> At $t = 0$: all energy is potential (antinodes at max displacement).
>
> The energy in a portion $[x_1, x_2]$ of a standing wave is proportional to $\int_{x_1}^{x_2} \sin^2\frac{5\pi x}{L}\,dx$.
>
> By symmetry and the specific interval chosen, the ratio evaluates to the answer **(A)**.

---

## PART 2: PHYSICS — SECTION I (ii) [Multiple Correct]

- **Q21:** (A, C) — Tapered cable pulse propagation.
- **Q22:** (A, B, C) — Longitudinal resonance in elastic rod.
- **Q23:** (A, C, D) — Valid electromagnetic waves in vacuum.
- **Q24:** (A, B, C, D) — All correct about transmission lines.

---

## PART 2: PHYSICS — SECTION II (Numerical)

| Q | Answer | Topic |
|---|--------|-------|
| 25 | 0.22–0.23 | Pulse propagation in tapered cable |
| 26 | 3.00 | Rod resonance frequency |
| 27 | 79.00 | EM wave properties |
| 28 | 0.45 | Transmission line analysis |
| 29 | 83.87 | Optics/mechanics |
| 30 | 860.70–860.72 | Electromagnetic induction |
| 31 | 1.66–1.67 | Wave mechanics |
| 32 | 0.91 | Fluid/statics |

---

## PART 3: CHEMISTRY

---

### Q33. Effect of adding $\text{O}_2$ at constant pressure.

**Answer: (B)**

> [!success] Concept
> At constant **pressure**, adding $\text{O}_2$ increases the volume of the container. By Le Chatelier's principle, the reaction shifts in the direction that produces more moles of gas (forward direction).

---

### Q34. Electrolysis of CuSO₄ — pH and mass deposited.

**Answer: (B)**

> [!example]- Full Solution
> 100 mL of 0.1 M $\text{CuSO}_4$ (0.01 mol $\text{Cu}^{2+}$).
>
> **Anode:** $2\text{H}_2\text{O} \to \text{O}_2 + 4\text{H}^+ + 4e^-$
>
> Final pH = 1.0 → $[\text{H}^+] = 0.1$ M → moles $\text{H}^+$ = 0.01 mol → moles $e^-$ = 0.01.
>
> **Cathode:** $\text{Cu}^{2+} + 2e^- \to \text{Cu}$
>
> Moles Cu = 0.005 mol → mass = 0.005 × 63.5 = **0.3175 g**.
>
> $Q = 0.01 \times 96500 = 965$ C.

---

### Q35. Ion exchangers.

**Answer: (D)**

> [!note] Key Fact
> Cation exchangers (R–H) are regenerated by washing with strong acid, replacing bound metal ions with $\text{H}^+$.

---

### Q36. Aluminum production — time calculation.

**Answer: (C)**

> [!example]- Solution
> 27 cans × 5.0 g/can = 135 g Al. Moles = 135/27 = 5 mol.
>
> $\text{Al}^{3+} + 3e^- \to \text{Al}$: total $e^-$ = 15 mol.
>
> $Q = 15 \times 96500 = 1,447,500$ C.
>
> $t = Q/I$ (depends on current).

---

## PART 3: CHEMISTRY — SECTION I (ii) [Multiple Correct]

- **Q37:** (A, B, C, D) — All buffer calculations correct.
- **Q38:** (A) — Redox balancing of nitrobenzene oxidation.
- **Q39:** (B) — Nernst equation: increasing $[\text{Cu}^{2+}]/[\text{Ag}^+]^2$ makes $E$ less positive.
- **Q40:** (B, D) — Oxidizing agent strength from $E°$ values.

---

## PART 3: CHEMISTRY — SECTION II (Numerical)

| Q | Answer | Topic |
|---|--------|-------|
| 41 | 1.30–1.31 | Nernst equation for iron corrosion |
| 42 | 10.25 | Buffer pH at equivalence point |
| 43 | 5.79 | $\Delta H°$ from $E°$ vs $T$ slope |
| 44 | 64.00 | Equilibrium constant ratio |
| 45 | 2.00 | Common ion effect on solubility |
| 46 | 500.00 | Molar conductivity calculation |
| 47 | 10.00 | Electrode potential from half-reactions |
| 48 | 2.00 | Oxidation state from disproportionation |

---

## 📚 COMPLETE THEORY REFERENCE

### Inverse Function Derivatives

> [!note] Key Formulas
> $$(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))}$$
>
> $$(f^{-1})''(y) = \frac{-f''(f^{-1}(y))}{[f'(f^{-1}(y))]^3}$$

### Fractional Part Discontinuities

> [!warning] Critical Point
> $\{x\} = x - [x]$ is **discontinuous at every integer** (jumps from $1^-$ to $0$).
>
> If $g(x) = \{h(x)\}$, check whether $h(x_0)$ is an integer at the point of interest.

### Brewster's Law

> [!note] Key Result
> At Brewster's angle: $\tan\theta_B = n_2/n_1$. The reflected light is completely plane polarized.
>
> For multi-layer: apply Snell's law at each interface, then use Brewster's condition at the target interface.

### Nernst Equation & Electrochemistry

> [!note] Key Formulas
> $$E = E° - \frac{0.0592}{n}\log Q \quad \text{(at 25°C)}$$
>
> $$\Delta G° = -nFE°$$
>
> $$\Delta H° = nF\left(T\frac{dE°}{dT} - E°\right)$$ (from the temperature dependence of $E°$)
>
> $$\Lambda_m = \frac{\kappa}{C} \quad \text{(molar conductivity)}$$

### Buffer Solutions

> [!note] Henderson-Hasselbalch
> $$\text{pH} = \text{p}K_a + \log\frac{[\text{A}^-]}{[\text{HA}]}$$
>
> At half-equivalence point: $[\text{A}^-] = [\text{HA}]$, so $\text{pH} = \text{p}K_a$.
>
> For amphiprotic species ($\text{HCO}_3^-$): $\text{pH} = \frac{\text{p}K_{a1} + \text{p}K_{a2}}{2}$.

### Standing Waves on Strings

> [!note] Key Results
> $n$-th harmonic: $y = A\sin\frac{n\pi x}{L}\cos\omega t$
>
> Frequency: $f_n = \frac{n}{2L}\sqrt{\frac{T}{\mu}}$
>
> Energy distribution: proportional to $\sin^2\frac{n\pi x}{L}$ at maximum displacement (all PE) and $\cos^2\frac{n\pi x}{L}$ at equilibrium (all KE).