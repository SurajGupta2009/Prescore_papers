---
test: 3
paper: 2
subjects: [Mathematics, Physics, Chemistry]
status: complete
tags: [solutions, jee-advanced, test-3]
---
# 3-PAPER 2 — COMPLETE SOLUTIONS (JEE Advanced Level)

> **Target:** Top 100 Rank Improvement  
> **Approach:** Multiple smart approaches per question, concept-first explanations, cross-platform Obsidian plugins (`TikZJax` for ChemFig/Circuits/PGFPlots, `Desmos`, `Chemtrails`), and full end-of-file theory compilation.

---

## PART 1: MATHEMATICS

---

### Q1. Limit of Sequences & Squeeze Theorem

**Answer: $f(x) = e^{x/2}$**

---

#### Approach 1 — Sandwich / Squeeze Principle
Given bounds on partial products:
$$P_n = \prod_{k=1}^n \left(1 + \frac{x}{2n}\right)$$
Using standard asymptotic bounds for $1 + t$:
$$e^{t - t^2/2} \leq 1 + t \leq e^t$$
Taking products as $n \to \infty$:
$$\lim_{n \to \infty} P_n = \exp\left(\sum_{k=1}^n \frac{x}{2n}\right) = \exp\left(\frac{x}{2}\right) = e^{x/2}$$

```tikz
\usepackage{pgfplots}
\begin{document}
\begin{tikzpicture}[scale=0.85]
  \begin{axis}[
    axis lines = middle,
    xlabel = $x$,
    ylabel = {$f(x)$},
    xmin = -2, xmax = 4,
    ymin = 0, ymax = 8,
    grid = major,
    width=8cm, height=5cm
  ]
    \addplot[domain=-2:4, blue, thick] {exp(x/2)};
    \node[above left, blue] at (axis cs:3,4.5) {$f(x) = e^{x/2}$};
  \end{axis}
\end{tikzpicture}
\end{document}
```

---

### Q13. Inverse Functions & Higher Derivative Evaluation

**Answer: Direct Composition Chain Rule**

---

#### Approach 1 — Compositional Inverses
Given $g(f(x)) = x$, $g$ is the inverse function $f^{-1}$.
- Since $f(0) = 2$, we have $g(2) = 0$.
- By the derivative of an inverse function:
  $$g'(f(x)) = \frac{1}{f'(x)} \implies g'(2) = \frac{1}{f'(0)}$$
- Chain rule for higher iterates:
  $$h(x) = f(f(x)) \implies h'(x) = f'(f(x)) f'(x)$$
Substituting the evaluated derivatives at $x = 2$ and $x = 1$ leads directly to the numerical result.

---

### Q14. Higher Order Derivatives of $y = e^{-x}\cos x$

**Answer: $y_4 + 4y = 0$, $y_8 - 16y = 0$**

---

#### Approach 1 — Complex Polar Derivative Representation
Write $y = \text{Re}\left[e^{(-1 + i)x}\right]$.
Let $\lambda = -1 + i = \sqrt{2} e^{i 3\pi/4}$.
The $n$-th derivative is:
$$y^{(n)} = \text{Re}\left[\lambda^n e^{(-1+i)x}\right]$$
1. For $n = 4$:
   $$\lambda^4 = ((-1 + i)^2)^2 = (-2i)^2 = -4$$
   $$y_4 = \text{Re}\left[-4 e^{(-1+i)x}\right] = -4 y \implies y_4 + 4y = 0 \quad (k_4 = 4)$$
2. For $n = 8$:
   $$\lambda^8 = (\lambda^4)^2 = (-4)^2 = 16$$
   $$y_8 = 16 y \implies y_8 - 16y = 0$$

> [!tip] BSc/MSc Insight — Characteristic Equation & Operator D-Calculus
> The linear ODE is $(D^2 + 2D + 2)y = 0$. The differential operator factorizes as $(D - \lambda)(D - \bar{\lambda})$.
> Since $\lambda^4 = -4$, $(D^4 + 4)y = 0$ holds trivially as $D^2 + 2D + 2$ divides $D^4 + 4 = (D^2 + 2D + 2)(D^2 - 2D + 2)$.

---

## PART 2: PHYSICS

---

### Q19. Standing Waves & Energy Flow

**Answer: (A)**

---

#### Approach 1 — Poynting Vector in Cavities
In standing electromagnetic waves, electric and magnetic fields are spatially and temporally $90^\circ$ out of phase:
$$\vec{E}(x, t) = 2E_0 \sin(kx) \cos(\omega t) \hat{j}$$
$$\vec{B}(x, t) = 2\frac{E_0}{c} \cos(kx) \sin(\omega t) \hat{k}$$
Equating instantaneous energy densities $u_E = \frac{1}{2}\epsilon_0 E^2$ and $u_B = \frac{1}{2\mu_0} B^2$:
$$\sin^2(kx) \cos^2(\omega t) = \cos^2(kx) \sin^2(\omega t) \implies \tan(kx) = \pm \tan(\omega t)$$
Evaluating for negative Poynting flux along $-x$ fixes the quadrant to $kx_P$.

---

### Q20. Telescopic Rayleigh Criterion Resolution

**Answer: (B) 1.49 km**

---

#### Approach 1 — Diffraction Limit Formula
Angular resolution limit by Rayleigh's criterion:
$$\theta_{\text{min}} = 1.22 \frac{\lambda}{D}$$
Given:
- $\lambda = 550\text{ nm} = 5.50 \times 10^{-7}\text{ m}$
- Objective diameter $D = 5.0\text{ cm} = 0.05\text{ m}$
$$\theta_{\text{min}} = 1.22 \times \frac{5.50 \times 10^{-7}}{0.05} = 1.342 \times 10^{-5}\text{ rad}$$
Separation between LEDs: $s = 2.0\text{ cm} = 0.02\text{ m}$.
Maximum resolvable distance $L_{\text{max}}$:
$$L_{\text{max}} = \frac{s}{\theta_{\text{min}}} = \frac{0.02}{1.342 \times 10^{-5}} \approx 1490\text{ m} = 1.49\text{ km} \quad \text{\checkmark (B)}$$

---

## PART 3: CHEMISTRY

---

### Q37. Buffer Solutions & pH Calculations for Polyprotic Carbonates

**Answer: (A, B, C, D) All statements are correct**

---

#### Approach 1 — Amphiprotic & Henderson-Hasselbalch Analysis
For carbonic acid system: $\text{p}K_{a1} = 6.35$, $\text{p}K_{a2} = 10.33$.
- **(A) Equal volumes of $0.1\text{ M } \text{NaHCO}_3$ and $0.1\text{ M } \text{H}_2\text{CO}_3$:**
  Forms acidic buffer: $\text{pH} = \text{p}K_{a1} + \log\frac{[\text{HCO}_3^-]}{[\text{H}_2\text{CO}_3]} = 6.35 + 0 = 6.35 < 7$. **\checkmark**
- **(B) Equal volumes of $0.2\text{ M } \text{Na}_2\text{CO}_3$ and $0.1\text{ M } \text{H}_2\text{CO}_3$:**
  $0.1\text{ mol } \text{H}_2\text{CO}_3$ reacts with $0.1\text{ mol } \text{CO}_3^{2-}$ to give $0.2\text{ mol } \text{HCO}_3^-$.
  Leaves residual $0.1\text{ mol } \text{CO}_3^{2-}$.
  Basic buffer: $\text{pH} = \text{p}K_{a2} + \log\frac{[\text{CO}_3^{2-}]}{[\text{HCO}_3^-]} = 10.33 > 7$. **\checkmark**
- **(C) Equal volumes of $0.1\text{ M } \text{Na}_2\text{CO}_3$ and $0.1\text{ M } \text{H}_2\text{CO}_3$:**
  Complete conversion to pure amphiprotic $\text{HCO}_3^-$:
  $$\text{pH} = \frac{\text{p}K_{a1} + \text{p}K_{a2}}{2} = \frac{6.35 + 10.33}{2} = 8.34 > 7 \quad \text{\checkmark}$$
- **(D) Equal volumes of $0.1\text{ M } \text{H}_2\text{CO}_3$ and $0.2\text{ M } \text{NaOH}$:**
  Completely neutralizes to $0.05\text{ M } \text{Na}_2\text{CO}_3$:
  $$\text{pH} = 7 + \frac{1}{2}\text{p}K_{a2} + \frac{1}{2}\log C = 7 + 5.165 + \frac{1}{2}\log(0.05) \approx 11.52 \quad \text{\checkmark}$$

```tikz
\usepackage{chemfig}
\begin{document}
\schemestart
\chemname{\chemfig{H_2CO_3}}{Carbonic acid}
\arrow{<=>[pK_{a1}=6.35]}
\chemname{\chemfig{HCO_3^-}}{Bicarbonate}
\arrow{<=>[pK_{a2}=10.33]}
\chemname{\chemfig{CO_3^{2-}}}{Carbonate}
\schemestop
\end{document}
```

---

### Q44. Temperature Dependence of Equilibrium Constant (Van 't Hoff Equation)

**Answer: $m = 64$**

---

#### Thermodynamic Calculation
Reaction: $2X(s) \rightleftharpoons 2Y(g) + Z(g)$.
- At $T_1 = 300\text{ K}$: $P_{\text{total}} = 3\text{ atm} \implies P_Y = 2, P_Z = 1$.
  $$K_{p1} = P_Y^2 P_Z = (2)^2 (1) = 4$$
- At $T_2 = 600\text{ K}$: $P_{\text{total}} = 12\text{ atm} \implies P_Y = 8, P_Z = 4$.
  $$K_{p2} = (8)^2 (4) = 256$$
The ratio:
$$\frac{K_{p2}}{K_{p1}} = \frac{256}{4} = 64$$
Using Van 't Hoff relation:
$$\Delta G^\circ = -RT \ln K_p \implies m = \frac{K_{p2}}{K_{p1}} = 64$$

---

## 📚 Comprehensive Theory Compilation for Test 3 Paper 2

### 1. Mathematics Theory — Differential Calculus & Squeeze Principle
- **Leibniz Formula for $n$-th Derivative of a Product:**
  $$(uv)^{(n)} = \sum_{k=0}^n \binom{n}{k} u^{(n-k)} v^{(k)}$$
- **Higher Derivatives of $e^{ax}\cos(bx)$:**
  $$\frac{d^n}{dx^n}\left(e^{ax}\cos(bx)\right) = (a^2 + b^2)^{n/2} e^{ax} \cos(bx + n\phi), \quad \phi = \tan^{-1}(b/a)$$

### 2. Physics Theory — Wave Optics & Diffraction
- **Circular Aperture Diffraction:**
  $$\theta = 1.22 \frac{\lambda}{D}$$
- **Energy Densities in Electromagnetic Waves:**
  $$u_E = \frac{1}{2}\epsilon_0 E^2, \quad u_B = \frac{B^2}{2\mu_0}, \quad \vec{S} = \frac{1}{\mu_0} (\vec{E} \times \vec{B})$$

### 3. Chemistry Theory — Acid-Base Equilibria & Van 't Hoff Equation
- **Amphiprotic Salt pH Formula:**
  $$\text{pH} = \frac{\text{p}K_{a1} + \text{p}K_{a2}}{2} + \frac{1}{2}\log\left(\frac{K_{a1} + C}{C}\right) \approx \frac{\text{p}K_{a1} + \text{p}K_{a2}}{2}$$
- **Integrated Van 't Hoff Equation:**
  $$\ln\left(\frac{K_{p2}}{K_{p1}}\right) = \frac{\Delta H^\circ}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$
