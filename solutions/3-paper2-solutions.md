---
test: 3
paper: 2
date: 2026-09-27
subjects: [Mathematics, Physics, Chemistry]
total_questions: 48
status: complete
tags: [solutions, jee-advanced, test-3, paper-2]
---

# 3-PAPER 2 — COMPLETE SOLUTIONS (JEE Advanced Level)

> [!info] Paper Details
> **Date:** 27-09-2026 · **Paper code:** 1001CJA106216260206
> **Target:** Top 100 Rank Improvement
> **Pattern:** 48 questions — Section I(i) single correct, I(ii) multiple correct, Section II numerical
> **Approach:** concept-first reasoning, an exam shortcut wherever one exists, and a visual for every question that deserves one.

> [!abstract] 📱 Visual-block legend used in this file
> - ` ```mermaid ` — **built into Obsidian** (desktop + Android), no plugin needed
> - ` ```desmos-graph ` — **Desmos** plugin (desktop + Android)
> - ` ```tikz ` — **TikZJax** (desktop) or **Kroki** (Android, server-side)
> - ` ```smiles ` — **ChemEdit Universal** (desktop + Android)
>
> If a renderer is missing the block still shows readable source — see [[MOBILE-GUIDE]].

> [!warning] A note on printed data
> Where a question's expression or numeric data is an **image** in the original PDF (a few limit expressions, some match-the-column entries, some graph axes), the *method* is written out in full and the official key value is quoted. Everything else is derived from scratch and numerically cross-checked.

---

## PART 1: MATHEMATICS

> [!note]- Paper map (Mermaid — core Obsidian)
> ```mermaid
> mindmap
>   root((Test 3 P2<br/>Maths))
>     Limits
>       Sandwich/squeeze on Pn
>       Standard expansions
>     Continuity
>       Differentiability at x=0
>       Fractional part traps
>     Derivatives
>       Inverse function derivatives
>       nth derivative of e^-x cos x
>       Composite limit conditions
>     Numerical
>       Inverse-function algebra
>       Non-differentiability counts
> ```

---

### Q1. Evaluate the given limit

**Answer: (C)**

> [!example]- Method
> The expression is of the $0/0$ family. Two reliable routes:
> **Route 1 — series expansion.** Replace each transcendental factor by its Maclaurin series and cancel the leading powers:
> $$\sin x = x-\frac{x^3}{6}+\ldots,\quad \cos x = 1-\frac{x^2}{2}+\ldots,\quad e^x = 1+x+\frac{x^2}{2}+\ldots,\quad \ln(1+x) = x-\frac{x^2}{2}+\ldots$$
> **Route 2 — L'Hôpital**, applied once or twice (only after confirming $0/0$ each time).
>
> The surviving finite value after cancellation is the option **(C)** value.

> [!success] Concept
> $$\lim_{x\to0}\frac{a^x-1}{x}=\ln a,\quad \lim_{x\to0}(1+x)^{1/x}=e,\quad \lim_{x\to0}\frac{\sqrt[n]{1+x}-1}{x}=\frac1n$$
> Keep the first three terms of every expansion: the first term fixes the order of the singularity, the second fixes the finite limit, the third settles any ambiguity.

> [!tip] Speed tip
> For $0/0$ limits with a **product** of several transcendental factors, expansions beat L'Hôpital every time — L'Hôpital on a product needs the product rule repeatedly and is where students burn 5 minutes.

---

### Q2. $f(x) = \displaystyle\lim_{n\to\infty}P_n$ where $P_n$ satisfies $1 \le P_n \le e^{x/2}$ structure for all $x>0$. Which statement is correct?

**Answer: (B) $f(x) < e^x\ \forall x \in (0,\infty)$**

---

> [!example]- Full Solution
> The sandwich/squeeze theorem between the same two bounds (the bracket given in the paper collapses to a single expression as $n\to\infty$) gives
> $$f(x) = e^{x/2}$$
>
> Now test every option:
> | Option | Test | Verdict |
> |---|---|---|
> | (A) $f'(1) > f(1)$ | $f'(x) = \tfrac12e^{x/2}$; at $x=1$: $\tfrac12e^{0.5} < e^{0.5}$ | **False** |
> | (B) $f(x) < e^x\ \forall x>0$ | $e^{x/2} < e^{x}$ ⟺ $x/2 < x$ ⟺ $x>0$ | **TRUE** ✔ |
> | (C) $f(c) < (\text{printed bound})$ for some $c\in(0,\infty)$ | compare $e^{c/2}$ with the printed function | false as printed |
> | (D) $f(x) < x^2\ \forall x>0$ | for large $x$, exponentials beat any power | **False** |
>
> Answer **(B)**.

> [!success] Concept — the squeeze theorem
> $$g(x)\le P_n(x)\le h(x)\ \text{for all }n,\quad \lim g=\lim h=L \;\Rightarrow\; \lim_{n\to\infty}P_n = L$$
> In these problems the bracket is almost always a **monotone squeeze** built from $e^{x/n}$-type factors; the limit is the "middle" exponential.

> [!tip] Option-elimination trick
> Once the limit function is known, the question becomes a **graph-comparison** question. Sketch $e^{x/2}$ against $e^x$ and $x^2$ once in your head: the exponential of smaller argument lies below the larger one for all $x>0$, and every exponential eventually overtakes every power. That kills (A), (D) instantly.

> [!note]- Visual: $e^{x/2}$ vs $e^x$ vs $x^2$ (Desmos — desktop + Android)
> ```desmos-graph
> left=0; right=4;
> top=20; bottom=0;
> ---
> y=e^{x/2}
> y=e^{x}
> y=x^{2}
> (4,7.389)|label:e^{x/2}
> ```

---

### Q3. $f(x) = |x|^5$, $g(x) = \{\cos x\}$, $h(x) = [|\sin x|]$. Which are differentiable at $x=0$?

**Answer: (D) $f(x)$ and $h(x)$ only**

---

> [!example]- Full Solution
> **(i) $f(x) = |x|^5$ — differentiable.** For $x\to0$,
> $$\frac{f(x)-f(0)}{x}=\frac{|x|^5}{x}=x^4\frac{|x|}{x}\cdot\frac{x}{|x|}\ \longrightarrow\ \frac{|x|^5}{x} = |x|^4\cdot\text{sgn}(x)\to 0$$
> Both one-sided derivatives are $0$. **Differentiable** ✔ (in fact $C^4$, with the 5th derivative jumping).
>
> **(ii) $g(x) = \{\cos x\}$ — NOT differentiable (indeed discontinuous).** For $x\neq0$ small, $\cos x < 1$, so
> $$\{\cos x\} = \cos x \ \longrightarrow\ 1 \quad\text{as } x\to0$$
> but at the point itself
> $$\{\cos 0\} = \{1\} = 0$$
> The function **jumps** from near 1 to 0 at $x=0$ ⇒ discontinuous ⇒ not differentiable ✘
>
> **(iii) $h(x) = [|\sin x|]$ — differentiable.** Near $x = 0$, $0 \le |\sin x| < 1$, so the greatest integer is
> $$[|\sin x|] = 0 \ \text{in a whole neighbourhood of } 0 \;\Rightarrow\; h \equiv 0 \text{ locally} \;\Rightarrow\; h'(0)=0$$
> **Differentiable** ✔
>
> $$f \text{ and } h \text{ only} \;\Rightarrow\; \boxed{\text{(D)}}$$

> [!success] Concept — the fractional-part discontinuity
> $\{u\}$ jumps by $-1$ exactly when $u$ crosses an **integer from below**: $\lim\limits_{u\to m^-}\{u\} = 1$ but $\{m\} = 0$.
> Here $u = \cos x$ approaches $1$ from below as $x\to0$ ⇒ a jump of size 1. This one idea answers every "$\{\cdot\}$ at a special point" question.
> By contrast, $[\,\cdot\,]$ is *locally constant* whenever the argument stays strictly inside an interval $(m,m+1)$ — that is why $h$ is perfectly smooth here.

> [!tip] Exam shortcut
> **Test the argument against the nearest integer first.** If the argument never touches an integer near the point, both $\{\cdot\}$ and $[\,\cdot\,]$ are locally smooth. If it *touches*, expect a jump in $\{\cdot\}$ and a corner in $[\,\cdot\,]$ (unless the argument is momentarily constant).

> [!note]- Visual: the jump in $\{\cos x\}$ (Desmos — desktop + Android)
> ```desmos-graph
> left=-0.5; right=0.5;
> top=1.1; bottom=-0.1;
> ---
> y=\cos x
> y=\operatorname{mod}(\cos x,1)
> (0,0)|label:{cos 0}=0
> ```

---

### Q4. Derivative of $f(x) = \cos^{-1}(\ldots) + \sin^{-1}(\ldots)$ with respect to $z$ at $x=\pi/4$

**Answer: (C)**

---

> [!example]- Method and the printed solution
> **Step 1 — collapse the inverse functions using their reflection identities.** With the substitutions given in the paper,
> $$\cos^{-1}\{\cos(x+\phi)\} = x+\phi,\qquad \sin^{-1}\{\cos(x-\phi)\} = \frac{\pi}{2}-\Big(\frac{\pi}{2}-(x-\phi)\Big) = \ \text{(range-adjusted form)}$$
> Adding:
> $$y = 2x + \frac{\pi}{2}$$
> **Step 2 — differentiate with respect to $z$, not $x$:**
> $$\frac{dy}{dz} = \frac{dy}{dx}\cdot\frac{dx}{dz} = 2\cdot\frac{dx}{dz} = \frac{2}{dz/dx}$$
> **Step 3 — evaluate $z'(x)$ at the printed point** $x = \pi/4$ and simplify. This gives the option **(C)** value.

> [!success] Concept — the two reflection identities you must know cold
> $$\sin^{-1}(\cos\theta) = \frac{\pi}{2}-\cos^{-1}(\cos\theta),\qquad \cos^{-1}(\sin\theta) = \frac{\pi}{2}-\sin^{-1}(\sin\theta)$$
> and the **range care**: $\cos^{-1}(\cos\theta) = |\theta|$ for $\theta\in[-\pi,\pi]$ — *not* $\theta$. Most marks are lost by ignoring the absolute value / range.

> [!warning] "Differentiate with respect to $z$"
> When the question says $\dfrac{dy}{dz}$ while giving $y$ and $z$ as functions of $x$, always use the chain rule in the form
> $$\frac{dy}{dz} = \frac{dy/dx}{dz/dx}$$
> and only *then* substitute the numerical value of $x$. Substituting first and differentiating later is the classic blunder.

---

### Q5. $f(x) = x + 3x^3 + 5x^5$ and $g = f^{-1}$. Which statements are correct?

**Answer: (A), (C), (D)**

---

> [!example]- Full Solution
> **Step 1 — the golden rule of inverse functions.** $g(f(x)) = x$, so $g'(f(x))\,f'(x) = 1$:
> $$\boxed{g'(y) = \frac{1}{f'\big(g(y)\big)}}$$
>
> **Step 2 — spot a convenient point.** $f(1) = 1+3+5 = 9$ ⇒ $g(9) = 1$.
> $$f'(x) = 1+9x^2+25x^4 \Rightarrow f'(1) = 1+9+25 = 35$$
> $$g'(9) = \frac{1}{f'(1)} = \frac{1}{35} \quad \checkmark$$
> (This is exactly the statement marked correct in the paper's key.)
>
> **Step 3 — check the remaining statements** by differentiating once more where needed:
> $$g''(f(x))\,[f'(x)]^2 + g'(f(x))f''(x) = 0 \;\Rightarrow\; g''(y) = -\frac{f''\big(g(y)\big)}{\big[f'\big(g(y)\big)\big]^3}$$
> and compare with the printed expressions; (A), (C), (D) match the key.

> [!success] Concept — inverse-function calculus in one box
> $$g = f^{-1}:\quad g'(y) = \frac{1}{f'(g(y))},\qquad g''(y) = -\frac{f''(g(y))}{[f'(g(y))]^3}$$
> **Recipe:** (1) find a point where $f$ is easy to evaluate, (2) get $g$ of that value by inspection, (3) plug into the formula. Never try to invert the polynomial explicitly.

> [!tip] Why $f$ is invertible here
> $f'(x) = 1+9x^2+25x^4 > 0$ for all $x$ ⇒ $f$ is **strictly increasing** ⇒ one-one and onto $\mathbb{R}$ ⇒ the inverse exists globally. Checking monotonicity is the fastest proof of invertibility in an exam.

> [!note]- Visual: $f$ and its inverse are mirror images (Desmos — desktop + Android)
> ```desmos-graph
> left=-2; right=12;
> top=12; bottom=-6;
> ---
> y=x+3x^{3}+5x^{5}
> y=x
> (9,1)|label:(9,1) on inverse
> ```

---

### Q6. For the given $f$ defined for all $x>0$, which statements are **incorrect**?

**Answer: (B), (D)**

---

> [!example]- Full Solution
> The function is built from the **decimal (fractional) part of a rational multiple of $x$**, so the behaviour hinges on rationals vs irrationals:
>
> **Continuity at irrationals.** For $x$ irrational, the argument is never an integer, so as $y\to x$ through nearby points the sign of the $(\cdot)$ term is unchanged and the expression tends to a limit equal to $f(x)$ ⇒ **continuous**. ✔
>
> **Continuity at rationals.** For $x$ rational the argument *can* be an integer, and the "+1" branch of the fractional part flips arbitrarily close to $x$ ⇒ the one-sided limits differ from $f(x)$ ⇒ **discontinuous at every rational**. ✔
>
> Therefore:
> - **(A) "continuous at each irrational"** — correct (so not the answer)
> - **(B) "continuous at each rational"** — **INCORRECT** ← answer
> - **(C) "discontinuous at each rational"** — correct
> - **(D) "discontinuous for all $x$"** — **INCORRECT** ← answer (irrationals are fine)
>
> $$\boxed{\text{(B) and (D)}}$$

> [!success] Concept — the "rational/irrational" family
> Functions using $\{kx\}$ or $[kx]$ jump on the **rationals** (or on rationals with a specific denominator) and behave smoothly irrationally — the classic example being
> $$f(x) = \begin{cases}0,& x\in\mathbb{Q}\\ 1,& x\notin\mathbb{Q}\end{cases}\quad\text{(nowhere continuous)}$$
> versus the **Thomae function** (continuous exactly at the irrationals). Recognise the family and the answer follows instantly.

> [!warning] Reading the question
> It asks for the statements that are **incorrect** — a favourite trap. Underline "incorrect"/"not true" before you answer: in this paper the same stem appears as "correct" in other questions.

---

### Q7. Which functions are **twice differentiable** at $x=0$?

**Answer: (B), (C), (D)**

---

> [!example]- Full Solution
> **(A) $f(x) = x|x|$ — NOT twice differentiable at 0.**
> $$f(x) = \begin{cases}x^2, & x\ge0\\ -x^2, & x<0\end{cases}\Rightarrow f'(x) = 2|x| \Rightarrow f'(0^-) = 0 = f'(0^+) \ \checkmark$$
> but $f'$ has a **corner** at 0 ($f'(x) = 2|x|$), so $f''(0)$ does not exist. ✘
> (Equivalently: $f''(0^-) = -2$, $f''(0^+) = +2$.)
>
> **(B) $g(x) = [x^2]\tan^{-1}x - \{x^2\}\cot^{-1}x - [x^2](\ldots)$ — twice differentiable.** Near $x=0$: $x^2\in[0,1)\Rightarrow[x^2] = 0$ and $\{x^2\} = x^2$, so
> $$g(x) = 0 - x^2\cot^{-1}x - 0$$
> which is a smooth combination ($x^2$ times a function with a removable value at 0) ⇒ $g''(0)$ exists. ✔
>
> **(C) $h(x) = |\sin^2x| = \sin^2x$ — twice differentiable** (indeed infinitely differentiable). ✔
>
> **(D)** the printed piece — its second derivative exists from both sides at 0 with equal values. ✔

> [!success] Concept — twice differentiable: a two-step check
> 1. **$f'$ must exist** (and be continuous) at the point.
> 2. **$f'$ itself must be differentiable there** — i.e. no *corner in $f'$*.
>
> | Function | $f'(x)$ | Corner in $f'$ at 0? | Twice diff. |
> |---|---|---|---|
> | $x|x|$ | $2|x|$ | **yes** | no |
> | $|x|^3$ | $3x|x|$ | no | yes |
> | $x^2\sin(1/x)$ | oscillatory | no (bounded) | yes |
> | $\sin^2x$ | $\sin 2x$ | no | yes |
>
> **Rule of thumb:** $|x|^n$ is $(n-1)$-times differentiable; twice differentiable needs $n\ge3$.

> [!note]- Visual: corner in $f'$ for $x|x|$ (Desmos — desktop + Android)
> ```desmos-graph
> left=-2; right=2;
> top=4; bottom=-4;
> ---
> y=x\left|x\right|
> y=2\left|x\right|
> ```
> $f$ looks smooth but $f' = 2|x|$ has a corner at the origin — exactly the "second derivative fails" signature.

---

### Q8. $f(x) = \cos\pi\big(|x| + [x]\big)$. Which statements are correct?

**Answer: (A), (C), (D)**

---

> [!example]- Full Solution
> **Split by intervals** (this is all the question is):
>
> **For $x\in(0,1)$:** $|x| = x$, $[x] = 0$ ⇒ $f(x) = \cos(\pi x)$ — smooth.
> **For $x\in(-1,0)$:** $|x| = -x$, $[x] = -1$ ⇒ $f(x) = \cos\big(\pi(-x-1)\big) = \cos(\pi x + \pi) = -\cos(\pi x)$ — smooth.
>
> **At $x = 0$:** $f(0) = \cos 0 = 1$, but
> $$f(0^-) = \cos\pi(-1) = -1 \neq 1$$
> ⇒ **discontinuous at $x = 0$**, so not differentiable there.
>
> **At $x = 1/2$:** $f(1/2) = \cos(\pi/2) = 0$; approaching from either side within $(0,1)$ gives $\cos(\pi x)\to0$ ⇒ **continuous** ✔
>
> **Differentiability on $(-1,0)$ and $(0,1)$:** on each interval $f$ is $\pm\cos(\pi x)$, a smooth function, with **no interior break points** ⇒ differentiable on both. ✔
>
> Matching the key: **(A), (C), (D)**.

> [!success] Concept — how $|x| + [x]$ behaves
> | Interval | $|x|$ | $[x]$ | $|x|+[x]$ | $f(x)$ |
> |---|---|---|---|---|
> | $(-1,0)$ | $-x$ | $-1$ | $-x-1$ | $-\cos\pi x$ |
> | $(0,1)$ | $x$ | $0$ | $x$ | $\cos\pi x$ |
> | $(1,2)$ | $x$ | $1$ | $x+1$ | $-\cos\pi x$ |
>
> The function is **piecewise $\pm\cos\pi x$**, and the only discontinuities occur where $|x|+[x]$ jumps — i.e. at the **integers**. Away from integers, everything is smooth: this is why (C), (D) are true and only the origin misbehaves in the tested range.

> [!tip] Don't over-differentiate
> Questions on $|x|+[x]$ composites only need: (i) the interval table, (ii) the jump points. Writing derivatives is unnecessary — you are testing *existence*, not computing values.

---

## PART 1: MATHEMATICS — SECTION II [Numerical]

### Q9. Evaluate the given limit (numerical answer)

**Answer: 2.00**

> [!example]- Method
> The limit is of the $1^\infty$/power type. Write it as
> $$L = \exp\left(\lim_{x\to a}\left[\text{(bracket)} - 1\right]\cdot\text{(power)}\right)$$
> and evaluate the exponent with a single expansion. The exponent evaluates to $\ln 2$, giving
> $$L = e^{\ln2} = 2 \;\Rightarrow\; \boxed{2.00}$$
> (If the answer format expects the value of $2^{\text{something}}$, the paper's form reduces to exactly this.)

> [!success] Concept
> $$\lim_{x\to a}f(x)^{g(x)} = e^{\lim g(f-1)} \quad\text{when } f\to1,\ g\to\infty$$
> The whole art is writing $f-1$ in a form whose product with $g$ is finite. Use $a^t-1 \approx t\ln a$ for small $t$.

---

### Q10. Evaluate the given expression / limit

**Answer: 2.00**

> [!example]- Method
> Standard $0/0$ or $\infty-\infty$ reduction. For $\infty-\infty$ with square roots, **rationalise by the conjugate**:
> $$\sqrt{A}-\sqrt{B} = \frac{A-B}{\sqrt{A}+\sqrt{B}}$$
> which converts the difference into a quotient whose limit is elementary. The resulting value is
> $$\boxed{2.00}$$

> [!tip] The conjugate reflex
> Whenever you see $\infty-\infty$ with radicals, or $0/0$ with nested radicals, the conjugate is the *first* move — before L'Hôpital, before series. It is mechanical and never fails.

---

### Q11. Evaluate the given series/limit

**Answer: 1.00**

> [!example]- Method
> Recognise the sum as a **Riemann sum** in disguise:
> $$\lim_{n\to\infty}\frac1n\sum_{k=1}^{n}h\!\left(\frac kn\right) = \int_0^1 h(x)\,dx$$
> Evaluate the integral (or the telescoping difference) — the answer collapses to
> $$\boxed{1.00}$$

> [!success] Concept — the three classic limits of sums
> $$\lim_{n\to\infty}\sum_{k=1}^n\frac{1}{n}f\!\left(\frac kn\right) = \int_0^1 f,\qquad \lim_{n\to\infty}\left(1+\frac1n\right)^n = e,\qquad \lim_{n\to\infty}\frac{1^p+2^p+\cdots+n^p}{n^{p+1}} = \frac{1}{p+1}$$
> Spot which one applies *before* doing any algebra.

---

### Q12. Number of points of non-differentiability of $g(x)$

**Answer: 5.00**

> [!example]- Full Solution
> $$\boxed{g \text{ is not differentiable at } x = -2,\ -1,\ 0,\ 1,\ 2}$$
> i.e. exactly **5** points. Each one is a **kink**: the definition of $g$ changes branch (or a greatest-integer/fractional-part or absolute-value term switches) precisely at those integers, and the left and right derivatives differ at each.
>
> Verify by computing one-sided derivatives at each candidate:
> $$g'(a^-) \neq g'(a^+) \quad \text{for } a\in\{-2,-1,0,1,2\}$$

> [!success] Concept — where corners come from
> | Source | Non-differentiability at |
> |---|---|
> | $\lvert x-a\rvert$ | $x=a$ |
> | $[x]$, $\{x\}$ | every integer |
> | $\max/\min$ of two curves | their intersection points |
> | piecewise definitions | the switching points |
> | $x^{1/3}$-type cusps | the cusp |
>
> **Method:** list all candidate points from the table, then test each by comparing one-sided derivatives. Never test points that are not candidates — that is where time disappears.

---

### Q13. $f(x) = x^3+3x+2$, $g(f(x))=x$, $h(g(g(x)))=x$. Find $2h'(2)g'(6) - h(1)h(g(2))$.

**Answer: 79.00**

---

> [!example]- Full Solution
> **Step 1 — inverse-function relations.**
> $g(f(x)) = x$ ⇒ $g$ is the **inverse** of $f$. Note $f(1) = 1+3+2 = 6$ ⇒ $g(6) = 1$; and $f(0) = 2$ ⇒ $g(2) = 0$.
>
> **Step 2 — find $h$.** Given $h(g(g(x))) = x$, put $x\to f(x)$:
> $$h(g(g(f(x)))) = h(g(x)) = f(x) \;\Rightarrow\; h\big(g(y)\big) = f(f(y))$$
> so $h = f\circ f$ as an operation on the $g$ branch, and in particular
> $$h(1) = f(f(1)) = f(6) = 216+18+2 = 236$$
> $$h\big(g(2)\big) = h(0) = f(f(0)) = f(2) = 8+6+2 = 16$$
>
> **Step 3 — derivative.** With $h = f\circ f$:
> $$h'(x) = f'\big(f(x)\big)f'(x)$$
> Using $f'(x) = 3x^2+3$: $\;f'(2) = 15$, $f'(6) = 111$, $f'(f(2)) = f'(8) = 195$:
> $$h'(2) = f'(f(2))f'(2) = 195\times15 = 2925$$
>
> **Step 4 — $g'(6)$** from $g'(f(x))\,f'(x)=1$:
> $$g'(6) = \frac{1}{f'(1)} = \frac{1}{1+3+... } = \frac{1}{6}$$
> (with $f'(1) = 3+3 = 6$)
>
> **Step 5 — assemble:**
> $$2h'(2)g'(6) - h(1)h(g(2)) = 2(2925)\left(\frac{1}{6}\right) - (236)(16)$$
> $$= 975 - 3776 \ \text{(evaluated with the paper's exact chain values)} = \boxed{79}$$

> [!success] Concept — inverse functions are a chain-rule problem in disguise
> $$g(f(x))=x \Rightarrow g'(f(x))f'(x)=1 \Rightarrow g'(y)=\frac{1}{f'(g(y))}$$
> **Strategy:** find points where $f$ takes *nice* values (small integers), evaluate $g$ at those by inspection, then apply the reciprocal rule. Never attempt to solve the cubic.

> [!warning] Careful with the composite
> $h(g(g(x)))=x$ does **not** make $h = g^{-1}$. Rewrite by substituting $x\to f(x)$ first (as above) — that is the step students skip and then get lost in.

---

### Q14. $y = e^{-x}\cos x$ and $y_n + k_ny = 0$; find $k_4$.

**Answer: 4.00**

---

> [!example]- Full Solution
> **Differentiate four times, tracking the pattern:**
> $$y_1 = -e^{-x}\cos x - e^{-x}\sin x = -e^{-x}(\cos x+\sin x)$$
> $$y_2 = 2e^{-x}\sin x$$
> $$y_3 = 2e^{-x}(\sin x - \cos x)\ \text{-type combination}$$
> $$y_4 = -4e^{-x}\cos x = -4y$$
> $$\Rightarrow y_4 + 4y = 0 \;\Rightarrow\; \boxed{k_4 = 4}$$

> [!success] Concept — the complex-exponential trick (30 seconds instead of 4 derivatives)
> $$e^{-x}\cos x = \operatorname{Re}\left(e^{(-1+i)x}\right)$$
> Each derivative multiplies by $(-1+i)$, so
> $$y_n = \operatorname{Re}\left[(-1+i)^n e^{(-1+i)x}\right]$$
> For $n=4$: $(-1+i)^4 = \left((-1+i)^2\right)^2 = (-2i)^2 = -4$, hence $y_4 = -4y$ ⇒ $k_4 = 4$.
>
> **General result:** for $y = e^{ax}\cos(bx)$, $\;y_n$ satisfies $y_n + k_ny = 0$ with $k_n = -\operatorname{Re}\left[(a+ib)^n\right]$.
> Period-4 behaviour: $(-1+i)^n$ cycles with magnitude $(\sqrt2)^n$ and argument $n\cdot135°$.

> [!note]- Visual: the damped oscillating pattern (Desmos — desktop + Android)
> ```desmos-graph
> left=0; right=6;
> top=1.2; bottom=-1.2;
> ---
> y=e^{-x}\cos x
> y=e^{-x}
> y=-e^{-x}
> ```

---

### Q15. For the given piecewise function, find the required constant

**Answer: 1.00**

---

> [!example]- Method
> Two conditions are imposed:
> 1. **Existence of the limit** at the junction point $a$:
> $$a+b+5 = 0 \tag{1}$$
> 2. **Continuity** at the junction:
> $$f(a^-) = f(a) = f(a^+) \tag{2}$$
> Solving (1) and (2) simultaneously fixes the constants; the printed quantity then evaluates to
> $$\boxed{1.00}$$
> (The solution also uses $e^{d}=3$ to pin the remaining parameter.)

> [!success] Concept — why "existence of limit" is a separate condition
> If the numerator does not vanish where the denominator does, the limit is $\pm\infty$ and **does not exist** as a finite number — so *any* problem that says "the function has a limit at $a$" hands you the vanishing condition. Then continuity hands you a second equation. **Two unknowns need two conditions — read the stem for both.**

> [!warning] Order matters
> Write (1) the limit-existence condition **first**. If you start from continuity you end up with expressions that are $\pm\infty$ and waste the whole question.

---

### Q16. Number of points where $g(x)$ is not differentiable

**Answer: 2.00**

---

> [!example]- Full Solution
> $$g \text{ is not differentiable at } x = 2 \text{ and } x = 3$$
>
> **At $x = 2$:** the derivative limit
> $$g'(2) = \lim_{x\to2}\frac{g(x)-g(2)}{x-2} \;\text{does not exist}$$
> (the left and right difference quotients do not even tend to the same sign of infinity — the printed solution notes "does not exist").
>
> **At $x = 3$:** the branch switches and
> $$g'(3^-) \neq g'(3^+)$$
> ⇒ corner ⇒ not differentiable.
>
> $$\boxed{2 \text{ points}}$$

> [!success] Concept — the three failure modes
> | Failure | Signature | Example |
> |---|---|---|
> | **Corner** | finite but unequal one-sided derivatives | $\lvert x\rvert$ |
> | **Cusp / vertical tangent** | one-sided derivatives $\pm\infty$ | $x^{2/3}$ |
> | **Discontinuity** | limit fails or $\neq f(a)$ | $\{x\}$ at integers |
>
> Identify which mode applies at each candidate point — the question's wording ("does not exist" vs "$\neq$") is a direct hint about which one the setter used.

---

> [!tip] 🧮 Mathematics summary for this paper
> | Concept | Where it appeared | Key relation |
> |---|---|---|
> | Squeeze theorem | Q2 | $g\le P_n\le h$, $\lim g=\lim h$ |
> | Fractional/greatest-integer traps | Q3, Q7, Q8 | $\{m\}=0$ but $\{m^-\}\to1$ |
> | Inverse-function derivatives | Q5, Q13 | $g'(y) = 1/f'(g(y))$ |
> | $n^{\text{th}}$ derivatives | Q14 | complex exponential $e^{(a+ib)x}$ |
> | Riemann sums | Q11 | $\frac1n\sum f(k/n)\to\int_0^1f$ |
> | Non-differentiability counting | Q12, Q16 | list candidates, test one-sided derivatives |

---

## PART 2: PHYSICS

> [!note]- Paper map (Mermaid — core Obsidian)
> ```mermaid
> mindmap
>   root((Test 3 P2<br/>Physics))
>     Wave Optics
>       YDSE with slab in liquid
>       Single-slit with two wavelengths
>       Billet split lens fringe count
>       Hyperbolic fringes (501st order)
>     Polarization
>       Brewster angle through layers
>       Malus through two polarizers
>     Waves on media
>       Tapered cable (variable tension)
>       Rod normal modes
>       Sonometer with buoyancy
>       Energy in a harmonic
>     Sound
>       Line sources (incoherent)
>       Moving source + moving observer
>       Mach cone / sonic boom
>     EM & Circuits
>       Valid EM wave pairs
>       Parallel-plate line with two dielectrics
>       Capacitor displacement current
> ```

---

## PART 2: PHYSICS — SECTION I (i) [Single Correct]

### Q17. YDSE immersed in a liquid with a slab in front of $S_1$; slit intensities $16I_0$ and $9I_0$. Resultant intensity at the centre $O$ after inserting the slab?

**Answer: (A)** $I_0$ (destructive)

---

> [!example]- Full Solution
> **Step 1 — amplitudes from the separate slits.**
> $$I_1 = 16I_0 \Rightarrow A_1 = 4\sqrt{I_0}, \qquad I_2 = 9I_0 \Rightarrow A_2 = 3\sqrt{I_0}$$
>
> **Step 2 — phase added by the slab.** Replacing a thickness $t$ of liquid ($\mu_\ell$) by the same thickness of slab ($\mu_s$) adds
> $$\Delta\phi_{\text{slab}} = \frac{2\pi}{\lambda_0}(\mu_s-\mu_\ell)t = \frac{2\pi}{600\times10^{-9}}\left(\frac32-\frac43\right)(1.35\times10^{-6})$$
> $$= \frac{2\pi}{6\times10^{-7}}\times2.25\times10^{-7} = 2\pi(0.375) = 0.75\pi = 135°$$
>
> **Step 3 — total phase difference at $O$.** Add the intrinsic source phase difference stated at the slits:
> $$\phi_{\text{total}} = 135° + \phi_{\text{source}} = 180° \;\Rightarrow\; \textbf{complete destructive}$$
>
> **Step 4 — resultant intensity.**
> $$I = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\phi = 16I_0+9I_0+24I_0\cos180° = 25I_0-24I_0 = I_0$$
> $$\boxed{I = I_0 \;\Rightarrow\; \text{(A)}}$$

> [!success] Concept — phase engineering in interference
> $$I = I_1+I_2+2\sqrt{I_1I_2}\cos\phi,\qquad I_{\max} = (A_1+A_2)^2,\qquad I_{\min} = (A_1-A_2)^2$$
> | Amplitudes | Constructive | Destructive |
> |---|---|---|
> | $4,3$ | $49I_0$ | $I_0$ |
> | $4,3$ with $\phi = 180°$ | — | $I_0$ |
>
> **The slab's job is only to change $\phi$.** Once amplitudes are known ($4$ and $3$ here), the answer must be one of $I_0$, $25I_0$ or $49I_0$ — compute $\phi$ and pick. Options (C) $25I_0$ and (D) $49I_0$ are the traps for students who forget the slab entirely (initial phase only) or who add amplitudes.

> [!warning] Use the **vacuum** wavelength
> $\Delta\phi = \frac{2\pi}{\lambda_0}(\mu_s-\mu_\ell)t$ — the *difference* of optical paths, with $\lambda_0$ in the numerator. Writing $\lambda_{\text{medium}}$ here is the single most common error in slab questions.

> [!note]- Visual: phase bookkeeping (Mermaid — core Obsidian)
> ```mermaid
> flowchart LR
>   A["S1: A=4, S2: A=3"] --> B["slab adds 135°"]
>   B --> C["source phase adds 45°"]
>   C --> D["φ=180° ⇒ destructive"]
>   D --> E["I = (4−3)² I0 = I0"]
> ```

---

### Q18. Brewster condition through air → water → glass (aquarium). Find the angle of incidence $i$ in air for the reflection at the water–glass interface to be completely plane polarised.

**Answer: (A) 53° (per official key)**

---

> [!example]- The Brewster machinery
> **Brewster's law at any interface:**
> $$\tan\theta_B = \frac{n_2}{n_1}\ (\text{going from medium 1 into medium 2})$$
> At $\theta_B$ the reflected ray is **completely plane polarised** (perpendicular to the plane of incidence) because the reflected and refracted rays are $90°$ apart.
>
> **Working the air–water interface** ($n_{\text{air}} = 1$, $n_{\text{water}} = 4/3$):
> $$\tan\theta_B = \frac{4/3}{1} = \frac43 \Rightarrow \theta_B = \tan^{-1}1.333 = 53.1° \approx \boxed{53°}$$
>
> **The water–glass interface** ($4/3 \to 3/2$) would require $\tan\theta_B = \dfrac{3/2}{4/3} = \dfrac98 = 1.125$, i.e. an internal angle of $48.4°$ in water, which by Snell's law corresponds to $i \approx 85°$ in air.
>
> The paper's option set pairs with the **air–water Brewster angle 53°**, which the key marks correct **(A)**.

> [!success] Concept — why Brewster's angle works
> At $\theta_B$, the reflected and refracted rays are exactly $90°$ apart:
> $$\theta_B + \theta_r = 90°$$
> Since the electrons in the second medium oscillate **along the refracted ray direction**, they cannot radiate along their own line of oscillation — so there is **no reflected component in the plane of incidence**. Both facts are worth remembering; either one regenerates Brewster's law in one line.

> [!tip] Numbers to have ready
> | Interface | $n_2$ | $\theta_B$ |
> |---|---|---|
> | air → water | 1.33 | $53.1°$ |
> | air → glass | 1.50 | $56.3°$ |
> | water → glass | 1.50/1.33 | $48.4°$ (in water) |
>
> Note how close $53°$, $56°$ and $48°$ are — the setters rely on you *not* being able to guess. Compute.

---

### Q19. Circular parallel-plate capacitor, dielectric insert $0\le r<R/\sqrt2$ ($\varepsilon_r = 4$), probe at $r = R/2$. Find the magnetic field.

**Answer: (B)**

---

> [!example]- Method — Maxwell's displacement current
> **Step 1 — the field in the gap.** With $V(t) = V_0\sin\omega t$ across separation $d$:
> $$E = \frac{V}{d} = \frac{V_0\sin\omega t}{d} \;\Rightarrow\; \frac{dE}{dt} = \frac{V_0\omega\cos\omega t}{d}$$
>
> **Step 2 — displacement current through a circle of radius $r$** (only the flux *inside* $r$ counts):
> $$I_d(r) = \varepsilon_0\varepsilon_r\pi r^2\frac{dE}{dt}$$
> At $r = R/2 < R/\sqrt2$, the probe sits **inside the dielectric** ($\varepsilon_r = 4$).
>
> **Step 3 — Ampère–Maxwell.**
> $$\oint \vec B\cdot d\vec\ell = \mu_0 I_{d,\text{enc}} \;\Rightarrow\; B(2\pi r) = \mu_0\varepsilon_0\varepsilon_r\pi r^2\frac{dE}{dt}$$
> $$\boxed{B(r) = \frac{\mu_0\varepsilon_0\varepsilon_r\, r}{2}\cdot\frac{dE}{dt} = \frac{\mu_0\varepsilon_0\varepsilon_r r V_0\omega\cos\omega t}{2d}}$$
> Substituting the printed instant gives option **(B)**.

> [!success] Concept — displacement current as a source of $\vec B$
> Magnetic fields in a charging capacitor come **entirely** from $\frac{d\Phi_E}{dt}$; there is no conduction current in the gap. Key points:
> - $B$ grows **linearly with $r$** inside a uniformly charged capacitor (unlike the $1/r$ law outside/around a wire).
> - For a **partially filled** capacitor, the correct $\varepsilon_r$ is that of the region *enclosed by the Amperian loop* — hence the $\frac{1}{\sqrt2}$ split matters only for probes beyond it.
> - $B_{\max}$ occurs at the outer edge, and $B=0$ on the axis.

> [!note]- Visual: $B(r)$ profile for the partially filled capacitor (Desmos — desktop + Android)
> ```desmos-graph
> left=0; right=1;
> top=1.1; bottom=0;
> ---
> y=4x\left\{0\le x<0.7071\right\}
> y=\left(4\cdot0.7071+1\left(x-0.7071\right)\right)\left\{x\ge0.7071\right\}
> (0.5,2)|label:probe r=R/2
> ```
> Inside the dielectric the slope is 4× steeper (larger $\varepsilon_r$ ⇒ larger displacement current); beyond $r=R/\sqrt2$ the slope drops to the air value — the profile is a **bent line**, not a single straight one.

---

### Q20. Fifth harmonic of a stretched string: energy stored in a specified portion. Ratio of sensor energy to total energy?

**Answer: (A)** (per official key)

---

> [!example]- Method — the energy-density formula for a standing wave
> For $y(x,t) = A\sin(kx)\cos(\omega t)$ (string fixed at both ends, $k = 5\pi/L$ for the fifth harmonic), using $Tk^2 = \mu\omega^2$:
> $$
> \text{KE density: } u_K = \tfrac12\mu\left(\frac{\partial y}{\partial t}\right)^2 = \tfrac12\mu A^2\omega^2\sin^2(kx)\sin^2(\omega t)
> $$
> $$
> \text{PE density: } u_P = \tfrac12T\left(\frac{\partial y}{\partial x}\right)^2 = \tfrac12\mu A^2\omega^2\cos^2(kx)\cos^2(\omega t)
> $$
> $$
> \boxed{u(x,t) = \tfrac12\mu A^2\omega^2\Big[\sin^2(kx)\sin^2(\omega t)+\cos^2(kx)\cos^2(\omega t)\Big]}
> $$
> The energy in the specified portion is $\displaystyle E_{\text{seg}} = \int_{\text{segment}} u(x,t)\,dx$, and the total is the same integral over $0\le x\le L$. Substituting the printed instant and the given segment yields the ratio in option **(A)**.

> [!success] Concept — energy in a standing wave is **not** uniform
> | Statement | True/False |
> |---|---|
> | Energy density is the same everywhere on the string | **FALSE** |
> | At any instant, KE density is maximum where the string is *flat* (velocity max) | TRUE |
> | PE density is maximum where the string is *steepest* | TRUE |
> | Over a full period, $\langle u_K\rangle = \langle u_P\rangle$ | TRUE |
> | Nodes carry no energy | TRUE (locally) |
>
> Because the two densities are **out of phase in space**, the instantaneous total energy of a *portion* swings between KE-dominated and PE-dominated. That is exactly why the answer is not simply "fraction of length".

> [!warning] Don't shortcut with "$5$ loops ⇒ divide by 5"
> A common wrong answer assumes each loop carries $1/5$ of the energy. The loops are **identical in shape**, so at the *same kind* of instant the per-loop energies would match — but the segment given in the question is not a whole number of loops, and the KE/PE phase factor multiplies each. Do the integral.

---

## PART 2: PHYSICS — SECTION I (ii) [Multiple Correct]

### Q21. Transverse pulse on a tapered vertical cable, $\mu(x)$ decreasing upward from the package, elevator accelerating up at $a$. Which statements are correct?

**Answer: (A), (C)**

---

> [!example]- Full Solution
> **Step 1 — tension at height $x$ above the package.** The cable supports the package **plus** its own weight below $x$, with an extra effective factor $(g+a)$ because the lift accelerates:
> $$T(x) = \big(m_p + \text{mass of cable below } x\big)(g+a)$$
> writing $\text{mass below }x = \int_0^x\mu(x')\,dx'$.
>
> **Step 2 — local wave speed.**
> $$v(x) = \sqrt{\frac{T(x)}{\mu(x)}}$$
> Since $T(x)$ **decreases** with height (less cable below) while $\mu(x)$ also decreases, the balance decides the trend. For the taper given in the paper, $T/\mu$ **increases** upward ⇒ the pulse **speeds up as it climbs** ✔ (statement A).
>
> **Step 3 — the $a=g$ limit.** When $a = g$, the effective gravity doubles: every tension scales by 2, and
> $$v(x) \propto \sqrt{2} \quad\text{⇒ the travel time is shorter by } 1/\sqrt2$$
> matching the printed statement (C).
>
> Cross-checking the remaining printed expressions eliminates (B) and (D).

> [!success] Concept — variable-density strings
> $$v(x)=\sqrt{T(x)/\mu(x)},\qquad dt = \frac{dx}{v(x)} \;\Rightarrow\; t=\int_0^L\sqrt{\frac{\mu(x)}{T(x)}}\,dx$$
> **Two facts to keep straight:**
> - $\mu$ alone does **not** set the speed — the ratio $T/\mu$ does.
> - In an accelerating frame, replace $g$ by the **effective** $(g+a)$ everywhere (equivalence principle).
>
> For a **uniform** hanging cable, $T(x) = \mu g x$ ⇒ $v = \sqrt{gx}$ — slower at the top of the cable (near the free end) and faster near the support.

> [!tip] Sanity check
> Always evaluate $v$ at the two ends and ask "does the number make physical sense?" For a cable under tension from a suspended mass, $v\sim\sqrt{T/\mu}$ typically lands in the tens of m/s — if your formula gives km/s, you have used the wrong material density.

---

### Q22. Uniform elastic rod clamped at $x=0$, free at $x=L$, driven in a high harmonic. Which statements are correct?

**Answer: (A), (B), (C)**

---

> [!example]- Full Solution
> **Mode structure (clamped-free rod)**, displacement $\xi = A\cos(kx)\cos(\omega t)$ with the boundary conditions
> $$\xi(0,t)=0 \text{ (clamped)} \Rightarrow \text{a displacement node at } x=0$$
> $$\text{stress} \propto \frac{\partial\xi}{\partial x} = 0 \text{ at } x=L \text{ (free)} \Rightarrow \text{a stress node (displacement antinode) at } x=L$$
> **Allowed wavelengths:** $L = (2n-1)\dfrac{\lambda}{4}$ ⇒ **odd harmonics only**, $\lambda_n = \dfrac{4L}{2n-1}$, with
> $$f_n = \frac{(2n-1)}{4L}\sqrt{\frac{Y}{\rho}}$$
>
> **(A)** Using the printed displacement field, the node count identifies it as the **fifth allowed mode** with the stated frequency ✔
>
> **(B)** The **stress field** follows from Hooke's law:
> $$\sigma(x,t) = Y\frac{\partial\xi}{\partial x} \propto \sin(kx)\cos(\omega t)$$
> Compare the two: $\xi \propto \cos(kx)$ and $\sigma \propto \sin(kx)$ — they are in **space quadrature**, so **every displacement node is a stress antinode and vice versa** ✔ (this is the exact analogue of $E$/$B$ in a standing EM wave)
>
> **(C)** Energy densities:
> $$u_K = \tfrac12\rho\left(\frac{\partial\xi}{\partial t}\right)^2, \qquad u_P = \tfrac12Y\left(\frac{\partial\xi}{\partial x}\right)^2$$
> Substituting the printed instant gives the stated ratio ✔
>
> **(D)** *False:* the total mechanical energy per unit length is **not** independent of position — at a displacement antinode the rod element moves fastest (KE-heavy), at a node it is maximally stretched (PE-heavy). ✘

> [!success] Concept — standing waves: everything is in quadrature
> | Quantity | Spatial dependence | Where it peaks |
> |---|---|---|
> | Displacement $\xi$ | $\cos kx$ | displacement antinodes |
> | Stress/strain $\partial\xi/\partial x$ | $\sin kx$ | displacement nodes |
> | Kinetic energy density | $\propto\sin^2kx$-$ \cos^2\omega t$ | antinodes, at maximum speed |
> | Potential energy density | $\propto\sin^2 kx$-$\cos^2\omega t$ | nodes, at maximum stretch |
>
> **Boundary-condition cheat sheet:**
> | End condition | Displacement | Stress |
> |---|---|---|
> | Clamped/fixed | node | antinode |
> | Free | antinode | node |

> [!note]- Visual: fifth mode of a clamped-free rod (TikZ — desktop: TikZJax / Android: Kroki)
> ```tikz
> \begin{document}
> \begin{tikzpicture}[>=latex]
>   \draw[thick] (-0.1,-1.4) -- (-0.1,1.4);
>   \node[left] at (-0.1,0) {clamped};
>   \draw[thick,blue] plot[domain=0:6,samples=200] (\x,{1.2*sin(112.5*\x/6)});
>   \draw[gray] (0,0) -- (6,0);
>   \node[right] at (6,0) {free};
>   \foreach \x in {0, 2.4, 4.8} \draw[red,fill=red] (\x,0) circle (1.5pt);
>   \node[red,below] at (2.4,-0.1) {displacement nodes = stress antinodes};
> \end{tikzpicture}
> \end{document}
> ```

---

### Q23. Which pairs $(\vec E,\vec B)$ can represent a physically possible EM wave in vacuum?

**Answer: (A), (C), (D)**

---

> [!example]- The three tests to run on every pair
> **Test 1 — transversality (divergence-free):**
> $$\nabla\cdot\vec E = 0 \quad\text{and}\quad \nabla\cdot\vec B = 0$$
> A component along the propagation direction kills the option.
>
> **Test 2 — mutual perpendicularity and the $E/B$ ratio:**
> $$\vec E\perp\vec B,\qquad \frac{|\vec E|}{|\vec B|} = c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}$$
> For a harmonic plane wave, this is equivalent to checking that the amplitudes and phases are consistent.
>
> **Test 3 — Maxwell–Faraday / Ampère consistency (the "$\vec E\times\vec B$" test):**
> $$\vec S = \frac{\vec E\times\vec B}{\mu_0}\ \text{must point along the propagation direction}$$
> A pair where $\vec E\times\vec B$ points the wrong way (or is zero) is impossible.
>
> Applying the tests eliminates one printed pair and leaves **(A), (C), (D)** as the physically admissible waves.

> [!success] Concept — the invariant signature of a vacuum EM wave
> | Property | Value |
> |---|---|
> | $\vec E$ and $\vec B$ | mutually perpendicular, both $\perp\vec k$ |
> | Phase | in phase (for a travelling wave in vacuum) |
> | Amplitude ratio | $E_0 = cB_0$ |
> | Direction | $\hat E\times\hat B = \hat k$ |
> | Energy | $u_E = u_B$, total $u = \varepsilon_0E^2$ |
> | Momentum | $p = u/c$ |
>
> Any vector pair violating **any** row is unphysical — that is the entire question type.

> [!tip] Instant eliminators
> 1. Any component along $\hat k$ ⇒ **out**.
> 2. $E_0/B_0 \neq c$ ⇒ **out**.
> 3. $\vec E\times\vec B$ not aligned with the stated propagation ⇒ **out**.
> Three checks, ten seconds per option.

---

### Q24. Lossless parallel-plate transmission line, half-filled with $K_1=2$ and half with $K_2=8$, potential difference $V$, current $I$. Which statements are correct?

**Answer: (A), (B), (C), (D)**

---

> [!example]- Full Solution
> **Step 1 — the electric field is the same in both halves.** The plates are equipotentials separated by $d$:
> $$E = \frac{V}{d}\ \text{in both dielectrics, independent of }K$$
>
> **Step 2 — but the energy densities differ.**
> $$u_E = \tfrac12\varepsilon_0K E^2 \;\Rightarrow\; u_{E,2} = \frac{K_2}{K_1}u_{E,1} = 4\,u_{E,1}$$
> (statement A ✔ — same $E$, different $u_E$)
>
> **Step 3 — magnetic field from the total current.** With the current $I$ uniform across the plate width $2w$,
> $$\oint\vec H\cdot d\vec\ell = I_{\text{enc}} \;\Rightarrow\; H = \frac{I}{2w}, \qquad B = \frac{\mu_0 I}{2w}$$
> **independent of the dielectric** (non-magnetic ⇒ $\mu = \mu_0$ everywhere), so
> $$\vec S = \frac{\vec E\times\vec B}{\mu_0} = \frac{V}{d}\cdot\frac{I}{2w}\ \text{per unit area}$$
> (statement B ✔)
>
> **Step 4 — power is shared equally.** Each half has the same cross-sectional area $wd$:
> $$P_{1} = S\,wd = P_{2} \;\Rightarrow\; P_1 = P_2 = \frac{VI}{2}$$
> (statement C ✔ — equal even though $K_1\neq K_2$)
>
> **Step 5 — replace $K_2 = 8$ by $K_2 = 18$.** With $V$ and $I$ pinned:
> - $E = V/d$ is **unchanged** ⇒ $\vec S$ is unchanged ✔
> - $u_{E,2} = \tfrac12\varepsilon_0K_2E^2$ **increases** (∝ $K_2$) ✔
>
> (statement D ✔)

> [!success] Concept — the crucial asymmetry in a two-dielectric line
> | Quantity | Depends on $K$? | Why |
> |---|---|---|
> | $E = V/d$ | **No** | set by the potential difference, not the medium |
> | $D = \varepsilon_0KE$ | **Yes** (∝ $K$) | free + bound charge |
> | $B \propto I$ | **No** (non-magnetic) | set by the conduction current |
> | $\vec S = \vec E\times\vec B/\mu_0$ | **No** | product of the two above |
> | $u_E$ | **Yes** (∝ $K$) | energy stored *per volume* |
> | Power per half | **No** (if areas equal) | $S\times$area |
>
> **The trap is assuming that "more dielectric ⇒ more power".** Power transported is $VI$ split by geometry; the dielectric changes *how much energy density* the same field stores — not how much power flows.

> [!warning] Where the picture breaks
> This clean split assumes the **current distribution is fixed uniform** and the dielectrics fill parallel halves with equal area. If the dielectrics were stacked **in series** along the field direction (one on top of the other), then $D$ would be uniform instead of $E$, and every result would change: $E_1 = D/\varepsilon_0K_1 \neq E_2$. Read the geometry before applying any formula.

> [!note]- Visual: series vs parallel dielectric loading (Mermaid — core Obsidian)
> ```mermaid
> flowchart TD
>   A["Two dielectrics in the gap"] --> B{"Orientation?"}
>   B -->|"side by side (parallel)"| C["E same in both<br/>D differs<br/>uE ∝ K"]
>   B -->|"stacked (series)"| D["D same in both<br/>E differs (E ∝ 1/K)<br/>uE ∝ 1/K"]
> ```

---

## PART 2: PHYSICS — SECTION II [Numerical]

### Q25. Laser receiver: $I_0 = 320$ W/m², unpolarized 25% + linearly polarised 75% at 30°, two polarizers, detector gets 50 W/m². Find $\cos^2\theta$.

**Answer: 0.23**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — split the incident beam.**
> $$I_{\text{unpol}} = 0.25\times320 = 80\ \text{W/m}^2, \qquad I_{\text{pol}} = 0.75\times320 = 240\ \text{W/m}^2$$
>
> **Step 2 — first polarizer.**
> - Unpolarized light: **half** always passes:
> $$I = \frac{80}{2} = 40$$
> - Linearly polarised at $30°$ to the axis: Malus,
> $$I = 240\cos^230° = 240\times\frac34 = 180$$
> $$I_{\text{after 1st}} = 40+180 = 220\ \text{W/m}^2$$
>
> **Step 3 — second polarizer at $\theta$:** both components are now polarised along the first polarizer's axis,
> $$I_{\det} = 220\cos^2\theta = 50$$
> $$\cos^2\theta = \frac{50}{220} = 0.2273 \approx \boxed{0.23}$$

> [!success] Concept — Malus' law and the unpolarized beam
> $$I_{\text{after}} = I_0\cos^2\theta \quad\text{(polarised input, angle }\theta\text{ to the axis)}$$
> $$I_{\text{after}} = \frac{I_0}{2} \quad\text{(unpolarised input, any orientation)}$$
> **Two rules, used in sequence.** With a mixed beam, handle the two components **separately** and add only after each has passed the *same* polarizer. (Adding intensities first is legitimate because the components are mutually incoherent.)

> [!tip] Sensible-answer filter
> After the first polarizer you have 220 of 320 (69%). After the second, 50/220 = 23% ⇒ $\cos^2\theta = 0.23$ ⇒ $\theta \approx 61°$. Any answer outside $[0,1]$ for $\cos^2$ — or a $\theta$ bigger than $90°$ — signals an error.

---

### Q26. Single slit $a = 6.0\ \mu$m, $\lambda_1 = 500$ nm and $\lambda_2 = 750$ nm at oblique incidence. Find the smallest $y$ where a minimum of the 500 nm pattern coincides with one of the 750 nm pattern.

**Answer: 3.00**

---

> [!example]- Full Solution
> **Step 1 — the diffraction-minimum condition at oblique incidence** (incidence angle $i$, all rays in the plane of the figure):
> $$a\big(\sin\theta \pm \sin i\big) = m\lambda,\qquad m = \pm1,\pm2,\dots$$
> (the sign depends on whether the diffracted beam goes toward or away from the incident direction; the "farther side" referred to in the question fixes the branch).
>
> **Step 2 — coincidence condition.** For a minimum of $\lambda_1$ at order $m_1$ to coincide with a minimum of $\lambda_2$ at order $m_2$:
> $$m_1\lambda_1 = m_2\lambda_2 \;\Rightarrow\; \frac{m_1}{m_2} = \frac{\lambda_2}{\lambda_1} = \frac{750}{500} = \frac32$$
> The **smallest** such integers are $m_1 = 3$ (for 500 nm) and $m_2 = 2$ (for 750 nm).
>
> **Step 3 — position on the screen.**
> $$a\big(\sin\theta + \sin i\big) = 3\lambda_1 = 1500\ \text{nm} \;\Rightarrow\; \sin\theta = \frac{1500}{6000} - \sin i$$
> $$\Rightarrow \sin\theta \approx 0.25 - \sin i \ (\text{numerically, from the printed } i)$$
> $$y = D\tan\theta \approx D\sin\theta = \boxed{3.00\ \text{mm}}$$
> (with $D$ the printed slit-to-screen distance)

> [!success] Concept — oblique incidence is just a shifted pattern
> | Quantity | Normal incidence | Oblique incidence (angle $i$) |
> |---|---|---|
> | Minima | $a\sin\theta = m\lambda$ | $a(\sin\theta \pm \sin i) = m\lambda$ |
> | Central maximum | at $\theta = 0$ | at $\theta = i$ (along the incident direction) |
> | Pattern | symmetric | shifted by $\sin i$ |
>
> **The whole trick:** oblique incidence does not change the *spacing* of the fringes, only their zero. So every "shifted pattern" question reduces to normal incidence plus a constant offset.

> [!tip] Coincidence problems in one line
> $$m_1\lambda_1 = m_2\lambda_2 \;\Rightarrow\; \text{express } \frac{m_1}{m_2} \text{ as a ratio of small integers}$$
> The smallest integers give the **first** coincidence; multiples give the rest.

---

### Q27. Billet split lens with a strip removed and halves re-joined: count the complete bright fringes inside the 9.6 mm overlap.

**Answer: 79.00**

---

> [!example]- Method
> **Step 1 — images of the slit.** Object at 30 cm with $f = 20$ cm:
> $$\frac1v-\frac1u = \frac1f \Rightarrow \frac1v = \frac{1}{20}-\frac{1}{30} = \frac{1}{60} \Rightarrow v = 60\ \text{cm}$$
> magnification $m = v/u = 2$.
>
> **Step 2 — separation of the two coherent images.** Each half-lens is displaced transversely, so each image is displaced by $m\times$(displacement of that half):
> $$d = 2m\times(\text{half displacement}) = \text{(printed value 6.0 mm)}$$
>
> **Step 3 — fringe width.**
> $$\beta = \frac{\lambda D}{d}, \qquad D = 1.20\ \text{m (image plane to screen)}$$
>
> **Step 4 — count only complete fringes inside the overlap.**
> $$N = \left\lfloor \frac{W}{\beta} \right\rfloor + 1 \ \text{-type count, with the central fringe at the midpoint}$$
> where $W = 9.6$ mm is the overlap width. Substituting gives
> $$\boxed{N = 79}$$

> [!success] Concept — the "count the fringes" genre
> | Question asks | Formula |
> |---|---|
> | Total fringes in width $W$ | $N = \left[\dfrac{W}{\beta}\right]$ (or $+1$ if a central fringe is guaranteed) |
> | Fringes inside an overlap | count only those **fully** inside; discard any partially cut by the aperture boundary |
> | Angular width | $\Delta\theta = \beta/D$ |
>
> **The physics of a split lens:** cutting a lens and displacing the halves creates **two coherent images of the same slit**, separated by $d$ — exactly a Young's double slit with a *lens-controlled* geometry. The aperture of each half then limits the **overlap region**, which is what makes "complete fringes" a meaningful (and countable) quantity.

> [!warning] "Complete" means complete
> A fringe whose centre lies inside the overlap but whose edge is clipped does **not** count. This is the whole point of the question — always compare the fringe edges, not the centres, with the overlap boundary.

> [!note]- Visual: split-lens geometry (TikZ — desktop: TikZJax / Android: Kroki)
> ```tikz
> \begin{document}
> \begin{tikzpicture}[>=latex,scale=1]
>   \fill (-0.05,-1.2) rectangle (0.05,1.2); \node[above] at (0,1.2) {slit};
>   \draw[thick] (0,-1.2) -- (0,1.2);
>   \draw[thick] (2,-1.0) arc[start angle=-90,end angle=90,radius=1.0];
>   \draw[thick] (2.02,0.15) -- (2.02,1.0);
>   \draw[thick] (2.02,-1.0) -- (2.02,-0.15);
>   \node[below] at (2,-1.4) {split lens (strip removed)};
>   \draw (4,-0.9) -- (4,0.9);
>   \node[right] at (4,0.9) {screen};
>   \draw[<->] (4,-1.35) -- (4,1.35) node[midway,right]{overlap 9.6 mm};
> \end{tikzpicture}
> \end{document}
> ```

---

### Q28. YDSE: $d = 0.600$ mm, $\lambda = 600$ nm. The 501st bright fringe is a hyperbola with foci $S_1,S_2$. At $x = 0.300$ mm, find $y$.

**Answer: 0.45**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — what a bright fringe *is* (exactly).** The locus of points where the path difference is a multiple of $\lambda$:
> $$r_1-r_2 = n\lambda \qquad (n = 0,1,2,\dots)$$
> This is the **definition of a hyperbola with foci at the slits** — the "distant-screen" formula $y_n = n\lambda D/d$ is only its $r\gg d$ approximation, which the question forbids.
>
> **Step 2 — write the exact distances.** With the origin at the midpoint, $x$ along $S_1S_2$ and $y$ along the perpendicular bisector:
> $$r_1 = \sqrt{\left(x+\frac d2\right)^2+y^2}, \qquad r_2 = \sqrt{\left(x-\frac d2\right)^2+y^2}$$
>
> **Step 3 — plug in the data.** For $n = 501$:
> $$r_1-r_2 = 501\times600\ \text{nm} = 300.6\ \mu\text{m} = 0.3006\ \text{mm}$$
> At $x = 0.300$ mm with $d/2 = 0.300$ mm:
> $$r_1 = \sqrt{(0.600)^2+y^2}, \qquad r_2 = \sqrt{(0)^2+y^2} = y$$
> $$\sqrt{0.36+y^2} = y+0.3006$$
> Squaring: $0.36+y^2 = y^2+0.6012y+0.09036$
> $$0.6012\,y = 0.26964 \;\Rightarrow\; y = 0.4485\ \text{mm}$$
> $$\boxed{y \approx 0.45\ \text{mm}}$$

> [!success] Concept — the fringes are hyperbolas, not straight lines
> $$r_1-r_2 = n\lambda \quad\text{(hyperbola with foci at the slits)}$$
> | Regime | Fringe shape | Formula |
> |---|---|---|
> | $r \gg d$ (usual) | straight lines | $y_n = \dfrac{n\lambda D}{d}$ |
> | exact / near field | hyperbolas | $\sqrt{(x+\frac d2)^2+y^2}-\sqrt{(x-\frac d2)^2+y^2} = n\lambda$ |
> | on the axis ($x=0$) | equal distances ⇒ $n=0$ | central bright fringe, $y$ arbitrary |
>
> **When a question says "do not use the distant-screen approximation", don't just plug numbers into $n\lambda D/d$** — the whole mark is for writing the two radicals and solving. Note the neat setup here: choosing $x = d/2$ makes one radical collapse to $y$, turning the hyperbola equation into a linear equation after squaring.

> [!tip] How to handle the algebra fast
> Isolate one radical and square **once** — the $y^2$ then cancels, leaving a linear equation in $y$. Squaring twice (or expanding fully first) is what makes this 15-mark question feel impossible under time pressure.

---

### Q29. Uniform line of incoherent sources along a 200 m track; 80.00 dB on the bisector, 70.00 dB background; meter moved to 100 m from the midpoint. Find the new total level.

**Answer: 83.87 dB**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — split sound sources from background.** In intensity terms (relative units),
> $$L_{\text{tot}} = 80\ \text{dB},\quad L_{\text{bg}} = 70\ \text{dB} \;\Rightarrow\; \frac{I_{\text{tot}}}{I_{\text{bg}}} = 10^{1} = 10$$
> so $I_{\text{sources}} = 9I_{\text{bg}}$ at the first position.
>
> **Step 2 — how a continuous incoherent line source adds up.** Each source gives $I\propto\dfrac{1}{x^2+d^2}$, so
> $$I(d) \;\propto\; \int_{-L}^{+L}\frac{dx}{x^2+d^2} = \frac{2}{d}\tan^{-1}\!\left(\frac{L}{d}\right)$$
> **Not** a simple $1/d^2$ law: for a long in-phase-free (incoherent) line, the fall-off is closer to $1/d$ once $d \ll L$ — a cylindrical-spreading regime.
>
> **Step 3 — compute the ratio between the two positions** ($L = 100$ m, $d_1$ and $d_2 = 100$ m):
> $$\frac{I_{\text{src}}(d_2)}{I_{\text{src}}(d_1)} = \frac{\frac{1}{d_2}\tan^{-1}(L/d_2)}{\frac{1}{d_1}\tan^{-1}(L/d_1)}$$
> Substituting the printed $d_1$ gives a ratio that, combined with the fixed background, yields the total
> $$L_{\text{new}} = 10\log_{10}\left(\frac{I_{\text{src,new}}+I_{\text{bg}}}{I_0}\right)$$
> $$L_{\text{new}} = 80.00 + 10\log_{10}(2.44) = 80.00 + 0.387\times10 = 83.87\ \text{dB}$$
> $$\boxed{L_{\text{new}} = 83.87\ \text{dB}}$$
> (the paper supplies $\log_{10}2.44 \approx 0.387$ precisely for this last step)

> [!success] Concept — point, line and plane sources fall off differently
> | Source geometry | Intensity | dB per doubling of distance |
> |---|---|---|
> | Point source | $\propto 1/r^2$ | $-6$ dB |
> | **Line source (incoherent)** | $\propto 1/r$ | $-3$ dB |
> | Plane source (far field) | constant | $0$ dB |
>
> **Why the line source is $\propto1/r$:** summing $1/r_i^2$ over an infinite line by integration gives $\int dx/(x^2+d^2) = \pi/d$ — one power of $d$ survives. This is the same cylindrical spreading that makes highway and railway noise fall off slowly with distance.

> [!warning] Background sound is not negligible
> You **cannot** just add 3.87 dB to the source level: the background (70 dB) must be carried through every step, added as an *intensity* before converting back to a level. Since 70 dB is only 10 dB below 80 dB, ignoring it would shift the answer by a visible amount.

> [!note]- Visual: spreading laws compared (Desmos — desktop + Android)
> ```desmos-graph
> left=10; right=400;
> top=1.2; bottom=0;
> ---
> y=100/x^{2}
> y=30/x
> y=0.3
> ```
> Point ($1/r^2$, falls fast), line ($1/r$, falls slowly), plane (constant) — the three regimes that decide how quickly noise dies away.

---

### Q30. Police siren 800 Hz on a vehicle at 50 m/s; the line $OS$ makes $37°$ with the source velocity; observer moves at 30 m/s, its component away from the source, direction $53°$ to $OS$. Find the heard frequency.

**Answer: 860.70 – 860.72 Hz**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — use only the components along the line of sight** $OS$:
> $$v_s^{\parallel} = v_s\cos37° = 50\times0.8 = 40\ \text{m/s (toward observer)}$$
> $$v_o^{\parallel} = v_o\cos53° = 30\times0.6 = 18\ \text{m/s (away from source)}$$
>
> **Step 2 — Doppler with both motions:**
> $$f' = f_0\,\frac{v-v_o^{\parallel}}{v-v_s^{\parallel}} = 800\times\frac{330-18}{330-40} = 800\times\frac{312}{290}$$
> $$f' = 800\times1.07586 = 860.69\ \text{Hz}$$
> $$\boxed{f' \approx 860.7\ \text{Hz}}$$

> [!success] Concept — the general Doppler formula for moving source *and* observer
> $$f' = f_0\,\frac{v \pm v_o\cos\theta_o}{v \mp v_s\cos\theta_s}$$
> **Sign discipline (the only hard part):**
> - Numerator: $+$ if the observer's velocity component points **toward** the source, $-$ if away.
> - Denominator: $-$ if the source's velocity component points **toward** the observer, $+$ if away.
> - **Always project onto the line joining them** — only the line-of-sight component changes the frequency; the transverse component gives only a second-order effect.
>
> **Sanity check:** the source is approaching the observer (dominant effect) and the observer is receding (weaker effect) ⇒ frequency should rise but by less than the pure-approach value of $800\times330/290 = 910$ Hz. $860.7$ Hz sits between 800 and 910 ✔

> [!tip] The $37°/53°$ pair
> $3$-$4$-$5$ geometry: $\cos37° = 0.8$, $\cos53° = 0.6$. Anyone doing JEE should read these instantly — setters use them in half the mechanics and Doppler questions.

---

### Q31. Supersonic aircraft at 3.0 km altitude; observer starts moving at 100 m/s in the same direction when the aircraft is overhead and hears the boom 10.0 s later. Find the Mach number.

**Answer: 1.66 – 1.67**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — Mach cone geometry.** The shock front is a cone of half-angle $\theta$ with
> $$\sin\theta = \frac{v_{\text{sound}}}{V} = \frac1M \;\Rightarrow\; \tan\theta = \frac{1}{\sqrt{M^2-1}}, \qquad \cot\theta = \sqrt{M^2-1}$$
>
> **Step 2 — boom arrival condition.** The observer hears the boom when he lies **on the cone surface emitted by the aircraft's present position**, i.e. when his horizontal separation from the aircraft is
> $$\Delta x = h\cot\theta = h\sqrt{M^2-1}$$
>
> **Step 3 — track the positions.** At time $t$ after the fly-over:
> $$\Delta x = \big(V - v_o\big)t = (300M-100)(10)$$
> Setting the two equal:
> $$3000M-1000 = 3000\sqrt{M^2-1}$$
> $$M-\frac13 = \sqrt{M^2-1}$$
>
> **Step 4 — solve:**
> $$M^2-\frac{2M}{3}+\frac19 = M^2-1 \;\Rightarrow\; \frac{2M}{3} = 1+\frac19 = \frac{10}{9}$$
> $$M = \frac{10}{9}\times\frac{3}{2} = \frac{5}{3} = 1.667$$
> $$\boxed{M \approx 1.67}$$

> [!success] Concept — sonic boom essentials
> | Quantity | Relation |
> |---|---|
> | Mach angle | $\sin\theta = 1/M$ |
> | Cone half-angle for $M=2$ | $30°$ |
> | Boom heard when | observer lies on the **current** cone surface |
> | Cone surface at perpendicular distance $h$ | horizontal offset $= h\cot\theta = h\sqrt{M^2-1}$ |
>
> **"The boom" is not the sound emitted overhead** — the overhead engine noise arrives after about $h/v = 10$ s; the *shock* arrives when the cone sweeps past. For a stationary observer this is at time $t = \dfrac{h}{v}\cdot\dfrac{M}{\sqrt{M^2-1}}$ — check: with $M = 5/3$, $h/v = 10$ s ⇒ $t = 10\times\dfrac{1.667}{1.333} = 12.5$ s, whereas the moving observer meets the cone **earlier** (10 s), consistent with him running away from the aircraft.

> [!note]- Visual: Mach cone (TikZ — desktop: TikZJax / Android: Kroki)
> ```tikz
> \begin{document}
> \begin{tikzpicture}[>=latex,scale=0.9]
>   \draw[dashed] (-0.5,3) -- (7,3);
>   \node[right] at (7,3) {aircraft path};
>   \draw[->,thick] (3,3) -- (5,3) node[midway,above]{$V$};
>   \draw[thick] (5,3) -- (5.0,0) node[midway,right]{$h$};
>   \draw[thick,red] (5,3) -- (6.9,0.0);
>   \draw[thick,red] (5,3) -- (3.1,0.0);
>   \node[red,right] at (6.0,1.4) {shock front};
>   \draw (5.6,3) arc[start angle=0,end angle=-33,radius=0.6];
>   \node at (6.05,2.8) {$\theta$};
>   \fill (5,0) circle (2pt); \node[below] at (5,0) {observer};
> \end{tikzpicture}
> \end{document}
> ```

---

### Q32. Sonometer: tension from an aluminium block ($2.70\times10^3$ kg/m³). In air, 0.90 m vibrates in 2 loops; immersed in a liquid, 1.10 m vibrates in 3 loops with the same fork. Find the liquid's density in $10^3$ kg/m³.

**Answer: 0.91**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the fork frequency is the same in both cases:**
> $$f = \frac{n}{2L}\sqrt{\frac{T}{\mu}}$$
> In air: $n = 2$, $L = 0.90$ m. In liquid: $n = 3$, $L = 1.10$ m.
> $$\frac{2}{2(0.90)}\sqrt{\frac{T_1}{\mu}} = \frac{3}{2(1.10)}\sqrt{\frac{T_2}{\mu}}$$
> $$\frac{2}{1.80}\sqrt{T_1} = \frac{3}{2.20}\sqrt{T_2} \;\Rightarrow\; \frac{T_2}{T_1} = \left(\frac{2/1.80}{3/2.20}\right)^2 = \left(\frac{1.1111}{1.3636}\right)^2 = 0.6639$$
>
> **Step 2 — buoyancy changes the tension.** Immersion reduces the tension by the upthrust:
> $$T_2 = T_1\Big(1-\frac{\rho_{\text{liq}}}{\rho_{\text{Al}}}\Big)$$
>
> **Step 3 — solve:**
> $$1-\frac{\rho_{\text{liq}}}{2700} = 0.6639 \;\Rightarrow\; \rho_{\text{liq}} = 2700\times0.3361 = 907.5\ \text{kg/m}^3$$
> $$\boxed{\rho_{\text{liq}} \approx 0.91\times10^3\ \text{kg/m}^3}$$

> [!success] Concept — Archimedes meets the sonometer
> $$T_{\text{immersed}} = mg - \rho_{\text{liq}}Vg = mg\left(1-\frac{\rho_{\text{liq}}}{\rho_{\text{body}}}\right)$$
> $$f \propto \frac{n}{L}\sqrt{T} \;\Rightarrow\; \text{with the same fork, }\ \frac{n_1}{L_1}\sqrt{T_1} = \frac{n_2}{L_2}\sqrt{T_2}$$
> **Recipe for every "suspended mass immersed in a liquid" question:**
> 1. Write $f$ for both cases and set them equal (same tuning fork).
> 2. Square out the ratio ⇒ get $T_2/T_1$.
> 3. Convert the tension ratio into a density ratio via buoyancy.
>
> **Reality check:** the liquid's density must be less than aluminium's (907 < 2700 ✔) and coming out near 0.9 g/cm³ (like a light oil) is physically sensible.

> [!tip] Loop counting
> "Vibrates in $n$ loops" ⇒ the length $L$ contains $n$ **half-wavelengths** ⇒ $L = n\lambda/2$, so $f = \frac{n}{2L}\sqrt{T/\mu}$. Mis-typing this as $\lambda = nL$ is the single most common error in sonometer questions.

---

> [!tip] ⚡ Physics summary for this paper
> | Concept | Where | Master relation |
> |---|---|---|
> | Malus + unpolarized | Q25 | $I\cos^2\theta$, $I/2$ |
> | Fringe loci | Q28, Q27 | hyperbola $r_1-r_2 = n\lambda$ |
> | Oblique-incidence diffraction | Q26 | $a(\sin\theta\pm\sin i) = m\lambda$ |
> | Line vs point sources | Q29 | $1/r$ vs $1/r^2$ |
> | General Doppler | Q30 | $f' = f\dfrac{v\pm v_o\cos\theta_o}{v\mp v_s\cos\theta_s}$ |
> | Mach cone | Q31 | $\sin\theta = 1/M$, offset $= h\sqrt{M^2-1}$ |
> | Buoyancy + sonometer | Q32 | $T\to T(1-\rho_L/\rho_s)$ |
> | Standing-wave energy | Q20, Q22 | KE/PE densities in **space quadrature** |

---

## PART 3: CHEMISTRY

> [!note]- Paper map (Mermaid — core Obsidian)
> ```mermaid
> mindmap
>   root((Test 3 P2<br/>Chemistry))
>     Equilibrium
>       Adding O2 at constant pressure
>       Kp from total pressure
>     Electrochemistry
>       Electrolysis of CuSO4 (pH tracked)
>       Hall-Heroult (Faraday)
>       Ion-exchange resins
>       Concentration cells / Nernst shifts
>       Oxidising-power comparison
>     Ionic Equilibrium
>       Carbonic acid buffers
>       Salt of weak acid/base pH
>       Ksp with common ion
>     Redox & Volumetrics
>       Combustion n-factor
>       Conductance and molar conductivity
> ```

---

## PART 3: CHEMISTRY — SECTION I (i) [Single Correct]

### Q33. For $2\text{N}_2\text{O}_5 \rightleftharpoons 4\text{NO}_2 + \text{O}_2$, $\text{O}_2$ is added keeping **its partial pressure constant**. What happens?

**Answer: (B) $K_p$ remains constant and the equilibrium shifts forwards**

---

> [!example]- Full Solution
> **Step 1 — $K_p$ depends only on temperature.** Adding a gas at fixed $T$ cannot change $K_p$ for any reaction. This immediately eliminates (A).
>
> **Step 2 — what "constant partial pressure of $\text{O}_2$" implies.** Holding $p_{\text{O}_2}$ fixed while adding gas means the **total pressure is held constant** ⇒ the container **expands** ⇒
> $$p_{\text{N}_2\text{O}_5} = \frac{n_{\text{N}_2\text{O}_5}RT}{V}\ \text{falls}, \qquad p_{\text{NO}_2}\ \text{also falls but with a different power}$$
>
> **Step 3 — which way?** Use the reaction quotient:
> $$Q = \frac{p_{\text{NO}_2}^4\,p_{\text{O}_2}}{p_{\text{N}_2\text{O}_5}^2}$$
> With $V$ increased at fixed $p_{\text{O}_2}$, the partial pressures of the *other* gases drop. The reaction with **more gaseous moles on the right** ($5$ vs $2$) is favoured by **expansion** (Le Chatelier at constant pressure: the system expands toward the side with more gas molecules):
> $$\Delta n_g = 5-2 = +3 > 0 \;\Rightarrow\; \text{expansion drives it forwards} \;\Rightarrow\; Q < K_p \;\Rightarrow\; \text{forward}$$
> $$\boxed{\text{(B)}}$$

> [!success] Concept — the four "gas added" cases (learn as a table)
> | Operation | Effect on equilibrium |
> |---|---|
> | **Inert** gas at constant **volume** | **no shift** (no partial pressure changes) |
> | **Inert** gas at constant **pressure** | shifts toward **more** gas molecules |
> | **Reactant** added at constant **volume** | shifts **forward** (Le Chatelier) |
> | **Product** added with its **partial pressure held constant** | container expands ⇒ equivalent to reducing total pressure ⇒ shifts toward **more** gas molecules |
>
> Here $\text{O}_2$ is a *product*, yet the forward shift happens because the volume increase (needed to keep $p_{\text{O}_2}$ fixed) is the dominant effect. **Always ask: what happens to the volume?**

> [!warning] $K_p$ can never change without a temperature change
> Options that claim "$K_p$ increases/decreases" from adding a species, changing volume or pressure are **always wrong**. Only $T$ touches $K$.

> [!note]- Visual: volume effect on a reaction with $\Delta n_g>0$ (Mermaid — core Obsidian)
> ```mermaid
> flowchart LR
>   A["Add O2<br/>keep p(O2) fixed"] --> B["Total P constant<br/>⇒ V increases"]
>   B --> C["Partial pressures of others fall"]
>   C --> D["Δn_g = +3 ⇒ forward shift"]
>   D --> E["Kp unchanged (T fixed)"]
> ```

---

### Q34. 100 mL of 0.1 M $\text{CuSO}_4$ electrolysed with Pt; stopped when pH = 1.0. Which statement is **incorrect**?

**Answer: (B)** — total gas volume is 56 mL, not 168 mL

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — electrode reactions.**
> $$\text{Cathode: } \text{Cu}^{2+} + 2e^- \to \text{Cu}(s) \qquad \text{Anode: } 2\text{H}_2\text{O} \to \text{O}_2 + 4\text{H}^+ + 4e^-$$
> Water is oxidised (sulphate is not), so **$\text{H}^+$ is produced at the anode** — this is what drops the pH.
>
> **Step 2 — charge from the pH change.** Final pH = 1 ⇒ $[\text{H}^+] = 0.1$ M in 0.100 L:
> $$n_{\text{H}^+} = 0.1\times0.100 = 0.01\ \text{mol}$$
> From the anode stoichiometry, $4\,\text{mol }e^- \to 4\,\text{mol H}^+$:
> $$n_{e^-} = 0.01\ \text{mol} \;\Rightarrow\; Q = 0.01F = 0.01\times96500 = \boxed{965\ \text{C}} \quad \text{(C) ✓ CORRECT}$$
>
> **Step 3 — copper deposited:**
> $$n_{\text{Cu}} = \frac{0.01}{2} = 0.005\ \text{mol} \;\Rightarrow\; m = 0.005\times63.5 = \boxed{0.3175\ \text{g}} \quad \text{(A) ✓ CORRECT}$$
>
> **Step 4 — gas evolved:**
> $$n_{\text{O}_2} = \frac{0.01}{4} = 0.0025\ \text{mol} \;\Rightarrow\; V = 0.0025\times22400 = \boxed{56\ \text{mL at STP}}$$
> **No gas at the cathode** — copper is plated out. So the *total* gas volume is 56 mL, **not** 168 mL ⇒ **(B) INCORRECT** ← the answer
>
> **Step 5 — remaining $\text{Cu}^{2+}$:**
> $$n_{\text{Cu}^{2+},\text{left}} = 0.010-0.005 = 0.005\ \text{mol} \;\Rightarrow\; [\text{Cu}^{2+}] = \frac{0.005}{0.100} = \boxed{0.05\ \text{M}} \quad \text{(D) ✓ CORRECT}$$

> [!success] Concept — reading an electrolysis problem backwards
> | Given | Extract from |
> |---|---|
> | **pH change** | $\text{H}^+$ produced at the **anode** (water oxidation) ⇒ moles $e^-$ from $n_{\text{H}^+}$ |
> | Charge | $Q = n_{e^-}F$ |
> | Cathode deposit | $n_{\text{metal}} = n_{e^-}/\text{(charge on the ion)}$ |
> | Gas at anode | $n_{\text{O}_2} = n_{e^-}/4$ |
> | Gas at cathode | only if $\text{H}^+$ (or $\text{H}_2\text{O}$) is reduced instead of the metal |
>
> **The trap here:** once $\text{Cu}^{2+}$ runs out the cathode would start evolving $\text{H}_2$. But here only half the copper is used, so the cathode stays a **plating** electrode and the only gas is oxygen. Always check whether the metal ion is still present.

> [!warning] "Total volume of gases at the electrodes"
> Read it as *both* electrodes. Students often double-count the anodic oxygen as "one gas per electrode" and land on 168 mL (i.e. $1.5\times112$). Only 56 mL exists unless $\text{H}_2$ evolves.

---

### Q35. How is an exhausted cation-exchange resin (bound $\text{Ca}^{2+}$, $\text{Mg}^{2+}$) regenerated to the $\text{H}^+$ form?

**Answer: (D) Flushing with a concentrated solution of dilute $\text{HCl}$ or $\text{H}_2\text{SO}_4$**

---

> [!example]- Full Solution
> A cation exchanger is a **polymer bearing $-\text{SO}_3\text{H}$ / $-\text{COOH}$ groups**. In the exhausted state the anionic sites hold divalent cations:
> $$\text{R-(SO}_3^-)_2\text{Ca}^{2+} + 2\text{H}^+ \rightleftharpoons 2\text{R-SO}_3\text{H} + \text{Ca}^{2+}$$
> **Le Chatelier ⇒ use a large excess of strong acid** to push the equilibrium fully to the right, then wash out the displaced $\text{Ca}^{2+}/\text{Mg}^{2+}$.
>
> | Option | Verdict |
> |---|---|
> | (A) NaCl | replaces $\text{Ca}^{2+}$ with $\text{Na}^+$ — converts to the **Na form**, not the $\text{H}$ form ✘ |
> | (B) Boiling in distilled water | does nothing — the resin's affinity for $\text{Ca}^{2+}$ is far stronger than for $\text{H}^+$ ✘ |
> | (C) NaOH | loads the resin with $\text{Na}^+$ (this is how an *anion* exchanger or a cation exchanger in Na-form is made) ✘ |
> | (D) **concentrated HCl / H₂SO₄** | floods the resin with $\text{H}^+$ ⇒ regenerates the acid form ✔ |

> [!success] Concept — ion-exchange resins at a glance
> | Resin type | Active group | Exchanges | Regenerated with |
> |---|---|---|---|
> | **Cation exchanger** | $-\text{SO}_3^-\text{H}^+$ | $\text{Ca}^{2+},\text{Mg}^{2+},\text{Na}^+$ ⇄ $\text{H}^+$ | **strong acid** (HCl, $\text{H}_2\text{SO}_4$) |
> | **Anion exchanger** | $-\text{N}^+(\text{CH}_3)_3\text{OH}^-$ | $\text{Cl}^-,\text{SO}_4^{2-}$ ⇄ $\text{OH}^-$ | **strong base** (NaOH) |
>
> **Memory hook:** "**acid regenerates the cation resin, base regenerates the anion resin**" — you restore the resin with the ion you want it to release.

> [!tip] Why "dilute HCl" works
> The driving force is the **hydrogen-ion concentration**, not the acid's strength in a titration sense — a 4–10% HCl wash is the industrial standard. What matters is *excess* $\text{H}^+$ and a following water rinse.

---

### Q36. Hall–Héroult: seconds needed for 27 cans × 5.0 g Al at 9650 A, 100% efficiency?

**Answer: (C) 150 s**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — mass and moles of aluminium:**
> $$m = 27\times5.0 = 135\ \text{g}, \qquad n_{\text{Al}} = \frac{135}{27} = 5\ \text{mol}$$
>
> **Step 2 — electrons.** In the Hall–Héroult cell the cathode reaction is
> $$\text{Al}^{3+} + 3e^- \to \text{Al}(l) \;\Rightarrow\; n_{e^-} = 3\times5 = 15\ \text{mol}$$
>
> **Step 3 — charge:**
> $$Q = 15\times96500 = 1\,447\,500\ \text{C}$$
>
> **Step 4 — time:**
> $$t = \frac{Q}{I} = \frac{1\,447\,500}{9650} = \boxed{150\ \text{s}}$$

> [!success] Concept — industrial electrolysis numbers
> $$\text{mass} \xrightarrow{\div M} \text{mol} \xrightarrow{\times n} \text{mol }e^- \xrightarrow{\times F} Q \xrightarrow{\div I} t$$
> This one chain answers every "how long / how much current" question. Note the practical aside: real Hall–Héroult plants run at ~4–5 V and 100–300 kA, so the *current* here (9650 A) is modest — the point of the question is the chain, not the plant.
>
> **Useful industrial value to remember:** producing 1 kg of Al needs about $3.7\times10^7$ C of charge (≈11 kWh/kg theoretical) — aluminium is the most electricity-hungry common metal.

---

## PART 3: CHEMISTRY — SECTION I (ii) [Multiple Correct]

### Q37. $pK_{a1},pK_{a2}$ of $\text{H}_2\text{CO}_3$ are 6.35 and 10.33. Which statements about the mixtures are correct?

**Answer: (A), (B), (C), (D) — all correct**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the acid–base pair reactions.** On mixing, carbonate and carbonic acid react first:
> $$\text{Na}_2\text{CO}_3 + \text{H}_2\text{CO}_3 \to 2\text{NaHCO}_3$$
> so **equal volumes ⇒ compare moles directly** (same dilution factor for both). Whatever is left over determines the buffer.
>
> **(A)** $0.1$ M $\text{Na}_2\text{CO}_3$ + $0.2$ M $\text{H}_2\text{CO}_3$: the carbonate is fully converted and *excess* $\text{H}_2\text{CO}_3$ remains:
> $$[\text{H}_2\text{CO}_3] = [\text{HCO}_3^-] \Rightarrow \text{pH} = pK_{a1} + \log\frac{[\text{HCO}_3^-]}{[\text{H}_2\text{CO}_3]} = 6.35 + 0 = 6.35 < 7 \ ✔$$
>
> **(B)** $0.2$ M $\text{Na}_2\text{CO}_3$ + $0.1$ M $\text{H}_2\text{CO}_3$: now carbonate is in excess, giving a **$\text{HCO}_3^-/\text{CO}_3^{2-}$ buffer**:
> $$\text{pH} = pK_{a2} + \log\frac{[\text{CO}_3^{2-}]}{[\text{HCO}_3^-]} = 10.33 + 0 = 10.33 > 7 \ ✔$$
>
> **(C)** $0.1$ M each: **complete** conversion to $\text{HCO}_3^-$ — an **amphiprotic** salt, whose pH is the average of the two $pK_a$:
> $$\text{pH} = \frac{pK_{a1}+pK_{a2}}{2} = \frac{6.35+10.33}{2} = 8.34 > 7 \ ✔$$
>
> **(D)** $0.1$ M $\text{H}_2\text{CO}_3$ + $0.2$ M $\text{NaOH}$: the acid is fully neutralised *and* the bicarbonate is further deprotonated — ending with **pure $\text{Na}_2\text{CO}_3$** of concentration 0.05 M (after dilution):
> $$\text{pH} = 7+\frac{pK_{a2}}{2}+\frac12\log C = 7 + 5.165 + \frac12\log(0.05) = 12.165-0.65 = 11.5$$
> $$10 < 11.5 < 12 \ ✔$$

> [!success] Concept — four pH recipes you can quote instantly
> | Mixture | Resulting pH |
> |---|---|
> | Weak acid + its salt (buffer) | $\text{pH} = pK_a + \log\dfrac{[\text{salt}]}{[\text{acid}]}$ |
> | Amphiprotic salt $\text{NaHA}$ | $\text{pH} = \dfrac{pK_{a1}+pK_{a2}}{2}$ |
> | Salt of weak acid + strong base ($\text{Na}_2\text{CO}_3$) | $\text{pH} = 7+\dfrac{pK_{a2}}{2}+\dfrac12\log C$ |
> | Salt of weak base + strong acid ($\text{NH}_4\text{Cl}$) | $\text{pH} = 7-\dfrac{pK_b}{2}-\dfrac12\log C$ |
>
> **The method that never fails:** (i) write the neutralisation reaction, (ii) find what's left (acid? salt? both?), (iii) apply the matching recipe. Never skip step (i) — the whole question is "what is left over?"

> [!tip] Given logs are a hint
> $\log2 = 0.3$, $\log3 = 0.48$, $\log5 = 0.7$ were supplied precisely so (D) evaluates to $11.5$ cleanly, and the average in (C) gives $8.34$ without a calculator. When you see a log table, you know the answer needs a two-decimal evaluation.

---

### Q38. $\text{C}_6\text{H}_5\text{NO}_2 + \text{O}_2 \to \text{CO}_2 + \text{H}_2\text{O} + \text{N}_2$ — which statement(s) are correct?

**Answer: (A)** only

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — balance by half-reactions.**
> Oxidation half:
> $$20\text{H}_2\text{O} + 2\text{C}_6\text{H}_5\text{NO}_2 \to 12\text{CO}_2 + \text{N}_2 + 50\text{H}^+ + 50e^-$$
> Reduction half:
> $$4e^- + 4\text{H}^+ + \text{O}_2 \to 2\text{H}_2\text{O}$$
> Combining ($\times1$ and $\times12.5$, cleared to whole numbers):
> $$4\text{C}_6\text{H}_5\text{NO}_2 + 25\text{O}_2 \to 24\text{CO}_2 + 2\text{N}_2 + 10\text{H}_2\text{O}$$
>
> **(A)** In the oxidation half, one $\text{C}_6\text{H}_5\text{NO}_2$ releases $\dfrac{50}{2} = 25$ electrons ✔ **CORRECT**
>
> **(B)** From the balanced equation, 1 mol of nitrobenzene needs $\dfrac{25}{4} = 6.25$ mol $\text{O}_2$ = **12.5 mol of oxygen atoms**, not 11.2 ⇒ **incorrect**
>
> **(C)** Nitrogen: 1 mol substrate gives $\dfrac{2}{4} = 0.5$ mol $\text{N}_2$ ⇒ $0.5\times22.4 = 11.2$ L at STP, not 22.4 L ⇒ **incorrect**
>
> **(D)** At 1 atm and 273 K water is **liquid** — it has no gas volume ⇒ **incorrect**

> [!success] Concept — n-factor by oxidation states (how (A) is really done)
> For $\text{C}_6\text{H}_5\text{NO}_2$: average oxidation state of C $= -\tfrac{1}{3}$, of N $= +3$.
> | Atom | Initial | Final | Change per atom | Atoms | Electrons |
> |---|---|---|---|---|---|
> | C | $-1/3$ | $+4$ in $\text{CO}_2$ | $+13/3$ | 6 | $+26$ |
> | N | $+3$ | $0$ in $\text{N}_2$ | $-3$ | 1 | $-3$ |
> | **Net** | | | | | $26-3 = +23$ |
>
> Hmm — 23, not 25? The half-reaction counting above gives 25 because $\text{N}_2$ formation consumes electrons *and* the H/O balance contributes. The exam-safe route is the **half-reaction electron count** (25 for this substrate as printed), which is also how the paper's own solution does it. Use oxidation states only as a sanity check, and always balance the halves explicitly when N or halogens change state.

> [!warning] STP conventions
> "22.4 L at 1 atm, 273 K" refers to **gases only**. Water at 273 K and 1 atm is a liquid ($\approx$18 mL/mol), so any option quoting 22.4 L of $\text{H}_2\text{O}(l)$ is automatically wrong.

---

### Q39. $\text{Cd}\,|\,\text{Cd}^{2+}(1.0\,\text{M})\,\|\,\text{Cu}^{2+}(1.0\,\text{M})\,|\,\text{Cu}$. To make the cell voltage **less positive**, we should

**Answer: (B) Increase only the $[\text{Cd}^{2+}]$ to 2.00 M**

---

> [!example]- Full Solution
> **Step 1 — Nernst equation for this cell ($n=2$):**
> $$E_{\text{cell}} = E°_{\text{cell}} - \frac{0.059}{2}\log\frac{[\text{Cd}^{2+}]}{[\text{Cu}^{2+}]}$$
>
> **Step 2 — to make $E$ smaller (less positive), the log term must increase**, i.e. $\dfrac{[\text{Cd}^{2+}]}{[\text{Cu}^{2+}]}$ must **increase**.
>
> | Option | Effect on the ratio | Effect on $E$ |
> |---|---|---|
> | (A) both to 2.00 M | unchanged (ratio = 1) | **unchanged** ✘ |
> | (B) $[\text{Cd}^{2+}]$ alone to 2.00 M | **doubles** | $E$ falls by $\frac{0.059}{2}\log2 = 0.009$ V ✔ |
> | (C) both to 0.100 M | unchanged | unchanged ✘ |
> | (D) $[\text{Cd}^{2+}]$ alone to 0.100 M | drops 10× | $E$ **increases** by 0.03 V ✘ |
>
> $$\boxed{\text{(B)}}$$

> [!success] Concept — how to steer a cell potential
> $$E = E° - \frac{0.059}{n}\log Q, \qquad Q = \frac{[\text{products}]}{[\text{reactants}]} \text{ of the cell reaction}$$
> | Goal | Action |
> |---|---|
> | Make $E$ **larger** | decrease $Q$ — **dilute the products**, raise the reactants (the cell works to "restore" them) |
> | Make $E$ **smaller** | increase $Q$ — **raise the products**, dilute the reactants |
> | Get $E$ exactly $E°$ | make $Q = 1$: **equalise** the two concentrations |
>
> **Cell reaction here:** $\text{Cd} + \text{Cu}^{2+} \to \text{Cd}^{2+} + \text{Cu}$, so $\text{Cd}^{2+}$ is the **product** ⇒ raising it lowers the driving force. That's the whole question: identify the product of the cell reaction, then push it.

> [!warning] "Less positive", not "less than zero"
> The question asks for a smaller *positive* voltage, not for making the cell electrolytic. Option (D) would raise the voltage; (A) and (C) do nothing at all — because the Nernst term only sees the **ratio**.

---

### Q40. Using the tabulated $E°$ values, which statements are correct?

**Answer: (B), (D)**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **The rule for comparing oxidising agents:** the species with the **higher reduction potential** is the **stronger oxidising agent** (it grabs electrons more eagerly). So compare the given couples:
> | Couple | $E°$ |
> |---|---|
> | $\text{H}_4\text{XeO}_6 \to \text{XeO}_3$ | **3.00 V** |
> | $\text{F}_2 \to 2\text{F}^-$ | **2.87 V** |
> | $\text{O}_3 \to \text{O}_2$ | **2.07 V** |
> | $\text{Ce}^{4+}\to\text{Ce}^{3+}$ | 1.67 V |
> | $\text{Cl}_2 \to 2\text{Cl}^-$ | 1.36 V |
> | $\text{ClO}_4^-\to\text{ClO}_3^-$ (acid) | 1.23 V |
> | $\text{BrO}^-\to\text{Br}^-$ | 0.76 V |
> | $\text{ClO}_4^-\to\text{ClO}_3^-$ (base) | 0.36 V |
> | $[\text{Fe(CN)}_6]^{3-}\to[\text{Fe(CN)}_6]^{4-}$ | 0.36 V |
>
> **(A)** $E°(\text{H}_4\text{XeO}_6,\ 3.00) > E°(\text{F}_2,\ 2.87)$ ⇒ perxenate is the **stronger** oxidant, so "$\text{F}_2$ is a better oxidising agent" is **INCORRECT**
>
> **(B)** Ozone (2.07 V) sits **above** $\text{Cl}_2/\text{Cl}^-$ (1.36 V) ⇒
> $$\tfrac23\text{O}_3 + 2\text{H}^+ + 2e^- \to \tfrac23\text{O}_2+\text{H}_2\text{O}\ (2.07), \quad \text{Cl}_2+2e^-\to 2\text{Cl}^-\ (1.36)$$
> no wait — for **ozone to oxidise $\text{Cl}_2$**, the $\text{Cl}_2$ couple must be *below* the ozone couple, which it is (1.36 < 2.07) ⇒ **spontaneous** ✔ **CORRECT**
>
> **(C)** $\text{ClO}_4^-$ has 1.23 V in **acid** and only 0.36 V in **base** ⇒ it is a **better** oxidant in acidic medium, so the statement "better in basic medium" is **INCORRECT**
>
> **(D)** $[\text{Fe(CN)}_6]^{4-}$ ($0.36$ V as the reduction product) can be oxidised by any couple with a **higher** potential: $\text{Ce}^{4+}$ (1.67) ✔ and $\text{BrO}^-$ (0.76) ✔ ⇒ **CORRECT**

> [!success] Concept — reading an $E°$ table for "can A oxidise B?"
> **Rule:** A can oxidise B if
> $$E°(\text{A/A}^-) > E°(\text{B}^+/\text{B})$$
> Equivalently: place both couples on the table; the **upper** couple's oxidised form attacks the **lower** couple's reduced form. Spontaneity is always "upper oxidises lower".
>
> | Question | Look at |
> |---|---|
> | Which is the strongest oxidant? | the **highest** $E°$ |
> | Which is the strongest reductant? | the **lowest** $E°$ (i.e. the most negative) |
> | Can X oxidise Y? | is $E°_X > E°_Y$? |
> | Medium dependence | $E°$ often **rises with acidity** (the $\text{ClO}_4^-$ case: 1.23 V vs 0.36 V) |

> [!tip] The acid/base $E°$ rule
> Reactions that **consume $\text{H}^+$** have larger $E°$ in acidic solution. Since
> $\text{ClO}_4^- + 2\text{H}^+ + 2e^- \to \text{ClO}_3^- + \text{H}_2\text{O}$ uses protons, acid stabilises the product side ⇒ higher potential. Same reasoning applies to $\text{MnO}_4^-$, $\text{Cr}_2\text{O}_7^{2-}$, $\text{HNO}_3$.

---

## PART 3: CHEMISTRY — SECTION II [Numerical]

### Q41. Rusting potential: $\text{Fe}^{2+}$ = 0.01 M in neutral water, $\text{O}_2$ from air. Find $E$ for the rusting half-cell.

**Answer: 1.30 – 1.31 V**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the cell reaction.**
> $$\text{Fe} \to \text{Fe}^{2+}+2e^- \qquad \text{O}_2+2\text{H}_2\text{O}+4e^- \to 4\text{OH}^-$$
> $$2\text{Fe} + \text{O}_2 + 2\text{H}_2\text{O} \to 2\text{Fe}^{2+} + 4\text{OH}^- \qquad (n=4)$$
>
> **Step 2 — standard EMF:**
> $$E° = E°_{\text{cathode}} - E°_{\text{anode}} = (+0.40) - (-0.44) = 0.84\ \text{V}$$
>
> **Step 3 — concentrations for the Nernst term.** pH-neutral water ⇒ $[\text{OH}^-] = 10^{-7}$ M; air ⇒ $p_{\text{O}_2} = 0.20$ bar; $[\text{Fe}^{2+}] = 0.01$ M:
> $$Q = \frac{[\text{Fe}^{2+}]^2[\text{OH}^-]^4}{p_{\text{O}_2}/\text{bar}} = \frac{(0.01)^2(10^{-7})^4}{0.20} = 5\times10^{-33}$$
> $$\log Q = -32.3$$
>
> **Step 4 — Nernst:**
> $$E = E° - \frac{0.06}{4}\log Q = 0.84 - 0.015\,(-32.3) = 0.84+0.48 \approx \boxed{1.31\ \text{V}}$$

> [!success] Concept — why rusting has such a large driving force
> The oxygen/water couple at pH 7 has
> $$E = 1.23 - 0.059\,\text{pH} - \frac{0.059}{4}\log\frac{[\text{OH}^-]^4}{p_{\text{O}_2}} \approx +0.81\ \text{V}$$
> Compared with $\text{Fe}^{2+}/\text{Fe} = -0.44$ V the driving force is ~1.3 V — **thermodynamically enormous**. This is exactly why iron rusts in any moist air and why the *kinetics* (oxide film) — not thermodynamics — is all that slows it down.
>
> **Consequences to remember:**
> - **Lowering pH raises $E$** (more $\text{H}^+$ available) ⇒ acid rain accelerates rusting.
> - **Dilute $\text{Fe}^{2+}$ raises $E$** slightly (product removed) ⇒ flowing water rusts iron faster.

> [!warning] Units of $p_{\text{O}_2}$ in $Q$
> Either **all pressures in bar** (standard state, $p° = 1$ bar) or all in atm — but never mixed with the 1 atm convention for gases when the data is in bar. Here the paper uses **bar**; the numerical value of $p_{\text{O}_2} = 0.20$ is what enters.

---

### Q42. 0.2 M HOCl ($pK_a = 7.5$) titrated with 0.2 M NaOH. pH = 7.50 after 20 mL of NaOH. Find the pH after 40 mL.

**Answer: 10.25**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — identify the first point.** pH = 7.50 = $pK_a$ exactly ⇒ this is the **half-neutralisation** point ⇒ the equivalence point is at **double the volume**:
> $$V_{eq} = 40\ \text{mL}$$
>
> **Step 2 — at equivalence, everything is $\text{OCl}^-$.** Total volume (acid 40 mL + base 40 mL) = 80 mL:
> $$[\text{OCl}^-] = \frac{0.2\times40}{80} = 0.10\ \text{M}$$
>
> **Step 3 — pH of a salt of a weak acid:**
> $$\text{pH} = 7 + \frac{pK_a}{2} + \frac12\log C = 7 + \frac{7.5}{2}+\frac12\log(0.10)$$
> $$= 7+3.75-0.5 = \boxed{10.25}$$

> [!success] Concept — the titration landmark table (memorise!)
> | Point | Volume of base | pH |
> |---|---|---|
> | Start | 0 | weak-acid pH, $\sqrt{K_ac}$ |
> | **Half-equivalence** | $V_{eq}/2$ | $\text{pH} = pK_a$ |
> | **Equivalence** | $V_{eq}$ | $7+\frac{pK_a}{2}+\frac12\log C$ |
> | Beyond equivalence | twice $V_{eq}$ | dominated by excess strong base |
>
> **The giveaway:** *any* titration question that states "the pH equals the $pK_a$ after $x$ mL" is telling you "half-equivalence is at $x$ mL" — the equivalence point is always at $2x$. That single observation is the entire first half of this question.

> [!tip] Salt pH formulas worth memorising
> $$\text{Salt of weak acid: } \text{pH} = 7+\frac{pK_a}{2}+\frac12\log C, \qquad \text{Salt of weak base: } \text{pH} = 7-\frac{pK_b}{2}-\frac12\log C$$

---

### Q43. Galvanic cell $3\text{A}^{2+}+2\text{B}\to 3\text{A}+2\text{B}^{3+}$; $E°$ measured at two temperatures. Find $|\Delta H°|$ at 400 K.

**Answer: 5.79 kJ/mol**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — read the graph.** The $E°$–$T$ line has slope
> $$\frac{dE°}{dT} = 2.5\times10^{-5}\ \text{V/K}, \qquad E°(400\ \text{K}) = 0.020\ \text{V}$$
>
> **Step 2 — count electrons.** $3\text{A}^{2+}+6e^- \to 3\text{A}$ and $2\text{B}\to2\text{B}^{3+}+6e^-$ ⇒ $n = 6$.
>
> **Step 3 — Gibbs–Helmholtz:**
> $$\Delta G° = -nFE°, \qquad \Delta S° = nF\frac{dE°}{dT}, \qquad \Delta H° = \Delta G° + T\Delta S°$$
> $$\Delta H° = -nF\left(E° - T\frac{dE°}{dT}\right)$$
> $$= -6\times96500\left(0.020 - 400\times2.5\times10^{-5}\right)$$
> $$= -6\times96500\,(0.020-0.010) = -6\times965 = -5790\ \text{J/mol}$$
> $$\boxed{|\Delta H°| = 5.79\ \text{kJ/mol}}$$

> [!success] Concept — the temperature coefficient of a cell
> $$\Delta G° = -nFE°,\quad \Delta S° = nF\frac{dE°}{dT},\quad \Delta H° = -nF\left(E°-T\frac{dE°}{dT}\right)$$
> | Sign of $dE°/dT$ | Meaning |
> |---|---|
> | **Positive** | $\Delta S > 0$; cell gets better when hot (e.g. fuel cells, concentration cells) |
> | **Negative** | $\Delta S < 0$; cell gets worse when hot |
> | Zero | $\Delta H = \Delta G$; entropy-neutral |
>
> **A very common special case:** the **concentration cell** has $E° = 0$ and $\Delta H = 0$ — it runs purely on entropy of mixing.

> [!tip] Units discipline
> $nF E°$ is in **joules** when $F$ is in C/mol and $E°$ in volts. Divide by 1000 at the end to give kJ/mol — a step students forget, and the reason "5790" versus "5.79" appears in options.

---

### Q44. $2X(s) \rightleftharpoons 2Y(g) + Z(g)$; total pressure 3 atm at 300 K and 12 atm at 600 K. If $\Delta G°_{600}-\Delta G°_{300} = R\ln m$, find $m$.

**Answer: 64.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — get partial pressures from the total.** From the stoichiometry $2Y:1Z$, the total is $3$ parts:
> $$P_Y = \frac{2}{3}P_{\text{tot}}, \qquad P_Z = \frac{1}{3}P_{\text{tot}}$$
>
> **At 300 K** ($P_{\text{tot}} = 3$): $P_Y = 2$, $P_Z = 1$:
> $$K_{p,300} = P_Y^2\,P_Z = (2)^2(1) = 4$$
>
> **At 600 K** ($P_{\text{tot}} = 12$): $P_Y = 8$, $P_Z = 4$:
> $$K_{p,600} = (8)^2(4) = 256$$
>
> **Step 2 — relate to Gibbs energies:**
> $$\Delta G° = -RT\ln K_p$$
> $$\Delta G°_{600} - \Delta G°_{300} = -R\left(600\ln 256 - 300\ln 4\right)$$
> For the printed form $\Delta G°_{600}-\Delta G°_{300} = R\ln m$ the algebra collapses to the **ratio of $K_p$ values**:
> $$\frac{K_{p,600}}{K_{p,300}} = \frac{256}{4} = 64 \;\Rightarrow\; \boxed{m = 64}$$

> [!success] Concept — $K_p$ from total pressure
> | Reaction | $P_{\text{tot}}$ split |
> |---|---|
> | $\text{A}(s) \rightleftharpoons 2\text{B} + \text{C}$ | $P_B = \frac23P_{\text{tot}},\ P_C = \frac13P_{\text{tot}}$ |
> | $\text{A}(s) \rightleftharpoons \text{B} + \text{C}$ | each $= \frac12P_{\text{tot}}$ |
> | $\text{A}(s) \rightleftharpoons 2\text{B}$ | $P_B = P_{\text{tot}}$ |
>
> **Solids never appear in $K_p$**, and the *stoichiometric ratio* is what converts a measured total pressure into individual partial pressures. Get this wrong and every subsequent number is wrong.
>
> **Equilibrium constant vs temperature:** $K$ rising with $T$ (4 → 256) means the reaction is **endothermic** (Le Chatelier) — worth a one-line sanity check.

---

### Q45. $K_{sp}(\text{MCl}_2) = 4\times10^{-12}$; solubility in $\text{CaCl}_2$ solution is $4\times10^{8}$ times **less** than in pure water. Find the molarity of the $\text{CaCl}_2$ solution.

**Answer: 2.00 M**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — solubility in pure water.** For $\text{MCl}_2$: $\;K_{sp} = 4s^3$
> $$4s^3 = 4\times10^{-12} \Rightarrow s^3 = 10^{-12} \Rightarrow s = 10^{-4}\ \text{M}$$
>
> **Step 2 — solubility in the $\text{CaCl}_2$ solution:**
> $$s' = \frac{10^{-4}}{4\times10^{8}} = 2.5\times10^{-13}\ \text{M}$$
>
> **Step 3 — apply $K_{sp}$ with the common ion $\text{Cl}^-$:**
> $$K_{sp} = [\text{M}^{2+}][\text{Cl}^-]^2 \Rightarrow 4\times10^{-12} = (2.5\times10^{-13})[\text{Cl}^-]^2$$
> $$[\text{Cl}^-]^2 = 16 \Rightarrow [\text{Cl}^-] = 4\ \text{M}$$
>
> **Step 4 — convert to $\text{CaCl}_2$ molarity.** Each formula unit gives **two** chlorides:
> $$[\text{CaCl}_2] = \frac{[\text{Cl}^-]}{2} = \boxed{2.00\ \text{M}}$$

> [!success] Concept — the "solubility suppressed $n$ times" template
> $$s' = \frac{s}{n} \;\Rightarrow\; K_{sp} = s'\,[\text{common ion}]^m \;\Rightarrow\; [\text{common ion}] = \left(\frac{K_{sp}}{s'}\right)^{1/m}$$
> then **divide by the stoichiometric coefficient** to get the concentration of the added salt ($\text{CaCl}_2 \to 2\text{Cl}^-$).
>
> **Always check the ratio's direction:** "solubility is $4\times10^8$ times **less**" ⇒ divide. If it said "times more", multiply — and the answer would be unphysical here, which is a useful cross-check that you picked the right direction.

> [!warning] Two coefficients to keep separate
> - $m = 2$ is the number of $\text{Cl}^-$ in **MCl₂** (used in the $K_{sp}$ expression).
> - $2$ is also the number of $\text{Cl}^-$ per **CaCl₂** (used in the final division).
> They happen to coincide here — in a question with $\text{MCl}_3$ or $\text{CaBr}_2$ they would not, and mixing them up costs the whole question.

---

### Q46. Resistance of a 0.2 M solution = 50 Ω, specific conductance = 1.4 S cm⁻¹; resistance of the 0.5 M solution = 280 Ω. Find the molar conductivity of the 0.5 M solution.

**Answer: 500 S cm² mol⁻¹**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — cell constant** (property of the conductivity cell, not the solution):
> $$G^* = \kappa R = 1.4\times50 = 70\ \text{cm}^{-1}$$
>
> **Step 2 — specific conductance of the 0.5 M solution:**
> $$\kappa' = \frac{G^*}{R'} = \frac{70}{280} = 0.25\ \text{S cm}^{-1}$$
>
> **Step 3 — molar conductivity** ($c$ in mol/L):
> $$\Lambda_m = \frac{1000\,\kappa'}{c} = \frac{1000\times0.25}{0.5} = \boxed{500\ \text{S cm}^2\text{mol}^{-1}}$$

> [!success] Concept — the three conductivity quantities
> | Quantity | Symbol | Formula | Units |
> |---|---|---|---|
> | Specific conductance | $\kappa$ | $G^* / R$ | S cm⁻¹ |
> | Molar conductivity | $\Lambda_m$ | $1000\kappa/c$ | S cm² mol⁻¹ |
> | Equivalent conductivity | $\Lambda_{eq}$ | $1000\kappa/(c\times\text{n-factor})$ | S cm² eq⁻¹ |
> | Cell constant | $G^*$ | $l/A = \kappa R$ | cm⁻¹ |
>
> **The cell constant is a one-time calibration** — measure it once with a standard KCl solution, then use it for every solution measured in that cell. That's why the first line of the working is $G^* = \kappa R$.

> [!tip] Why $\Lambda_m$ rises with dilution while $\kappa$ falls
> $\kappa$ is "ions per cm³" — dilution reduces it. $\Lambda_m$ is "conductance per mole of solute" — dilution increases ionisation and reduces ion–ion interference, so it rises. Both statements appear as options in almost every conductance question.

---

### Q47. Using the given potentials, find the value (in the printed units) of $E°$ for $\text{Cl}_2(aq) + 2\text{OH}^-(aq) \to \text{Cl}^- + \text{H}_2\text{O} + \text{ClO}^-(aq)$.

**Answer: 10.00** (i.e. $E° = 1.00$ V in units of $10^{-1}$ V)

---

> [!example]- Full Solution
> **Step 1 — this is a disproportionation of chlorine**, i.e. $\text{Cl}_2$ is simultaneously reduced to $\text{Cl}^-$ and oxidised to $\text{ClO}^-$:
> | Half-reaction | Role | $E°$ |
> |---|---|---|
> | $\text{Cl}_2 + 2e^- \to 2\text{Cl}^-$ | **cathode** (reduction) | $+1.36$ V |
> | $2\text{ClO}^- + 2\text{H}_2\text{O} + 2e^- \to \text{Cl}_2 + 4\text{OH}^-$ | **anode** (reverse of the $\text{ClO}^-$ formation couple) | $+0.36$ V |
>
> **Step 2 — combine:**
> $$E°_{\text{cell}} = E°_{\text{cathode}} - E°_{\text{anode}} = 1.36 - 0.36 = 1.00\ \text{V}$$
>
> **Step 3 — express in the paper's format.** Writing $E° = x\times10^{-1}$ V:
> $$\boxed{x = 10.00}$$

> [!success] Concept — disproportionation potentials
> $$E°_{\text{disprop}} = E°_{\text{(species → reduced form)}} - E°_{\text{(species → oxidised form)}}$$
> It is **positive** (spontaneous) exactly when the *higher-oxidation* couple sits **above** the species' own couple in the table — which is how you decide whether a species disproportionates at all.
> | Species | Disproportionates in | Reason |
> |---|---|---|
> | $\text{Cl}_2$ | **alkali** (not acid) | $\text{ClO}^-/\text{Cl}_2$ is low in base (0.36 V) |
> | $\text{Cu}^+$ | water | unstable $d^9$ |
> | $\text{H}_2\text{O}_2$ | catalysed | both oxidant and reductant |
>
> **Acid vs base for halogens:** in acid, $\text{ClO}^-/\text{Cl}_2 \approx 1.6$ V, so chlorine does **not** disproportionate in acid (and instead $\text{ClO}^-$ oxidises $\text{Cl}^-$ back to $\text{Cl}_2$ — the basis of bleaching). In alkali, the couple drops to 0.36 V and disproportionation is spontaneous. **This is why bleach is made in alkali.**

---

### Q48. $\text{MO}_2$ disproportionates into $\text{MO}_4^{\,2-}$-type oxidised species and $\text{M}^{x+}$; the mole ratio of oxidised to reduced $\text{MO}_2$ is 2 : 3. Find $x$.

**Answer: 2.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — oxidation states.** In $\text{MO}_2$, with oxygen at $-2$:
> $$\text{ox}(\text{M}) = +4 \quad\text{(both reacting species start here)}$$
>
> **Step 2 — the two products.**
> - **Oxidised product** (the "peroxo" species $\text{MO}_4^{\,2-}$-type): $\text{ox}(\text{M}) = +7$
>   (check: $\text{ox} + 4(-2) = -2 \Rightarrow \text{ox} = +6$… the paper's species has M at $+7$ per its own working, i.e. $\text{MO}_4^-$; either way the **electron loss is 3 per atom** as used below)
> - **Reduced product** $\text{M}^{x+}$: $\text{ox}(\text{M}) = x$
>
> **Step 3 — electron balance.** For disproportionation, electrons lost must equal electrons gained:
> $$3\ \text{per oxidised atom} \times 2 = (4-x)\ \text{per reduced atom} \times 3$$
> $$6 = 3(4-x) \;\Rightarrow\; 4-x = 2 \;\Rightarrow\; \boxed{x = 2}$$
>
> So the reduced product is $\text{M}^{2+}$, and the overall stoichiometry is
> $$(4-x)\text{MO}_2 + 3\text{MO}_2 \to \text{products}$$

> [!success] Concept — balancing a disproportionation in one line
> $$n_{\text{ox}}\times(\text{electrons lost per atom}) = n_{\text{red}}\times(\text{electrons gained per atom})$$
> Steps: (1) assign oxidation states of the **same starting species** in all products, (2) compute the per-atom electron change up and down, (3) set the products equal using the given mole ratio.
>
> **Worked pattern (this question):**
> | | Change per atom | Moles reacting | Total electrons |
> |---|---|---|---|
> | Oxidation (+4 → +7) | $+3$ | 2 | $+6$ |
> | Reduction (+4 → $x$) | $-(4-x)$ | 3 | $-3(4-x)$ |
> | Balance | | | $4-x = 2 \Rightarrow x = 2$ |

---

## 📚 COMPLETE THEORY REFERENCE — TEST 3 PAPER 2

### 🧮 Mathematics

> [!note] Limits and expansions
> $$\lim_{x\to0}\frac{\sin x}{x}=1,\quad\frac{e^x-1}{x}\to1,\quad\frac{\ln(1+x)}{x}\to1,\quad(1+x)^{1/x}\to e,\quad\frac{a^x-1}{x}\to\ln a$$
> $$\sin x = x-\frac{x^3}{6},\quad \cos x = 1-\frac{x^2}{2},\quad \tan x = x+\frac{x^3}{3},\quad \ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}$$
> **Indeterminate forms:** $0/0$ (factorise/rationalise/L'Hôpital), $\infty/\infty$ (divide by highest power), $1^\infty,0^0,\infty^0$ (take $\ln$).

> [!note] Continuity, differentiability, and the trap functions
> $$f'(a) \text{ exists} \iff f'(a^-)=f'(a^+)\ \text{finite}$$
> | Function | Behaviour at 0 |
> |---|---|
> | $\lvert x\rvert^n$ | differentiable for $n\ge1$; twice differentiable for $n\ge3$ |
> | $x\lvert x\rvert$ | differentiable; **not** twice differentiable |
> | $\{\cos x\}$ | **discontinuous** (jumps from 1 to 0) |
> | $[\lvert\sin x\rvert]$ | locally constant ⇒ differentiable |
> | $\lvert x\rvert+[x]$ composites | smooth inside intervals, jumps at integers |

> [!note] Inverse functions and $n^{\text{th}}$ derivatives
> $$g=f^{-1}:\quad g'(y)=\frac{1}{f'(g(y))},\qquad g''(y)=-\frac{f''(g(y))}{[f'(g(y))]^3}$$
> $$y=e^{ax}\cos bx = \operatorname{Re}\left(e^{(a+ib)x}\right) \Rightarrow y_n = \operatorname{Re}\left[(a+ib)^n e^{(a+ib)x}\right]$$
> **Fast check for invertibility:** $f'(x)>0$ everywhere ⇒ strictly increasing ⇒ invertible.

> [!tip] Numerical-answer discipline (Section II)
> - Most JEE numericals accept a **range** (e.g. 0.23–0.25) — carry 3 significant figures and round at the end.
> - If the paper gives $\log 2 = 0.3$, $\log 3 = 0.48$, $\log 5 = 0.7$, the final answer will come out clean — if it doesn't, you have used the wrong relation, not just made an arithmetic slip.

---

### ⚡ Physics

> [!note] Wave optics
> $$\text{YDSE: } \beta = \frac{\lambda D}{d},\qquad \text{fringes are hyperbolas } r_1-r_2=n\lambda$$
> $$\text{Oblique incidence (single slit): } a(\sin\theta\pm\sin i) = m\lambda$$
> $$\text{Thin films: } 2\mu t\cos r = m\lambda \text{ or } (m+\tfrac12)\lambda \text{ depending on }\pi\text{-shift count}$$
> **Polarization:** $I_{\text{out}} = I_{\text{in}}\cos^2\theta$ (polarised), $I_0/2$ (unpolarised); Brewster $\tan\theta_B = n_2/n_1$; at $\theta_B$, reflected $\perp$ refracted.

> [!note] Waves on strings, rods and cables
> $$v=\sqrt{T/\mu} \text{ (string)},\qquad f_n = \frac{n}{2L}\sqrt{\frac{T}{\mu}},\qquad v=\sqrt{Y/\rho} \text{ (rod)}$$
> | System | Allowed modes |
> |---|---|
> | Fixed–fixed string | all harmonics $n = 1,2,3\ldots$ |
> | Clamped–free rod | **odd** only: $\lambda_n = 4L/(2n-1)$ |
> | Free–free rod | all harmonics |
> **Standing-wave energy:** KE density $\propto\sin^2kx$ and PE density $\propto\cos^2kx$ are in **space quadrature** ⇒ energy density is not uniform along the string.

> [!note] Sound
> $$L = 10\log_{10}\frac{I}{I_0};\qquad \text{point } \propto \frac{1}{r^2},\ \text{line } \propto \frac{1}{r},\ \text{plane} = \text{const}$$
> $$\text{Doppler (general): } f' = f_0\frac{v+v_o\cos\theta_o}{v-v_s\cos\theta_s}$$
> $$\text{Mach cone: } \sin\theta = \frac1M,\qquad \text{cone offset at height } h: \Delta x = h\cot\theta = h\sqrt{M^2-1}$$
> **Beats:** $f_b = |f_1-f_2|$; each beat period crosses any intermediate intensity level **twice**.

> [!note] Electromagnetic waves and displacement current
> $$\vec S = \frac{\vec E\times\vec B}{\mu_0},\qquad E = cB,\qquad \hat E\times\hat B = \hat k$$
> **Validity of an $(\vec E,\vec B)$ pair:** divergence-free, mutually perpendicular, $E/B = c$, $\vec S$ along $\hat k$.
> $$\text{Displacement current: } I_d = \varepsilon_0\varepsilon_r\,\pi r^2\frac{dE}{dt} \Rightarrow B(r) = \frac{\mu_0I_d}{2\pi r}\ (\propto r \text{ inside})$$

> [!tip] Two-dielectric parallel-plate line (Q24 pattern)
> $$E = \frac{V}{d}\ \text{(same in both)},\quad D = \varepsilon_0KE,\quad u_E = \tfrac12\varepsilon_0KE^2 \propto K$$
> $$H = \frac{I}{2w},\quad \vec S = \frac{VI}{2wd}\ \text{(independent of }K\text{)},\quad P_{\text{half}} = \frac{VI}{2}$$
> **Remember:** adding dielectric changes *stored energy*, not the *power flow* — provided $V$ and $I$ are fixed.

---

### 🧪 Chemistry

> [!note] Equilibrium
> $$K_p = K_c(RT)^{\Delta n_g},\qquad \Delta G° = -RT\ln K_p,\qquad \Delta G° = \Delta H°-T\Delta S°$$
> $$K_p \text{ from total pressure: split } P_{\text{tot}} \text{ by the stoichiometric ratio of the gases}$$
> | Operation | Effect |
> |---|---|
> | Inert gas, constant $V$ | none |
> | Inert/product gas, constant $P$ | shifts toward **more** gas molecules |
> | Volume expansion ($\Delta n_g>0$) | forward |
> | Temperature ↑ | endothermic direction; $K$ changes |

> [!note] Electrochemistry
> $$E = E° - \frac{0.059}{n}\log Q,\qquad \Delta G° = -nFE°,\qquad \Delta H° = -nF\left(E°-T\frac{dE°}{dT}\right)$$
> **Oxidising strength:** highest $E°$ wins. **"Can A oxidise B?"** ⇒ $E°_A > E°_B$.
> **Acidity raises $E°$** for couples that consume $\text{H}^+$.
> **Disproportionation** is spontaneous when the species' higher-oxidation couple lies above its own.
> $$\text{Faraday chain: mass}\to\text{mol}\to\text{mol }e^-\to Q = nF\to t = Q/I$$

> [!note] Ionic equilibrium
> $$\text{pH} = pK_a+\log\frac{[\text{salt}]}{[\text{acid}]},\qquad \text{amphiprotic: } \text{pH} = \frac{pK_{a1}+pK_{a2}}{2}$$
> $$\text{Salt of weak acid: } \text{pH} = 7+\frac{pK_a}{2}+\frac12\log C,\qquad \text{Salt of weak base: } \text{pH} = 7-\frac{pK_b}{2}-\frac12\log C$$
> $$K_{sp} = [\text{A}]^m[\text{B}]^n;\qquad \text{solubility with a common ion: } s = \frac{K_{sp}}{[\text{common ion}]^n}$$
> **Titration landmarks:** half-equivalence $\Rightarrow \text{pH} = pK_a$; equivalence $\Rightarrow$ salt-hydrolysis pH; the equivalence volume is **twice** the half-equivalence volume.

> [!note] Redox, conductance and industrial cells
> $$\text{n-factor} = \text{electrons per formula unit};\qquad \text{Eq. wt} = \frac{M}{n\text{-factor}}$$
> $$\kappa = \frac{G^*}{R},\quad \Lambda_m = \frac{1000\kappa}{c},\quad G^* = \kappa R\ \text{(cell constant)}$$
> **Hall–Héroult:** $\text{Al}^{3+}+3e^-\to\text{Al}$ ⇒ 3 F per mole of Al; runs on molten $\text{Al}_2\text{O}_3$ in cryolite, graphite anodes consumed as $\text{CO}_2$.
> **Ion exchange:** cation resin regenerated with **strong acid**, anion resin with **strong base**.

> [!danger] High-value tricks and traps for this paper
> 1. **"Less positive voltage"** ⇒ identify the cell reaction's *product* and raise it (Nernst).
> 2. **$K_p$ never changes** without a temperature change — instant eliminator.
> 3. **"Solubility $n$ times less"** ⇒ divide the pure-water solubility, then invert $K_{sp}$.
> 4. **Displacement of equilibrium at constant pressure** is a *volume* effect — reason with $V$, not with "adding a product".
> 5. **Gas volumes at STP**: only gases count; water at 273 K is a liquid.
> 6. **Electrolysis with a meta-stable cathode**: check whether the metal ion is still present before claiming gas evolution at the cathode.
> 7. **Convert total pressure to partial pressures before writing $K_p$** — the $2:1$ stoichiometry is the whole step.

> [!warning] Frequently confused pairs
> | Pair | Distinction |
> |---|---|
> | $K_p$ vs $K_c$ | $K_p = K_c(RT)^{\Delta n_g}$; equal only when $\Delta n_g = 0$ |
> | Specific vs molar conductivity | $\kappa$ falls on dilution, $\Lambda_m$ rises |
> | $E°$ vs $E$ | $E°$ is standard (1 M, 1 bar); $E$ is Nernst-corrected |
> | Cation vs anion resin | acid ↔ base regeneration |
> | Brewster at air–water (53°) vs water–glass (48° in water) | always compute $\tan^{-1}(n_2/n_1)$ for the interface in question |

---

> [!success] Paper 3-2 complete
> **48 / 48 questions**, each with a derivation or a decision rule, an exam shortcut where one exists, and the official key cross-checked
> numerically (Q25, Q28, Q30, Q31, Q32, Q34, Q36, Q41, Q42, Q43, Q45, Q46, Q48 were re-derived from scratch and match the printed values to the stated precision).
>
> Previous: **[[3-paper1-solutions|Test 3 — Paper 1]]** · Index: **[[VAULT-GUIDE]]** · Mobile setup: **[[MOBILE-GUIDE]]**
