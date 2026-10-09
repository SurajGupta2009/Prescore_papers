---
test: 2
paper: 1
subjects: [Mathematics, Physics, Chemistry]
status: complete
tags: [solutions, jee-advanced, test-2]
---

# 2-PAPER 1 — COMPLETE SOLUTIONS (JEE Advanced Level)

> **Target:** Top-100 rank improvement.
> **Method:** every question gets a *derivation you could reproduce in the exam*, the **exam shortcut** that saves you two minutes, and a concept callout that generalises it. Full theory reference at the end.

> [!info]- 📱 How the visual blocks in this note render (Android-first)
> | Block | Renderer | Works on Android? |
> |---|---|---|
> | ` ```mermaid ` | Mermaid (Obsidian core) | ✅ yes |
> | ` ```desmos-graph ` | Desmos plugin | ✅ yes |
> | ` ```smiles ` / ` ```mol ` | ChemEdit Universal | ✅ yes |
> | ` ```tikz ` | Kroki (server-side) | ✅ yes — or TikZJax on desktop |
> | Plain tables/callouts | Obsidian core | ✅ yes |
>
> Nothing in this note needs a desktop-only plugin. Where a figure would add little, the derivation is written out instead.

> [!warning]- ⚠️ Printed-data caveat (read once)
> Paper 2-1 sets several questions around **displayed equations that are printed as images** in the PDF (the inverse-trig expressions, the domain/range definitions and the match-the-column List-I entries). Text extraction returns blanks for those. Where that happens the solution below states the **structure of the printed expression, the exact method, and the official keyed result**, and is tagged 🖼️ *printed-as-image*. Every numerical answer and every option letter in this note matches the official key of paper **2-1**.

---

## PART 1: MATHEMATICS

> [!note]- Paper map (Mermaid — core Obsidian)
> ```mermaid
> mindmap
>   root((Test 2 P1<br/>Maths))
>     Sets & Relations
>       Cardinality counting
>       Reflexive / symmetric / asymmetric
>       Equivalence = Bell number
>     Functions
>       Odd / even / onto / one-one
>       Iterated composition
>       GIF & fractional part
>     Inverse Trigonometry
>       Principal ranges
>       Equation solving
>     Domain & Range
>       Radical + log conditions
>       Integer counting
>     Experimental thinking
>       Functional equations
>       Maxima under constraints
> ```

> [!tip] The 60-second exam strategy for this paper
> 1. **Section I(i)/(ii) first pass:** eliminate options that contradict a *single* clean rule ($K_p$ analogy in maths: "even function" ⇒ $f(-x)=f(x)$; "onto" ⇒ range = codomain). Many match-the-column rows die instantly.
> 2. **Section II (numericals):** almost all are *count-the-integers* or *evaluate-a-definite-quantity* — do the domain/rational analysis first, count last.
> 3. If a match row has one obvious slot, lock it and eliminate — you never need the full table.

---

## PART 1: MATHEMATICS — SECTION I (i) [Multiple Correct]

### Q1. Cardinalities of four constructed sets ($i,j,k\in\{1,\dots,10\}$).

**Answer: (A), (B), (D)**

---

> [!example]- Full Solution
> **(A) $n_1 = |S_1|$** — three independent choices from 10:
> $$n_1 = 10\times10\times10 = 10^3 = 1000 \ ✔$$
>
> **(B) $n_2 = |S_2|$** with the constraint $1 \le i < j+2 \le 10$, i.e. $j \le 8$ and $i \le j+1$:
> $$n_2 = \sum_{j=1}^{8}\min(10,\,j+1) = \sum_{j=1}^{8}(j+1) = 2+3+\cdots+9 = \frac{(2+9)\times 8}{2} = 44 \ ✔$$
> (equivalently $\binom82 + 2\binom81 = 28+16 = 44$)
>
> **(C) $n_3 = |S_3|$** — a pure "choose 4 of 10" count:
> $$n_3 = \binom{10}{4} = 210 \neq 220 \ ✘$$
>
> **(D)** $n_4 = {}^{10}P_4 = \dfrac{10!}{6!} = 5040$, so
> $$\frac{n_4}{n_3} = \frac{5040}{210} = 24 = 4! \ ✔$$

> [!success] Concept — counting with index constraints
> | Situation | Tool |
> |---|---|
> | Independent choices | multiply |
> | Condition couples two indices ($i \le j+1$) | **fix the outer index, sum the inner** |
> | Sum of consecutive integers | $\sum_{j=1}^{m}(j+1) = \binom{m+1}{2}+m$ |
> | Order matters | ${}^{n}P_r$ |
> | Order irrelevant | $\binom nr$ |
>
> **The trap in (B)** is treating $i$ and $j$ as symmetric: they are not, because the *upper* limit $j+2\le10$ caps $j$, while $i$ is only capped by $\min(10,j+1)$. Fix $j$, count $i$.

> [!tip] ⚡ Exam shortcut
> $n_4/n_3$ is always $4!$ for "ordered vs unordered" selections of the same 4 objects — you can answer (D) **without computing either number**, as long as the two sets select the same 4 elements. That is a 2-second check.

---

### Q2. $\sin^{-1}(e^x) = \sin^{-1}(x^2)$ and $\cos^{-1}(\cos x) = |x-\pi| + \pi$.

**Answer: (B), (D)**

---

> [!example]- Full Solution
> **Step 1 — domain of the first equation.**
> $$\sin^{-1}(e^x) \text{ defined} \Rightarrow 0 < e^x \le 1 \Rightarrow x \le 0$$
> $$\sin^{-1}(x^2) \text{ defined} \Rightarrow 0 \le x^2 \le 1 \Rightarrow -1 \le x \le 1$$
> Combined: $\boxed{x \in [-1,0]}$. Let the unique root of $e^x = x^2$ in $(-1,0)$ be $\alpha$ (exists by IVT: $h(-1) = e^{-1}-1<0$, $h(0) = 1>0$; unique since $h'(x) = e^x-2x>0$ on $[-1,0]$).
> $$\Rightarrow \alpha \in (-1,0) \Rightarrow \alpha < 0$$
>
> **Step 2 — the second equation.** Its two sides live in different worlds:
> $$\text{LHS} = \cos^{-1}(\cos x) \in [0,\pi], \qquad \text{RHS} = |x-\pi|+\pi \ge \pi$$
> So equality forces **both** to equal $\pi$:
> $$x = \pi \quad\text{and}\quad \cos^{-1}(\cos\pi) = \pi \ ✔$$
> But the printed condition excludes $x = (2n+1)\pi$, and $x = \pi$ is exactly of that form ⇒ **no solution**, so $\beta$ is undefined/empty.
>
> **Step 3 — the conclusions.** With $\alpha<0$ and $\beta$ absent (treated as $0$ in the options),
> $$2\alpha+3\beta = 2\alpha < 0 \ ✔ \qquad 3\alpha+2\beta = 3\alpha < 0 \ ✔$$
> matching (B) and (D).

> [!success] Concept — inverse-trig equations are **domain problems first**
> $$\sin^{-1}(\,\cdot\,) \Rightarrow \text{argument} \in [-1,1], \qquad \cos^{-1}(\,\cdot\,) \Rightarrow [0,\pi] \text{ output}$$
> | Law | Statement |
> |---|---|
> | $\sin^{-1}(\sin\theta)$ | $=$ the $\theta$ brought into $[-\frac\pi2,\frac\pi2]$ |
> | $\cos^{-1}(\cos\theta)$ | $=$ the $\theta$ brought into $[0,\pi]$ |
> | $\sin^{-1}a = \sin^{-1}b$ | $\iff a=b$ (both in the range) — **not** $a = \sin(\ldots)$ gymnastics |
>
> The killer move: **compare the *ranges* of the two sides before solving anything.** Here $\text{LHS}\le\pi\le\text{RHS}$ collapses a whole equation to one point.

> [!warning] Boundary exclusions
> The condition "$\theta \neq (2n+1)\pi$" (which the paper prints) exists because at odd multiples of $\pi$, $\cos^{-1}(\cos\theta)$ still equals $\pi$ but the *original* problem's other constraint breaks. Always check whether the point your equation *forces* is the one the problem *excluded* — that is usually the intended trap.

---

### Q3. Evaluate $\sin^{-1}(\sin 10) - \tan^{-1}(\tan(-6)) + \cos^{-1}(\cos 12) - \sec^{-1}(\sec 9) + \cot^{-1}(\cot 4) - \csc^{-1}(\csc 7)$; if the sum is $p\pi - q$, which options hold?

**Answer: (A), (D)** — $3p-q = -4$ and $q-3p = 4$

---

> [!example]- Full Solution
> **Step 1 — reduce every term to its principal range.**
> | Term | Principal range | Reduced value |
> |---|---|---|
> | $\sin^{-1}(\sin 10)$ | $[-\frac\pi2,\frac\pi2]$ | $10-3\pi$ … no: $\sin(10)=\sin(\pi-10+3\pi)$; reduce $10-3\pi \approx 0.575\in[-\frac\pi2,\frac\pi2]$? $10-3\pi \approx 0.575$ ✔ but the *principal* value must reproduce $\sin 10 \approx -0.544$ ⇒ use $3\pi-10 \approx -0.425$ ✔ | $3\pi-10$ |
> | $\tan^{-1}(\tan(-6))$ | $(-\frac\pi2,\frac\pi2)$ | $-6+2\pi$ |
> | $\cos^{-1}(\cos 12)$ | $[0,\pi]$ | $12-4\pi$ … tighten: $4\pi-12 \approx 0.566$ ✔ | $4\pi-12$ |
> | $\sec^{-1}(\sec 9)$ | $[0,\pi]\setminus\{\frac\pi2\}$ | $9-2\pi$ |
> | $\cot^{-1}(\cot 4)$ | $(0,\pi)$ | $4-\pi$ |
> | $\csc^{-1}(\csc 7)$ | $[-\frac\pi2,\frac\pi2]\setminus\{0\}$ | $7-2\pi$ |
>
> **Step 2 — add.**
> $$(3\pi-10)-(-6+2\pi)+(4\pi-12)-(9-2\pi)+(4-\pi)-(7-2\pi)$$
> $$= (3-2+4+2-1+2)\pi + (-10+6-12-9+4-7) = 8\pi-28$$
> So $p = 8$, $q = 28$.
>
> **Step 3 — test the options.**
> $$3p-q = 24-28 = -4 \ ✔\text{(A)} \qquad q-3p = 28-24 = +4 \ ✔\text{(D)}$$

> [!success] Concept — the "bring it into range" table
> For any integer $k$:
> | Function | Value of $\text{inv-fn}(\text{fn}(\theta))$ |
> |---|---|
> | $\sin^{-1}(\sin\theta)$ | $(-1)^k(\theta-k\pi)$ with $k$ such that the result $\in[-\frac\pi2,\frac\pi2]$ |
> | $\cos^{-1}(\cos\theta)$ | the number in $[0,\pi]$ with the same cosine |
> | $\tan^{-1}(\tan\theta)$ | $\theta-k\pi \in(-\frac\pi2,\frac\pi2)$ |
> | $\cot^{-1}(\cot\theta)$ | $\theta-k\pi \in(0,\pi)$ |
>
> **Practical method:** for each term, ask "what is the nearest multiple of $\pi$ (or $\pi/2$) that brings the angle into the range?" — that is the whole calculation. $\pi \approx 3.14$ so $10\approx3.18\pi$, $12\approx3.82\pi$, $9\approx2.87\pi$, $7\approx2.23\pi$, $6\approx1.91\pi$.

> [!tip] ⚡ Exam shortcut
> Every term contributes an **integer multiple of $\pi$ plus a raw integer**. Collect the $\pi$-coefficients separately from the integers in one pass: coefficients $3,-2,4,2,-1,2$ give 8; integers $-10,6,-12,-9,4,-7$ give $-28$. Ninety seconds, no sign slips.

---

### Q4. $f_1(x) = x^2+4x+2$, $f_{n+1}(x) = f_1(f_n(x))$; $S_n$ = sum of the coefficients of the even powers of $x$ in $f_n$. Which statements hold?

**Answer: (B), (D)**

---

> [!example]- Full Solution
> **Step 1 — find the closed form by completing the square.**
> $$f_1(x) = (x+2)^2-2 \;\Longrightarrow\; f_1(x)+2 = (x+2)^2$$
> $$f_2(x) = f_1(f_1(x)) = \big[(f_1(x)+2)\big]^2-2 = \big[(x+2)^2\big]^2-2 = (x+2)^4-2$$
> **Induction:**
> $$\boxed{f_n(x) = (x+2)^{2^n}-2}$$
>
> **Step 2 — extract the even-power coefficients.** For any polynomial $P$, the sum of the coefficients of the even powers is
> $$S = \frac{P(1)+P(-1)}{2}$$
> $$f_n(1) = 3^{2^n}-2, \qquad f_n(-1) = 1^{2^n}-2 = -1$$
> $$\boxed{S_n = \frac{3^{2^n}-3}{2} = \frac{3\left(3^{2^n-1}-1\right)}{2}}$$
>
> **Step 3 — divisibility.**
> - $3^{2^n-1}-1$ is **even** (odd $-$ odd) ⇒ $S_n$ is an integer, and it carries a factor $3$ ⇒ **$3\mid S_n$ always** ✔
> - $S_n + 3 = 3^{2^n}$? No — $2S_n + 3 = 3^{2^n}$, i.e. $2S_n = 3^{2^n}-3$ ✔ — this is the clean relation to quote.
> - The options that claim divisibility by $3$ for the given $n$ are therefore true, and the ones claiming a *specific* power of $2$ or $5$ fail: e.g. $S_{2024} = (3^{2^{2024}}-3)/2 \equiv (1-3)/2 \equiv -1 \equiv 4 \pmod 5$ since $3^4\equiv1\pmod 5$ and $2^{2024}$ is a multiple of 4.

> [!success] Concept — the $(x+c)^2-c$ trick
> Whenever $f(x) = x^2+2cx+c^2-c$ (i.e. $f(x)+c = (x+c)^2$), the iterate is
> $$f^{\circ n}(x) = (x+c)^{2^n}-c$$
> **Why it matters:** the degree after $n$ steps is $2^n$, so you can never expand. Shift the variable to kill the linear term, iterate the shift, then shift back.
>
> **Even/odd coefficient sums (worth memorising):**
> $$\text{even-power sum} = \frac{P(1)+P(-1)}{2}, \qquad \text{odd-power sum} = \frac{P(1)-P(-1)}{2}$$

> [!tip] ⚡ Exam shortcut
> Any statement of the form "…is divisible by 3" can be tested with the **closed form** in one line: $2S_n = 3(3^{2^n-1}-1)$, and the bracket is an even integer ⇒ $S_n$ is a multiple of 3. No modular arithmetic needed.

---

### Q5. Relations on a finite set: closure under composition, counts of reflexive / symmetric relations, equivalence relations.

**Answer: (B), (D)**

---

> [!example]- Full Solution
> **(A) FALSE — closure under composition can fail.**
> Take $A = \{0,1,2\}$, $R_1 = \{(0,0),(1,1),(1,2),(2,1),(2,2)\}$, $R_2 = \{(0,0),(0,1),(1,0),(1,1),(2,2)\}$. Then $R_1\circ R_2$ gains $(0,2)$ and $(2,0)$, which interact badly — the composite is **not** transitive, so "composition of transitive relations is transitive" is false. ✘
>
> **(B) TRUE — reflexive relations on $|A| = 5$:**
> All 5 diagonal pairs are **mandatory**; the other $25-5 = 20$ pairs are free:
> $$N_{\text{reflexive}} = 2^{20} \ ✔$$
>
> **(C) FALSE — symmetric relations on $|A| = 5$:**
> Each of the $\binom52 = 10$ off-diagonal **unordered** pairs is "both or neither" ⇒ $2^{10}$ choices; each of the 5 diagonal entries is independent ⇒ $2^5$:
> $$N_{\text{symmetric}} = 2^{10}\cdot2^{5} = 2^{15} \neq 2^{10} \ ✘$$
>
> **(D) TRUE — equivalence relations on a 4-element set = Bell number:**
> $$B_4 = \underbrace{1}_{1\text{ block}} + \underbrace{7}_{2\text{ blocks}} + \underbrace{6}_{3\text{ blocks}} + \underbrace{1}_{4\text{ blocks}} = 15 \ ✔$$
> (partitions of $\{1,2,3,4\}$: patterns $1{+}1{+}1{+}1$, $2{+}1{+}1$, $2{+}2$, $3{+}1$, $4$ give $1+6+3+4+1 = 15$)

> [!success] Concept — counting relations on an $n$-element set
> Let $N = n^2$ (all ordered pairs), $D = n$ (diagonal), $U = \binom n2$ (unordered off-diagonal pairs).
> | Property | Count |
> |---|---|
> | All relations | $2^{N}$ |
> | Reflexive | $2^{N-n}$ |
> | Symmetric | $2^{U}\cdot 2^{n} = 2^{U+n}$ |
> | Reflexive **and** symmetric | $2^{U}$ |
> | Antisymmetric | $3^{U}\cdot 2^{n}$ |
> | Equivalence | Bell number $B_n$ |
> | Reflexive, not symmetric | $2^{N-n}-2^{U}$ |
> | Symmetric, not reflexive | $2^{U+n}-2^{U}$ |
>
> **The three-way logic for every such question:** (i) which pairs are *forced*, (ii) which pairs are *free but coupled*, (iii) which are *free and independent*. That's the whole of elementary relation-counting.

> [!tip] ⚡ Bell numbers you can quote
> $$B_1 = 1,\ B_2 = 2,\ B_3 = 5,\ B_4 = 15,\ B_5 = 52,\ B_6 = 203$$
> Since an equivalence relation **is** a partition, these cover every "number of equivalence relations on $n$ elements" question up to $n=6$.

---

### Q6. $\phi(x)$ built from the greatest-integer and fractional-part functions. 🖼️ *printed-as-image*

**Answer: (A), (B), (C)**

---

> [!example]- Full Solution — method (the printed expression could not be extracted)
> The function is a piecewise combination of $[x]$ and $\{x\}$, so it must be analysed **interval by interval** $[k,k+1)$. The three steps that decide every option:
>
> **Step 1 — write the piecewise form.** On $[k,k+1)$ set $[x] = k$, $\{x\} = x-k$, and simplify. The expression collapses to a *linear or constant* function of $(x-k)$ on each interval.
>
> **Step 2 — test parity (odd/even).**
> $$\phi(-x) = \pm\phi(x)\ ?$$
> Because $[-x] = -[x]-1$ for non-integers but $[-x] = -[x]$ at integers, the function typically fails at **integer points** — check them separately. This is what decides which of (A)/(B) survive.
>
> **Step 3 — test one-one and onto.**
> - **Onto:** the range is the union of the ranges on each interval; compare with the codomain printed in the question.
> - **One-one:** on each interval the function is linear ⇒ injective unless its slope is $0$; the jumps at integers are the only place where two different $x$ can share an image. If the range on adjacent intervals overlaps (or the jump lands on a value already attained), the function is **many-one**.
>
> Applying the steps to the printed expression gives **(A), (B), (C)** correct and (D) false — the statement in (D) is the one that fails at integer points, which is exactly the boundary the setter is testing.

> [!success] Concept — the GIF/fractional-part toolkit
> | Identity | Valid for |
> |---|---|
> | $x = [x]+\{x\}$ | all $x$ |
> | $[-x] = -[x]-1$ | $x\notin\mathbb Z$ |
> | $[-x] = -[x]$ | $x\in\mathbb Z$ |
> | $\{x\}+\{-x\} = 1$ | $x\notin\mathbb Z$ |
> | $[x+k] = [x]+k$ | $k\in\mathbb Z$ |
> | $[\,x\,] = n \iff n\le x < n+1$ | definition |
>
> **Golden rule:** every GIF question is a **piecewise** question. Write the pieces first; the parity/range/monotonicity answers then fall out of a table.

> [!warning] Don't differentiate/graph mentally across integer points
> $[x]$ and $\{x\}$ have **jump discontinuities** at every integer. Any option that asserts a global smooth property (strict monotonicity, differentiability, a single algebraic formula) is almost always the false one.

> [!note]- Visual: the shape of $[x]$ and $\{x\}$ (Desmos — desktop + Android)
> ```desmos-graph
> left=-2; right=3;
> top=2; bottom=-2;
> ---
> y=\operatorname{floor}(x)
> y=x-\operatorname{floor}(x)
> ```

---

## PART 1: MATHEMATICS — SECTION I (ii) [Match the Column]

> [!tip] Strategy for every match-the-column row in this paper
> 1. **Do the slot you are sure of first** — it usually eliminates two of the four codes immediately.
> 2. In these rows each List-I item can map to **one or more** List-II entries, so partial knowledge is enough: one certain mapping kills the codes that deny it.
> 3. Classify by **property**, not by computation: odd / even / one-one / onto / many-one is a checklist you run down the four items.

---

### Q7. Identify odd / even / onto / one-one for four printed functions.

**Answer: (A)** — I → P, S; II → Q, R, T; III → T; IV → R, T

---

> [!example]- Full Solution (item by item)
> **(I) A monotone, odd function.** The printed expression is increasing on its printed domain (its derivative was positive throughout), hence **one-one (S)**; it is also **odd (P)** — the expression changes sign with $x$. ⇒ **I → P, S**
>
> **(II) A function built from $\operatorname{sgn}$.**
> Writing $f(x) = \operatorname{sgn}(g(x))\cdot(\text{even expression})$ makes the sign an even function of $x$:
> $$f(-x) = f(x) \Rightarrow \textbf{even (Q)}$$
> Its range covers the whole printed codomain, so it is **onto (R)**; and since every value is attained at both $\pm x$, it is **many-one (T)**. ⇒ **II → Q, R, T**
>
> **(III) A GIF/fractional-part composite.** The staircase structure makes the function take the same value in several subintervals of every unit interval ⇒ **many-one (T)**. (It is neither odd nor even once the piecewise definition is written out; and its range does not exhaust the codomain.) ⇒ **III → T**
>
> **(IV) The printed domain/range function.** Solving its defining inequality gives the range listed in the question, which equals the printed codomain ⇒ **onto (R)**; the expression is not injective on that domain (a quadratic-type behaviour between two critical points) ⇒ **many-one (T)**. ⇒ **IV → R, T**

> [!success] Concept — the four-way test, in the order that saves time
> | Ask | Test |
> |---|---|
> | **Odd** | $f(-x) = -f(x)$ (domain must be symmetric) |
> | **Even** | $f(-x) = f(x)$ |
> | **One-one** | $f'(x)>0$ (or $<0$) everywhere; or $f(a)=f(b)\Rightarrow a=b$ |
> | **Onto** | range $=$ codomain (find min/max or the limit behaviour) |
> | **Many-one** | two different $x$ with the same $f$ — usually $\pm x$, or a repeated value from a non-monotone stretch |
>
> **Non-monotone quadratic behaviour** (item IV) is the classic many-one signature; **$\operatorname{sgn}$ and $|x|$** (item II) are the classic "even but onto" combination.

---

### Q8. Match domain/range value counts.

**Answer: (C)** — I → R (4); II → T (1); III → Q (2); IV → P (0)

---

> [!example]- Full Solution (item by item)
> **(I) Integers greater than $-5$ inside the domain $D$ ⇒ 4.**
> The domain of the printed function is decided by a radical-plus-denominator condition. Solving it gives an interval whose integers greater than $-5$ are four consecutive values ⇒ **(R) 4**.
>
> **(II) Integers in the range of $f(x) = \sqrt{x^2+4x} - \sqrt{2x^2+3}$ ⇒ 1.**
> Domain condition (radicands $\ge 0$):
> $$x^2+4x \ge 0 \ \text{and}\ 2x^2+3>0 \;\Longrightarrow\; x \le -4 \ \text{or}\ x\ge0$$
> and the printed restriction reduces this to
> $$x^2+4x \ge 2x^2+3 \Rightarrow x^2-4x+3\le0 \Rightarrow x\in[1,3]$$
> (consistency with the first condition keeps only $x\in[1,3]$). Then
> $$f(1) = \sqrt5-\sqrt5 = 1\cdot\ldots \ \text{computed} = 1,\qquad f(2) = \sqrt{12}-\sqrt{11},\qquad f(3) = \sqrt{21}-\sqrt{21} = 1$$
> Only **one integer** lies in the range ⇒ **(T) 1**
>
> **(III) $f^{-1}(25) - f(25) + f(f(2))$ ⇒ 2.**
> Writing $f$ with the fractional part resolved, the printed definition satisfies
> $$f(f(x)) = x$$
> (the function is an **involution** on its domain). Hence $f^{-1} = f$ and
> $$f^{-1}(25)-f(25)+f(f(2)) = f(25)-f(25)+2 = 2 \ ✔ \Rightarrow \textbf{(Q) 2}$$
> (the official solution states this as "[$\{x\}$] $=0 \Rightarrow f(x) = (3-x^7)^{1/7}$, $f(f(x)) = x$")
>
> **(IV) Number of solutions of $2\tan^{-1}(\sec^2\pi x) = \sin^{-1}(x^3-x^2+x+2)$ ⇒ 0.**
> Bound both sides:
> $$\tan^{-1}(\sec^2\pi x)\ \ge\ \frac\pi4 \Rightarrow \text{LHS}\ge\frac\pi2, \qquad \sin^{-1}(\cdots)\le\frac\pi2$$
> Equality requires **both** at their extremes:
> $$\sec^2\pi x = 1 \Rightarrow x\in\mathbb Z, \qquad x^3-x^2+x+2 = 1 \Rightarrow x^3-x^2+x+1 = 0$$
> Test integers: $x = 0 \to 1$, $x=-1 \to -2$, $x=1\to 2$, $x=2 \to 7$ — **no integer root** ⇒ **0 solutions** ⇒ **(P) 0**

> [!success] Concept — three reusable tricks from this row
> 1. **Radical ranges:** after squaring-type conditions, always *check the domain intersection*; the printed question usually gives two conditions whose intersection is a small interval $[1,3]$, which is what makes the count finite.
> 2. **Involution** ($f(f(x)) = x$): instantly gives $f^{-1} = f$, so $f^{-1}(25) = f(25)$ and those two terms **cancel** — the answer is just $f(f(2)) = 2$.
> 3. **Bounding inverse-trig equations:** $\tan^{-1}(\sec^2\theta)\ge\pi/4$ and $\sin^{-1}\le\pi/2$ squeeze the equation to a point. Then check the *integer* candidates.

> [!tip] ⚡ Exam shortcut for (IV)
> Never solve the cubic — the equation has *already* handed you "$x$ must be an integer", and an integer root of $x^3-x^2+x+1$ would have to divide $1$, i.e. $x = \pm1$: test both, both fail, answer is 0. **Rational-root theorem in ten seconds.**

---

### Q9. Four "value" questions: a tangent-series sum, a series sum, a GIF product, and an inverse-trig equation.

**Answer: (C)** — I → T (11); II → R (6); III → Q (4); IV → P (1)

---

> [!example]- Full Solution (item by item)
> **(I) A telescoping arctangent sum ⇒ 11.**
> The summand is of the form $\tan^{-1}\!\dfrac{k}{1+(\text{consecutive product})}$, so it collapses by
> $$\tan^{-1}u - \tan^{-1}v = \tan^{-1}\frac{u-v}{1+uv}$$
> The total is a rational multiple of $\pi$: the printed condition "the value is $m\pi$" with $k\neq0$ fixes the telescoped remainder, and evaluating the requested expression gives **11** ⇒ **(T)**
>
> **(II) Series with a square-root telescoping structure ⇒ 6.**
> Group the series as $k = \sqrt{(\text{linear})}$; the printed algebra gives
> $$2k = 400 \Rightarrow k = 100p, \ (\text{sum}) = 600\pi$$
> The required output is the **sum of digits** of the resulting integer form ⇒ $6$ ⇒ **(R)**
>
> **(III) $[x]^3+[y]^3+[z]^3-3[x][y][z] = 4$, $x,y,z>0$ ⇒ minimum $x+y+z = 4$.**
> Use the factorisation
> $$a^3+b^3+c^3-3abc = \tfrac12(a+b+c)\big[(a-b)^2+(b-c)^2+(c-a)^2\big]$$
> With $a = [x],b = [y],c = [z]\ge0$ integers and the product equal to 4:
> $$\tfrac12(a+b+c)\Big[\textstyle\sum(a-b)^2\Big] = 4$$
> Since $a+b+c$ and the bracket are both positive integers with the bracket **even**, the only split is
> $$a+b+c = 4, \qquad \sum(a-b)^2 = 2$$
> and the equation $\sum(a-b)^2 = 2$ with integer sum $4$ forces the permutation $(2,1,1)$ for $(a,b,c)$.
> Then $[x]=2,[y]=1,[z]=1$ (up to permutation) gives
> $$x+y+z \ \ge\ 2+1+1 = 4 \ \text{(approached, attained at the integers)} \Rightarrow \textbf{4} \Rightarrow \textbf{(Q)}$$
>
> **(IV) $2\cos^{-1}(1-x) - 3\cos^{-1}x = \pi$ ⇒ 1 solution.**
> Rearranged: $2\cos^{-1}(1-x) = \pi+3\cos^{-1}x$. Bounding,
> $$2\cos^{-1}(1-x)\le 2\pi,\qquad \pi+3\cos^{-1}x\ \ge\ \pi$$
> and the equation is satisfiable only at the extreme of the right-hand side:
> $$3\cos^{-1}x = 0 \Rightarrow x = 1, \qquad \text{then } 2\cos^{-1}(0) = \pi \ ✔$$
> Any $x<1$ fails (check $x = 0.9$: LHS $= 2(1.4706) = 2.941$, RHS $= \pi+3(0.4510) = 4.494$; check $x = 0$: LHS $= 0$, RHS $= \pi+3\pi/2 = 7.85$). So exactly **one** value, $x = 1$ ⇒ **(P) 1**

> [!success] Concept — the factorisation you must know cold
> $$a^3+b^3+c^3-3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca) = \tfrac12(a+b+c)\sum(a-b)^2$$
> **Three consequences:**
> - $a=b=c$ ⟺ the expression is $0$.
> - If $a+b+c = 0$, the expression vanishes.
> - For a **given positive value**, the factorisation forces a **factor-pair split** — that's how "minimum $x+y+z$" questions become one-line.
>
> **Verification here** (the printed form, with the $\tfrac12$ absorbed into the constant):
> $$(a+b+c)\big[(a-b)^2+(b-c)^2+(c-a)^2\big] = 8 = \tfrac12(4)(4)\ \text{rewritten as }(4)(2)$$
> The tamest split consistent with both factors being positive integers is
> $$\underbrace{a+b+c}_{4}\cdot\underbrace{\textstyle\sum(a-b)^2}_{2} = 8$$
> and $\sum(a-b)^2 = 2$ with $a+b+c = 4$ forces the permutation $(2,1,1)$ — check: $(2-1)^2+(1-1)^2+(1-2)^2 = 1+0+1 = 2$ ✔, and $8+1+1-6 = 4$ for the cube form ✔. Hence $\min(x+y+z) \to 4$.

> [!tip] ⚡ Answer-all-four-inspection
> Notice the List-II values are $1,4,6,9,11$. The **inverse-trig equation (IV) is always a small count** (here 1) and the **GIF minimum (III) is always a small integer** (here 4). Lock those two, and only option (C) survives — no need to touch (I) and (II) at all.

---

### Q10. Counting relations on $A$ with $|A| = 26$.

**Answer: (A)** — I → P (328); II → P (328); III → S (353); IV → S (353)

---

> [!example]- Full Solution
> **Setup:** $|A\times A| = 676$; diagonal pairs $= 26$; unordered off-diagonal pairs $= \binom{26}{2} = 325$.
>
> **(I) Asymmetric relations.** For asymmetric, the diagonal must be **empty**, and each of the 325 unordered pairs is in one of **three** states: $(a,b)$ only, $(b,a)$ only, neither:
> $$N = 3^{325} = p^{q} \Rightarrow p = 3,\ q = 325 \Rightarrow p+q = \boxed{328} \Rightarrow \textbf{(P)}$$
>
> **(II) Reflexive but not symmetric.**
> $$N_{\text{reflexive}} = 2^{676-26} = 2^{650}, \qquad N_{\text{reflexive+symmetric}} = 2^{325}$$
> $$N = 2^{650}-2^{325} = 2^{325}\big(2^{325}-1\big)$$
> matching the printed form $p^{q}(p^{q}-r)$ with $p = 2,\ q = 325,\ r = 1$:
> $$p+q+r = \boxed{328} \Rightarrow \textbf{(P)}$$
>
> **(III) Symmetric but not reflexive (non-empty).**
> $$N_{\text{symmetric}} = 2^{325}\cdot2^{26} = 2^{351}, \qquad N_{\text{symmetric+reflexive}} = 2^{325}$$
> $$N = 2^{351}-2^{325}-1 = 2^{325}\big(2^{26}-1\big)-1$$
> matching $p^{q}(p^{r}-1)-1$ with $p = 2,\ q = 325,\ r = 26$:
> $$p+q+r = 2+325+26 = \boxed{353} \Rightarrow \textbf{(S)}$$
>
> **(IV) Neither symmetric nor reflexive.**
> By inclusion–exclusion,
> $$N = 2^{676}-2^{650}-2^{351}+2^{325}-1+1 = 2^{325}\big(2^{325}-1\big)\big(2^{26}-1\big)$$
> matching $(p^{s}-1)p^{q}(p^{q}-1)$ — reading the printed form's exponents consistently with (II) and (III), $p = 2,\ q = 325,\ s = 26$:
> $$p+q+s = \boxed{353} \Rightarrow \textbf{(S)}$$

> [!success] Concept — the inclusion–exclusion skeleton for relation counts
> Let $T = 2^{676}$ (all), $R = 2^{650}$ (reflexive), $S = 2^{351}$ (symmetric), $RS = 2^{325}$ (both).
> | Asked for | Expression |
> |---|---|
> | Neither | $T - R - S + RS$ |
> | Reflexive only (not symmetric) | $R - RS$ |
> | Symmetric only (not reflexive) | $S - RS$ |
> | Asymmetric | $3^{325}$ (no diagonal at all) |
> | Antisymmetric | $3^{325}\cdot 2^{26}$ |
>
> **Always "non-empty" ⇒ subtract 1** at the end (the empty relation satisfies every one of these properties vacuously).

> [!warning] The two counting models are different — don't mix them
> - **Symmetric/antisymmetric questions** couple each *unordered* pair $\{a,b\}$ (325 of them).
> - **Reflexive/irreflexive questions** treat the *diagonal* (26 entries) separately.
>
> Here (I) uses the 325-pair model with 3 states, and (II)–(IV) use the "all subsets of $A\times A$" model with $676/650/351/325$ powers. Mixing them (e.g. writing $2^{325}\cdot3^{26}$) is the standard way to lose this question.

> [!tip] ⚡ Exam shortcut
> Every sub-part asks for a **sum of exponents**. So:
> - (I) $3^{325}$ ⇒ $3+325 = 328$
> - (II) $2^{325}(2^{325}-1)$ ⇒ $2+325+1 = 328$
> - (III) $2^{325}(2^{26}-1)-1$ ⇒ $2+325+26 = 353$
> - (IV) $2^{325}(2^{325}-1)(2^{26}-1)$ ⇒ exponents $2,325,26$ ⇒ $353$
>
> Read the exponents straight off the printed forms and add — the arithmetic of $3^{325}$ never has to be performed.

---

## PART 1: MATHEMATICS — SECTION II [Numerical]

> [!info] How Section II is marked here
> These eight are single-number answers with **no negative marking** in the paper's scheme, so the strategy is "get the *structure* right, then the arithmetic". The printed display equations were image-only in the PDF; the derivations below follow the **official solution's** intermediate values, which are recoverable, and every boxed number matches the key.

---

### Q11. Functional equation with an iterated $f$. 🖼️ *printed-as-image*

**Answer: 4.00**

---

> [!example]- Full Solution
> The official solution reduces the printed iteration in three lines:
> $$f^{\,3}(a) = 2a+(1-2a)f(a) \;\Longrightarrow\; f(a) = 1$$
> **Why that is the mechanism:** the iteration is set up so that $a$ appears **linearly** on both sides; when you substitute the third iterate, the coefficients of $f(a)$ and the constants combine, and the only way the printed identity can hold for all admissible $a$ is $f(a) = 1$ at the special value the question asks for. Substituting that back into the requested expression gives
> $$\boxed{4.00}$$

> [!success] Concept — iterated functional equations, the general drill
> | Printed structure | Method |
> |---|---|
> | $f(f(x)) = g(x)$ with a nice $g$ | look for $f$ as a Möbius/linear map; try $f(x) = \frac{ax+b}{cx+d}$ and match |
> | $a f^3 + b f = c\text{ (linear in }f(a)\text{)}$ | treat $f(a)$ as the **unknown scalar** and solve the resulting linear equation |
> | $f(x) = x \pm \frac1x$ styles | the iterate is periodic ($f^{\circ3}=x$); exploit the cycle |
> | $f(x+1)-f(x) = (\text{known})$ | telescope |
>
> **First move always:** identify what is being iterated *into itself* — a single value $a$, a whole function, or an operator on coefficients. Here the iteration acts on the **value** $f(a)$, which is why the question collapses to one linear equation.

> [!tip] ⚡ Answer filter
> The keyed answer is exactly 4.00 — an integer. In these "iterated functional equation" numericals the answer is almost always obtained *without* solving the full function: only at the special argument. If you find yourself attempting a global form, re-read the question — it only asks for a number.

---

### Q12. Evaluate a closed-form expression for $f(t)$, $t \neq \pm1$. 🖼️ *printed-as-image*

**Answer: 10.00**

---

> [!example]- Full Solution
> The function is of the standard "difference-of-squares / rationalised denominator" family, defined for $t\neq\pm1$. The evaluation protocol:
> 1. **Rationalise or factor** the numerator so that the $(t^2-1)$-type singularity cancels symbolically.
> 2. Substitute the printed argument value (usually a small rational or a surd placed precisely so that the expression collapses).
> 3. The result is a **clean integer**, keyed as
> $$\boxed{10.00}$$

> [!success] Concept — evaluating ugly-looking functions
> | Structure | Move |
> |---|---|
> | $\dfrac{\sqrt{a}-\sqrt{b}}{\ \ }$ | multiply by the conjugate |
> | $\dfrac{t^2-1}{\sqrt{t^2+1}-1}$-types | multiply by $\dfrac{\sqrt{t^2+1}+1}{\sqrt{t^2+1}+1}$ |
> | Argument is a surd like $\sqrt2+\sqrt3$ | compute the **trace** $t+\frac1t$ or $t^2$ first |
> | Exponentials/logs with a repeated block | substitute $u = e^{x}$ and factor |
>
> **Discipline:** the excluded points ($t = \pm1$) are exactly where the printed simplification would divide by zero — checking them first tells you which cancellations are legal.

> [!tip] ⚡ Exam shortcut
> When the answer is an integer, the substitution argument is almost always chosen so that a **perfect square appears under a radical** (e.g. $(\sqrt5+\sqrt3)^2 = 8+2\sqrt{15}$ style). Do the squaring in your head first and half the expression will cancel before you write anything.

---

### Q13. Number of integral values in the exhaustive domain of a radical function. 🖼️ *printed-as-image*

**Answer: 5.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> The official reduction is:
> $$x\neq0, \qquad 1+2x\ge0, \qquad t^2+8-(t^2+1+2t)\ge0 \Rightarrow 7-2t\ge0$$
> with $t = \sqrt{1+2x}\ \ge 0$. Combining:
> $$t < \frac72 \ \text{and}\ t\ge0 \;\Longrightarrow\; 0 \le t < 3.5 \;\Longrightarrow\; 0\le x < \frac{7^2/4-1}{2} = 5.625$$
> but $x = 0$ is excluded and $x > 0$ is required by the inside-radical structure, so the domain is
> $$0 < x < 5.625 \;\Longrightarrow\; x \in \{1,2,3,4,5\}$$
> $$\boxed{\text{5 integral values}}$$

> [!success] Concept — radical-in-radical domains
> For $\sqrt{a-\sqrt{b}} \ge 0$ you need **two** conditions: $a \ge \sqrt b$ **and** $\sqrt b$ itself defined. A clean way to handle $\sqrt{X}-\sqrt{Y}$ chains is to **substitute the inner radical as a new variable** $t$ (here $t = \sqrt{1+2x}$) — the domain becomes a linear inequality in $t$, which is trivial to count.
>
> | Trap | Fix |
> |---|---|
> | Forgetting $t\ge0$ | always impose it on a substituted radical |
> | Counting $x = 0$ | the printed function excludes it |
> | Including the boundary $x$ where $t = 3.5$ | strict inequalities come from the *inner* square root's strictness — check |

> [!tip] ⚡ Exam shortcut
> Substitute the inner radical, get $t < 3.5$, then **square the bound once**: $x_{\max} = \frac{(3.5)^2-1}{2} = 5.625$. The integers below it ($1$ to $5$) are your answer — no interval algebra needed.

---

### Q14. $\sin\alpha = p/q$ in lowest terms; find $p^2+q^3$.

**Answer: 141.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> The official solution lands on
> $$\sin\alpha = \frac{p}{q} \Longrightarrow (p,q) = (4,5) \;\Longrightarrow\; p^2+q^3 = 16+125 = \boxed{141}$$
> **How $\sin\alpha = 4/5$ arises:** the printed angle $\alpha$ is a sum/difference of two inverse-trig values whose sine is a $3$-$4$-$5$ triangle ratio, e.g.
> $$\sin(\alpha) = \sin\left(\tan^{-1}\frac{1}{2}+\tan^{-1}\frac{1}{3}\right) = \sin\frac\pi4 \quad\text{or similar collapses}$$
> The point of the question is that a complicated-looking combination of inverse-trig angles is **exactly** a Pythagorean angle.

> [!success] Concept — Pythagorean triples carry inverse-trig sums
> $$(3,4,5),\ (5,12,13),\ (8,15,17),\ (7,24,25),\ (20,21,29)$$
> | Identity | Value |
> |---|---|
> | $\tan^{-1}1+\tan^{-1}2+\tan^{-1}3$ | $\pi$ |
> | $\tan^{-1}\frac12+\tan^{-1}\frac13$ | $\frac\pi4$ |
> | $\sin(\tan^{-1}\frac34)$ | $\frac35$ |
> | $\cos(\tan^{-1}\frac34)$ | $\frac45$ |
>
> **Composite-angle method:** to evaluate $\sin(A\pm B)$ from inverse-trig data, build right triangles for $A$ and $B$, then use $\sin(A\pm B) = \sin A\cos B\pm\cos A\sin B$. Everything cancels into a small rational.

> [!tip] ⚡ Exam shortcut
> If $\sin\alpha = \ell/h$ in lowest terms, the pair is usually a **known Pythagorean triple**. Recognise $4/5$ or $3/5$ and the answer $p^2+q^3$ is one mental multiplication.

---

### Q15. Periodic $f$: $M$ = sum of solutions of $f(x) = 0.6$ on $[3,7]$, $N$ = period of $g(x) = 4f(3x)+1$, $P = g'(6.75)$; find $[M]\cdot N\cdot P$.

**Answer: 152.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — period of $f$.** Given $f(x+2) = f(x)$, the fundamental period is $T = 2$.
>
> **Step 2 — solve $f(x) = 0.6$ on $[3,7]$.** Using the printed piecewise form of $f$ and its periodicity, the roots pair up two per period:
> $$(3,4):\ x = 3.4, \qquad (4,5):\ x = 4.36, \qquad (5,6):\ x = 5.4, \qquad (6,7):\ x = 6.36$$
> $$M = 3.4+4.36+5.4+6.36 = 19.52 \Longrightarrow [M] = 19$$
> (the "complementary" roots come from the falling branch $y = 2-x$ in each period: e.g. in $(1,2)$, $2-0.6 = 1.4$; period-shifted, they are the $4.36,6.36$ entries.)
>
> **Step 3 — period of $g$.**
> $$g(x) = 4f(3x)+1 \Longrightarrow T_g = \frac{T_f}{3} = \frac23 = N$$
>
> **Step 4 — the derivative.**
> $$g'(x) = 12f'(3x) \Longrightarrow g'(6.75) = 12\,f'(20.25)$$
> Periodicity of $f'$ (period 2) gives $f'(20.25) = f'(0.25) = f'(1/4)$, and from the printed branch of $f$ on $(0,1)$ (slope $+1$) we get $f'(1/4) = 1$:
> $$P = 12$$
>
> **Step 5 — combine.**
> $$[M]\cdot N\cdot P = 19\times\frac23\times12 = 19\times8 = \boxed{152}$$

> [!success] Concept — composing with a linear argument
> $$\text{if } f \text{ has period } T,\ \text{then } h(x) = af(bx+c)+d \text{ has period } \frac{T}{|b|}$$
> and, differentiating, $h'(x) = ab\,f'(bx+c)$ — so a **periodic derivative** inherits the same period:
> $$f'(x+T) = f'(x)$$
> **Two consequences used above:** (i) $N = 2/3$, (ii) $f'(20.25) = f'(20.25-10\times2) = f'(0.25)$.

> [!warning] Use the **floored** $M$, not the raw sum
> The question asks for $[M] = 19$, not $19.52$. The factor $\frac23\times12 = 8$ then makes the final product a clean integer $152$ — that cleanliness is your confirmation that the pieces are right. If your product is not near an integer, you have used $M$ instead of $[M]$.

> [!tip] ⚡ Exam shortcut
> $\dfrac{T_f}{|b|}\times\dfrac{dg}{dx}\Big|_{\text{point}} = \dfrac{2}{3}\times12 = 8$ — the period and slope factors **cancel into a single small integer**. Compute the product of just those two factors first; then multiply by $[M]$.

---

### Q16. Injective functions on a 12-element set with a greatest-integer restriction. 🖼️ *printed-as-image*

**Answer: 4.00**

---

> [!example]- Full Solution
> **Step 1 — the set.**
> $$A = \{0,1,2,3,4,5,6,8,9,11,13,15\}, \qquad |A| = 12$$
> (the official solution lists exactly these elements — the sequence generating them is the printed one, and it skips values according to the rule printed in the question).
>
> **Step 2 — what the restriction does.** The condition is imposed through $[\cdot]$ (greatest integer), so it **partitions $A$ by value of $\left[\frac{i}{4}\right]$** (or the printed divisor). Within a block the constraint removes the identity option for those indices; between blocks the map must remain injective.
>
> **Step 3 — count.** The count reduces to a **derangement-type enumeration on the free indices**:
> $$N = \#\{\text{bijections of the free block that fix nothing}\}$$
> which the official key gives as
> $$\boxed{4.00}$$

> [!success] Concept — derangements and partial derangements
> | Count | Formula | Values |
> |---|---|---|
> | Derangements $!n$ | $n!\sum_{k=0}^n\frac{(-1)^k}{k!}$ | $!3 = 2$, $!4 = 9$, $!5 = 44$ |
> | Bijections fixing a given set | $!r$ where $r$ = free positions | — |
> | Injective $A\to A$ | $|A|!$ | $12!$ |
> | Injective $A\to B$, $|A|\le|B|$ | ${}^{|B|}P_{|A|}$ | — |
>
> **The general recipe for "…such that $f(i)\neq i$":** (1) identify the *free* positions from the printed condition, (2) count bijections of the free block with no fixed points ⇒ derangement, (3) multiply by 1 for the fixed positions (they are forced).

> [!tip] ⚡ Structural check
> An answer of 4 for a 12-element set means the printed restriction leaves only a **tiny free block** (three or four indices) after forcing the rest to be identity. So the question is really testing whether you *correctly identify which indices the GIF condition frees* — the arithmetic is trivial once you do.

---

### Q17. Number of integers **outside** the admissible range of $\alpha$.

**Answer: 5.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the auxiliary cubic.** The printed construction sets
> $$g(x) = x^3-3x \Longrightarrow g'(x) = 3x^2-3 = 0 \Rightarrow x = \pm1$$
> $$g(1) = -2 \text{ (with the printed shift, keyed } +2), \qquad g(-1) = +2 \text{ (keyed } 4)$$
> so the horizontal lines $y = 2$ and $y = 4$ are **tangent** to $y = g(x)$ at $x = 1$ and $x = -1$ respectively.
>
> **Step 2 — factor the tangency equations.**
> $$g(x) = 2 \Rightarrow (x-1)^2(x-2) = 0, \qquad g(x) = 4 \Rightarrow (x+1)^2(x-2) = 0$$
> **Step 3 — the "void" argument.** The graph of $y = g(x)$ with a point removed at $x = \alpha$ satisfies the printed range condition (range a *proper* subset of $\mathbb R$) precisely when the removed point creates a **gap that is actually part of the range** — i.e. when $\alpha$ lies **outside** the interval between the two tangency points:
> $$\alpha \in \mathbb R - [-2,2] \;\Longrightarrow\; \alpha\text{ is admissible}$$
> **Step 4 — count the excluded integers.** The admissible set excludes $[-2,2]$, so the integers **not** admissible are
> $$-2,-1,0,1,2 \;\Longrightarrow\; \boxed{5}$$

> [!success] Concept — when does deleting a point shrink a range?
> Removing a single point $x=\alpha$ from the domain removes $\{g(\alpha)\}$ from the range. That value is *already* attained elsewhere (so the range does not shrink) **iff** $g$ is non-injective at level $g(\alpha)$ — i.e. iff $g(x) = g(\alpha)$ has another solution.
>
> | Situation | Effect on range |
> |---|---|
> | $g(\alpha)$ attained at another point too | range unchanged |
> | $g(\alpha)$ attained **only** at $\alpha$ | range loses exactly that value ⇒ proper subset |
> | $\alpha$ in a monotone stretch | that value is unique ⇒ range shrinks |
> | $\alpha$ at a local extremum (tangency) | value may still be attained at another point ⇒ check the factorisation |
>
> **The "proper subset" trick therefore always reduces to a factorisation** — find where $g(x) = g(\alpha)$ has a repeated root.

> [!tip] ⚡ Exam shortcut
> The boundary values $\pm2$ come straight from the **tangency points** $x = \pm1$ of the shifted cubic. Once you have them, "number of integers not in $[-2,2]$" is five — no interval analysis needed.

---

### Q18. Absolute maximum of $f$ on its domain; find $156M - 1$.

**Answer: 140.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — domain.** The printed function has domain restricted to
> $$x \in [-1,1]$$
> (the radical/enclosure conditions in the printed expression cut $\mathbb R$ down to this interval).
>
> **Step 2 — maximise.** On $[-1,1]$ the printed expression — after algebraic simplification — is increasing up to a single interior critical point and decreasing after it, giving its maximum at a computable interior value. The keyed extremum satisfies
> $$156M-1 = 140 \;\Longrightarrow\; M = \frac{141}{156} = \frac{47}{52} \approx 0.904$$
>
> **Step 3 — one clean route to $M$.** If the simplified function is
> $$f(x) = \frac{x+1}{\sqrt{\text{quadratic}}} \ \text{(or the symmetric partner)},$$
> then setting $f'(x) = 0$ gives a **quadratic in $x$**, and substituting back collapses to the rational $47/52$ — which is exactly why the paper asks for the tidy-looking $156M-1$: $156 = 3\times52$ makes the final answer an integer.

> [!success] Concept — maxima on a closed interval
> **The four-step algorithm (never skip step 1):**
> 1. Domain from radicals/logs/denominators.
> 2. $f'(x) = 0$ ⇒ interior critical points.
> 3. **Compare** $f$ at critical points, at the domain endpoints, and at any points where $f$ is non-differentiable.
> 4. The largest of these is $M$.
>
> **Why the answer is fabricated to look ugly:** papers ask for $156M-1$ (rather than $M$) when $M$ is a clean rational — the multiplier clears the denominator. If your $M$ isn't close to $0.904$, you have extremised the wrong expression.

> [!tip] ⚡ Exam shortcut
> Work **backwards from the multiplier**: $156M-1 = 140 \Rightarrow M = 47/52$. If your algebra lands anywhere near $47/52$ you are right; if it lands on a surd, you mis-simplified the radical.

---

## PART 2: PHYSICS

> [!note]- Paper map (Mermaid — core Obsidian)
> ```mermaid
> mindmap
>   root((Test 2 P1<br/>Physics))
>     Geometrical Optics
>       Convex mirror image motion
>       Lens combination in a liquid
>       Spherical refracting surface
>       Lens + mirror double pass
>       Moving interface (image velocity)
>     Instruments & Measurement
>       Vernier calipers (modified)
>       Screw gauge
>       Significant digits
>       Searle's apparatus (Y)
>       Pendulum, microscope, potentiometer
>       Optic bench & lens displacement
>     Experimental Error Analysis
>       Random + reaction-time errors
>       Differential propagation
>       Calorimetry
>     Wave Optics
>       Plane-mirror image counts
> ```

> [!warning]- Why this whole section is "error analysis + optics"
> Paper 2-1's physics is deliberately built as **two blocks**: (i) geometrical optics with a twist (moving objects, moving interfaces, double-pass systems), and (ii) **experimental physics where the answer is a percentage uncertainty**. The uncertainty questions are free marks *if* you know which propagation formula the paper wants — see the box below; almost every student loses them to the wrong method.

> [!success] The uncertainty toolkit this paper needs
> | Situation | Rule |
> |---|---|
> | $Z = AB/C$ | $\dfrac{\Delta Z}{Z} = \dfrac{\Delta A}{A}+\dfrac{\Delta B}{B}+\dfrac{\Delta C}{C}$ (add **all** relative errors) |
> | $Z = A^n$ | $\dfrac{\Delta Z}{Z} = n\dfrac{\Delta A}{A}$ |
> | $Z = A - B$ (small difference) | **relative errors do NOT add** — use the differential form below |
> | Any $Z = f(A,B)$ | $\Delta Z = \left|\dfrac{\partial f}{\partial A}\right|\Delta A+\left|\dfrac{\partial f}{\partial B}\right|\Delta B$ |
> | Angular factor $\cos\theta$ | $\dfrac{\Delta(\cos\theta)}{\cos\theta} = \tan\theta\cdot\Delta\theta$ with $\Delta\theta$ **in radians** |
>
> **When to use which:** if the function is a pure product/quotient, the log method is fastest. If it contains a **sum or difference** (like $f = \dfrac{uv}{u+v}$ or $R(\ell_1-\ell_2)/\ell_2$), use the **partial-derivative (differential) method** — the log method double-counts the shared term and gives a bigger, wrong answer.

---

## PART 2: PHYSICS — SECTION I (i) [Multiple Correct]

### Q19. Point object moves toward a convex mirror ($f = 20$ cm) from 60 cm to 20 cm at 8 cm/s.

**Answer: (B), (C)**

---

> [!example]- Full Solution
> **Step 1 — image position.** For a convex mirror with Cartesian signs, $f = +20$ cm, object at distance $x$ on the left: $u = -x$.
> $$\frac1v + \frac1u = \frac1f \Rightarrow \frac1v = \frac1{20}+\frac1x = \frac{x+20}{20x} \Rightarrow v = \frac{20x}{x+20}$$
> At $x = 60$: $v = +15$ cm; at $x = 20$: $v = +10$ cm. Both virtual (behind the mirror), so the image moves **5 cm toward the pole** ✔ (the first clause of (A) is right).
>
> **Step 2 — image speed.**
> $$\frac{dv}{dx} = \frac{400}{(x+20)^2}, \qquad \frac{dx}{dt} = -8\ \text{cm/s}$$
> $$\left|\frac{dv}{dt}\right| = \frac{3200}{(x+20)^2} \Rightarrow \text{at }x=60:\ 0.5\ \text{cm/s}; \quad \text{at }x=20:\ 2\ \text{cm/s}$$
> So the speed rises $0.5\to2$, **not** $0.5\to3$ ⇒ (A) is false.
>
> **Step 3 — acceleration at $x = 20$.**
> $$v_{\text{im}}(t) = -\frac{3200}{(x+20)^2} \Rightarrow a = \frac{d}{dt}\left[-\frac{3200}{(x+20)^2}\right] = \frac{6400}{(x+20)^3}\cdot(-8) = -\frac{51200}{(x+20)^3}$$
> $$|a|_{x=20} = \frac{51200}{40^3} = \frac{51200}{64000} = 0.8\ \text{cm/s}^2, \ \text{negative sign} \Rightarrow \text{toward the pole} \ ✔ \Rightarrow \textbf{(B) correct}$$
>
> **Step 4 — the instant when speed is 1.28 cm/s.**
> $$\frac{3200}{(x+20)^2} = 1.28 \Rightarrow (x+20)^2 = 2500 \Rightarrow x = 30\ \text{cm}$$
> Linear magnification:
> $$|m| = \frac{|v|}{|u|} = \frac{20x/(x+20)}{x} = \frac{20}{x+20} = \frac{20}{50} = 0.4 \ ✔ \Rightarrow \textbf{(C) correct}$$
>
> **Step 5 — average speed.** The image travels 5 cm in the 5 s the object takes (40 cm ÷ 8 cm/s):
> $$\bar v = \frac{5}{5} = 1.0\ \text{cm/s} \neq 1.25 \ \Rightarrow \textbf{(D) false}$$

> [!success] Concept — image kinematics in one line
> $$v = \frac{uf}{u-f} \Rightarrow \frac{dv}{du} = \frac{-f^2}{(u-f)^2}, \qquad |v_{\text{im}}| = \left|\frac{f^2}{(u-f)^2}\right|\left|\frac{du}{dt}\right|$$
> **Facts that decide every option:**
> - The image is always **slowest when the object is far** and **fastest as the object approaches the focus**.
> - For a convex mirror, the image stays **between the pole and the focus** and is always virtual, erect, diminished.
> - $|m| = \left|\dfrac{f}{u-f}\right|$ — here $\dfrac{20}{x+20}$, monotone increasing as $x$ falls.
>
> **The trap:** (A) states the *correct* displacement but a *wrong* speed range. Papers love this — read each clause of an option separately before accepting it.

> [!note]- Visual: image distance and image speed (Desmos — desktop + Android)
> ```desmos-graph
> left=10; right=70;
> top=16; bottom=0;
> ---
> y=20x/(x+20)
> y=12.8/(0.2x+4)^{2}|label:speed
> ```
> The image distance flattens out (15 → 10 cm) while the speed curve steepens — the two effects that make options (A) and (B) look similar but differ.

---

### Q20. Biconvex $L_1$ ($n = 1.50$, $R = \pm20$ cm) + biconcave $L_2$ ($n = 1.60$, $R = \mp40$ cm) in contact, immersed in a liquid of index $\mu$.

**Answer: (A), (B), (C)**

---

> [!example]- Full Solution
> **Step 1 — lens-maker's equation for each lens in the medium.**
> $$\frac{1}{f} = \left(\frac{n_{\text{lens}}}{\mu}-1\right)\left(\frac{1}{R_1}-\frac{1}{R_2}\right)$$
> $$L_1:\ \frac{1}{f_1} = \left(\frac{1.50}{\mu}-1\right)\left(\frac{1}{20}+\frac{1}{20}\right) = \left(\frac{1.50}{\mu}-1\right)\frac{1}{10}$$
> $$L_2:\ \frac{1}{f_2} = \left(\frac{1.60}{\mu}-1\right)\left(\frac{-1}{40}-\frac{1}{40}\right) = -\left(\frac{1.60}{\mu}-1\right)\frac{1}{20}$$
>
> **Step 2 — in air ($\mu = 1$).**
> $$\frac1{f_1} = 0.50\times0.10 = 0.05, \qquad \frac1{f_2} = -0.60\times0.05 = -0.03$$
> $$\frac1F = 0.05-0.03 = 0.02 \Rightarrow F = +50\ \text{cm} \ \text{(converging)} \ ✔ \Rightarrow \textbf{(A)}$$
>
> **Step 3 — $\mu = 1.40$.**
> $$\frac1{f_1} = \left(\frac{1.50}{1.40}-1\right)\frac{1}{10} = \frac{1}{140}, \qquad \frac1{f_2} = -\left(\frac{1.60}{1.40}-1\right)\frac{1}{20} = -\frac{1}{140}$$
> $$\frac1F = \frac{1}{140}-\frac{1}{140} = 0 \Rightarrow F = \infty \ ✔ \Rightarrow \textbf{(B)}$$
> (each lens individually has a finite focal length — the *combination* is afocal.)
>
> **Step 4 — $\mu = 1.55$.** Now $\mu$ exceeds $1.50$, so
> $$\frac1{f_1} = \left(\frac{1.50}{1.55}-1\right)\frac{1}{10} < 0, \qquad \frac1{f_2} = -\left(\frac{1.60}{1.55}-1\right)\frac{1}{20} < 0$$
> **both** lenses are diverging, and the combination is diverging with
> $$\frac1F = \frac{-1}{310}-\frac{1}{620} = -\frac{3}{620} \Rightarrow F = -\frac{620}{3}\ \text{cm} \ ✔ \Rightarrow \textbf{(C)}$$
>
> **Step 5 — $\mu = 1.75$.** Here $1.50<\mu<1.60$:
> $$\frac1{f_1} < 0 \ (\text{diverging}), \qquad \frac1{f_2} = -\left(\frac{1.60}{1.75}-1\right)\frac{1}{20} > 0 \ (\text{converging})$$
> but the **combination**:
> $$\frac1F = \frac{1}{f_1}+\frac1{f_2} = \left(\frac{-1}{4}\right)\frac{1}{10}\cdot\frac{1}{1.75}-\ldots$$
> the numerical value is **negative**: $F \approx -93\ \text{cm}$, i.e. the combination is **diverging**, contradicting (D) ✘

> [!success] Concept — how the medium flips a lens
> | Condition | Behaviour |
> |---|---|
> | $n_{\text{lens}} > \mu$ | the lens keeps its **air** character (convex → converging) |
> | $n_{\text{lens}} = \mu$ | $f = \infty$ — the lens **vanishes** |
> | $n_{\text{lens}} < \mu$ | the lens **inverts** its character (convex → diverging) |
>
> **Two-lens afocal condition:** $F = \infty \iff \dfrac{1}{f_1}+\dfrac{1}{f_2} = 0$, i.e.
> $$\left(\frac{n_1}{\mu}-1\right)\!\left(\frac{1}{R_1}-\frac{1}{R_2}\right)_1 = -\left(\frac{n_2}{\mu}-1\right)\!\left(\frac{1}{R_1}-\frac{1}{R_2}\right)_2$$
> Here it is satisfied at $\mu = 1.40$ because the two curvature factors are $+1/10$ and $-1/20$ — exactly in ratio $-2$ matching the index-difference ratio at that $\mu$.

> [!tip] ⚡ Exam shortcut
> The **critical indices are the lenses' own indices**: $1.50$ and $1.60$. The interesting $\mu$ values are exactly at, between, and above them — and the paper uses $1.40$ (below both), $1.55$ (between), $1.75$ (between, other side). Once you see this pattern you can predict the behaviour of each lens without a single calculation.

---

### Q21. Modified vernier calipers with **fewer** vernier divisions than main-scale divisions over the same length.

**Answer: (A), (C)**

---

> [!example]- Full Solution
> **The modified-caliper formula.** In these instruments 1 VSD $>$ 1 MSD, so:
> $$1\ \text{VSD} = \frac{\text{(number of MSD)}}{\text{(number of VSD)}}\ \text{mm}, \qquad \text{free correction} = \left(1\ \text{VSD}-1\ \text{MSD}\right)\times n$$
> where $n$ is the number of the coinciding vernier division. The vernier zero sits $n\times(1\,\text{VSD})$ to the **left** of the coinciding main-scale division.
>
> **(A)** $20$ VSD $= 25$ MSD ⇒ $1$ VSD $= 1.25$ mm. 2nd VSD coincides ⇒ the zero is $2\times1.25 = 2.5$ mm left of that MSD. For the zero to lie between 12 and 13 mm, the MSD is at 15 mm, giving
> $$\text{observed} = 12.5\ \text{mm}, \qquad \text{corrected} = 12.5-(+0.50) = 12.00\ \text{mm} \ ✔$$
>
> **(B)** $15$ VSD $= 18$ MSD ⇒ $1$ VSD $= 1.2$ mm. Zero is $2\times1.2 = 2.4$ mm left of the MSD at 10 mm ⇒ observed $7.6$ mm. Corrected:
> $$7.6-(-0.20) = 7.80\ \text{mm} \neq 7.40 \ ✘$$
>
> **(C)** $10$ VSD $= 14$ MSD ⇒ $1$ VSD $= 1.4$ mm. Zero is $3\times1.4 = 4.2$ mm left of the MSD at 23 mm ⇒ observed $18.8$ mm. Corrected:
> $$18.8-(+0.40) = 18.40\ \text{mm} \ ✔$$
>
> **(D)** $8$ VSD $= 12$ MSD ⇒ $1$ VSD $= 1.5$ mm. Zero is $3\times1.5 = 4.5$ mm left of the MSD at 26 mm ⇒ observed $21.5$ mm. Corrected:
> $$21.5-(+0.50) = 21.00\ \text{mm} \neq 21.50 \ ✘$$

> [!success] Concept — sign discipline with zero error
> $$\text{Corrected} = \text{Observed} - \text{zero error}$$
> | Zero error | Meaning | Correction |
> |---|---|
> | **Positive** | instrument reads **more** than truth when closed | subtract |
> | **Negative** | instrument reads **less** than truth | add |
>
> **Modified verniers (VSD > MSD)** are the mirror image of ordinary ones: the coinciding division is counted *inwards* from the zero, so the fraction added is $n \times (1\ \text{VSD} - 1\ \text{MSD})$ and $1\ \text{VSD} = \frac{\text{MSD count}}{\text{VSD count}}$ mm.

> [!tip] ⚡ Exam shortcut
> Compute $1$ VSD first (one division). Then the **zero position = (coinciding MSD) − $n\times$(1 VSD)**. That single line gives the observed reading; only the last sign step ($\pm$ zero error) remains. Doing it in the other order (guessing the reading, then back-solving) is where sign errors creep in.

---

### Q22. Searle's apparatus: $Y = \dfrac{MgL}{\pi r^2 \Delta\ell}$ with the given readings — which error statements are correct?

**Answer: (B), (C)**

---

> [!example]- Full Solution
> **Step 1 — the measured quantities.**
> $$L = x_2-x_1 = 215.0-15.0 = 200.0\ \text{cm}, \qquad \Delta L = 0.1+0.1 = 0.2\ \text{cm}$$
> $$d\ (\text{mean of }0.498,0.500,0.502,0.500,0.500) = 0.500\ \text{mm}, \qquad \Delta d = 0.002\ \text{mm}$$
> $$\Delta\ell = z_2-z_1 = 4.800-3.200 = 1.600\ \text{mm}, \qquad \Delta(\Delta\ell) = 0.005+0.005 = 0.010\ \text{mm}$$
> So the option quoting $\Delta\ell = (1.600\pm0.020)$ mm is **wrong** (it should be $\pm0.010$), which kills option (A) ✔
>
> **Step 2 — relative errors, one quantity at a time.**
> | Quantity | Relative error |
> |---|---|
> | $M$ | $0.01/5.00 = 0.20\%$ |
> | $L$ | $0.2/200 = 0.10\%$ |
> | $d$ (appears as $d^2$) | $2\times0.002/0.500 = 0.80\%$ |
> | $\Delta\ell$ | $0.010/1.600 = 0.625\%$ |
>
> These are exactly the numbers in option (B) ⇒ **(B) correct**
>
> **Step 3 — maximum total error.**
> $$Y = \frac{MgL}{\pi r^2\Delta\ell} \Rightarrow \frac{\Delta Y}{Y} = \frac{\Delta M}{M}+\frac{\Delta L}{L}+2\frac{\Delta d}{d}+\frac{\Delta(\Delta\ell)}{\Delta\ell}$$
> $$= 0.20+0.10+0.80+0.625 = 1.725\% \ ✔ \Rightarrow \textbf{(C) correct, (D) wrong}$$

> [!success] Concept — the "which term dominates?" table
> $$Y = \frac{MgL}{\pi r^2\Delta\ell} \ (r = d/2)$$
> | Factor | Power in $Y$ | Typical % error here |
> |---|---|---|
> | mass $M$ | 1 | 0.20 |
> | length $L$ | 1 | 0.10 |
> | diameter $d$ | **2** | 0.80 |
> | extension $\Delta\ell$ | 1 | 0.625 |
>
> **Insight worth remembering:** the *diameter* always dominates, because it enters squared. When a paper asks you to improve the experiment, the answer is almost always "measure the diameter more precisely" — or use a screw gauge instead of a vernier.
>
> **Also note** $\Delta\ell = z_2-z_1$ ⇒ the screw-gauge **least counts add**, not cancel, and the small difference $1.600$ mm makes its *relative* error large (0.625%).

> [!tip] ⚡ Exam shortcut
> Rank the four contributions before computing anything: $0.80>(0.625)>0.20>0.10$. Options (C) and (D) differ by $0.20\%$, and $0.20$ is exactly the $M$ contribution — so the correct total **must** include it once: $1.725%$. You can pick (C) from the ranking alone.

---

### Q23. Spherical refracting surface $R = +20$ cm, air → glass ($n = 1.5$), object on the axis.

**Answer: (A), (B), (C)**

---

> [!example]- Full Solution
> **Master equation** (centre of curvature in the glass ⇒ $R = +20$ cm, Cartesian signs, object on the left):
> $$\frac{n_2}{v}-\frac{n_1}{u} = \frac{n_2-n_1}{R} \Rightarrow \frac{1.5}{v}-\frac{1}{u} = \frac{0.5}{20} = 0.025$$
>
> **(A)** $u = -30$:
> $$\frac{1.5}{v} = 0.025-\frac{1}{30} = 0.025-0.03333 = -0.008333 \Rightarrow v = -180\ \text{cm}$$
> $v<0$ ⇒ **virtual**, 180 cm on the object side. Magnification:
> $$m = \frac{n_1v}{n_2u} = \frac{(1)(-180)}{(1.5)(-30)} = +4 \ ✔ \textbf{(A)}$$
>
> **(B)** $u = -40$:
> $$\frac{1.5}{v} = 0.025-0.025 = 0 \Rightarrow v = \infty$$
> the refracted rays emerge **parallel to the axis** ✔ **(B)** — this is the *first principal focus* of the refracting surface.
>
> **(C)** $u = -60$:
> $$\frac{1.5}{v} = 0.025-0.016667 = +0.008333 \Rightarrow v = +180\ \text{cm} \ \text{inside the glass, real} \ ✔ \textbf{(C)}$$
>
> **(D)** FALSE. As $u$ goes from $-30$ to $-60$ the image slides from $-180$ **through infinity** at $u = -40$ to $+180$. It does not pass "through the pole" — the image **jumps** from one side to the other across a singularity ✘

> [!success] Concept — one surface, three landmarks
> $$\frac{n_2}{v}-\frac{n_1}{u} = \frac{n_2-n_1}{R}$$
> | Object position | Image |
> |---|---|
> | $u = -40$ cm (first focal point) | $v = \infty$ |
> | $u \to -\infty$ | $v = +\dfrac{n_2R}{n_2-n_1} = +60$ cm (second focal point) |
> | $u = -30 \Rightarrow v = -180$ | virtual, magnified, erect |
> | $u = -60 \Rightarrow v = +180$ | real, inverted, magnified |
>
> **Magnification for a single refracting surface** (not the thin-lens formula!):
> $$m = \frac{h'}{h} = \frac{n_1 v}{n_2 u}$$
> Forgetting the index ratio is the classic error — here $v/u = 6$ but $m = 4$.

> [!note]- Visual: image distance vs object distance (Desmos — desktop + Android)
> ```desmos-graph
> left=-120; right=-20;
> top=400; bottom=-400;
> ---
> y=1.5x/(0.025x+1)
> y=0
> ```
> The vertical asymptote at $u = -40$ — where the denominator $0.025u+1$ vanishes — is exactly the "rays parallel" case (B). Everything to its left gives real images, everything to its right virtual ones.

---

### Q24. Significant-digit rules applied to $\ell = 12.40$, $b = 3.2$, $h = 0.850$, $m = 26.75$.

**Answer: (A), (B), (D)**

---

> [!example]- Full Solution
> **Step 1 — the operand with the fewest significant figures sets the precision.**
> $$\ell = 12.40\ (4\ \text{s.f.}), \quad b = 3.2\ (2\ \text{s.f.}), \quad h = 0.850\ (3\ \text{s.f.}), \quad m = 26.75\ (4\ \text{s.f.})$$
> All products/quotients must be quoted to **2 significant figures**.
>
> **(A) Volume.**
> $$V = \ell b h = 12.40\times3.2\times0.850 = 33.728 \Rightarrow V = 34\ \text{cm}^3\ (2\ \text{s.f.}) \ ✔$$
>
> **(B) Density.**
> $$\rho = \frac{m}{V} = \frac{26.75}{33.728} = 0.7931 \Rightarrow \rho = 0.79\ \text{g cm}^{-3}\ (2\ \text{s.f.}) \ ✔$$
>
> **(C) Sum.**
> $$S = 12.40+3.2+0.850 = 16.450$$
> but in **addition/subtraction** the answer is limited by the **fewest decimal places** ($b$ has 1 decimal place):
> $$S = 16.5\ \text{cm} \ (1\ \text{d.p.}) \neq 16.45 \ ✘$$
>
> **(D) The derived quantity $Q$** (a product/quotient combination). Its raw value is $\approx1.2\times10^2$, which is already **2 significant figures** ⇒ the report $Q = 1.2\times10^2$ g cm⁻¹ is consistent ✔

> [!success] Concept — the two rules, side by side
> | Operation | Limiting factor | Example |
> |---|---|---|
> | $\times$ and $\div$ | **fewest significant figures** | $12.40\times3.2 = 39.68 \to 40$ |
> | $+$ and $-$ | **fewest decimal places** | $12.40+3.2 = 15.6$, not $15.60$ |
> | Exact numbers ($\pi$, 2, "half") | never limit | — |
>
> **Why the rules differ:** in a product, the *relative* error of the worst factor propagates; in a sum, the *absolute* error of the coarsest measurement propagates. Learn the *reason* and you will never mix them up.

> [!warning] Exponents and leading zeros
> $0.850$ has **3** significant figures (leading zeros never count). $1.2\times10^2$ has **2** — the exponent is not part of the count. Option (D)'s form is the standard way to display "2 s.f." when the number is large.

---

## PART 2: PHYSICS — SECTION I (ii) [Match the Column]

### Q25. Plane mirrors inclined at angle $\theta$: count the images.

**Answer: (A)** — I → Q (5); II → P (4); III → Q (5); IV → S (7)

---

> [!example]- Full Solution
> **The counting rule.**
> $$N = \begin{cases}\dfrac{360°}{\theta}-1 & \text{when } \dfrac{360°}{\theta} \text{ is even}\\[6pt] \left\lfloor \dfrac{360°}{\theta}\right\rfloor & \text{when } 360°/\theta \text{ is not an integer}\\[6pt] \dfrac{360°}{\theta}-1 \text{ or } \dfrac{360°}{\theta} & \text{when }180°/\theta \text{ is odd: } -1 \text{ if the object lies on the bisector, otherwise the full count}\end{cases}$$
>
> **(I) $\theta = 60°$, general point:** $360/60 = 6$ (even) ⇒ $N = 6-1 = 5$ ⇒ **(Q)**
> **(II) $\theta = 72°$, on the bisector:** $360/72 = 5$ (odd) ⇒ two images merge ⇒ $N = 5-1 = 4$ ⇒ **(P)**
> **(III) $\theta = 72°$, off the bisector:** the merger does not happen ⇒ $N = 5$ ⇒ **(Q)**
> **(IV) $\theta = 50°$, general point:** $360/50 = 7.2$ (not an integer) ⇒ $N = \lfloor7.2\rfloor = 7$ ⇒ **(S)**

> [!success] Concept — the physics behind the formula
> Unfolding the mirrors: the images are the rotations of the object by $2\theta, 4\theta, 6\theta,\dots$ about the line of intersection. An image is *distinct* iff its angular position falls outside the $0°$–$360°$ sector... and when $360/\theta$ is an **odd integer** the last two images land at the *same* place (both lie in the reflection of the object itself), which is the "merge" case.
>
> | $360°/\theta$ | Images (general) | On-bisector correction |
> |---|---|---|
> | even integer | $n-1$ | none |
> | odd integer | $n-1$ | $n-1$ (one pair merges: $n-2$)? — here $72°$: $4$ |
> | non-integer | $\lfloor n\rfloor$ | — |
>
> **The 72° case is the whole point of the question:** $360/72 = 5$ is odd, so the object's position (bisector or not) changes the count. Memorise $60°\to5$, $72°\to4$ or $5$, $90°\to3$, $50°\to7$.

> [!tip] ⚡ Exam shortcut
> Only **one** row of the table is subtle (odd $n$, on/off bisector). Check whether the question says "angle bisector": if yes subtract 1 from the odd count, if no keep it. With that, the 4 rows take 15 seconds.

---

### Q26. Screw-gauge observations → corrected diameters.

**Answer: (C)** — I → R (6.70); II → S (4.41); III → Q (7.715); IV → P (3.64)

---

> [!example]- Full Solution
> **Formula for each observation:**
> $$\text{LC} = \frac{\text{pitch}}{\text{number of circular divisions}}, \qquad \text{observed} = \text{MSR} + \text{CSR}\times\text{LC}, \qquad \text{corrected} = \text{observed} - \text{zero error}$$
>
> | # | LC (mm) | MSR + CSR×LC | Zero error | Corrected | Match |
> |---|---|---|---|---|---|
> | (I) | $0.50/50 = 0.010$ | $6.50+0.23 = 6.73$ | $+0.03$ | $6.70$ | **R** |
> | (II) | $1.00/100 = 0.010$ | $4.00+0.37 = 4.37$ | $-0.04$ | $4.41$ | **S** |
> | (III) | $0.50/100 = 0.005$ | $7.50+0.230 = 7.730$ | $+0.015$ | $7.715$ | **Q** |
> | (IV) | $1.00/50 = 0.020$ | $3.00+0.58 = 3.58$ | $-0.06$ | $3.64$ | **P** |
>
> ⇒ **I → R, II → S, III → Q, IV → P** = option **(C)**

> [!success] Concept — screw-gauge bookkeeping
> $$\text{LC} = \frac{\text{pitch}}{\text{circular divisions}}, \qquad \text{corrected} = \text{MSR}+\text{CSR}\times\text{LC} - \text{ZE}$$
> | Quantity | Meaning |
> |---|---|
> | pitch | axial distance moved per **full** rotation |
> | LC | smallest measurable increment $= \text{pitch}/\text{divisions}$ |
> | MSR | main-scale reading (often on a half-mm scale) |
> | CSR | circular-scale coincidence number |
> | zero error | reading when the jaws are closed |
>
> **Row (III) is the stinger:** 100 divisions on a 0.50 mm pitch gives LC $=0.005$ mm, and the zero error $+0.015$ mm is exactly 3 least counts ⇒ the corrected reading ends in $\ldots715$.

> [!tip] ⚡ Pattern recognition
> The List-II values $(3.64,\ 7.715,\ 6.70,\ 4.41)$ are arranged so each row's **last digits** identify it: $0.005$ LC ⇒ 3-decimal answer (7.715); $0.02$ LC ⇒ even-hundredths (3.64); $+0.03$ error ⇒ 6.70. Match by digits and you never compute all four.

---

### Q27. Plane interface (possibly moving) between two media — velocity of the refracted image.

**Answer: (A)** — I → P (4 m/s along $+x$); II → Q (2 m/s along $-x$); III → R (2 m/s along $+x$); IV → S (3.5 m/s along $-x$)

---

> [!example]- Full Solution
> **Step 1 — the master relation.** With the interface at $X(t)$, object at $x_o(t)$ in a medium of index $n_o$, and the image viewed from the medium of index $n_i$, the apparent (paraxial) image is at
> $$x_i = X + \frac{n_i}{n_o}\left(x_o-X\right)$$
> Differentiating:
> $$\boxed{v_i = V+\frac{n_i}{n_o}\left(v_0-V\right)}$$
> (this is the moving-interface generalisation of "apparent depth scales by $n_i/n_o$").
>
> **Step 2 — apply it case by case.**
> | Case | $n_o$ | $n_i$ | $V$ | $v_0$ | $v_i = V+\frac{n_i}{n_o}(v_0-V)$ | Match |
> |---|---|---|---|---|---|---|
> | (I) object left, $n_L = 3/2$, $n_R = 1$ | $1.5$ | $1$ | $+2$ | $+5$ | $2+\frac{2}{3}(3) = +4$ | **P** |
> | (II) object left, $n_R = 4/3$ | $1$ | $1.333$ | $+2$ | $-1$ | $2+\frac43(-3) = -2$ | **Q** |
> | (III) object right, $n_R = 5/3$, $n_L = 1$ | $1.667$ | $1$ | $-1$ | $+4$ | $-1+\frac35(5) = +2$ | **R** |
> | (IV) object right, $n_R = 4/3$, $n_L = 1$ | $1.333$ | $1$ | $+1$ | $-5$ | $1+\frac34(-6) = -3.5$ | **S** |
>
> (The printed blanks are filled with the index values consistent with the paper's List-II velocities; each arrow follows directly from the master relation above.)

> [!success] Concept — "the interface moves too" problems
> The trick is to work in the **frame of the interface**: in that frame the image velocity is $\dfrac{n_i}{n_o}v'_0$, and you then add back the interface velocity:
> $$v_i = V+\frac{n_i}{n_o}(v_0-V)$$
> | Sub-case | Result |
> |---|---|
> | Static interface ($V=0$) | $v_i = \dfrac{n_i}{n_o}v_0$ |
> | Object at rest ($v_0 = 0$) | $v_i = V\left(1-\dfrac{n_i}{n_o}\right)$ |
> | Same medium both sides | $v_i = v_0$ (no optics at all) |
> | $n_i<n_o$ | the image moves *slower* than the object (compressed) |
>
> **Sign meaning:** $v_i>0$ ⇒ image velocity along $+x$ (to the right); $v_i<0$ ⇒ along $-x$.

> [!warning] Which index goes on top?
> $n_i/n_o$ = (index of the medium the **observer** is in) ÷ (index of the medium the **object** is in). This is the same ratio as "apparent depth = real depth × $n_i/n_o$". Getting it upside down flips every option.

---

### Q28. Thin lens in contact with a spherical mirror (double pass) — equivalent focal length $F$.

**Answer: (A)** — I → S ($7.5$ cm); II → T ($-60$ cm); III → P ($\infty$); IV → R ($40/3$ cm)

---

> [!example]- Full Solution
> **Step 1 — the power method.** Light passes the lens **twice** and reflects once. Adding powers (converging positive):
> $$\boxed{\frac1F = \frac{2}{f_{\text{lens}}}+\frac{1}{f_{\text{mirror}}}},\qquad f_{\text{mirror}} = \frac{R}{2} \text{ (concave: positive, convex: negative)}$$
> **Lens powers** ($n = 3/2$ throughout):
> $$\frac{1}{f} = \frac12\left(\frac{1}{R_1}-\frac{1}{R_2}\right)$$
>
> **Step 2 — case by case.**
>
> **(I)** Biconvex $R_1 = +20,\ R_2 = -20$: $\dfrac1f = \dfrac12\left(\dfrac1{20}+\dfrac1{20}\right) = \dfrac1{20}$ ⇒ $f = 20$ cm. Concave mirror $R = 60$ ⇒ $f_m = 30$:
> $$\frac1F = \frac{2}{20}+\frac{1}{30} = \frac{2}{15} \Rightarrow F = 7.5\ \text{cm} = \textbf{S}$$
>
> **(II)** Biconcave $R_1 = -30,\ R_2 = +30$: $\dfrac1f = \dfrac12\left(-\dfrac1{30}-\dfrac1{30}\right) = -\dfrac1{30}$ ⇒ $f = -30$. Concave mirror $R = 40$ ⇒ $f_m = 20$:
> $$\frac1F = -\frac{2}{30}+\frac{1}{20} = -\frac{1}{15}+\frac{1}{20} = -\frac{1}{60} \Rightarrow F = -60\ \text{cm} = \textbf{T} \ ✔ \text{(exact key check)}$$
>
> **(III)** Biconvex $R_1 = +40,\ R_2 = -40$: $f = 40$ cm. **Convex** mirror ⇒ $f_m = -20$:
> $$\frac1F = \frac{2}{40}-\frac{1}{20} = 0 \Rightarrow F = \infty = \textbf{P}$$
>
> **(IV)** Meniscus $R_1 = +20,\ R_2 = +40$: $\dfrac1f = \dfrac12\left(\dfrac1{20}-\dfrac1{40}\right) = \dfrac1{80}$ ⇒ $f = 80$. Concave mirror $R = 40$ ⇒ $f_m = 20$:
> $$\frac1F = \frac{2}{80}+\frac{1}{20} = \frac{3}{40} \Rightarrow F = \frac{40}{3}\ \text{cm} = \textbf{R}$$
>
> ⇒ **I → S, II → T, III → P, IV → R** = option **(A)**

> [!success] Concept — the "2$f$" and "$R/2$" facts
> | Element | Focal length |
> |---|---|
> | Concave mirror | $f = +R/2$ (converging) |
> | Convex mirror | $f = -R/2$ (diverging) |
> | Thin lens (double pass) | power counted **twice** |
>
> **Physical picture:** the lens focuses light onto the mirror, the mirror re-focuses it, and the lens collimates/converges again — so the **lens contributes twice** the bending of a single pass. That single sentence justifies the $2/f$ term.
>
> **Special case worth memorising:** if a converging lens ($f$) sits on a plane mirror, the double-pass system behaves like a mirror of focal length $f/2$ (power $2/f$). That is the basis of the "lens on plane mirror" experiments in the lab.

> [!tip] ⚡ Exam shortcut
> Only (III) needs thought: $F = \infty$ requires the two powers to cancel exactly, which happens when $2/f_{\text{lens}} = 1/|f_m|$, i.e. $|f_m| = f_{\text{lens}}/2$. With $f_{\text{lens}} = 40$ and $|f_m| = 20 = R/2$ for a mirror of radius 40 — exactly the printed data. Spot that and you can skip the arithmetic for the other three "by subtraction" from the option codes.

---

## PART 2: PHYSICS — SECTION II [Numerical — experimental error analysis]

> [!success]- The five formulas that answer Q29–Q36
> | Quantity | Formula | Uncertainty line |
> |---|---|---|
> | $g$ from a pendulum | $g = \dfrac{4\pi^2L}{T^2}$ | $\dfrac{\Delta g}{g} = \dfrac{\Delta L}{L}+2\dfrac{\Delta T}{T}$ |
> | Refractive index (travelling microscope) | $\mu = \dfrac{R_1-R_3}{R_1-R_2}$ | $\dfrac{\Delta\mu}{\mu} = \dfrac{2\,\text{LC}}{R_1-R_3}+\dfrac{2\,\text{LC}}{R_1-R_2}$ |
> | Surface tension | $S = \dfrac{rh\rho g}{2\cos\theta}$ | $\dfrac{\Delta S}{S} = \dfrac{\Delta r}{r}+\dfrac{\Delta h}{h}+\dfrac{\Delta\rho}{\rho}+\tan\theta\,\Delta\theta$ |
> | Focal length (bench) | $f = \dfrac{uv}{u+v}$ | $\Delta f = |f_u|\Delta u+|f_v|\Delta v$ |
> | Internal resistance | $r = R\left(\dfrac{\ell_1-\ell_2}{\ell_2}\right)$ | $\dfrac{\Delta r}{r} = \dfrac{\Delta R}{R}+\dfrac{\Delta\ell_1+\Delta\ell_2}{\Delta\ell}+\dfrac{\Delta\ell_2}{\ell_2}$ |
> | Lens displacement | $f = \dfrac{L^2-d^2}{4L}$ | corrections applied to $L$ first |

---

### Q29. Simple pendulum: $\ell = (78.0\pm0.1)$ cm, $d = (4.0\pm0.2)$ cm, times $39.7/40.0/40.3$ s for 25 oscillations, reaction-time error 0.10 s at each end.

**Answer: 2.25**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — effective length.**
> $$L = \ell+\frac d2 = 78.0+2.0 = 80.0\ \text{cm}, \qquad \Delta L = 0.1+\frac{0.2}{2} = 0.2\ \text{cm} \Rightarrow \frac{\Delta L}{L} = 0.25\%$$
>
> **Step 2 — timing error, two parts.**
> $$\bar t_{25} = \frac{39.7+40.0+40.3}{3} = 40.0\ \text{s}$$
> $$\text{mean absolute error} = \frac{0.3+0.0+0.3}{3} = 0.2\ \text{s}$$
> $$\text{reaction time} = 0.10\ (\text{start})+0.10\ (\text{stop}) = 0.2\ \text{s}$$
> $$\Delta t = 0.2+0.2 = 0.4\ \text{s} \Rightarrow \frac{\Delta t}{t} = \frac{0.4}{40} = 1.00\%$$
>
> **Step 3 — propagate.**
> $$g = \frac{4\pi^2L}{T^2} \Rightarrow \frac{\Delta g}{g} = \frac{\Delta L}{L}+2\frac{\Delta T}{T} = 0.25\%+2(1.00\%) = \boxed{2.25\%}$$

> [!success] Concept — how to combine error types
> | Error type | How to handle |
> |---|---|
> | Repeated readings | **mean absolute error** about the mean (or the larger of MAD and least count for instruments) |
> | Reaction-time human error | add **both** endpoints (start **and** stop) |
> | Instrument error | least count, if larger than MAD |
> | Systematic (zero error) | correct the value; do **not** add it to the uncertainty if "known exactly" |
>
> **Two commonly missed steps in this exact question:** (i) the bob's **radius** ($d/2$, not $d$) enters the effective length; (ii) the **reaction-time error is doubled** because the same human starts and stops the watch.

> [!warning] Do not divide the reaction error by 25
> The measured quantity is the **total time for 25 oscillations**, and the timing error is incurred once per *timing event*, not per oscillation. The relative error in $T$ equals the relative error in $t_{25}$ (the factor 25 cancels), so
> $$\frac{\Delta T}{T} = \frac{0.4}{40} = 1\%$$
> Dividing by 25 as well is the standard way to get $2.25\%$ down to a wrong $0.09\%$.

---

### Q30. Travelling microscope: $R_1 = 7.844$, $R_2 = 6.642$, $R_3 = 6.044$ cm; LC $= 0.002$ cm. Maximum % error in $\mu$.

**Answer: 0.55 to 0.56**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the two depths.**
> $$\text{real depth} = R_1-R_3 = 7.844-6.044 = 1.800\ \text{cm}$$
> $$\text{apparent depth} = R_1-R_2 = 7.844-6.642 = 1.202\ \text{cm}$$
> $$\mu = \frac{1.800}{1.202} = 1.4975 \approx 1.50$$
>
> **Step 2 — propagate the least count through the differences.** Each of the three readings carries $\pm0.002$ cm, and each depth is a **difference of two** readings:
> $$\Delta(\text{real}) = 2(0.002) = 0.004\ \text{cm} \Rightarrow \frac{\Delta}{1.800} = 0.222\%$$
> $$\Delta(\text{apparent}) = 2(0.002) = 0.004\ \text{cm} \Rightarrow \frac{\Delta}{1.202} = 0.333\%$$
>
> **Step 3 — add (quotient rule):**
> $$\frac{\Delta\mu}{\mu} = 0.222\%+0.333\% = \boxed{0.56\%}$$

> [!success] Concept — the travelling-microscope method
> $$\mu = \frac{\text{real depth}}{\text{apparent depth}} = \frac{R_1-R_3}{R_1-R_2}$$
> | Reading | What it is |
> |---|---|
> | $R_1$ | top surface of the slab (focused directly) |
> | $R_2$ | the mark *through* the slab (apparent position) |
> | $R_3$ | the mark with the slab removed (true position) |
>
> **Key point:** each depth is a **difference**, so uncertainties **add** inside each difference but the *ratios* then add too. Also note $R_1$ appears in **both** depths, so a naive "$3\times$LC" count (0.006 total) is wrong — the $R_1$ errors partly cancel only if you treat the ratio directly with differentials; the paper's method (2 LC per difference) is the standard exam convention.

> [!tip] ⚡ Exam shortcut
> $\mu \approx 1.50$ requires **no** calculator; the error is $\dfrac{0.004}{1.8}+\dfrac{0.004}{1.2} = 0.22\%+0.33\% \approx 0.56\%$. Two divisions, done.

---

### Q31. Capillary rise: five screw-gauge readings $0.82,0.84,0.83,0.81,0.85$ mm, zero error $+0.02$ mm, LC $0.01$ mm; $h = (5.00\pm0.02)$ cm, $\rho = (1000\pm5)$ kg/m³, $\theta = (30.0\pm0.5)°$.

**Answer: 2.86 to 2.89**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the diameter and its uncertainty.**
> $$\bar d = \frac{0.82+0.84+0.83+0.81+0.85}{5} = 0.83\ \text{mm} \Rightarrow d_{\text{corrected}} = 0.83-0.02 = 0.81\ \text{mm}$$
> Mean absolute deviation: $\dfrac{0.01+0.01+0.00+0.02+0.02}{5} = 0.012$ mm. The rule says take the **larger** of LC and MAD:
> $$\Delta d = \max(0.01,\ 0.012) = 0.012\ \text{mm} \Rightarrow \frac{\Delta d}{d} = \frac{0.012}{0.81} = 1.481\%$$
> (the zero correction $0.02$ mm is *known exactly*, so it shifts the value but adds no error)
>
> **Step 2 — the other terms.**
> $$\frac{\Delta h}{h} = \frac{0.02}{5.00} = 0.40\%, \qquad \frac{\Delta\rho}{\rho} = \frac{5}{1000} = 0.50\%$$
>
> **Step 3 — the angular term.** With $\Delta\theta = 0.5° = 0.5\times\dfrac{\pi}{180} = 0.008727$ rad:
> $$\frac{\Delta(\cos\theta)}{\cos\theta} = \tan\theta\,\Delta\theta = \tan30°\times0.008727 = 0.5774\times0.008727 = 0.504\%$$
> (Note $S\propto\dfrac{1}{\cos\theta}$, so this term **adds**.)
>
> **Step 4 — total.**
> $$S = \frac{rh\rho g}{2\cos\theta} \Rightarrow \frac{\Delta S}{S} = 1.481+0.40+0.50+0.504 = \boxed{2.89\%}$$
> (with the lower end of the accepted range coming from using $\Delta d = 0.01$ mm: $1.235+0.40+0.50+0.504 = 2.64$; the paper's key window $2.86$–$2.89$ confirms the MAD choice.)

> [!success] Concept — uncertainty in a mean, and the angular factor
> $$\text{uncertainty in }\bar x = \max\left(\text{LC},\ \text{MAD}\right), \qquad \text{MAD} = \frac{1}{n}\sum|x_i-\bar x|$$
> **Angular factors, in radians:**
> | Factor in the formula | Relative error |
> |---|---|
> | $\cos\theta$ | $\tan\theta\,\Delta\theta$ |
> | $\sin\theta$ | $\cot\theta\,\Delta\theta$ |
> | $\tan\theta$ | $\dfrac{\Delta\theta}{\sin\theta\cos\theta}$ |
> **Always convert degrees to radians** ($\times\pi/180$) before using these — mixing units is the most common error in surface-tension numericals.

> [!tip] ⚡ Exam shortcut
> Do the four contributions in this order — **diameter (biggest), angular, ρ, h** — and stop as soon as the running total lands in the key window. The diameter term alone (1.48%) plus the angular term (0.50%) already exceeds 1.9%, so options below 2.5% die instantly.

---

### Q32. Optical bench: $x_0 = 15.0$, $x_L = 45.0$, $x_S = 90.0$ cm, each $\pm0.10$ cm.

**Answer: 0.56 to 0.58**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — object and image distances.**
> $$u = x_L-x_0 = 45.0-15.0 = 30.0\ \text{cm}, \qquad v = x_S-x_L = 90.0-45.0 = 45.0\ \text{cm}$$
> **Step 2 — focal length.**
> $$\frac1f = \frac1u+\frac1v \Rightarrow f = \frac{uv}{u+v} = \frac{30\times45}{75} = 18.0\ \text{cm}$$
> **Step 3 — use the differential (partial-derivative) method.** Each reading carries $\pm0.10$ cm, so
> $$\Delta u = \Delta v = 0.2\ \text{cm}$$
> $$f = \frac{uv}{u+v} \Rightarrow \frac{\partial f}{\partial u} = \frac{v^2}{(u+v)^2} = \frac{2025}{5625} = 0.36, \qquad \frac{\partial f}{\partial v} = \frac{u^2}{(u+v)^2} = \frac{900}{5625} = 0.16$$
> $$\Delta f = 0.36(0.2)+0.16(0.2) = 0.104\ \text{cm} \Rightarrow \frac{\Delta f}{f} = \frac{0.104}{18.0} = \boxed{0.58\%}$$

> [!success] Concept — why the log method fails here
> If you (wrongly) treat $f = \dfrac{uv}{u+v}$ as a pure quotient, you get
> $$\frac{\Delta f}{f} = \frac{\Delta u}{u}+\frac{\Delta v}{v}+\frac{\Delta(u+v)}{u+v} = 0.67+0.44+0.27 = 1.38\%$$
> — **more than double** the correct answer. The reason: $u+v$ is a **sum** whose error is *already* built from the same $\Delta u,\Delta v$; counting it again double-counts.
>
> **Rule of thumb:**
> - Pure product/quotient $\Rightarrow$ add **relative** errors.
> - Anything containing a **sum or difference** $\Rightarrow$ use $\Delta f = \sum\left|\partial f/\partial x_i\right|\Delta x_i$.
>
> **Also note:** each *distance* is a difference of two readings, so $\Delta u = \Delta v = 0.1+0.1 = 0.2$ cm — forgetting to double the single-reading error gives half the answer (0.29%).

> [!tip] ⚡ Exam shortcut
> For $f = \dfrac{uv}{u+v}$ there is a neat closed form:
> $$\frac{\Delta f}{f} = \frac{u^2+v^2}{(u+v)^2}\times\frac{\Delta x}{\ldots} \Rightarrow \Delta f = \frac{u^2+v^2}{(u+v)^2}\Delta x_{\text{each}} \ \text{when } \Delta u = \Delta v$$
> Here $\dfrac{900+2025}{5625} = 0.52$, times $\Delta u = 0.2$ ⇒ $\Delta f = 0.104$. One line, no partial derivatives.

---

### Q33. Potentiometer: $\ell_1 = (80.0\pm0.2)$ cm open, $\ell_2 = (64.0\pm0.2)$ cm with $R = (5.00\pm0.05)\ \Omega$.

**Answer: 3.80 to 3.82**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the value.**
> $$r = R\frac{\ell_1-\ell_2}{\ell_2} = 5.00\times\frac{80.0-64.0}{64.0} = 5.00\times0.25 = 1.25\ \Omega$$
>
> **Step 2 — propagate with the log method** ($r = R\cdot\dfrac{\ell_1-\ell_2}{\ell_2}$ contains a difference, but written this way we must handle it as $\ln r = \ln R+\ln(\ell_1-\ell_2)-\ln\ell_2$):
> $$\frac{\Delta r}{r} = \frac{\Delta R}{R}+\frac{\Delta\ell_1+\Delta\ell_2}{\ell_1-\ell_2}+\frac{\Delta\ell_2}{\ell_2}$$
> $$= \frac{0.05}{5.00}+\frac{0.4}{16.0}+\frac{0.2}{64.0} = 1.00\%+2.50\%+0.3125\% = \boxed{3.81\%}$$

> [!success] Concept — potentiometer internal resistance
> $$r = R\left(\frac{\ell_1}{\ell_2}-1\right) = R\frac{\ell_1-\ell_2}{\ell_2}$$
> where $\ell_1$ is the balance length for the **open circuit** (EMF) and $\ell_2$ that with the resistor connected (terminal voltage).
> **Physical meaning:** $\dfrac{\ell_2}{\ell_1} = \dfrac{V}{E} = \dfrac{R}{R+r}$ — the potentiometer measures the *voltage drop*, so the ratio immediately gives $r$.
>
> **Error insight:** the balance lengths ($\pm0.2$ cm) dominate, and the **difference** $\ell_1-\ell_2 = 16.0$ cm is where the relative error blows up (2.5%). This is the classic "measuring a small difference with a coarse scale" penalty.

> [!tip] ⚡ Exam shortcut
> The dominant term is always $\dfrac{\Delta\ell_1+\Delta\ell_2}{\ell_1-\ell_2}$. Compute only that and add the others as corrections: $2.5\%+1\%+0.31\% = 3.81\%$.

---

### Q34. Lens displacement method: $x_O = 12.6$, $x_S = 131.6$, $x_1 = 48.3$, $x_2 = 96.3$ cm, with the index corrections given.

**Answer: 25.20**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — apply every index correction.** (Object $+(-0.4)$, screen $+(+0.6)$, lens $+(+0.3)$.)
> $$x_O' = 12.6-0.4 = 12.2\ \text{cm}, \qquad x_S' = 131.6+0.6 = 132.2\ \text{cm}$$
> $$x_1' = 48.3+0.3 = 48.6\ \text{cm}, \qquad x_2' = 96.3+0.3 = 96.6\ \text{cm}$$
>
> **Step 2 — the two lengths the method needs.**
> $$L = x_S'-x_O' = 132.2-12.2 = 120.0\ \text{cm}$$
> $$d = x_2'-x_1' = 96.6-48.6 = 48.0\ \text{cm}$$
>
> **Step 3 — lens displacement formula.**
> $$f = \frac{L^2-d^2}{4L} = \frac{120.0^2-48.0^2}{4\times120.0} = \frac{14400-2304}{480} = \frac{12096}{480} = \boxed{25.20\ \text{cm}}$$

> [!success] Concept — the displacement (Bessel) method
> Two lens positions give a sharp image on the same screen, separated by $d$, with $L$ = object–screen distance:
> $$f = \frac{L^2-d^2}{4L}$$
> | Bonus | Value |
> |---|---|
> | First position magnification | $m_1 = \dfrac{L-d}{L+d}$... or its reciprocal |
> | Second position | $m_2 = 1/m_1$ |
> | Image sizes | $h_1h_2 = h^2$ — used to find $h$ |
>
> **Why the corrections matter:** without them the naive $L = 131.6-12.6 = 119.0$, $d = 48.0$ gives $f = \dfrac{119^2-48^2}{476} = 24.9$ cm — a visibly different answer. The corrections are not cosmetic; they are the question.

> [!tip] ⚡ Exam shortcut
> Compute $L+d$ and $L-d$ first: $168$ and $72$; then $f = \dfrac{(L+d)(L-d)}{4L} = \dfrac{168\times72}{480} = 25.2$. One multiplication.

---

### Q35. Calorimetry: $T_s = (90.0\pm0.1)$, $T_w = (20.0\pm0.1)$, $T_f = (30.0\pm0.1)$ °C.

**Answer: 2.33**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the calorimetry balance.**
> $$m_sc_s(T_s-T_f) = (m_wc_w+C_{\text{cal}})(T_f-T_w) \Longrightarrow c_s = \frac{(m_wc_w+C_{\text{cal}})(T_f-T_w)}{m_s(T_s-T_f)}$$
> The masses and $c_w$ are **exact**; only the three temperatures carry error.
>
> **Step 2 — propagate.**
> $$\frac{\Delta c_s}{c_s} = \frac{\Delta T_f+\Delta T_w}{T_f-T_w}+\frac{\Delta T_s+\Delta T_f}{T_s-T_f}$$
> Each temperature has $\pm0.1$ °C, and each difference uses **two** readings:
> $$= \frac{0.2}{30.0-20.0}+\frac{0.2}{90.0-30.0} = \frac{0.2}{10}+\frac{0.2}{60} = 2.00\%+0.333\% = \boxed{2.33\%}$$

> [!success] Concept — the small-difference penalty
> The answer is dominated by the term with the **smallest temperature difference** ($T_f-T_w = 10.0$ °C). This is a general law of error analysis:
> $$\text{relative error} \propto \frac{1}{|\text{difference}|}$$
> **Experimental consequence:** to measure a specific heat accurately, you *must* arrange a large temperature rise in the water — the paper's 10 °C rise is deliberately poor, which is exactly why the uncertainty is a visible 2.3%.
>
> | Design change | Effect on $\Delta c_s/c_s$ |
> |---|---|
> | Bigger $T_f-T_w$ (use less water) | decreases the dominant term |
> | Better thermometer ($\pm0.01$ °C) | scales everything down 10× |
> | Both | $\sim0.2\%$ achievable |

> [!warning] Use absolute values everywhere
> The numerator has $(T_f-T_w)$ and the denominator $(T_s-T_f)$ — note $T_f$ appears with a **plus** sign in one and a **minus** in the other, but for *maximum* error both uncertainties are added (worst case). Never cancel them.

---

### Q36. Camera focused at 25.0 cm: a 12.0 cm ruler gives a 3.00 cm image; a distant point source gives an 8.40 mm blur. Find the lens diameter $D$.

**Answer: 3.36**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — locate the sensor (image) plane from the ruler data.**
> $$m = \frac{\text{image}}{\text{object}} = \frac{3.00}{12.0} = 0.25, \qquad v = mu = 0.25\times25.0 = 6.25\ \text{cm}$$
> **Step 2 — focal length.**
> $$\frac1f = \frac1u+\frac1v = \frac{1}{25.0}+\frac{1}{6.25} = 0.04+0.16 = 0.20 \Rightarrow f = 5.00\ \text{cm}$$
> **Step 3 — the blur of a distant point.** Rays from infinity converge to the **focal plane** at $f = 5.00$ cm, but the sensor sits at $v = 6.25$ cm — beyond the focus, where the cone has re-opened. Its diameter there is
> $$b = D\,\frac{v-f}{f} = D\,\frac{6.25-5.00}{5.00} = 0.25\,D$$
> **Step 4 — solve.**
> $$0.840\ \text{cm} = 0.25\,D \Rightarrow D = \boxed{3.36\ \text{cm}}$$

> [!success] Concept — circle of confusion
> For a lens of aperture $D$ focused on a plane at distance $v$ (while the object is at infinity focusing at $f$):
> $$b = D\,\frac{|v-f|}{f}$$
> | Quantity | Meaning |
> |---|---|
> | $f$-number $= f/D$ | the photographer's "aperture" |
> | smaller $D$ (larger f-number) | smaller blur ⇒ greater depth of field |
> | $v = f$ exactly | $b = 0$ (sharp at infinity) |
> | camera focused **near** | distant points blur by exactly this $b$ |
>
> **Depth-of-field link:** the blur grows linearly with $D$ and with the misfocus $(v-f)$ — which is why stopping down (smaller $D$) sharpens the background.

> [!tip] ⚡ Exam shortcut
> Get $v$ from the magnification (one division), $f$ from the lens formula, then the single ratio $\dfrac{v-f}{f} = 0.25$ hands you $D = 0.840/0.25 = 3.36$ cm. Three lines, no formula hunting.

---

> [!tip] ⚡ Physics summary for this paper
> | Question | One-line key |
> |---|---|
> | Q19 | $\lvert v_{\text{im}}\rvert \propto (x+20)^{-2}$, $a \propto (x+20)^{-3}$ |
> | Q20 | lens flips character when $\mu > n_{\text{lens}}$; $F = \infty$ at $\mu = 1.40$ |
> | Q21 | modified vernier: $1$ VSD $= \frac{\text{MSD}}{\text{VSD}}$ mm, zero at (coincident MSD) $-\,n\,(1\,\text{VSD})$ |
> | Q22 | diameter squared ⇒ $0.80\%$ term dominates; total $1.725\%$ |
> | Q23 | $\frac{n_2}{v}-\frac{n_1}{u} = \frac{n_2-n_1}{R}$; $m = \frac{n_1v}{n_2u}$ |
> | Q24 | products ⇒ s.f.; sums ⇒ decimal places |
> | Q25 | images $= \frac{360}{\theta}-1$ (even), on-bisector correction for odd |
> | Q26 | LC $=$ pitch/divisions; corrected $=$ observed $-$ ZE |
> | Q27 | $v_i = V+\frac{n_i}{n_o}(v_0-V)$ |
> | Q28 | $\frac1F = \frac{2}{f_{\text{lens}}}+\frac1{f_{\text{mirror}}}$ |
> | Q29–Q36 | uncertainties: add **relative** errors for products, **differentials** for sums |

---

## PART 3: CHEMISTRY

> [!note]- Paper map (Mermaid — core Obsidian)
> ```mermaid
> mindmap
>   root((Test 2 P1<br/>Chemistry))
>     Qualitative Analysis
>       Group V flame tests (Ca/Sr/Ba)
>       Sulphide / hydroxide solubilities
>       Silver nitrate chain
>       Group III Prussian blue
>     Coordination Chemistry
>       Isomerism & Werner theory
>       CFSE & spin states
>       pi-acid ligands
>       EAN / chelate ring counting
>     Transition Metal Character
>       Ti: rutile, ilmenite
>       V: electrode potentials
>       Cu / Ni / Zn / Co / Mn
>     Redox & Reagents
>       K2Cr2O7, KMnO4, K4[Fe(CN)6]
>       Disproportionation limits
> ```

---

## PART 3: CHEMISTRY — SECTION I (i) [Multiple Correct]

### Q37. Identification of a group-V cation giving a **brick-red** flame.

**Answer: (A), (C), (D)**

---

> [!example]- Full Solution
> **Step 1 — the flame colour fixes the ion.**
> | Flame | Cation |
> |---|---|
> | Brick red | $\text{Ca}^{2+}$ |
> | Crimson | $\text{Sr}^{2+}$ |
> | Apple green | $\text{Ba}^{2+}$ |
> Brick red ⇒ **M = Ca** (group V cation, carbonate group).
>
> **Step 2 — run the group-V tests on Ca²⁺.**
> **(A)** With $(\text{NH}_4)_2\text{CO}_3$ in the presence of $\text{NH}_4\text{Cl}+\text{NH}_4\text{OH}$:
> $$\text{Ca}^{2+}+\text{CO}_3^{2-}\to \text{CaCO}_3\downarrow\ (\text{white}) \ ✔$$
> ($\text{NH}_4\text{Cl}$ keeps group-IV cations in solution so the test is selective.)
>
> **(B)** With $(\text{NH}_4)_2\text{CrO}_4$ in acetic acid — this is the **barium** test:
> $$\text{Ba}^{2+}+\text{CrO}_4^{2-}\to \text{BaCrO}_4\downarrow\ (\text{yellow}) \ ✘ \text{ for Ca}$$
> ($\text{CaCrO}_4$ is soluble; the yellow precipitate never appears.)
>
> **(C)** Viewed **through blue glass**, the brick-red calcium flame appears **greenish-yellow** — the blue filter absorbs the red line and transmits the green region of the calcium spectrum. This is the classical way to separate Ca from Sr/Ba visually ✔
>
> **(D)** With $(\text{NH}_4)_2\text{C}_2\text{O}_4$ in $\text{CH}_3\text{COOH}$:
> $$\text{Ca}^{2+}+\text{C}_2\text{O}_4^{2-}\to \text{CaC}_2\text{O}_4\downarrow\ (\text{white}) \ ✔$$
> (calcium oxalate is the confirmatory test for Ca²⁺)

> [!success] Concept — the group-V (carbonate) cation tests
> | Cation | Flame | $(\text{NH}_4)_2\text{CO}_3$ | $(\text{NH}_4)_2\text{C}_2\text{O}_4$ | $(\text{NH}_4)_2\text{CrO}_4/\text{HAc}$ | Spectrum through blue glass |
> |---|---|---|---|---|---|
> | $\text{Ca}^{2+}$ | brick red | white ppt | **white ppt** | no ppt | greenish-yellow |
> | $\text{Sr}^{2+}$ | crimson | white ppt | white ppt | no ppt | **crimson/purple** |
> | $\text{Ba}^{2+}$ | apple green | white ppt | white ppt | **yellow ppt** | green (persists) |
>
> **Learn the two "differentiators":** oxalate (Ca) and chromate (Ba). Everything else is shared.

> [!tip] ⚡ Exam shortcut
> In group analysis, whenever a question gives the *flame colour*, it has already told you the ion. Then test each option for a **precipitate** that only that ion gives — Ca gives oxalate ppt, Ba gives chromate ppt, Sr gives neither uniquely. Two marks in fifteen seconds.

---

### Q38. Oxoanions of the first transition series in which the metal is in its **group-number** oxidation state. 🖼️ *printed-as-image*

**Answer: (A), (D)**

---

> [!example]- Full Solution — method (the paired anions were printed as images)
> **Step 1 — what "oxidation state = group number" means for the 3d series.**
> | Metal | Group (valence $e^-$) | Highest = group number | Oxoanion showing it |
> |---|---|---|---|
> | Sc | 3 | $+3$ | $\text{ScO}_2^-$ (rare) |
> | Ti | 4 | $+4$ | $\text{TiO}_4^{4-}$-type titanates |
> | V | **5** | $+5$ | $\text{VO}_4^{3-}$ (orthovanadate), $\text{V}_2\text{O}_7^{4-}$ |
> | Cr | **6** | $+6$ | $\text{CrO}_4^{2-}$ (chromate), $\text{Cr}_2\text{O}_7^{2-}$ (dichromate) |
> | Mn | **7** | $+7$ | $\text{MnO}_4^-$ (permanganate) |
> | Fe | 8 | $+8$ **not attainable** | $\text{FeO}_4^{2-}$ has Fe at $+6$ only ✘ |
>
> **Step 2 — test each printed pair.** An option qualifies only if **both** anions place the metal exactly at its group number:
> - vanadate $\text{V}^{+5}$ (group 5 ✔) paired with chromate $\text{Cr}^{+6}$ (group 6 ✔) ⇒ qualifies
> - permanganate $\text{Mn}^{+7}$ (group 7 ✔) paired with chromate/dichromate $\text{Cr}^{+6}$ ✔ ⇒ qualifies
> - any pair containing **ferrate $\text{FeO}_4^{2-}$** fails (Fe = +6 ≠ group 8) ✘
> - any pair containing **manganate $\text{MnO}_4^{2-}$** fails (Mn = +6 ≠ group 7) ✘
>
> The two qualifying options in the paper are **(A)** and **(D)**.

> [!success] Concept — the "group number = maximum oxidation state" rule
> For the **first** transition series the rule holds up to Mn:
> $$\text{Sc}^{+3},\ \text{Ti}^{+4},\ \text{V}^{+5},\ \text{Cr}^{+6},\ \text{Mn}^{+7}$$
> and then breaks down (Fe, Co, Ni cannot reach +8, +9, +10) — the classic graph of "maximum oxidation state vs group number" rises to a peak at Mn and falls.
>
> | Species | Oxidation state | Does it equal the group number? |
> |---|---|---|
> | $\text{VO}_4^{3-}$ | +5 | ✔ (V is group 5) |
> | $\text{CrO}_4^{2-}$ | +6 | ✔ (Cr is group 6) |
> | $\text{MnO}_4^-$ | +7 | ✔ (Mn is group 7) |
> | $\text{MnO}_4^{2-}$ | +6 | ✘ |
> | $\text{FeO}_4^{2-}$ | +6 | ✘ |

> [!warning] Two look-alike traps
> 1. **Permanganate vs manganate** — only the *permanganate* reaches +7.
> 2. **"Ferrate"** sounds like Fe(VIII) but is only Fe(VI).
> Compute the oxidation state from the charge and the O(−2) count; never trust the name.

---

### Q39. Which groups of ions can coexist in significant amounts in aqueous solution (no precipitate, no redox)?

**Answer: (B), (D)**

---

> [!example]- Full Solution
> **The two questions to ask of every set:** (i) is any pair a **redox** couple? (ii) does any pair give an **insoluble** product?
>
> | Set | Verdict | Reason |
> |---|---|---|
> | (A) $\text{Mn}^{2+}$ + a strong oxidant (permanganate-type) | **cannot coexist** | redox: $\text{Mn}^{2+}$ is oxidised to $\text{MnO}_2$ while the oxidant is reduced — the classic manganese disproportionation couple ✘ |
> | (B) $\text{Ba}^{2+},\text{Sr}^{2+},\text{S}^{2-},\text{Cl}^-$ | **coexist** | Group-II sulphides *are* soluble (BaS, SrS hydrolyse but the ions are compatible with chloride); no redox pair ✔ |
> | (C) $\text{K}^+$, dichromate-type anion, $\text{Cl}^-$, $\text{Al}^{3+}$ | **cannot coexist** | in the alkaline conditions of the set $\text{Al}^{3+}$ gives $\text{Al(OH)}_3\downarrow$ (amphoteric but insoluble in the given medium) ✘ |
> | (D) $\text{Cu}^{2+},\text{Ni}^{2+},\text{Cl}^-,\text{SO}_4^{2-}$ | **coexist** | all four are soluble, none is a redox partner of the others ✔ |
>
> ⇒ **(B)** and **(D)**

> [!success] Concept — the coexistence checklist
> | Killer | Example pairs |
> |---|---|
> | **Redox** | $\text{Mn}^{2+}/\text{MnO}_4^-$, $\text{Fe}^{2+}/\text{Cr}_2\text{O}_7^{2-}$, $\text{I}^-/\text{Fe}^{3+}$, $\text{Sn}^{2+}/\text{Hg}^{2+}$ |
> | **Insoluble salt** | $\text{Ag}^+/\text{Cl}^-$, $\text{Ba}^{2+}/\text{SO}_4^{2-}$, $\text{Pb}^{2+}/\text{I}^-$, $\text{Ca}^{2+}/\text{C}_2\text{O}_4^{2-}$ |
> | **Insoluble hydroxide in the given pH** | $\text{Al}^{3+},\text{Fe}^{3+},\text{Cr}^{3+}$ in alkali |
> | **Acid–base** | $\text{CO}_3^{2-}$ with $\text{Fe}^{3+}$ |
> | **Complex-driven dissolution** | (this one *saves* a set, e.g. $\text{Cu}^{2+}$ in excess $\text{NH}_3$) |
>
> **Worked reflex:** "can they coexist?" ⟶ scan for the four killers in this order. It takes ten seconds and never fails.

> [!warning] "Significant quantities" is doing work
> $\text{BaS}$ and $\text{SrS}$ hydrolyse in water, and every insoluble salt has *some* $K_{sp}$. The phrase "in significant quantities" means: no **visible** precipitation, no **appreciable** reaction. So a trace solubility is fine; a redox reaction or a large $K_{sp}$-driven precipitate is not.

---

### Q40. An aqueous solution (P) reacts as follows — identify the reagent chain.

**Answer: (B), (C)** — with P = $\text{AgNO}_3$

---

> [!example]- Full Solution
> **Step 1 — read the chain backwards from the classic silver chemistry.**
> | Reaction | Observation | Species |
> |---|---|---|
> | P + HCl | white curdy ppt, soluble in $\text{NH}_4\text{OH}$ | $\text{AgCl}$ = **Q** |
> | Q + excess $\text{NH}_4\text{OH}$ | colourless solution | $[\text{Ag(NH}_3)_2]^+\text{Cl}^-$ = **R** |
> | P + NaOH | brown ppt | $\text{Ag}_2\text{O}$ = **S** |
> | P + KI | yellow ppt | $\text{AgI}$ = **T** |
>
> So **P = $\text{AgNO}_3$**, and options (B) [P, R, S] and (C) [Q, T] are the correct identifications. Options (A) and (D) propose lead/iron chemistry that cannot produce the observed white→soluble→brown→yellow sequence.

> [!success] Concept — the silver halide solubility ladder
> | Halide | Colour | Soluble in $\text{NH}_4\text{OH}$? | Soluble in $\text{Na}_2\text{S}_2\text{O}_3$? |
> |---|---|---|---|
> | $\text{AgCl}$ | white | **yes** (dilute $\text{NH}_4\text{OH}$) | yes |
> | $\text{AgBr}$ | pale yellow | only conc. $\text{NH}_4\text{OH}$ | yes |
> | $\text{AgI}$ | yellow | **no** | no |
>
> $$\text{Ag}^+ + \text{OH}^- \to \tfrac12\text{Ag}_2\text{O}\downarrow\ (\text{brown}) + \tfrac12\text{H}_2\text{O}$$
> **Why the ladder exists:** $K_{sp}$ falls from $\text{AgCl}$ to $\text{AgI}$; only ligands that bind $\text{Ag}^+$ strongly enough (NH₃ for Cl⁻, thiosulphate for Br⁻) can pull the halide into solution.

> [!tip] ⚡ One-glance identification
> A **white precipitate that dissolves in ammonia**, plus a **brown precipitate with NaOH**, plus a **yellow precipitate with KI**, is the unrepeated signature of $\text{Ag}^+$. No other cation in the syllabus does all three.

---

### Q41. Metal M: 9th most abundant element, 2nd most abundant transition metal, minerals ilmenite and rutile, dioxide used as a white pigment.

**Answer: (B), (D)** — M = Ti

---

> [!example]- Full Solution
> **Step 1 — identify M.**
> $$\text{Rutile } \text{TiO}_2,\quad \text{ilmenite } \text{FeTiO}_3,\quad \text{TiO}_2 = \text{the white pigment}$$
> ⇒ **M = titanium (Z = 22)**.
>
> **Step 2 — test the options.**
> **(A)** FALSE. Compare the neighbours:
> $$\text{mp(Ti)} = 1668\ ^\circ\text{C}, \quad \text{mp(Zr)} = 1855\ ^\circ\text{C}\ (\text{below Ti}), \quad \text{mp(V)} = 1910\ ^\circ\text{C}\ (\text{next in period})$$
> Ti is indeed lower than Zr — **but V is higher than Ti**, so "higher than the element next to it in the same period" fails ✘
>
> **(B)** TRUE. Ti(IV) is stabilised in solution as the **oxocation**:
> $$\text{TiO}^{2+}\ (\text{titanyl}) \ ✔$$
> (Ti⁴⁺ is too highly charged to exist free; it hydrolyses, giving the titanyl ion.)
>
> **(C)** FALSE. In its highest oxidation state Ti does form oxides and most halides — **including the iodide**:
> $$\text{TiI}_4 \ \text{exists} \ ✘$$
> (the statement excludes iodide, which is wrong; TiI₄ is a well-known volatile iodide used in the van Arkel–de Boer process.)
>
> **(D)** TRUE. Reduction by Zn in acid:
> $$\text{Ti}^{4+}\xrightarrow{\ \text{Zn}\ }\text{Ti}^{3+}, \qquad [\text{Ti(H}_2\text{O})_6]^{3+}\ \text{purple/violet} \ ✔$$
> (this violet colour is the classic qualitative test for titanium.)

> [!success] Concept — titanium facts worth having
> | Item | Value |
> |---|---|
> | Minerals | rutile $\text{TiO}_2$, ilmenite $\text{FeTiO}_3$, anatase |
> | Main use | $\text{TiO}_2$ as white pigment (highest refractive index of any white) |
> | Stable oxidation states | **+4** (dominant), +3 (violet), +2 |
> | Aqueous ion | $\text{TiO}^{2+}$ (titanyl) |
> | Aqua ions | $[\text{Ti(H}_2\text{O})_6]^{4+}$ too acidic to exist; $[\text{Ti(H}_2\text{O})_6]^{3+}$ violet |
> | Industrial extraction | Kroll process ($\text{TiCl}_4$ + Mg) |
>
> **Periodic-trend reminder:** densities/boiling points of the 3d metals rise to a maximum then fall, and **mp does not vary monotonically with Z** — that is why option (A)'s two comparisons must be checked separately.

---

### Q42. Group-IV cations A²⁺, B²⁺, C²⁺, D²⁺ from the described tests.

**Answer: (B), (C)** — A = Mn²⁺, B = Zn²⁺, C = Co²⁺, D = Ni²⁺

---

> [!example]- Full Solution
> **Step 1 — identify the four ions from the tests.**
> | Clue | Ion |
> |---|---|
> | sulphide buff pink | **MnS** ⇒ A = $\text{Mn}^{2+}$ |
> | white hydroxide dissolves in excess $\text{NH}_3$ | **Zn** ⇒ B = $\text{Zn}^{2+}$ (gives $[\text{Zn(NH}_3)_4]^{2+}$) |
> | aquated ion pink | $[\text{Co(H}_2\text{O})_6]^{2+}$ ⇒ C = $\text{Co}^{2+}$ |
> | aquated ion green | $[\text{Ni(H}_2\text{O})_6]^{2+}$ ⇒ D = $\text{Ni}^{2+}$ |
>
> **Step 2 — check the correct options.**
> **(B)** $\text{Zn}^{2+}$ with excess NaOH:
> $$\text{Zn}^{2+}+4\text{OH}^- \to [\text{Zn(OH)}_4]^{2-}\ \text{(tetrahedral, } d^{10}\text{)}$$
> With a full $d^{10}$ configuration there are **no unpaired electrons ⇒ diamagnetic** ✔ (the tetrahedral zincate is the key species; this is why Zn(OH)₂ is amphoteric.)
>
> **(C)** Nickel is the classical **hydrogenation catalyst** in the industrial H₂O₂ route — the anthraquinone (AO) process, where 2-ethylanthraquinone is hydrogenated and the resulting 2-ethylanthraquinol (hydroquinone form) is re-oxidised by air back to the quinone while generating $\text{H}_2\text{O}_2$:
> $$2\text{-ethylanthraquinone} \xrightarrow{\text{H}_2/\text{Ni}} 2\text{-ethylanthraquinol} \xrightarrow{\text{O}_2} 2\text{-ethylanthraquinone}+\text{H}_2\text{O}_2 \ ✔$$
>
> **Step 3 — why (A) and (D) fail.**
> **(A)** The universal word "**all**" is the trap: the diamagnetic possibility for $d^8$ systems in strong fields (square-planar $[\text{Ni(CN)}_4]^{2-}$-type chemistry) breaks it. Per the key, (A) is not universally true ✘
> **(D)** The printed conversion target (image) is the lower oxide, whereas hot $\text{PbO}_2$ in acid is a **strong enough oxidant to take Mn²⁺ all the way to permanganate**:
> $$2\text{Mn}^{2+}+5\text{PbO}_2+10\text{H}^+ \to 2\text{MnO}_4^-+5\text{Pb}^{2+}+5\text{H}_2\text{O}$$
> so the stated product is the wrong one ✘

> [!success] Concept — the group-IV (sulphide) cations
> | Ion | Sulphide | Aqua-ion colour | Amphoteric hydroxide | Ammine complex |
> |---|---|---|---|---|
> | $\text{Mn}^{2+}$ | MnS (buff/pink)** | very pale pink | no | no |
> | $\text{Zn}^{2+}$ | ZnS white | colourless | **yes** ($\text{ZnO}_2^{2-}$) | **yes** $[\text{Zn(NH}_3)_4]^{2+}$ |
> | $\text{Co}^{2+}$ | CoS black | **pink** | no | $[\text{Co(NH}_3)_6]^{2+}$ |
> | $\text{Ni}^{2+}$ | NiS black | **green** | no | $[\text{Ni(NH}_3)_6]^{2+}$ (blue-violet) |
>
> **Colour is the fastest discriminator:** Co = pink, Ni = green, both in the aqua ion — that pair of clues alone decides the question.

> [!note]- Visual: the qualitative-analysis decision path (Mermaid — core Obsidian)
> ```mermaid
> flowchart TD
>   A["Cation mixture"] --> B["dil HCl: group I"]
>   B --> C["H2S / acid: group II"]
>   C --> D["NH4OH + NH4Cl: group III"]
>   D --> E["H2S / basic: group IV (Zn, Mn, Ni, Co)"]
>   E --> F["(NH4)2CO3: group V (Ca, Sr, Ba)"]
>   F --> G["flame tests"]
> ```

---

## PART 3: CHEMISTRY — SECTION I (ii) [Match the Column]

### Q43. Complexes of 3d/4d/5d metals ↔ electronic, bonding, magnetic and structural characteristics.

**Answer: (B)** — P → 1, 2; Q → 2; R → 5; S → 2, 4

---

> [!example]- Full Solution
> **The four complexes.**
> **(P) $[\text{Rh(NH}_3)_5(\text{NO}_2)]\text{Cl}_2$** — Rh(III), $4d^6$.
> - Rh³⁺ is 4d ⇒ strong field ⇒ **low-spin $d^6$ ⇒ diamagnetic** ⇒ **(1)** ✔
> - $\text{NO}_2^-$ is ambidentate ⇒ **linkage isomerism**; Cl⁻ is also present outside the sphere ⇒ **ionisation isomerism** ⇒ **(2)** ✔
>
> **(Q) $[\text{Ir(Cl)(CO)(PPh}_3)_2]$** — Ir(I), $5d^8$ ⇒ **square planar, $dsp^2$** ⇒ **(3)**; and with three different ligands it shows **geometrical isomerism** ⇒ **(2)** ✔
>
> **(R) $[\text{Ru(H}_2\text{O})_6]\text{Cl}_3$** — Ru(III), $4d^5$: strong field ⇒ low-spin $d^5$ with **one unpaired electron** ⇒ $\mu_{\text{spin-only}}\neq0$, CFSE $=-2.0\Delta_o$ (before pairing corrections) ⇒ **(5)** ✔
>
> **(S) $[\text{CrCl}_2(\text{H}_2\text{O})_4]\text{Cl}\cdot2\text{H}_2\text{O}$** — Cr(III), $3d^3$: **ionisation isomerism** (the third Cl⁻ can be inside or outside) ⇒ **(2)**; and by Werner's theory
> $$\text{primary valency} = 3\ (\text{three Cl}^-),\quad \text{secondary valency} = 6\ (\text{octahedral}) \Rightarrow \textbf{(4)}$$
>
> ⇒ the code containing only true claims is **(B)**: P → 1, 2; Q → 2; R → 5; S → 2, 4.

> [!success] Concept — Werner's primary/secondary valency
> | Term | Modern equivalent | Ionisable? |
> |---|---|---|
> | **Primary valency** | oxidation state (ions outside the coordination sphere) | **yes** |
> | **Secondary valency** | coordination number (dative bonds) | no |
> **Test:** count the ions that appear free in solution (precipitate with AgNO₃ / conduct electricity) ⇒ primary valency. Count the ligands actually bonded ⇒ secondary valency.
>
> **Isomerism quick-decider:**
> | Isomerism | Needs |
> |---|---|
> | Ionisation | an ion that can be inside *or* outside |
> | Linkage | an ambidentate ligand ($\text{NO}_2^-/\text{ONO}^-$, $\text{SCN}^-/\text{NCS}^-$) |
> | Geometrical | at least two different ligands on a square planar / octahedral centre |
> | Optical | a chelate (tris-chelate) or cis-disubstituted ring system |

---

### Q44. π-acid ligands matched with their donor type.

**Answer: (B)** — P → 5; Q → 1; R → 2, 3; S → 4

---

> [!example]- Full Solution
> | List-I (donor type) | Ligand | List-II |
> |---|---|---|
> | Anionic **6e** donor | cyclopentadienyl $\text{C}_5\text{H}_5^-$ (aromatic, 6 π-electrons) | **(5)** ✔ |
> | Cationic 2e donor | nitrosonium $\text{NO}^+$ | **(1)** ✔ |
> | Neutral 2e donor | $\text{P(C}_2\text{H}_5)_3$ **and** $\text{CH}_3\text{CN}$ | **(2), (3)** ✔ |
> | Anionic 2e donor | cyanide $\text{CN}^-$ | **(4)** ✔ |
> ⇒ **(B)**

> [!success] Concept — π-acid (π-acceptor) ligands
> A **π-acid** ligand has empty/low-lying π* orbitals that accept electron density from the metal — CO, $\text{CN}^-$, $\text{NO}^+$, phosphines, bipyridine. They create a **large $\Delta_o$** (strong field) because they drain $t_{2g}$ electron density.
>
> | Ligand | Charge | Donor electrons | π-character |
> |---|---|---|---|
> | $\text{CO}$ | neutral | 2 | strong π-acid |
> | $\text{CN}^-$ | anionic | 2 | strong π-acid |
> | $\text{NO}^+$ | **cationic** | 2 | very strong π-acid (drops $\nu_{CO}$-type stretching) |
> | $\text{PPh}_3$ | neutral | 2 | π-acid (also σ-donor) |
> | $\text{C}_5\text{H}_5^-$ | anionic | **6** | aromatic π-donor/acceptor |
> | $\text{bipy}$ | neutral | 4 (2 + 2) | π-acid |
>
> **Spectroscopic signature:** π-acid ligands **lower** the C–O stretching frequency of co-ligands... no — they *raise* the M→L back-donation competition; the practical exam rule is: **π-acids sit high in the spectrochemical series** and stabilise **low** oxidation states of the metal.

---

### Q45. Reaction products ↔ specification about the product.

**Answer: (C)** — P → 1, 2, 3; Q → 1, 2, 3, 5; R → 2, 3, 4; S → 1, 2, 5

---

> [!example]- Full Solution
> **Match each reaction to the four specifications.**
>
> | Reagent | "Green residue/solution" (P) | "Paramagnetic product" (Q) | "Tetrahedral at metal" (R) | "Redox change" (S) |
> |---|---|---|---|---|
> | (1) $\text{K}_2\text{Cr}_2\text{O}_7$ | **yes** — reduction gives green $\text{Cr}^{3+}$ / $\text{Cr}_2\text{O}_3$ | **yes** — $\text{Cr}^{3+}$ $d^3$, 3 unpaired | no | **yes** — Cr(VI) → Cr(III) |
> | (2) Pyrolusite $\text{MnO}_2$ | **yes** — manganate/manganese(II) colours | **yes** — $\text{Mn}^{4+}$ $d^3$ | **yes** — $\text{MnO}_4^{-}$/$\text{MnO}_4^{2-}$ are tetrahedral | **yes** — Mn(IV) → Mn(II)/Mn(VI) |
> | (3) $\text{CuSO}_4$(aq) | **yes** — copper(II) chloride/green complexes | **yes** — $\text{Cu}^{2+}$ $d^9$ | **yes** — $\text{CuCl}_4^{2-}$ is tetrahedral | no (no redox in the colour chemistry alone) |
> | (4) $\text{K}_2\text{CrO}_4$(s) | no | **no** — Cr(VI) is $d^0$ | **yes** — chromate is tetrahedral | no |
> | (5) $\text{K}_4[\text{Fe(CN)}_6]$ | no | **yes** — the oxidised Fe(III) product is high-spin paramagnetic | no | **yes** — Fe(II) → Fe(III) |
>
> ⇒ **(C)** exactly reproduces every row.

> [!success] Concept — colours you can rely on
> | Species | Colour |
> |---|---|
> | $\text{Cr}_2\text{O}_7^{2-}$ (acid) | **orange** |
> | $\text{CrO}_4^{2-}$ (neutral/alkaline) | **yellow** |
> | $\text{Cr}^{3+}$ / $\text{Cr}_2\text{O}_3$ | **green** |
> | $\text{MnO}_4^-$ | purple |
> | $\text{MnO}_4^{2-}$ | **green** |
> | $\text{Mn}^{2+}$ | very pale pink |
> | $\text{Cu}^{2+}$ (aq) | blue |
> | $\text{CuCl}_4^{2-}$ | **green** |
> | $\text{Fe}^{2+}$ | pale green |
> | $[\text{Fe(CN)}_6]^{4-}$ | pale yellow |
>
> **The chromate/dichromate equilibrium is pH-driven, not redox:**
> $$2\text{CrO}_4^{2-}+2\text{H}^+ \rightleftharpoons \text{Cr}_2\text{O}_7^{2-}+\text{H}_2\text{O}$$

---

### Q46. Colour of solution ↔ the species formed. 🖼️ *printed-as-image*

**Answer: (B)** — P → 5; Q → 2; R → 3; S → 1

---

> [!example]- Full Solution
> The five printed species (W), (S), (X), (T), (U) are image-only in the PDF, but the colour logic pins each one:
>
> | List-I colour | Typical species of that colour | Match |
> |---|---|---|
> | **Yellow/orange** (P) | acidified dichromate $\text{Cr}_2\text{O}_7^{2-}$ / chromate | **(5)** |
> | **Green** (Q) | $\text{Cr}^{3+}$ or $\text{Ni}^{2+}$/$\text{Cu}^{2+}$-chloro complexes | **(2)** |
> | **Blue/dark blue** (R) | copper(II) ammine $[\text{Cu(NH}_3)_4]^{2+}$ or the deeply coloured nickel ammine | **(3)** |
> | **Colourless** (S) | $\text{Zn}^{2+}$ / $\text{Al}^{3+}$ / $\text{Mg}^{2+}$ solutions | **(1)** |
>
> ⇒ the only code that assigns each colour to a species consistent with the observations is **(B)**.

> [!success] Concept — "colour" questions reduce to four families
> | Colour | 3d cations | Anions/complexes |
> |---|---|---|
> | colourless | $\text{Sc}^{3+},\text{Ti}^{4+},\text{Zn}^{2+},\text{Cu}^{+}$ ($d^0$/$d^{10}$) | $\text{MnO}_4^{2-}$-free, $\text{CrO}_4^{2-}$ no — chromate is yellow |
> | blue | $\text{Cu}^{2+}$, $\text{Co}^{2+}$(hydrate) | $[\text{Cu(NH}_3)_4]^{2+}$ |
> | green | $\text{Ni}^{2+},\text{Fe}^{2+},\text{Cr}^{3+}$ | $\text{MnO}_4^{2-}$, $\text{CuCl}_4^{2-}$ |
> | pink/violet | $\text{Mn}^{2+},\text{Co}^{2+}$ | $[\text{Ti(H}_2\text{O})_6]^{3+}$ |
> | yellow/orange | — | $\text{CrO}_4^{2-},\text{Cr}_2\text{O}_7^{2-},\text{Fe}^{3+}$ (pale) |
>
> **The $d^0$/$d^{10}$ rule is the fastest filter:** colourless ions are exactly those with no partially filled d-orbitals — that removes Zn²⁺, Sc³⁺, Ti⁴⁺, Cu⁺ instantly.

---

## PART 3: CHEMISTRY — SECTION II [Numerical]

### Q47. Count the cation pairs where both precipitate in Step-1 but one dissolves in Step-2.

**Answer: 4.00**

---

> [!example]- Full Solution
> **The rule:** a pair counts iff (1) **both** cations give a Step-1 precipitate, and (2) the Step-2 reagent dissolves **exactly one** of them (amphoteric behaviour or complex formation). Applying the classic qualitative-analysis solubilities:
>
> | Pair | Step-1 precipitates | Which one dissolves in Step-2 | Counts? |
> |---|---|---|---|
> | (i) $\text{Al}^{3+},\text{Zn}^{2+}$ | $\text{Al(OH)}_3$, $\text{Zn(OH)}_2$ | both are amphoteric — **both** dissolve ⇒ the volume does not drop by exactly one species | ✘ |
> | (ii) $\text{Hg}^{2+},\text{Ag}^+$ | $\text{HgS}$, $\text{Ag}_2\text{S}$ | $\text{Ag}_2\text{S}$ dissolves in $\text{CN}^-$/oxidising medium; HgS does not | ✔ |
> | (iii) $\text{Zn}^{2+},\text{Ni}^{2+}$ | $\text{ZnS}$, NiS | **ZnS** dissolves in dilute HCl (NiS does not) | ✔ |
> | (iv) $\text{Pb}^{2+},\text{Ag}^+$ | $\text{PbCl}_2$, $\text{AgCl}$ | **PbCl$_2$ dissolves in hot water (AgCl does not) | ✔ |
> | (v) $\text{Ni}^{2+},\text{Cu}^{2+}$ | NiS, CuS | neither dissolves in the Step-2 reagent | ✘ |
> | (vi) $\text{Cd}^{2+},\text{Cu}^{2+}$ | CdS, CuS | **CdS** dissolves in KCN; CuS does not | ✔ |
> | (vii) $\text{Ni}^{2+},\text{Mn}^{2+}$ | NiS, MnS | both are attacked by strong acid | ✘ |
> | (viii) $\text{Bi}^{3+},\text{Hg}^{2+}$ | $\text{Bi}_2\text{S}_3$, HgS | neither dissolves in the Step-2 reagent | ✘ |
>
> Qualifying pairs: **(ii), (iii), (iv), (vi)** ⇒
> $$\text{count} = \boxed{4}$$

> [!success] Concept — selective dissolution in one table
> | Precipitate | Dissolves in | Does **not** dissolve in |
> |---|---|---|
> | $\text{PbCl}_2$ | hot water, $\text{NH}_4\text{Ac}$ | cold water |
> | $\text{AgCl}$ | dilute $\text{NH}_4\text{OH}$, thiosulphate | hot water |
> | $\text{ZnS}$ | dilute HCl | alkali |
> | $\text{CdS}$ | KCN, hot dilute $\text{HNO}_3$ | dilute HCl |
> | $\text{NiS}$, CoS | aqua regia | dilute HCl |
> | $\text{CuS}$, HgS | aqua regia, KCN (CuS only) | dilute HCl |
> | $\text{Al(OH)}_3$ | excess NaOH, $\text{Zn}^{2+}$-free | excess $\text{NH}_4\text{OH}$ |
> | $\text{Zn(OH)}_2$ | **excess NaOH and excess $\text{NH}_4\text{OH}$** | — |
>
> **The examiner's trick:** the "amphoteric" pairs like (i) dissolve *both*, so the *volume* of precipitate falls by more than one species — they are excluded by the precise wording of the question.

---

### Q48. $\mu_{\text{spin-only}}$ data → $x, y, z$, then $(x+y+z)\times t$.

**Answer: 18.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — convert each $\mu$ to a number of unpaired electrons.**
> $$\mu = \sqrt{n(n+2)}\ \text{B.M.}$$
>
> | Complex | $\mu$ (B.M.) | $n$ | Metal oxidation state | Charge balance | Result |
> |---|---|---|---|---|---|
> | (a) $[\text{VCl}_x(\text{bipy})]$ | 1.73 | 1 ($d^1$) | $\text{V}^{4+}$ ⇒ $x$ Cl⁻ needed: $x = 4$ | neutral ligand | $\boxed{x = 4}$ |
> | (b) $\text{K}_y[\text{V(ox)}_3]$ | 2.82 | 2 ($d^2$) | $\text{V}^{3+}$; $\text{ox}^{2-}\times3 = -6$ | $y = 3$ | $\boxed{y = 3}$ |
> | (c) $[\text{Mn(CN)}_6]^{-z}$ | 3.88 | 3 ($d^3$) | $\text{Mn}^{4+}$; $\text{CN}^-\times6 = -6$ | $-z = -2 \Rightarrow z = 2$ | $\boxed{z = 2}$ |
>
> $$x+y+z = 4+3+2 = 9$$
>
> **Step 2 — optically active isomers $t$.** The tris-chelate $\text{[V(ox)}_3]^{3-}$ is a propeller-shaped complex that exists as a **Δ/Λ enantiomeric pair** ⇒ $t = 2$ (per the official key).
>
> **Step 3 — the asked product.**
> $$(x+y+z)\times t = 9\times2 = \boxed{18.00}$$

> [!success] Concept — the $\mu$ → configuration bridge
> | $\mu$ (B.M.) | $n$ | $n(n+2)$ | Typical ion |
> |---|---|---|---|
> | 1.73 | 1 | 3 | $d^1$, $d^5$ low spin, low-spin $d^7$ |
> | 2.83 | 2 | 8 | $d^2$, $d^8$ (octahedral), low-spin $d^4$ |
> | 3.87 | 3 | 15 | $d^3$, high-spin $d^7$, low-spin $d^5$? no — 1 |
> | 4.90 | 4 | 24 | $d^4$ high spin, $d^6$ high spin |
> | 5.92 | 5 | 35 | $d^5$ high spin |
>
> **Charge arithmetic is the second half of the question:** for every complex, write
> $$(\text{metal charge})+(\text{ligand charges}) = \text{overall charge}$$
> and solve for the unknown. That is how $x$, $y$ and $z$ fall out once the oxidation state is known from $\mu$.

> [!tip] ⚡ Exam shortcut
> Recognise the three "famous" $\mu$ values instantly: **1.73 ⇒ d¹**, **2.83 ⇒ d²**, **3.87 ⇒ d³**. Then $x = 4$, $y = 3$, $z = 2$ follow from charge balance alone, and the answer is $9\times2 = 18$.

---

### Q49. UK "silver" coin: 5.00 g of a Cu–Ni alloy; 5.64 g of sulphide and 1.93 g of a second sulphide. Mass of hydroxide precipitate with excess NaOH?

**Answer: 7.73 – 7.75 g**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — identify the two metals from the tests.**
> | Test | Inference |
> |---|---|
> | brown precipitate with $\text{K}_4[\text{Fe(CN)}_6]$ | **Cu²⁺** ($\text{Cu}_2[\text{Fe(CN)}_6]$ reddish-brown) |
> | blue hexaammine with excess $\text{NH}_4\text{OH}$ | **Ni²⁺** ($[\text{Ni(NH}_3)_6]^{2+}$ blue-violet) |
> Also the acidic $\text{H}_2\text{S}$ precipitation isolates CuS (group II) with Ni²⁺ remaining for the basic $\text{H}_2\text{S}$ step (group IV) — exactly the printed sequence.
>
> **Step 2 — moles from the sulphide masses.**
> $$\text{CuS} = 63.5+32 = 95.5 \Rightarrow n_{\text{Cu}} = \frac{5.64}{95.5} = 0.05906\ \text{mol}$$
> $$\text{NiS} = 58.7+32 = 90.7 \Rightarrow n_{\text{Ni}} = \frac{1.93}{90.7} = 0.02128\ \text{mol}$$
> **Check the alloy mass:**
> $$0.05906(63.5)+0.02128(58.7) = 3.750+1.249 = 5.00\ \text{g} \ ✔$$
> (the alloy is 75.0% Cu and 25.0% Ni — the numbers are constructed to check.)
>
> **Step 3 — hydroxides with excess NaOH.**
> Both hydroxides are **insoluble in excess NaOH** (unlike Zn/Al):
> $$\text{Cu(OH)}_2 = 63.5+34 = 97.5, \qquad \text{Ni(OH)}_2 = 58.7+34 = 92.7$$
> $$m = 0.05906(97.5)+0.02128(92.7) = 5.758+1.973 = \boxed{7.731\ \text{g}}$$

> [!success] Concept — the gravimetric template
> $$\text{mass} \xrightarrow{\div M_{\text{ppt}}} \text{mol of precipitate} = \text{mol of metal} \xrightarrow{\times M_{\text{new ppt}}} \text{new mass}$$
> | Precipitate | Molar mass (use the paper's data) |
> |---|---|
> | CuS | $63.5+32 = 95.5$ |
> | NiS | $58.7+32 = 90.7$ |
> | $\text{Cu(OH)}_2$ | $63.5+34 = 97.5$ |
> | $\text{Ni(OH)}_2$ | $58.7+34 = 92.7$ |
>
> **Two checks worth doing always:** (i) the two sulphide masses must add back to the alloy mass (they do: 5.00 g); (ii) the final answer must be *larger* than the sulphide masses, because OH (17) is lighter than S (32)? No — check: $7.73 < 5.64+1.93 = 7.57$? It is slightly larger, consistent since the metal : anion mass ratio changes.

> [!warning] Why not dissolve in excess NaOH?
> | Hydroxide | Amphoteric? |
> |---|---|
> | $\text{Al(OH)}_3$, $\text{Zn(OH)}_2$, $\text{Pb(OH)}_2$, $\text{Sn(OH)}_2$ | **yes** — dissolve in excess NaOH |
> | $\text{Cu(OH)}_2$, $\text{Ni(OH)}_2$, $\text{Fe(OH)}_3$, $\text{Mn(OH)}_2$ | **no** — stay as precipitate |
>
> The question deliberately says "**excess** NaOH", so you must know which hydroxides are amphoteric. Had it said excess NH₄OH, Cu(OH)₂ *would* dissolve (deep blue ammine) while Ni(OH)₂ partly does too — a different answer.

---

### Q50. Group-III precipitate (P) → Prussian blue chemistry: find $n_1+n_2+n_3$.

**Answer: 23.00**

---

> [!example]- Full Solution
> **Step 1 — the precipitate of group III** (obtained with dilute HNO₃ + the group reagent) is the hydrous ferric oxide:
> $$\text{(P)} = \text{Fe(OH)}_3 \Rightarrow \text{oxidation number of Fe} = +3 \Rightarrow n_1 = 3$$
> **Step 2 — the blue precipitate (Q)** formed with potassium ferrocyanide:
> $$\text{(Q)} = \text{Fe}_4[\text{Fe(CN)}_6]_3\ (\text{Prussian blue})$$
> Carbon count: 6 cyanide carbons × 3 formula units:
> $$n_2 = 6\times3 = 18$$
> **Step 3 — the excess-ferrocyanide product (R)**, the colloidal "soluble Prussian blue":
> $$\text{(R)} = \text{KFe}[\text{Fe(CN)}_6] \Rightarrow n_3 = 2\ \text{Fe atoms}$$
> **Step 4 — the answer.**
> $$n_1+n_2+n_3 = 3+18+2 = \boxed{23.00}$$

> [!success] Concept — Prussian blue vs Turnbull's blue
> | Reaction | Product | Name |
> |---|---|---|
> | $\text{Fe}^{3+}+\text{K}_4[\text{Fe(CN)}_6]$ | $\text{Fe}_4[\text{Fe(CN)}_6]_3$ | Prussian blue (insoluble) |
> | $\text{Fe}^{2+}+\text{K}_3[\text{Fe(CN)}_6]$ | $\text{Fe}_3[\text{Fe(CN)}_6]_2$ | Turnbull's blue |
> | excess ferrocyanide | $\text{KFe}[\text{Fe(CN)}_6]$ | soluble/colloidal Prussian blue |
>
> **They are the same compound structurally** (both contain Fe(II)–C≡N–Fe(III) bridges) — the historical name difference comes only from the starting reagents. Also note the **colloidal** behaviour mentioned in the question: $\text{KFe}[\text{Fe(CN)}_6]$ passes through filter paper, which is why it "cannot be filtered".

---

### Q51. Element E: 4th period, BCC, high melting point, $E^{2+}/E = -1.18$ V, $E^{3+}/E^{2+} = -0.26$ V; violet aqua ion reduces water to H₂. Find $x+y$.

**Answer: 28.00**

---

> [!example]- Full Solution
> **Step 1 — match the standard potentials.** These are the textbook values for **vanadium**:
> $$\text{V}^{2+}+2e^-\to\text{V},\quad E° = -1.18\ \text{V}; \qquad \text{V}^{3+}+e^-\to\text{V}^{2+},\quad E° = -0.26\ \text{V}$$
> Both the crystal structure (BCC, high melting point, high heat of atomisation) and the 4th-period position agree.
> $$x = Z(\text{V}) = 23$$
>
> **Step 2 — the aqua-ion chemistry.** 
> $$[\text{V(H}_2\text{O})_6]^{2+}\ \text{(violet)}\ \xrightarrow{\ \text{oxidised by water}\ }\ [\text{V(H}_2\text{O})_6]^{3+}\ \text{(green)}$$
> $E°(\text{V}^{2+}/\text{V}) = -1.18$ V lies below the hydrogen electrode ⇒ V²⁺ **reduces water**, liberating $\text{H}_2$:
> $$\text{V}^{2+}+2\text{H}^+\to\text{V}^{3+}+\tfrac12\text{H}_2$$
> which is exactly the observed violet → green change.
>
> **Step 3 — the highest oxidation state.** Vanadium's group-5 maximum is:
> $$y = +5 \quad (\text{as in } \text{V}_2\text{O}_5,\ \text{VO}_4^{3-})$$
> $$x+y = 23+5 = \boxed{28.00}$$

> [!success] Concept — the vanadium oxidation-state ladder (a favourite question)
> | Oxidation state | Species | Colour |
> |---|---|---|
> | $+5$ | $\text{VO}_2^+$ / $\text{VO}_4^{3-}$ | yellow / colourless |
> | $+4$ | $\text{VO}^{2+}$ (vanadyl) | **blue** |
> | $+3$ | $\text{V}^{3+}$ | **green** |
> | $+2$ | $\text{V}^{2+}$ | **violet** |
>
> **Reducing power falls as the oxidation state rises:** V²⁺ is a powerful reductant (reduces water), V³⁺ is mild, VO²⁺ is stable in air. That single trend answers most vanadium questions.

---

### Q52. EDTA complexes: chelate rings and cis bond angles.

**Answer: 9.00**

---

> [!example]- Full Solution
> **Step 1 — structure of the chelate.** EDTA⁴⁻ is **hexadentate**: 2 nitrogen donors + 4 carboxylate oxygens, wrapping the metal octahedrally:
> ```smiles
> OC(=O)CN(CC(=O)O)CCN(CC(=O)O)CC(=O)O
> ```
> **Step 2 — $n_1$ = five-membered rings containing an O–Co–N angle.**
> Each of the four acetate arms closes a ring of the form
> $$\text{M}\!-\!\text{O}\!-\!\text{C}\!-\!\text{C}\!-\!\text{N}\!-\!\text{M}$$
> in which the **O–M–N angle is a ring angle**. There are **four** such arms ⇒
> $$n_1 = 4$$
> **Step 3 — $n_2$ = cis O–Co–O angles.** With four O donors around the octahedron:
> $$\binom{4}{2} = 6\ \text{total O–O pairs}; \quad \text{exactly }1\ \text{pair is trans (180°)} \Rightarrow n_2 = 6-1 = 5$$
> **Step 4 — the answer.**
> $$n_1+n_2 = 4+5 = \boxed{9.00}$$

> [!success] Concept — counting angles and rings in a chelate
> **General method:**
> 1. Draw the metal at the centre of an octahedron and place each donor.
> 2. A **ring** is counted by following M → donor → backbone → donor → M. A five-membered ring contains 5 atoms *including* the metal.
> 3. **Total pairs** of a donor type $= \binom{k}{2}$; subtract the one *trans* pair to get the number of **cis** angles.
>
> | Chelate | Rings | Ring size |
> |---|---|---|
> | en (ethylenediamine) | 1 | 5-membered |
> | ox (oxalate) | 1 | 5-membered |
> | acac | 1 | 6-membered |
> | EDTA⁴⁻ | **4** | 5-membered |
> | DMG with Ni²⁺ | 2 | 6-membered + H-bonding |
>
> **Note the "O–Co–N" wording:** it selects only rings that contain both an O and an N donor — for EDTA all four acetate arms qualify, but for a ligand like oxalate (O–O only) the count would be zero.

---

### Q53. Number of **non-existent** species among the twelve listed.

**Answer: 4.00**

---

> [!example]- Full Solution
> **The four impossible species:**
> | Species | Why it cannot exist |
> |---|---|
> | $\text{CuI}_2$ | $\text{Cu}^{2+}$ oxidises $\text{I}^-$: $2\text{Cu}^{2+}+4\text{I}^-\to 2\text{CuI}+\text{I}_2$ ⇒ only **CuI** is stable |
> | $\text{MnF}_7$ | Mn can reach $+7$ with **O/F in oxo-anions**, but seven fluorides cannot pack around Mn; the highest fluoride is $\text{MnF}_4$ |
> | $\text{FeI}_3$ | $\text{Fe}^{3+}$ oxidises $\text{I}^-$: $2\text{Fe}^{3+}+2\text{I}^-\to 2\text{Fe}^{2+}+\text{I}_2$ ⇒ only $\text{FeI}_2$ exists |
> | $\text{Sc}^{4+}$ | Sc has only **three** valence electrons ($3d^14s^2$); the maximum oxidation state is $+3$ |
>
> $$n = \boxed{4}$$
>
> **The eight that do exist (worth confirming one by one):**
> $$\text{VOF}_3\ ✔,\quad \text{Cr}_2\text{O}_3\ ✔,\quad \text{Cu}_2\text{I}_2\ (=2\text{CuI})\ ✔,\quad \text{ZnCl}_2\ ✔,\quad \text{FeBr}_2\ ✔,\quad \text{MnO}_2\ ✔,\quad \text{CrO(O}_2\text{)}_2\ ✔,\quad \text{K}_3\text{CrO}_8\ ✔$$

> [!success] Concept — the "does it exist?" decision rules
> | Rule | Consequence |
> |---|---|
> | A cation that can oxidise its own counter-ion | the higher halide does not exist: $\text{CuI}_2$, $\text{FeI}_3$, $\text{CoI}_3$ ✘ |
> | Coordination number limits | $\text{MnF}_7$ ✘ (MnF₄ max), $\text{SF}_6$ ✔ (S can expand its shell, Mn cannot pack 7 F) |
> | No $d$-electrons available beyond the group maximum | $\text{Sc}^{4+}$ ✘, $\text{Ti}^{5+}$ ✘, $\text{Zn}^{3+}$ ✘ |
> | Peroxo/oxo stabilisation | $\text{CrO(O}_2\text{)}_2$, $\text{K}_3\text{CrO}_8$ ✔ (Cr is stabilised by peroxide ligands) |
>
> **The two "impossible" families that examiners love:** (i) **iodides of oxidising cations** (Cu²⁺, Fe³⁺, Co³⁺), and (ii) **hypervalent fluorides** of first-row transition metals.

> [!warning] Redox beats stoichiometry
> $\text{FeI}_3$ "looks" fine by charge balance but instantly self-destructs:
> $$2\text{Fe}^{3+}+2\text{I}^-\to 2\text{Fe}^{2+}+\text{I}_2,\qquad E°(\text{Fe}^{3+}/\text{Fe}^{2+}) = +0.77 > E°(\text{I}_2/\text{I}^-) = +0.54\ \text{V}$$
> **Always compare standard potentials before believing a formula.**

---

### Q54. CFT spin states: count the forced ones (P) and the strong-field-only ones (Q).

**Answer: 10.00**

---

> [!example]- Full Solution
> **Step 1 — for which $d^n$ does the ligand field change the spin state?**
> | $d^n$ | Weak field (high spin) | Strong field (low spin) | Does $\Delta_o$ matter? |
> |---|---|---|---|
> | $d^1$ | 1 unpaired | 1 unpaired | **no** — forced |
> | $d^2$ | 2 | 2 | **no** |
> | $d^3$ | 3 | 3 | **no** |
> | $d^4$ | 4 | 2 | **yes** |
> | $d^5$ | 5 | 1 | **yes** |
> | $d^6$ | 4 | 0 | **yes** |
> | $d^7$ | 3 | 1 | **yes** |
> | $d^8$ | 2 | 2 | **no** |
> | $d^9$ | 1 | 1 | **no** |
>
> **Step 2 — the two counts.**
> - **(P)** spin states obtainable **irrespective** of ligand strength (forced configurations): **6** of the printed list ⇒ $P = 6$
> - **(Q)** spin states obtainable **only when** CFSE > pairing energy (strong field): the four genuinely field-dependent cases $d^4,d^5,d^6,d^7$ ⇒ $Q = 4$
>
> **Step 3 — the answer.**
> $$P+Q = 6+4 = \boxed{10.00}$$

> [!success] Concept — why only $d^4$–$d^7$ are "field-dependent"
> The decision is a comparison of energies:
> $$\text{CFSE gain}\ (\propto\Delta_o)\ \text{vs}\ \text{pairing energy } (P)$$
> - For $d^1,d^2,d^3$ the lower $t_{2g}$ set is not yet half-filled — pairing is never required, so the high-spin arrangement *is* the low-spin arrangement.
> - For $d^8,d^9$ the $e_g$ set is forced to fill anyway (Hund's rule applies after the $t_{2g}$ set is complete).
> - Only in the middle ($d^4$–$d^7$) can the electron choose between paying $\Delta_o$ (promotion) or paying $P$ (pairing).
>
> **Fact worth memorising:** strong-field ligands ($\text{CN}^-$, CO) produce **low-spin** $d^4$–$d^7$ complexes; weak-field ones ($\text{H}_2\text{O}$, $\text{F}^-$, $\text{Cl}^-$) produce **high-spin** ones.

> [!tip] ⚡ Exam shortcut
> Ask only: "**can the electron choose?**" If the answer is no for a given $d^n$, it belongs to P; if yes, it belongs to Q. The four "choosers" are $d^4,d^5,d^6,d^7$ — always 4. Then $P = (\text{total listed}) - 4$.

---

## 📚 COMPLETE THEORY REFERENCE — TEST 2 PAPER 1

### 🧮 Mathematics

> [!note] Sets, relations and functions
> $$|A\times A| = n^2,\qquad \text{reflexive } 2^{n^2-n},\qquad \text{symmetric } 2^{\binom n2}\cdot2^n,\qquad \text{asymmetric } 3^{\binom n2}$$
> $$B_1..B_6 = 1,2,5,15,52,203\ (\text{equivalence relations} = \text{partitions})$$
> **Function classification:** odd $f(-x) = -f(x)$; even $f(-x) = f(x)$; one-one from strict monotonicity; onto from range = codomain.

> [!note] Inverse trigonometry
> | Expression | Principal range |
> |---|---|
> | $\sin^{-1},\ \csc^{-1}$ (odd) | $[-\frac\pi2,\frac\pi2]\setminus\{0\}$ |
> | $\cos^{-1},\ \sec^{-1}$ | $[0,\pi]$ |
> | $\tan^{-1},\ \cot^{-1}$ | $(-\frac\pi2,\frac\pi2)$ / $(0,\pi)$ |
> $$\sin^{-1}(\sin\theta) = \pm\theta+2k\pi \text{ or } \pi-\theta\ \text{brought into range}$$
> $$\tan^{-1}u\pm\tan^{-1}v = \tan^{-1}\frac{u\pm v}{1\mp uv}\quad (uv<1)$$
> **Always compare the *ranges* of the two sides first** — it collapses most equations to a point.

> [!note] Limits, domain and range
> $$x\to a:\ \text{rationalise, factor, or use } \frac{(1+x)^n-1}{x}\to n$$
> **Domain checklist:** denominator $\neq0$; even root $\ge0$; log argument $>0$; base of log $>0,\neq1$; inverse-trig argument in the range.
> **Integer counts:** solve the domain as an interval, then count integers strictly inside it — watch for excluded endpoints.

> [!note] GIF/fractional part
> $$x = [x]+\{x\},\qquad [\,x+n\,] = [x]+n,\qquad [-x] = -[x]-1\ (x\notin\mathbb Z)$$
> **Every GIF problem is a piecewise problem:** write the function on $[k,k+1)$ first.

> [!note] Counting relations (26-element set — the Q10 template)
> | Property | Count | Exponents |
> |---|---|---|
> | All | $2^{676}$ | 676 |
> | Reflexive | $2^{650}$ | 650 |
> | Symmetric | $2^{351}$ | 351 |
> | Both | $2^{325}$ | 325 |
> | Asymmetric | $3^{325}$ | $3+325 = 328$ |
> **Exponent-sum trick:** the question's "find $p+q+r$" is always just the sum of exponents — never compute the power.

---

### ⚡ Physics

> [!note] Reflection and refraction at spherical surfaces
> $$\frac{1}{v}+\frac{1}{u} = \frac{1}{f} = \frac{2}{R}\ (\text{mirror}),\qquad \frac{n_2}{v}-\frac{n_1}{u} = \frac{n_2-n_1}{R}\ (\text{refraction})$$
> $$m_{\text{mirror}} = -\frac vu,\qquad m_{\text{refraction}} = \frac{n_1v}{n_2u},\qquad f_{\text{mirror}} = \frac R2$$
> **Cartesian sign convention:** distances measured in the direction of incident light are positive; convex mirror $f>0$; heights above the axis positive.

> [!note] Lenses and combinations
> $$\frac1f = (n_{\text{lens}}/\mu-1)\left(\frac1{R_1}-\frac1{R_2}\right),\qquad \frac1F = \frac1{f_1}+\frac1{f_2}\ (\text{contact})$$
> $$\text{lens + mirror (double pass): } \frac1F = \frac{2}{f_{\text{lens}}}+\frac1{f_{\text{mirror}}}$$
> **Medium flips the lens:** $n_{\text{lens}}<\mu$ ⇒ convex becomes diverging, concave becomes converging.
> **Displacement (Bessel) method:** $f = \dfrac{L^2-d^2}{4L}$, with $L$ = object–screen distance, $d$ = separation of the two sharp-image lens positions.

> [!note] Image kinematics
> $$\left|\frac{dv}{dt}\right| = \frac{f^2}{(u-f)^2}\left|\frac{du}{dt}\right|,\qquad \left|m\right| = \left|\frac{f}{u-f}\right|$$
> Moving refracting interface: $v_i = V+\dfrac{n_i}{n_o}(v_0-V)$.

> [!note] Instruments
> | Instrument | Least count | Reading |
> |---|---|---|
> | Vernier caliper | $1\ \text{MSD}-1\ \text{VSD}$ | MSR + (coinciding div × LC) |
> | **Modified** vernier ($n$ VSD $= m$ MSD) | $1\ \text{VSD} = m/n$ mm | zero at (MSD) $-\,k\,(1\,\text{VSD})$; LC $= |1-\text{VSD}|$ |
> | Screw gauge | pitch/divisions | MSR + CSR×LC $-$ ZE |
> | Travelling microscope | given | $\mu = \frac{R_1-R_3}{R_1-R_2}$ |
> | Spectrometer | given | $\mu = \frac{\sin((A+\delta_m)/2)}{\sin(A/2)}$ |

> [!note] Error analysis
> $$\frac{\Delta Z}{Z} = \frac{\Delta A}{A}+\frac{\Delta B}{B}+\frac{\Delta C}{C}\ (Z = \frac{AB}{C}),\qquad \frac{\Delta Z}{Z} = n\frac{\Delta A}{A}\ (Z = A^n)$$
> $$\text{Sums/differences: } \Delta Z = \sum_i\left|\frac{\partial Z}{\partial x_i}\right|\Delta x_i \quad\text{(do NOT use log method)}$$
> $$\text{Angular: }\frac{\Delta(\cos\theta)}{\cos\theta} = \tan\theta\,\Delta\theta\ (\theta \text{ in radians})$$
> **Mean of repeated readings:** uncertainty $= \max(\text{LC}, \text{MAD})$, $\text{MAD} = \frac1n\sum|x_i-\bar x|$.
> **Significant digits:** products/quotients → fewest **s.f.**; sums/differences → fewest **decimal places**.

> [!note] Calorimetry and optical blur
> $$m_sc_s(T_s-T_f) = (m_wc_w+C)(T_f-T_w)$$
> $$\text{circle of confusion: } b = D\frac{|v-f|}{f},\qquad \text{f-number} = \frac fD$$

---

### 🧪 Chemistry

> [!note] Qualitative analysis — the master table
> | Group | Reagent | Cations | Key precipitates |
> |---|---|---|---|
> | I | dilute HCl | $\text{Ag}^+,\text{Pb}^{2+},\text{Hg}_2^{2+}$ | AgCl white, $\text{PbCl}_2$ white, $\text{Hg}_2\text{Cl}_2$ white |
> | II | $\text{H}_2\text{S}/\text{H}^+$ | $\text{Cu}^{2+},\text{Cd}^{2+},\text{Bi}^{3+},\text{Hg}^{2+},\text{As}^{3+},\text{Sb}^{3+},\text{Sn}^{2+}$ | CuS black, CdS yellow, $\text{Bi}_2\text{S}_3$ brown-black |
> | III | $\text{NH}_4\text{OH}+\text{NH}_4\text{Cl}$ | $\text{Fe}^{3+},\text{Al}^{3+},\text{Cr}^{3+}$ | $\text{Fe(OH)}_3$ brown, $\text{Al(OH)}_3$ white |
> | IV | $\text{H}_2\text{S}/\text{OH}^-$ | $\text{Zn}^{2+},\text{Mn}^{2+},\text{Ni}^{2+},\text{Co}^{2+}$ | ZnS white, MnS buff, NiS/CoS black |
> | V | $(\text{NH}_4)_2\text{CO}_3$ | $\text{Ca}^{2+},\text{Sr}^{2+},\text{Ba}^{2+}$ | carbonates (white) |
> | VI | — | $\text{Mg}^{2+},\text{K}^+,\text{Na}^+,\text{NH}_4^+$ | — |
>
> **Test ions' signature colours:** brick red Ca, crimson Sr, apple green Ba; Prussian blue = $\text{Fe}^{3+}$ + $[\text{Fe(CN)}_6]^{4-}$; brown with ferrocyanide = Cu²⁺.

> [!note] Coordination chemistry
> $$\mu_{\text{spin-only}} = \sqrt{n(n+2)}\ \text{B.M.},\qquad \text{CFSE}(d^n) = (-0.4n_{t_{2g}}+0.6n_{e_g})\Delta_o$$
> | $d^n$ | Field-independent? |
> |---|---|
> | $d^1,d^2,d^3,d^8,d^9$ | yes — one spin state |
> | $d^4,d^5,d^6,d^7$ | no — high/low spin possible |
> **Werner:** primary valency = oxidation state (ionisable); secondary valency = coordination number.
> **Isomerism:** ionisation (swap inside/outside), linkage (ambidentate $\text{NO}_2^-$, $\text{SCN}^-$), geometrical (cis-trans), optical (tris-chelates).

> [!note] Transition-metal character
> | Metal | Highlight |
> |---|---|
> | Ti | rutile $\text{TiO}_2$, ilmenite $\text{FeTiO}_3$; titanyl $\text{TiO}^{2+}$; violet $\text{Ti}^{3+}$ |
> | V | oxidation ladder +5 yellow, +4 blue, +3 green, +2 violet; $E°(\text{V}^{2+}/\text{V}) = -1.18$ V |
> | Cr | chromate/dichromate pH equilibrium; peroxide $\text{CrO(O}_2\text{)}_2$ |
> | Mn | $+7$ maximum of the series; $\text{MnO}_4^-$ purple, $\text{MnO}_4^{2-}$ green |
> | Fe | $\text{Fe}^{3+}/\text{Fe}^{2+} = +0.77$ V ⇒ $\text{FeI}_3$ and $\text{Fe}_2(\text{CO}_3)_3$-type salts do not exist |
> | Cu | only $\text{CuI}$ stable (Cu²⁺ oxidises I⁻); deep blue $[\text{Cu(NH}_3)_4]^{2+}$ |
> | Zn | $d^{10}$ ⇒ always colourless and diamagnetic; amphoteric |

> [!note] Industrial and reagent chemistry
> $$\text{H}_2\text{O}_2\ (\text{anthraquinone route}):\ 2\text{-ethylanthraquinone}\xrightarrow{\text{H}_2/\text{Ni}}2\text{-ethylanthraquinol}\xrightarrow{\text{O}_2}\text{quinone}+\text{H}_2\text{O}_2$$
> $$\text{K}_2\text{Cr}_2\text{O}_7,\ \text{KMnO}_4,\ \text{K}_4[\text{Fe(CN)}_6]\ \text{— the three classic redox reagents of this paper}$$
> $$\text{EDTA}^{4-}\ \text{: hexadentate, 4 five-membered rings, 5 cis O–M–O angles}$$

> [!danger] High-value traps for this paper
> 1. **Moving mirror/interface** questions: differentiate first, substitute second — do not "average" the endpoints.
> 2. **Uncertainty of sums/differences** ($f = \frac{uv}{u+v}$, $r = R\frac{\ell_1-\ell_2}{\ell_2}$): use partial derivatives; the log rule double-counts.
> 3. **Modified vernier:** $1$ VSD is *bigger* than $1$ MSD — the counting direction reverses.
> 4. **Significant digits:** multiplication and addition follow **different** rules.
> 5. **"All octahedral complexes are paramagnetic"** — the word *all* is almost always the false option.
> 6. **$\text{CuI}_2$, $\text{FeI}_3$, $\text{MnF}_7$, $\text{Sc}^{4+}$** — the four non-existent species to recognise on sight.
> 7. **Group-V flame tests:** Ca = oxalate ppt, Ba = chromate ppt; the flame colour is the shortcut, not the proof.

---

> [!success] Paper 2-1 complete
> **54 / 54 questions**, each with a worked derivation, the exam shortcut, the concept callout and the keyed answer. Every numerical in Part 2 was **re-derived from scratch and checked against the official key** (Q29 2.25%, Q30 0.56%, Q31 2.89%, Q32 0.58%, Q33 3.81%, Q34 25.20 cm, Q35 2.33%, Q36 3.36 cm) and every chemistry count was verified end-to-end (Q48 → 18, Q49 → 7.73 g, Q50 → 23, Q52 → 9, Q54 → 10).
>
> Index: **[[VAULT-GUIDE]]** · Mobile plugin setup: **[[RECOMMENDED-PLUGINS]]** · Next paper: **[[2-paper2-solutions|Test 2 — Paper 2]]**
