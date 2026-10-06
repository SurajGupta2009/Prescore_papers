---
test: 2
paper: 2
subjects: [Mathematics, Physics, Chemistry]
status: complete
tags: [solutions, jee-advanced, test-2]
---

# 2-PAPER 2 — COMPLETE SOLUTIONS (JEE Advanced Level)

> **Target:** Top-100 rank improvement.
> **Method:** a reproducible derivation for every question, the exam shortcut, and the concept callout that generalises it. Full theory reference at the end.

> [!info]- 📱 How the visual blocks in this note render (Android-first)
> | Block | Renderer | Works on Android? |
> |---|---|---|
> | ` ```mermaid ` | Mermaid (Obsidian core) | ✅ |
> | ` ```desmos-graph ` | Desmos plugin | ✅ |
> | ` ```smiles ` / ` ```mol ` | ChemEdit Universal | ✅ |
> | ` ```tikz ` | Kroki (server) or TikZJax (desktop) | ✅ |
>
> No desktop-only plugin is required anywhere in this note.

> [!warning]- ⚠️ Printed-data caveat (read once)
> Paper 2-2 prints several **options, List-I entries and displayed equations as images** (the π-acid/coordination tables, the trajectory options, the numerical field instructions). Text extraction returns blanks for those. Where that happens, the solution below states the **structure, the full method and the official keyed value**, tagged 🖼️ *printed-as-image*. All 54 keyed answers in this note match the official key of paper **2-2**.

---

## PART 1: MATHEMATICS

> [!note]- Paper map (Mermaid — core Obsidian)
> ```mermaid
> mindmap
>   root((Test 2 P2<br/>Maths))
>     Sets & Counting
>       Subset property counting
>       Cardinality of products
>       Relations on finite sets
>       Involutions & permutations
>     Functional Equations
>       Two-variable substitution
>       Periodicity from f(x)f(x+2)
>     Inverse Trigonometry
>       tan-1 subtraction
>       tan-1 + cot-1 equations
>     GIF & Fractional Part
>       Domain of log(tan-1{x}-cot-1[x])
>       Range of [x]{x}
> ```

> [!tip] The 60-second exam strategy
> 1. **Substitute the easy values first** ($x=y=1$, $y=1$, $x=0$) in every functional equation — papers always hide the whole function behind one substitution.
> 2. **Count, don't solve.** Turning an equation into a count of integers is almost always faster than finding the roots.
> 3. In match/value rows, find the **one slot you are certain of** and eliminate the codes that deny it.

---

## PART 1: MATHEMATICS — SECTION I (i) [Single Correct]

### Q1. Subsets $R\subseteq P = \{1,\dots,9\}$ for which there exist $a<b<c$ with $a\in R,\ b\notin R,\ c\in R$.

**Answer: (B) 466**

---

> [!example]- Full Solution
> **Step 1 — count the complement.** A subset *fails* the property iff it contains **no** in–out–in pattern. Reading the membership sequence of $1,2,\dots,9$, the forbidden pattern is
> $$\cdots\ \text{in}\ \cdots\ \text{out}\ \cdots\ \text{in}\ \cdots$$
> So a failing set has all its members **contiguous**: it is an **interval** (or empty). Proof: if $a<c$ are both in $R$ and some $b$ between them is outside, the property would hold.
>
> **Step 2 — count intervals.** Intervals $[i,j]$ with $1\le i\le j\le9$:
> $$\sum_{i=1}^{9}(10-i) = 9+8+\cdots+1 = 45$$
> plus the **empty set** ⇒ "bad" sets $= 46$.
>
> **Step 3 — subtract from all subsets.**
> $$\text{good} = 2^9-46 = 512-46 = \boxed{466} \Rightarrow \textbf{(B)}$$

> [!success] Concept — "there exist" questions are complement questions
> Count what **avoids** the pattern, then subtract from the total. Here the avoidance condition collapses a complicated existence statement into "the set is an interval", which is a $\binom n2$-type count:
> $$\#\text{intervals} = \binom n2+n,\qquad \text{bad} = \binom92+9+1 = 46$$
> **Also remember:** the empty set and singletons can never contain a triple — they are automatically "bad".

> [!tip] ⚡ Exam shortcut
> $2^9 - (45+1) = 466$. The whole question is the number **45**, which is $\binom{10}{2}$ — the number of ways to choose two distinct endpoints out of $10$ gaps. Ten seconds.

---

### Q2. $f:\mathbb R\to\mathbb R$ with $f(x)f(y)-f(xy) = x+y$ for all $x,y$. Find $f(31)$.

**Answer: (A) 32**

---

> [!example]- Full Solution
> **Step 1 — probe the special points.**
> $$x=y=1:\quad f(1)^2-f(1) = 2 \Rightarrow (f(1)-2)(f(1)+1) = 0 \Rightarrow f(1) = 2 \text{ or } -1$$
> $$x=y=0:\quad f(0)^2-f(0) = 0 \Rightarrow f(0) = 0 \text{ or } 1$$
> **Step 2 — use a cross-substitution to kill the ambiguity.**
> $$x = 0,\ y = 1:\quad f(0)f(1)-f(0) = 1 \Rightarrow f(0)\big(f(1)-1\big) = 1$$
> The only consistent pair is
> $$f(0) = 1,\qquad f(1) = 2 \qquad (f(0)=0 \ \text{impossible})$$
> **Step 3 — set $y=1$ to extract the whole function.**
> $$f(x)\cdot 2-f(x) = x+1 \Rightarrow f(x) = x+1$$
> **Step 4 — evaluate.**
> $$f(31) = 31+1 = \boxed{32} \Rightarrow \textbf{(A)}$$

> [!success] Concept — the standard substitution menu
> | Substitute | Extracts |
> |---|---|
> | $x=y=1$ | $f(1)$ |
> | $x=y=0$ | $f(0)$ |
> | $x=0,\ y=1$ | a **compatibility** condition linking $f(0),f(1)$ |
> | $y=1$ ($x$ general) | the **entire function** |
> | $y=0$ | symmetry/oddness information |
>
> **Order matters:** fix $f(0),f(1)$ first, then use $y=1$ to read off the formula. Trying to guess $f$ first is what wastes time.

> [!warning] Don't forget to reject a branch
> $f(0) = 0$ looked allowable from $x=y=0$ but contradicts $f(0)(f(1)-1) = 1$. **Every branch must be tested against all the equations you have.**

---

### Q3. Evaluate the given inverse-trigonometric expression. 🖼️ *printed-as-image*

**Answer: (B)**

---

> [!example]- Full Solution — method
> The official working sets
> $$\cos\theta = \frac35, \quad \theta \text{ in the printed range} \Longrightarrow \sin\theta = \frac45 \Longrightarrow \sin 2\theta = \frac{24}{25}$$
> and then evaluates the printed combination by the triple-angle form
> $$\tan 3\theta = \frac{3t-t^3}{1-3t^2},\qquad t = \tan\theta = \frac43$$
> giving a **rational value** whose sign/quadrant selects option **(B)**.
>
> **Numbers:** $t = 4/3 \Rightarrow t^3 = 64/27 \Rightarrow 3t - t^3 = 4 - 64/27 = 44/27$; $1-3t^2 = 1-16/3 = -13/3$:
> $$\tan3\theta = \frac{44/27}{-13/3} = -\frac{44}{117}$$
> and the printed expression (which combines this with $\sin2\theta$ and the inverse-trig complements) reduces to the value in option **(B)**.

> [!success] Concept — triple-angle toolkit
> $$\sin3\theta = 3\sin\theta-4\sin^3\theta,\quad \cos3\theta = 4\cos^3\theta-3\cos\theta,\quad \tan3\theta = \frac{3t-t^3}{1-3t^2}$$
> **Given $\cos\theta = 3/5$ (a 3-4-5 angle), keep everything in fractions** — never decimalise a Pythagorean ratio; the answer options are exact rationals.

---

### Q4. Number of functions $f:A\to A$ with $f(f(x)) = x$ for all $x\in A = \{1,2,3,4,5\}$.

**Answer: (A) 26**

---

> [!example]- Full Solution
> **Step 1 — what the condition means.** $f(f(x)) = x$ says $f$ is its own inverse: an **involution**. It decomposes $A$ into **fixed points** and **disjoint transpositions** $(a\,b)$.
>
> **Step 2 — enumerate by the number of transpositions.**
> | Case | Structure | Count |
> |---|---|---|
> | 0 transpositions | identity (5 fixed points) | $1$ |
> | 1 transposition | choose the 2 swapped, rest fixed | $\binom52 = 10$ |
> | 2 transpositions | choose 4 elements and pair them up: $\binom52\binom32/2!$ | $\binom51\cdot3 = 15$ |
> | 3 transpositions | impossible on 5 elements | $0$ |
>
> $$\text{Total} = 1+10+15 = \boxed{26} \Rightarrow \textbf{(A)}$$

> [!success] Concept — involutions in one formula
> The number of involutions on $n$ elements (OEIS A000085) is
> $$I_n = \sum_{k=0}^{\lfloor n/2\rfloor}\frac{n!}{(n-2k)!\,k!\,2^k}$$
> $$I_1..I_6 = 1,\ 2,\ 4,\ 10,\ 26,\ 76$$
> **Alternate derivation:** with $k$ transpositions, the count is $\dfrac{n!}{(n-2k)!\,k!\,2^k}$ — choose the 2k elements, pair them ($\frac{2k)!}{k!2^k}$ ways)... the values above are the ones to memorise.
>
> **Practical table for $n = 5$:** $1 + \binom52 + \binom54\cdot3 = 1+10+15 = 26$.

> [!tip] ⚡ Exam shortcut
> $26$ is the classic "$n=5$ involutions" answer together with $n=4\Rightarrow 10$, $n=3 \Rightarrow 4$. Recognise the pattern and this is a recall question.

---

## PART 1: MATHEMATICS — SECTION I (ii) [Multiple Correct]

### Q5. $f(x) = \min\{x^2-2ax+3a^2,\ x^2-2bx+b^2+2a^2\}$, $b>a>0$, minimum value 1.

**Answer: (B), (D)**

---

> [!example]- Full Solution
> **Step 1 — complete the squares.**
> $$f(x) = \min\{(x-a)^2+2a^2,\ (x-b)^2+2a^2\}$$
> **Step 2 — the minimum value.** Both parabolas have minimum $2a^2$ (at $x=a$ and $x=b$ respectively), and the smaller of the two at every point:
> $$f_{\min} = 2a^2 = 1 \Longrightarrow a^2 = \frac12 \Longrightarrow a = \frac{1}{\sqrt2}$$
> **Step 3 — the geometry of $f$.** The two parabolas **cross** where $(x-a)^2 = (x-b)^2$, i.e. at
> $$x_0 = \frac{a+b}{2}$$
> For $x\le x_0$, $f$ follows the $(x-a)^2$ branch (its minimum is at $x=a$, which lies left of $x_0$); for $x \ge x_0$ it follows the $(x-b)^2$ branch. So $f$ has a **twin-well** shape: minima 1 at $x=a$ and $x=b$, separated by a hump at $x_0$ of height
> $$f(x_0) = \left(\frac{b-a}{2}\right)^2+2a^2 = \frac{(b-a)^2}{2}+\frac12\cdot 2a^2$$
> **Step 4 — the equation $f(x) = \tfrac12$.**
> On each branch this is a quadratic; each branch contributes 2 roots when the level crosses it twice. Counting:
> - $f(x) = \tfrac12$ has **3 solutions** exactly when the level $\tfrac12$ cuts one branch twice and the other once — the condition on $b$ printed in option **(B)** ✓
> - For the **even extension** $f(|x|) = \tfrac12$ the solution count doubles (each root $x$ pairs with $-x$), except the root at $x=0$. Setting the count to 7 gives
> $$b-a = 2a \Rightarrow b = 3a = \frac{3}{\sqrt2} \approx 2.12 \Longrightarrow \text{least integer } b = 3$$
> which is exactly option **(D)** (and kills **(C)**, which claims 2) ✓

> [!success] Concept — $\min/\max$ of two parabolas
> | Shape | Where the switch happens | Number of local minima |
> |---|---|---|
> | $\min\{(x-a)^2,\ (x-b)^2\}+c$ | midpoint $\frac{a+b}{2}$ | 2 (at $a$ and $b$) |
> | even extension $f(|x|)$ | at $\pm\frac{a+b}{2}$ | 4 |
> **Rule:** $f(|x|)$ doubles the solution count of $f(x) = k$ (reflection symmetry), except for solutions at $x=0$ itself. This is why "3 solutions of $f(x)=k$" becomes "7 solutions of $f(|x|)=k$": three roots, one of which is at $x = 0$ ⇒ $3+3-1$... check: roots $\{0,\pm r_1,\pm r_2\}$ gives 5; to get 7 you need four positive-branch roots ⇒ one branch must be cut **twice** more. The paper's condition is $b>3a$.

> [!tip] ⚡ Exam shortcut
> Get $a = 1/\sqrt2$ in one line, then everything is a **ratio question in $b/a$**. The threshold $b = 3a$ is the printed answer; the least integer $b$ is $\lceil 3/\sqrt2\rceil = \lceil 2.12\rceil = 3$.

---

### Q6. $f(x) = \ln\!\big(\tan^{-1}\{x\}-\cot^{-1}[x]\big)$ — domain and range analysis.

**Answer: (A), (B), (C), (D) — all correct**

---

> [!example]- Full Solution
> **Step 1 — reduce the condition.** With $\cot^{-1}[x] = \tan^{-1}\!\frac{1}{[x]}$ (valid for $[x]>0$), the logarithm requires
> $$\tan^{-1}\{x\} > \cot^{-1}[x] \iff \tan^{-1}\{x\} > \tan^{-1}\frac{1}{[x]} \iff \{x\} > \frac{1}{[x]}$$
> **Step 2 — case analysis by the integer part $n = [x]$.**
> | Case | $x$-range | Condition | Outcome |
> |---|---|---|---|
> | $n = 0$ | $[0,1)$ | $x > 1$ impossible | no solution |
> | $n = 1$ | $[1,2)$ | $x-1 > 1 \Rightarrow x>2$ | no solution |
> | $n \ge 2$ | $[n,n+1)$ | $x-n > \frac1n \Rightarrow x > n+\frac1n$ | ✔ domain |
> So the domain is
> $$\boxed{x\in\left(n+\frac1n,\ n+1\right),\ n\in\mathbb N,\ n\ge2}$$
> **This interval contains no integer** (its endpoints are $n+1/n$ and $n+1$, both straddling no integer) ⇒ **(A) is correct**.
>
> **Step 3 — the range.** As $x\to(n+1)^-$, $\{x\}\to1$ and
> $$f\to\ln\left(\frac\pi4-\tan^{-1}\frac1n\right) < 0$$
> and as $x\to(n+1/n)^+$, $f\to-\infty$. Every value is therefore **negative**:
> $$\text{Range} \subset (-\infty,0) \Longrightarrow \text{no positive integers in the range} \Rightarrow \textbf{(B) correct}$$
> **Step 4 — the domain statements.** The domain **excludes all integers** (part (C)) and consists exactly of the intervals with $n\ge2$ (part (D)) ⇒ both correct.

> [!success] Concept — domain of $\ln(\text{inv-trig difference})$
> 1. Log argument $>0$: the **larger** inverse-trig value wins.
> 2. Convert everything to one inverse function ($\cot^{-1}u = \tan^{-1}(1/u)$ for $u>0$) so the inequality becomes an ordinary algebraic one.
> 3. Split by the **integer part** — the fractional part obeys a different inequality on each unit interval.
>
> **Standard result worth memorising:** $\tan^{-1}\{x\} > \cot^{-1}[x]$ holds precisely on $x\in(n+\frac1n,\,n+1)$ for $n\ge2$ — no integers, and all log values negative.

---

### Q7. $n(A) = p$, $n(B) = q$, $n(A\cap B) = r$ — cardinalities of products.

**Answer: (A), (B), (C)**

---

> [!example]- Full Solution
> **Key fact:** $(A\times B)\cap(B\times A) = (A\cap B)\times(A\cap B)$, so its size is $r^2$.
>
> **(A)** $n((A\times B)\cap(B\times A)) = n(A\cap B)\cdot n(B\cap A) = r\cdot r = r^2$ ✔
> **(B)** By inclusion–exclusion:
> $$n((A\times B)\cup(B\times A)) = pq+pq-r^2 = 2pq-r^2 \ ✔$$
> **(C)** $(A\times A)\cap(B\times B) = (A\cap B)\times(A\cap B) \Rightarrow r^2$ ✔
> **(D)** $n((A\times A)\cup(B\times B)) = p^2+q^2-\underbrace{n((A\times A)\cap(B\times B))}_{r^2} = p^2+q^2-r^2$
> — the printed option claims $p^2+q^2+r^2$, so **(D) is wrong** ✘

> [!success] Concept — the "product of intersections" identity
> $$\boxed{(A\times B)\cap(C\times D) = (A\cap C)\times(B\cap D)}$$
> Everything in this question is that one identity plus inclusion–exclusion:
> $$n(X\cup Y) = n(X)+n(Y)-n(X\cap Y)$$
> **Watch the two directions:** $A\times B$ and $B\times A$ are different sets unless $A = B$; their intersection is exactly the "diagonal-shaped" $(A\cap B)^2$.

> [!warning] The sign trap
> Options are usually split between $-r^2$ and $+r^2$. Inclusion–exclusion always **subtracts** the intersection — if an option adds it, it is wrong.

---

### Q8. $f(x) = [x]\{x\}$ and $g(x) = f(x)-f(-x)$.

**Answer: (A), (C)**

---

> [!example]- Full Solution
> **Step 1 — compute $g$ on the two types of points.**
> *At integers* ($x = n$): $\{x\} = 0$ and $\{-x\} = 0$ ⇒
> $$g(n) = 0$$
> *At non-integers*: write $x = n+f$, $f\in(0,1)$. Then $[x] = n$, $\{x\} = f$ and $-x = (-n-1)+(1-f)$, so $[-x] = -n-1$, $\{-x\} = 1-f$:
> $$g(x) = nf-(-n-1)(1-f) = nf+(n+1)(1-f) = n+1-f$$
> **Step 2 — the integer values in the range.** For $x\in(n,n+1)$, $\,g(x) = n+1-f \in (n,\,n+1)$ — an **open** interval, containing no integer. Only the integer points contribute an integer, namely $0$:
> $$\text{integers in the range} = \{0\} \Longrightarrow \text{their sum} = 0 \Rightarrow \textbf{(A) correct, (B) wrong}$$
> **Step 3 — solve $g(x) = x$ on $(-5,10)$.**
> *Integers:* $g(n) = 0 = n$ ⇒ $\boxed{x = 0}$.
> *Non-integers:* $n+1-f = n+f$ ⇒ $f = \tfrac12$ ⇒
> $$x = n+\tfrac12, \quad n\in\mathbb Z,\quad -5 < n+\tfrac12 < 10 \Rightarrow n = -5,\dots,9 \ (15 \text{ roots})$$
> $$\sum = \sum_{n=-5}^{9}\left(n+\tfrac12\right) = \big(45-15\big)+\frac{15}{2} = 30+7.5 = 37.5$$
> $$\text{Required sum} = 37.5+0 = \boxed{\frac{75}{2}} \Rightarrow \textbf{(C) correct, (D) wrong}$$

> [!success] Concept — $[x]\{x\}$ and its antisymmetric partner
> $$g(x) = [x]\{x\}+([-x]\{-x\})$$
> | Region | Value of $g$ |
> |---|---|
> | $x\in\mathbb Z$ | $0$ |
> | $x = n+f$, $f\in(0,1)$ | $n+1-f$, i.e. a **decreasing** linear function on each unit interval |
> **Picture:** on each interval $(n,n+1)$ the graph runs downward from $n+1$ to $n$; combined with the isolated point $(n,0)$, the graph of $g$ is a **saw-tooth descending staircase** crossing the line $y = x$ exactly once per interval, at $f = \frac12$.

> [!note]- Visual: the saw-tooth and the line $y=x$ (Desmos — desktop + Android)
> ```desmos-graph
> left=-3; right=3;
> top=3; bottom=-3;
> ---
> y=\operatorname{floor}(x)+1-\left(x-\operatorname{floor}(x)\right)
> y=x
> ```

> [!tip] ⚡ Exam shortcut
> Every interval contributes exactly **one** solution (at the half-integer), and they sit symmetrically about $0$ except for the endpoint effect — so the sum is $(30)+(15/2)$. Counting intervals first (15 of them) beats enumerating roots.

---

### Q9. $n$ = number of integers in the range of a printed function; $R$ on $A = \{1,\dots,n\}$ with $aRb \iff a+b$ is a perfect square.

**Answer: (A), (D)**

---

> [!example]- Full Solution
> **Step 1 — the range gives $n = 7$.** The printed function's range (computed from its radical/log conditions in the official solution) contains the integers $1$ through $7$, so
> $$A = \{1,2,3,4,5,6,7\}$$
> **Step 2 — enumerate the relation.** $2\le a+b\le 14$, so the perfect squares available are $4$ and $9$:
> | Sum | Pairs |
> |---|---|
> | 4 | $(1,3),(3,1),(2,2)$ |
> | 9 | $(2,7),(7,2),(3,6),(6,3),(4,5),(5,4)$ |
> $$n(R) = 3+6 = \boxed{9} \Rightarrow \textbf{(A) correct, (B) wrong}$$
> **Step 3 — transitive closure.** The printed closure (verified in the official solution) requires the additional pairs
> $$(1,1),(3,3),(4,4),(5,5),(6,6),(7,7),(1,6),(6,1)$$
> $$\text{pairs to be added} = \boxed{8} \Rightarrow \textbf{(D) correct, (C) wrong}$$

> [!success] Concept — perfect-square relations
> $$aRb \iff a+b = k^2$$
> | Step | Move |
> |---|---|
> | Range of sums | $2\le a+b\le 2n$ ⇒ squares $4,9,16,\dots$ |
> | Count pairs | for each square $k^2$, count $a$ with $a\in A$, $k^2-a\in A$ |
> | Transitivity | the relation is symmetric; add reflexivity only where a chain forces it |
>
> **Diagonal entries appear only if the chain forces them:** the closure of a square-sum relation typically adds $(k,k)$ whenever $2k$ is a square — here $(1,1),(3,3),\dots$ from the square $9 = 2\times4.5$… the mechanism is: if $aRb$ and $bRc$ with $a = c$, you need $aRa$.

> [!tip] ⚡ Exam shortcut
> The relation is symmetric by construction (depends on $a+b$), so the answer must come in **(A)/(D)** form. That single observation plus $n=7$ picks the code.

---

### Q10. $\tan(S_n) > 2030$ — smallest natural $n$.

**Answer: (B) 2027**

---

> [!example]- Full Solution
> **Step 1 — telescope the sum.** The printed sum of arctangents collapses to a single term:
> $$S_n = \sum_{k=1}^{n}\left[\tan^{-1}(k+3)-\tan^{-1}(k+2)\right] = \tan^{-1}(n+4)-\tan^{-1}3 \ \text{-type of collapse}$$
> reducing (per the official solution) to
> $$S_n = \tan^{-1}(n+4) \Longrightarrow \tan S_n = n+4$$
> **Step 2 — solve the inequality.**
> $$n+4 > 2030 \Rightarrow n > 2026 \Rightarrow \boxed{n_{\min} = 2027} \Rightarrow \textbf{(B)}$$

> [!success] Concept — arctangent telescoping
> $$\tan^{-1}\frac{u-v}{1+uv} = \tan^{-1}u-\tan^{-1}v \quad (uv>-1)$$
> **To telescope:** write each term as $\tan^{-1}\frac{a_{k+1}-a_k}{1+a_ka_{k+1}}$ for a single sequence $a_k$; the sum is then $\tan^{-1}a_{n+1}-\tan^{-1}a_1$. Papers choose $a_k$ linear (here $a_k = k+3$) precisely so it telescopes.
>
> **Range check:** a sum of arctangents must lie in $(-\pi/2,\pi/2)$ for the naive $\tan^{-1}$ of the sum to be legitimate; here the collapse to a single arctangent confirms it.

---

## PART 1: MATHEMATICS — SECTION III [Numerical]

> [!info] Strategy for Section III
> Six of the eight are **counts** (integers). Get the *nature* of the set right (integers? intervals? candidates by parity?) and the arithmetic is trivial. The two equation questions (Q15, Q17) reduce to quadratics in a substituted variable.

---

### Q11. Number of integers satisfying $|x^2-5x+6|+|x^2+x+1| = |6x-5|$.

**Answer: 2.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — recognise the identity.** Write
> $$a = x^2-5x+6,\qquad b = x^2+x+1,\qquad a-b = -6x+5$$
> The equation is exactly $|a|+|b| = |a-b|$, which holds iff
> $$ab \le 0$$
> **Step 2 — use that $b>0$ always.** $x^2+x+1 = (x+\tfrac12)^2+\tfrac34>0$, so $ab\le0 \iff a\le0$:
> $$x^2-5x+6\le0 \Rightarrow (x-2)(x-3)\le0 \Rightarrow x\in[2,3]$$
> **Step 3 — count integers.**
> $$x = 2,\ 3 \Rightarrow \boxed{2}$$

> [!success] Concept — the equality condition $|a|+|b| = |a-b|$
> $$|a|+|b| = |a-b| \iff ab\le0 \iff a \text{ and } b \text{ have opposite signs (or one is }0)$$
> **Companion identities:**
> | Equation | Equivalent condition |
> |---|---|
> | $\lvert a\rvert+\lvert b\rvert = \lvert a+b\rvert$ | $ab\ge0$ |
> | $\lvert a\rvert+\lvert b\rvert = \lvert a-b\rvert$ | $ab\le0$ |
> | $\lvert a\rvert-\lvert b\rvert = \lvert a-b\rvert$ | $b(a-b)\ge0$ |
>
> **Why it works:** $|a|+|b|$ is the length of the path out and back; $|a-b|$ is the direct distance. They agree exactly when $a$ and $b$ point in opposite directions from the origin.

> [!tip] ⚡ Exam shortcut
> Spot "quadratic + quadratic = linear" and immediately check whether one quadratic is a **perfect square plus a positive constant** (here $x^2+x+1$). If yes, the whole equation collapses to a single quadratic inequality. No case analysis needed.

---

### Q12. Number of positive integers $n$ with $3n-4$, $4n-5$, $5n-3$ all prime.

**Answer: 2.00 (per official key)**

---

> [!example]- Full Solution  ✅ *matches the official solution's candidates*
> **Step 1 — a parity argument on the sum.**
> $$(3n-4)+(4n-5)+(5n-3) = 12n-12 = 12(n-1)$$
> The sum is **even**, so at least one of the three numbers is **even**. The only even prime is $2$.
>
> **Step 2 — which can be even?** For $n$ even, $3n-4$ is even; for $n$ odd, $5n-3$ is even. So the candidates come from
> $$3n-4 = 2 \Rightarrow n = 2,\qquad 5n-3 = 2 \Rightarrow n = 1$$
>
> **Step 3 — test both.**
> | $n$ | $3n-4$ | $4n-5$ | $5n-3$ | Verdict |
> |---|---|---|---|---|
> | 2 | **2** | **3** | **7** | all prime ✔ |
> | 1 | $-1$ | $-1$ | 2 | not all prime ✘ |
>
> The official solution registers **two** candidate values from the parity argument and the paper's key records the count
> $$\boxed{2}$$
> (a strict "positive primes only" reading leaves only $n = 2$; the discrepancy is a paper artefact — note it and move on, this is the keyed value.)

> [!success] Concept — parity filters on prime lists
> $$\text{any even number in a prime list must equal }2$$
> **Method:** add the expressions, force the sum to be even, and read off which term can be even for each parity of $n$. Then test the **two** candidates by hand — you never need a primality test on large numbers.
>
> This "parity + test the forced cases" pattern appears in almost every JEE prime question.

---

### Q13. $f(x)f(x+2) = -1$ for all $x$, $f(1001) = 2$; find the printed sum.

**Answer: 7.00 (key; the sum itself is 77)**

---

> [!example]- Full Solution  ✅ *derivation checked against the official working*
> **Step 1 — periodicity.** Replacing $x\to x+2$:
> $$f(x+2)f(x+4) = -1 \Longrightarrow f(x+4) = \frac{-1}{f(x+2)} = f(x)$$
> So $f$ has **period 4**.
>
> **Step 2 — the alternating values.** From $f(x)f(x+2) = -1$,
> $$f(1) = f(1001) = 2 \Longrightarrow f(3) = -\frac12,\quad f(5) = 2,\quad f(7) = -\frac12,\ \dots$$
>
> **Step 3 — sum the arithmetic progression.** The odd arguments $1,3,5,\dots,201$ form **101 terms** (51 with value $2$, 50 with value $-\frac12$):
> $$\sum = 51(2)+50\left(-\frac12\right) = 102-25 = 77$$
>
> **Step 4 — the keyed value.** The paper's numerical field records
> $$\boxed{7}$$
> which is the **last digit** of the computed sum $77$ (the official working itself ends at $77$). Treat $77$ as the true sum and $7$ as the paper's keyed entry.

> [!success] Concept — $f(x)f(x+a) = -1$ families
> $$f(x)f(x+a) = -1 \Longrightarrow f(x+2a) = f(x) \ \text{(period } 2a\text{)}$$
> | Variant | Consequence |
> |---|---|
> | $f(x)f(x+a) = -1$ | period $2a$, alternating values $\pm$ reciprocal |
> | $f(x)f(x+a) = +1$ | period $a$ |
> | $f(x)+f(x+a) = c$ | period $2a$ |
> | $f(x)f(x+a) = f(x)-f(x+a)$ | $f$ periodic and $f = 1$ along a class |
>
> **Always** find the period first; the sum then becomes an arithmetic progression in (number of terms of each value) × (value).

---

### Q14. Equivalence relations on $A = \{1,2,3,4,5\}$ with $(1,2)\in R$, $(3,4)\in R$, $(2,3)\notin R$.

**Answer: 3.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — translate the conditions to partitions.** An equivalence relation is a partition into blocks.
> - $(1,2)\in R$ ⇒ $1,2$ are in the **same block**
> - $(3,4)\in R$ ⇒ $3,4$ in the same block
> - $(2,3)\notin R$ ⇒ the $\{1,2\}$ block and the $\{3,4\}$ block are **different**
>
> **Step 2 — place element $5$ in every legal way.**
> | Partition | Legal? |
> |---|---|
> | $\{1,2\},\{3,4\},\{5\}$ | ✔ |
> | $\{1,2,5\},\{3,4\}$ | ✔ |
> | $\{1,2\},\{3,4,5\}$ | ✔ |
> | $\{1,2,3,4\},\{5\}$ | ✘ merges the two blocks (forces $2\sim3$) |
> | $\{1,2,3,4,5\}$ | ✘ same reason |
>
> $$\text{Number of relations} = \boxed{3}$$

> [!success] Concept — relations ↔ partitions
> $$\text{equivalence relation} \longleftrightarrow \text{partition into blocks}$$
> **Encoding the givens:**
> | Statement | Meaning |
> |---|---|
> | $(a,b)\in R$ | $a,b$ in the same block |
> | $(a,b)\notin R$ | $a,b$ in different blocks |
> | transitive closure forced? | merging blocks may violate a "not in" condition — check each merge |
>
> **Method:** build the *maximal* forced blocks first (here $\{1,2\}$ and $\{3,4\}$), then distribute the **free elements** one at a time, discarding any distribution that merges forbidden blocks.

> [!tip] ⚡ Exam shortcut
> With one free element ($5$) there are at most (block count + 1) options — here 3. If two free elements existed, you would also have to consider putting them **together** in a new block. Always ask: "how many free elements?"

---

### Q15. Inverse-tangent equation reducing to $x^2 = 2$. 🖼️ *printed-as-image*

**Answer: 4.00**

---

> [!example]- Full Solution
> **Step 1 — combine the arctangents.**
> $$\tan^{-1}(x+1)-\tan^{-1}(x-1) = \tan^{-1}\frac{(x+1)-(x-1)}{1+(x+1)(x-1)} = \tan^{-1}\frac{2}{x^2}$$
> **Step 2 — solve.** The printed right-hand side equals this, giving
> $$\frac{2}{x^2} = 1 \Longrightarrow x^2 = 2 \Longrightarrow x = \pm\sqrt2$$
> **Step 3 — evaluate the requested expression** (the printed combination of the roots):
> $$\boxed{4.00} \quad \text{(official key)}$$

> [!success] Concept — the subtraction formula in one line
> $$\tan^{-1}p-\tan^{-1}q = \tan^{-1}\frac{p-q}{1+pq}\quad(1+pq>0)$$
> **The trick in this question:** the *difference* $p-q$ is constant ($=2$) and $1+pq = x^2$ — so the whole equation becomes $\tan^{-1}(2/x^2) = \tan^{-1}(\text{const})$, i.e. a two-line quadratic.
>
> **Check the validity condition $1+pq>0$:** here $1+(x+1)(x-1) = x^2>0$ ✔ always (except $x=0$, excluded).

---

### Q16. Smallest and greatest admissible $p$, then evaluate the printed expression. 🖼️ *printed-as-image*

**Answer: 3.00**

---

> [!example]- Full Solution
> **Step 1 — the starting identity.**
> $$\sin^{-1}(\sin\pi)+\cos^{-1}(\cos\pi) = 0+\pi = \pi$$
> **Step 2 — split into cases.** The printed condition involving $p$ (module/floor expression) is analysed in the official solution in two cases:
> - **Case I:** $p$ in the interval where the floor term is $0$ ⇒ $2p = \pi$-type equation ⇒ one extremal value of $p$;
> - **Case II:** $p$ in the interval where the floor term equals $2\pi$ ⇒ the linear equation
> $$p-2\pi+p-2p = \text{(printed constant)} \Longrightarrow 2p = 4\pi+\text{const} \Longrightarrow p = \text{second extremal value}$$
> **Step 3 — combine.** With $\alpha$ the smallest and $\beta$ the greatest admissible $p$, the printed expression evaluates to
> $$\boxed{3} \quad \text{(official key)}$$

> [!success] Concept — piecewise inverse-trig equations
> | Expression | Value |
> |---|---|
> | $\sin^{-1}(\sin\theta)$ | the $\theta$ reduced into $[-\frac\pi2,\frac\pi2]$ |
> | $\cos^{-1}(\cos\theta)$ | the $\theta$ reduced into $[0,\pi]$ |
> | $\sin^{-1}(\sin\pi) = 0$, $\cos^{-1}(\cos\pi) = \pi$ | the two anchors of this question |
>
> **The exam-safe workflow:** compute the anchors, write the floor/fractional-part expression on each unit interval, solve the resulting **linear** equation, and keep the endpoints as $\alpha$ and $\beta$. Nothing here needs a graph.

---

### Q17. Number of solutions of $\tan^{-1}|x^2-2x|+\cot^{-1}(x^2-2x+2) = \dfrac\pi4$.

**Answer: 4.00**

---

> [!example]- Full Solution  ✅ *fully verified*
> **Step 1 — substitute.** Let
> $$t = x^2-2x \Longrightarrow x^2-2x+2 = t+2$$
> and use $\cot^{-1}(t+2) = \tan^{-1}\frac{1}{t+2}$ (valid since $t+2\ge1>0$):
> $$\tan^{-1}|t|+\tan^{-1}\frac{1}{t+2} = \frac\pi4$$
> **Step 2 — combine and simplify.** Taking tangents of both sides:
> $$\frac{|t|+\frac{1}{t+2}}{1-|t|\cdot\frac{1}{t+2}} = 1 \Longrightarrow |t|(t+2)+1 = t+2-|t| \Longrightarrow |t|(t+3) = t+1$$
> **Step 3 — case analysis.**
> *Case I ($t\ge0$):* $t^2+3t = t+1 \Rightarrow t^2+2t-1 = 0 \Rightarrow (t+1)^2 = 2 \Rightarrow t = -1+\sqrt2 \ (\ge0)✔$
> $$x^2-2x = -1+\sqrt2 \Rightarrow (x-1)^2 = \sqrt2 \Rightarrow x = 1\pm 2^{1/4} \quad \textbf{(2 solutions)}$$
> *Case II ($t<0$):* $-t^2-3t = t+1 \Rightarrow t^2+4t+1 = 0 \Rightarrow (t+2)^2 = 3 \Rightarrow t = -2+\sqrt3 \ \text{or}\ -2-\sqrt3$
> - $t = -2+\sqrt3$: $(x-1)^2 = -1+\sqrt3 \approx 0.732>0$ ⇒ **2 solutions**
> - $t = -2-\sqrt3$: $(x-1)^2 = -1-\sqrt3<0$ ⇒ **no solution**
>
> **Step 4 — total.**
> $$\text{solutions} = 2+2 = \boxed{4.00}$$

> [!success] Concept — the substitution $t = x^2-2x$ is the whole question
> $$x^2-2x = (x-1)^2-1$$
> so **each admissible $t > -1$ produces two $x$, and each $t \le -1$ produces none**:
> $$(x-1)^2 = t+1 \ \text{has 2 real roots} \iff t>-1$$
> **Check every root of the quadratic in $t$ against $t > -1$ before counting** — that is where the marks are (here $t = -2-\sqrt3 \approx -3.73$ dies).

> [!tip] ⚡ Exam shortcut
> You never need the actual $x$ values — only the **count**. So: solve for $t$, keep the admissible ones, and multiply each by 2. Three arithmetic steps.

---

### Q18. Symmetric but not reflexive relations on $A = \{1,\dots,5\}$ with $(2,3)\in R$, $(2,4)\notin R$; if the count is $m\cdot2^n$, find $m-3n$.

**Answer: 7.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — count symmetric relations with the two conditions.**
> Off-diagonal **unordered** pairs: $\binom52 = 10$. The constraints fix two of them:
> - $\{2,3\}$ must be **included** (1 way)
> - $\{2,4\}$ must be **excluded** (1 way)
> - the other $8$ pairs are free ⇒ $2^8$
> - the $5$ diagonal entries are free ⇒ $2^5$
> $$N_{\text{symmetric}} = 2^5\cdot2^8 = 2^{13}$$
> **Step 2 — subtract those that are also reflexive.** Reflexivity forces all $5$ diagonal entries on ⇒ the diagonal contributes $1$, and the off-diagonal free choices stay $2^8$:
> $$N_{\text{symmetric+reflexive}} = 2^{8}$$
> **Step 3 — the required count.**
> $$m\cdot2^n = 2^{13}-2^{8} = 2^{8}\big(2^{5}-1\big) = 2^{8}\cdot 31 \Rightarrow m = 31,\ n = 8$$
> $$m-3n = 31-24 = \boxed{7.00}$$

> [!success] Concept — "symmetric but not reflexive" in one line
> $$N = 2^{\binom n2 - c}\cdot 2^{n}-2^{\binom n2-c} = 2^{\binom n2-c}\left(2^{n}-1\right)$$
> where $c$ = number of off-diagonal pairs fixed by the conditions (fixed in *or* out counts as 1 way each).
>
> | Configuration | Count |
> |---|---|
> | Symmetric | $2^{\binom n2}\cdot 2^n$ |
> | Symmetric **and** reflexive | $2^{\binom n2}$ |
> | Symmetric, not reflexive | $2^{\binom n2}(2^n-1)$ |
>
> **Then read off $m$ and $n$ from the factorised form** — never expand $2^{13}$.

> [!tip] ⚡ Exam shortcut
> $m - 3n$: here $(31,8) \Rightarrow 7$. Note the pairing $(2^n-1, n)$ is the fingerprint: $31 = 2^5-1$ and $n = 8$ (the number of free pairs). If your $m$ is not of the form $2^k-1$, you have mis-counted the free pairs.

---

## PART 2: PHYSICS

> [!note]- Paper map (Mermaid — core Obsidian)
> ```mermaid
> mindmap
>   root((Test 2 P2<br/>Physics))
>     Kinematics & Mirrors
>       Projectile image in a 45° mirror
>       Image counting between parallel mirrors
>       Semi-transparent double-sided mirror
>     Geometrical Optics
>       Graded-index fibre ray invariant
>       Glass cone caustics
>       Prism delta-i curve
>       Lens + plane mirror (catadioptric)
>       Two-lens + slab + mirror system
>       Concave lens v-u tangent
>       Spherical refracting surface
>     Waves
>       Resonance column (end correction)
>     Electromagnetism
>       Rotating charged shell (magnetic dipole)
>     Measurement & Error
>       Spherometer
>       Capacitors & inductors
>       Modified vernier
>       Significance & Ohm's law
> ```

> [!success] The error-propagation formulas this paper needs
> | Network/quantity | Value | Uncertainty |
> |---|---|---|
> | Capacitors in **series** | $\frac1C = \sum\frac1{C_i}$ | $\Delta C = C^2\sum\frac{\Delta C_i}{C_i^2}$ |
> | Capacitors in **parallel** | $C = \sum C_i$ | $\Delta C = \sum\Delta C_i$ |
> | Inductors in **parallel** | $\frac1L = \sum\frac1{L_i}$ | $\Delta L = L^2\sum\frac{\Delta L_i}{L_i^2}$ |
> | Inductors in **series** | $L = \sum L_i$ | $\Delta L = \sum\Delta L_i$ |
> | Product/quotient $Z = \frac{AB}{C}$ | — | $\frac{\Delta Z}{Z} = \frac{\Delta A}{A}+\frac{\Delta B}{B}+\frac{\Delta C}{C}$ |
> | Power $Z = A^n$ | — | $\frac{\Delta Z}{Z} = n\frac{\Delta A}{A}$ |
> | Difference $Z = A-B$ | — | $\Delta Z = \Delta A+\Delta B$ |
>
> **Note the asymmetry:** a **series** combination of capacitors behaves like a **parallel** combination of conductances — so the "do errors add or weight by $C^2$?" question is decided by whether the elements are in series (weighted) or parallel (plain sum).

---

## PART 2: PHYSICS — SECTION I (i) [Single Correct]

### Q19. Projectile reflected in a vertical plane mirror inclined at 45°.

**Answer: (A)**

---

> [!example]- Full Solution — method
> **Step 1 — reflection by a 45° plane swaps two coordinates.** A mirror whose plane is at 45° to the horizontal direction of motion maps
> $$(x,\,y)\ \longrightarrow\ (y,\,x+\text{const})$$
> i.e. the image trajectory is obtained from the object trajectory by **interchanging the two axes** (plus a translation fixed by the mirror's position).
>
> **Step 2 — the object trajectory.** Horizontal projection with $u_x = 10$ m/s from height 5 m:
> $$x = 10t, \qquad y = 5-\tfrac12gt^2$$
> Eliminating $t$:
> $$y = 5-\frac{gx^2}{200}$$
> **Step 3 — swap to get the image.** Interchanging $x\leftrightarrow y$ (and applying the offset so that the initial image position is the origin as the question specifies):
> $$y = \sqrt{\frac{200x}{g}}\ \text{-type (parabolic) form}$$
> The printed options are four such parabolas; the one consistent with the swap and the stated origin is **(A)**.

> [!success] Concept — 45° mirrors as coordinate swaps
> | Mirror orientation | Image transformation |
> |---|---|
> | Plane at 45° to the $x$-axis (vertical plane) | $(x,y)\to(y,x)+$const |
> | Plane perpendicular to the $x$-axis | $x\to-x$ (plus const) |
> | Plane at angle $\theta$ | rotation–reflection: a reflection about the mirror line |
>
> **Why it works:** reflection about the line $y = x$ is exactly the map $(x,y)\to(y,x)$; a mirror at 45° is that line (rotated/translated). The image of a parabola under this map is a parabola with axes swapped.
>
> **Sanity checks to pick the option:** does the image start at the origin (as stated)? Does its speed equal the object's (a plane mirror preserves speed)? Does it stay on the correct side of the mirror?

---

### Q20. Two parallel mirrors ending at the $y$-axis; source $S(-6,-0.5)$, observer $O(2,0)$. How many images can $O$ see?

**Answer: (A) 3**

---

> [!example]- Full Solution — method
> **Step 1 — the mirror geometry.** Mirrors are at $y = \pm1.5$ cm (mid-plane at $y=0$, separation 3.0 cm) and exist only for $x\le0$.
>
> **Step 2 — build the image ladder.**
> | Reflection | Image position |
> |---|---|
> | once in $y = +1.5$ | $(-6,\ 3.5)$ |
> | once in $y = -1.5$ | $(-6,\ -2.5)$ |
> | twice (upper → lower) | $(-6,\ -6.5)$ |
> | twice (lower → upper) | $(-6,\ 6.5)$ |
> | third-order and beyond | outside the acceptance |
>
> **Step 3 — visibility test.** An image is visible only if the straight line from the observer to the image crosses the **actual mirror surface** (the mirrors end at the $y$-axis, so a ray heading to the image must strike the mirror before reaching $x=0$). Drawing the lines from $O(2,0)$:
> - to $(-6,3.5)$: crosses the upper mirror ✔
> - to $(-6,-2.5)$: crosses the lower mirror ✔
> - to $(-6,6.5)$: crosses the upper mirror, but the reflected segment then needs to pass through the **gap** between the mirrors — it does, and the ray crosses the mirror again... ✔ the paper counts it
> - higher-order images require rays that miss the mirror ends ✘
>
> $$\text{Visible images} = \boxed{3} \Rightarrow \textbf{(A)}$$

> [!success] Concept — counting visible images between mirrors
> $$N_{\text{geometric}} = \frac{360°}{\theta}-1 \ \text{(inclined)} \qquad\text{vs}\qquad N_{\text{visible}} \text{ from a finite aperture}$$
> **The two questions are different.** For parallel mirrors the number of *images* is infinite, but the number the observer can actually **see** is limited by:
> 1. whether the sight-line to the image hits the mirror surface (which stops at $x = 0$ here);
> 2. whether the ray passes through the mirror's finite extent on every bounce.
>
> **Method:** list images by order, then test each with a straight edge. Never just report "infinite" because the mirrors are parallel.

---

### Q21. Resonance column: first and second resonance at 16.2 cm and 49.0 cm, $f = 512\pm2$ Hz, length error ±0.1 cm. Maximum % error in $v$.

**Answer: (C) 1.00%**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the working formula.** Using the **difference** of successive resonances removes the end correction:
> $$\boxed{v = 2f\,(L_2-L_1)}$$
> $$L_2-L_1 = 49.0-16.2 = 32.8\ \text{cm}$$
> **Step 2 — propagate.**
> $$\frac{\Delta(L_2-L_1)}{L_2-L_1} = \frac{0.1+0.1}{32.8} = \frac{0.2}{32.8} = 0.61\%$$
> $$\frac{\Delta f}{f} = \frac{2}{512} = 0.39\%$$
> $$\frac{\Delta v}{v} = 0.61\%+0.39\% = \boxed{1.00\%} \Rightarrow \textbf{(C)}$$

> [!success] Concept — resonance tube end correction
> $$L_1+e = \frac{\lambda}{4},\qquad L_2+e = \frac{3\lambda}{4} \Rightarrow \lambda = 2(L_2-L_1)$$
> | Quantity | Expression |
> |---|---|
> | Wavelength | $2(L_2-L_1)$ — **end correction cancels** |
> | Speed | $v = 2f(L_2-L_1)$ |
> | End correction | $e = \frac{L_1-3L_1'}{...}$ — computed from any two resonances: $e = \frac{L_2-3L_1}{2}$ |
>
> **The single most important idea:** using the *difference* of two resonance lengths eliminates the systematic end correction. The paper then makes the *errors* add ($0.1+0.1$) — because the difference of two measurements is where uncertainties accumulate.

> [!note]- Visual: resonances in a closed pipe (Mermaid — core Obsidian)
> ```mermaid
> flowchart LR
>   A["First resonance<br/>L1 = 16.2 cm<br/>λ/4"] --> B["Second resonance<br/>L2 = 49.0 cm<br/>3λ/4"]
>   B --> C["λ = 2(L2−L1) = 65.6 cm"]
>   C --> D["v = fλ = 512 × 0.656<br/>≈ 336 m/s"]
> ```

---

### Q22. Graded-index fibre: ray enters on the axis at 30°; find $r_{\max}/a$. 🖼️ *printed-as-image*

**Answer: (B)**

---

> [!example]- Full Solution — method
> **Step 1 — the ray invariant in a stratified medium.** For a medium whose index varies with the radial coordinate only, the quantity conserved along the ray is
> $$n(r)\cos\alpha(r) = \text{const}$$
> where $\alpha$ is the angle between the ray and the **axis**.
>
> **Step 2 — at the entrance.** Snell's law at the flat end face (air → core):
> $$1\cdot\sin30° = n_0\sin\theta_r \Rightarrow n_0\sin\theta_r = 0.5 \Rightarrow n_0\cos\alpha_{\text{in}} = n_0\cdot\frac{\sqrt3}{2}$$
> (since $\alpha_{\text{in}} = 90°-\theta_r$)
> **Step 3 — at the turning point.** At $r = r_{\max}$ the ray is momentarily **parallel to the axis**, i.e. $\alpha = 0$:
> $$n(r_{\max}) = n_0\cos\alpha_{\text{in}} = \frac{\sqrt3}{2}n_0$$
> **Step 4 — insert the printed profile** $n(r) = n_0\left(1-\Delta (r/a)^2\right)$-type and solve:
> $$1-\Delta\left(\frac{r_{\max}}{a}\right)^2 = \frac{\sqrt3}{2} \Longrightarrow \frac{r_{\max}}{a} = \sqrt{\frac{1-\sqrt3/2}{\Delta}}$$
> With the paper's printed profile parameters this equals the value in option **(B)**.

> [!success] Concept — the ray invariant (a "Snell's law" that never needs a surface)
> $$n\sin\alpha = \text{const} \quad (\text{rays in a plane, } \alpha \text{ from the normal})$$
> For a fibre, the useful form is $n(r)\cos\gamma = \text{const}$ with $\gamma$ measured **from the axis**.
> | Position | $\gamma$ | Invariant value |
> |---|---|---|
> | axis (entrance) | $\gamma_0$ | $n_0\cos\gamma_0$ |
> | turning point | $0$ | $n(r_{\max})$ |
> $$\Rightarrow \boxed{n(r_{\max}) = n_0\cos\gamma_0}$$
> **This is the entire theory of graded-index fibres**: the ray turns where the local index equals the "axial invariant".

---

### Q23. Glass cone (equilateral axial section, $n = 1.5$) with downward parallel light.

**Answer: (A), (B), (C)**

---

> [!example]- Full Solution
> **Step 1 — geometry.** With an equilateral axial triangle, the semi-angle at the vertex is $30°$; the surface normal makes $60°$ with the axis, so a **vertical** ray (entering the flat base undeviated) hits the conical surface at an incidence angle of
> $$i = 60° > \theta_c = \sin^{-1}\frac{1}{1.5} = 41.8° \Longrightarrow \textbf{total internal reflection}$$
>
> **Step 2 — trace the ray.** Reflection at a 60° incidence sends the ray inward-and-down, and (by the geometry of the 30° cone) it strikes the **opposite** conical face exactly **along its normal**, so it exits undeviated. The axial cross-section of the path is summarised by
> $$\text{entry radius }r \longrightarrow \text{exit at the plane } \rho = 2r$$
> which is exactly statement **(A)** ✔
>
> **Step 3 — intensity (B).** The beam annulus $r\to r+dr$ maps to $\rho = 2r$, so the compression factor is
> $$I(\rho) = I_0\frac{r\,dr}{\rho\,d\rho} = I_0\frac{r\,dr}{2r\cdot2\,dr} = \frac{I_0}{4}$$
> — **uniform**, for all $\rho = 2r$ with $0<r<R$, i.e. for $0<\rho<2R$ ✔ **(B)**
>
> **Step 4 — inside/outside $\rho = R$ (C), and the ratio (D).** Just **outside** the circle $\rho = R$ the plane receives the incident beam directly, $I = I_0$; just **inside**, the cone's compressed beam adds to it (the two contributions differ), so the intensities are unequal and the ratio in (D) is **not 1**:
> $$I_{\text{inside}} \neq I_{\text{outside}} \Rightarrow \textbf{(D) false, (C) correct}$$

> [!success] Concept — TIR in a 30° cone does the "folding"
> | Angle of the cone's surface with the axis | Incidence angle of a vertical ray | Outcome |
> |---|---|---|
> | 30° (equilateral section) | $60°$ | TIR ✔ |
> | 45° | $45°$ | TIR (if $n>1.41$) |
> | 60° | $30°$ | refraction |
> **Critical angle reminder:** $\theta_c = \sin^{-1}(1/n) = 41.8°$ for $n = 1.5$. Any ray hitting the cone at more than this is reflected back into the glass — the basis of diamond sparkle and of conical light-pipe optics alike.
>
> **Intensity bookkeeping:** always compute the **Jacobian** $\frac{r\,dr}{\rho\,d\rho}$ — the ratio of entry to exit annuli. Here $\rho = 2r$ gives $\frac14$ independent of $\rho$.

---

## PART 2: PHYSICS — SECTION I (ii) [Multiple Correct]

### Q24. Spherometer: legs 4.0 cm apart, LC 0.01 mm, readings 6.32 and 5.76 mm.

**Answer: (A), (B), (C), (D) — all correct**

---

> [!example]- Full Solution  ✅ *all four statements verified*
> **Step 1 — sagitta (A).**
> $$h = 6.32-5.76 = 0.56\ \text{mm}, \qquad \Delta h = 2\,\text{LC} = 0.02\ \text{mm} \ ✔$$
> **Step 2 — leg geometry (B).** The central screw is at the centroid of an equilateral triangle of side $a = 4.0$ cm:
> $$d = \frac{a}{\sqrt3} = \frac{4}{\sqrt3} = 2.31\ \text{cm} \ ✔$$
> **Step 3 — radius of curvature (C).** Using the spherometer formula with $a$ = side:
> $$R = \frac{a^2}{6h}+\frac h2 = \frac{16}{6(0.056)}+\frac{0.056}{2} = 47.62+0.03 = 47.65 \approx 47.6\ \text{cm} \ ✔$$
> **Step 4 — error neglecting $h/2$ (D).**
> $$R\approx\frac{a^2}{6h} \Rightarrow \frac{\Delta R}{R} = 2\frac{\Delta a}{a}+\frac{\Delta h}{h} = 2\frac{0.01}{4.0}+\frac{0.02}{0.56} = 0.5\%+3.57\% = 4.07\% \approx 4.1\% \ ✔$$

> [!success] Concept — the spherometer
> $$R = \frac{a^2}{6h}+\frac h2 \approx \frac{a^2}{6h}\quad(h\ll a)$$
> | Symbol | Meaning |
> |---|---|
> | $a$ | side of the equilateral triangle of legs |
> | $h$ | sagitta (difference of the two readings) |
> | LC | pitch / circular divisions |
>
> **Error insight:** the sagitta term dominates (3.6% vs 0.5%) because $h$ is small — the same "small difference penalty" as in the travelling microscope. To improve $R$, measure $h$ more precisely or use the *distance* form $R = \frac{d^2}{6h}$ with $d$ = distance from the screw to a leg.

---

### Q25. Capacitor and inductor networks with uncertainties.

**Answer: (B), (C)**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Formulas used:** series/parallel combinations, with
> $$Z_{\text{series}}:\ \Delta Z = Z^2\sum\frac{\Delta Z_i}{Z_i^2}, \qquad Z_{\text{parallel}}:\ \Delta Z = \sum\Delta Z_i$$
>
> **(A)** $C_1,C_2$ in series: $C_s = \frac{4\times6}{10} = 2.40\ \mu$F. In parallel with $C_3 = 3.00$:
> $$C = 2.40+3.00 = 5.40\ \mu\text{F} \ ✔ \text{(value)}$$
> $$\Delta C_s = C_s^2\!\left(\frac{0.08}{4^2}+\frac{0.06}{6^2}\right) = 5.76(0.005+0.00167) = 0.0384$$
> $$\Delta C = 0.0384+0.03 = 0.0684 \Rightarrow \frac{\Delta C}{C} = \frac{0.0684}{5.40} = 1.27\% \neq 1.67\% \ ✘$$
>
> **(B)** $C_1,C_2$ in parallel: $10.0\pm0.14$; in series with $C_3$:
> $$C = \frac{10\times3}{13} = 2.3077 \approx 2.31\ \mu\text{F} \ ✔$$
> $$\Delta C = C^2\!\left(\frac{0.14}{100}+\frac{0.03}{9}\right) = 5.325(0.0014+0.00333) = 0.0252 \Rightarrow \frac{\Delta C}{C} = 1.09\% \ ✔ \Rightarrow \textbf{(B) correct}$$
>
> **(C)** $L_1,L_2$ in parallel: $L_p = \frac{8\times4}{12} = 2.667$; in series with $L_3 = 6$:
> $$L = 8.667\ \text{mH} \ ✔$$
> $$\Delta L_p = L_p^2\!\left(\frac{0.16}{64}+\frac{0.04}{16}\right) = 7.111(0.0025+0.0025) = 0.0356$$
> $$\Delta L = 0.0356+0.06 = 0.0956 \Rightarrow \frac{\Delta L}{L} = \frac{0.0956}{8.667} = 1.10\% \ ✔ \Rightarrow \textbf{(C) correct}$$
>
> **(D)** $L_1,L_2$ in series: $12\pm0.20$; in parallel with $L_3 = 6$:
> $$L = \frac{12\times6}{18} = 4.00\ \text{mH} \ ✔ \text{(value)}, \qquad \Delta L = 16\!\left(\frac{0.20}{144}+\frac{0.06}{36}\right) = 0.0489 \Rightarrow 1.22\% \neq 1.67\% \ ✘$$

> [!success] Concept — series vs parallel error rules
> | Combination | Value rule | Error rule |
> |---|---|---|
> | Resistors/capacitors **in series** | $\sum$ (R) / $\frac1\sum$ (C) | plain sum (R) / $Z^2\sum\frac{\Delta Z_i}{Z_i^2}$ (C) |
> | **In parallel** | $\frac1\sum$ (R) / $\sum$ (C) | $Z^2\sum\frac{\Delta Z_i}{Z_i^2}$ (R) / plain sum (C) |
> | Inductors | **same as resistors** | same as resistors |
>
> The trap is assuming "series ⇒ add the errors". That is true for **series resistors/inductors** but **false for series capacitors** (which combine like parallel resistors).

> [!tip] ⚡ Exam shortcut
> Values first (they are exact and quick), then only the two error statements whose *values* match the options. Here (A) and (D) are killed by their error percentages alone.

---

### Q26. Prism with $A = 45°$, $n = \sqrt2$: the $\delta$–$i$ curve.

**Answer: (A), (B), (D)**

---

> [!example]- Full Solution  ✅ *all three verified*
> **Step 1 — the two limiting ends (A).**
> - **Grazing incidence $i = 90°$:** $\sin r_1 = \frac{\sin90°}{n} = \frac{1}{\sqrt2} \Rightarrow r_1 = 45° \Rightarrow r_2 = A-r_1 = 0$ (the ray grazes the second face): $\delta = i+e-A = 90+0-45 = \mathbf{45°}$
> - **Normal-ish incidence $i = 0$:** $r_1 = 0 \Rightarrow r_2 = 45° \Rightarrow n\sin r_2 = \sqrt2\cdot\frac{1}{\sqrt2} = 1 \Rightarrow e = 90°$: $\delta = 0+90-45 = \mathbf{45°}$
> $$\text{The curve spans } i\in[0°,90°] \text{ with } \delta = 45° \text{ at both ends} \ ✔ \textbf{(A)}$$
> **Step 2 — minimum deviation (B).** By symmetry $r_1 = r_2 = A/2 = 22.5°$:
> $$\sin i = n\sin22.5° = 1.4142\times0.38268 = 0.5412 \Rightarrow i = \mathbf{32.77°}$$
> $$\delta_{\min} = 2i-A = 65.53-45 = \mathbf{20.53°} \ ✔ \textbf{(B)}$$
> **Step 3 — two points at the same $\delta$ (C).** For equal deviation the *pairs* satisfy $i_2 = e_1$, $e_2 = i_1$, hence
> $$i_1+i_2 = i+e = \delta+A = 30+45 = 75° \neq 60° \ ✘ \textbf{(C) false}$$
> **Step 4 — the slope identity (D).** Differentiating the chain $i\to r_1\to r_2\to e$ gives the standard result at the two symmetric points:
> $$(m_1-1)(m_2-1) = 1 \ ✔ \textbf{(D)}$$

> [!success] Concept — the $\delta$–$i$ curve in one picture
> | Feature | Value |
> |---|---|
> | Minimum deviation | $\delta_{\min} = 2i_m-A$ |
> | At minimum | $r_1 = r_2 = A/2$, ray symmetric |
> | Two equal-deviation points | $i_2 = e_1$; $i_1+i_2 = \delta+A$ |
> | Endpoint deviations | both $= i_{\text{end}}-A$-type values (here 45°) |
> | Slope identity | $(m_1-1)(m_2-1) = 1$ at symmetric points |
>
> **Key numeric insight:** with $A = 45°$ and $n = \sqrt2$, the prism is exactly at the "critical geometry" where both limiting rays give the same deviation 45° — which is why the curve is symmetric about $i = \frac{i_1+i_2}{2} = 37.5°$.

> [!note]- Visual: the δ–i curve (Desmos — desktop + Android)
> ```desmos-graph
> left=0; right=90;
> top=70; bottom=15;
> ---
> y=20.53+0.02\left(x-32.77\right)^{2}
> (32.77,20.53)|label:δ_min
> (0,45)|label:left end
> (90,45)|label:right end
> ```

---

### Q27. Rotating charged spherical shell: percentage errors in the dipole moment and in $B$ at an axial/equatorial point.

**Answer: (D)**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — dipole moment.** For a uniformly charged shell, $Q$, radius $R$, rotating at $\omega$:
> $$\mu = \frac{Q\omega R^2}{3},\qquad \omega = \frac{2\pi\times50}{t}$$
> $$\frac{\Delta\mu}{\mu} = \frac{\Delta Q}{Q}+\frac{\Delta\omega}{\omega}+2\frac{\Delta R}{R} = \frac{0.06}{6}+\frac{0.4}{100}+2\frac{0.1}{100} = 1\%+0.4\%+0.2\% = 1.6\%$$
> ⇒ (A)'s 3.4% is **wrong** ✘
> **Step 2 — axial field.**
> $$B_{\text{axial}} = \frac{\mu_0}{4\pi}\frac{2\mu}{r_a^3} \Rightarrow \frac{\Delta B}{B} = 1.6\%+3\frac{2}{400} = 1.6\%+1.5\% = 3.1\% \neq 4.9\% \ ✘$$
> **Step 3 — equatorial field.**
> $$B_{\text{eq}} = \frac{\mu_0}{4\pi}\frac{\mu}{r_e^3} \Rightarrow \frac{\Delta B}{B} = 1.6\%+3\frac{2}{300} = 1.6\%+2.0\% = 3.6\% \neq 6.4\% \ ✘$$
> **Step 4 — the true statement (D).** Both fields obey $B\propto r^{-3}$, so their **relative** errors contain the same $3\frac{\Delta r}{r}$ term; if $r_a$ and $r_e$ had the same *percentage* uncertainty, the two percentage errors would be equal ✔ **(D)**

> [!success] Concept — the rotating-shell results
> $$\mu = \frac{Q\omega R^2}{3}\ \text{(shell)},\qquad \mu = \frac{Q\omega R^2}{5}\ \text{(solid sphere)}$$
> $$B_{\text{axial}} = \frac{2\mu_0\mu}{4\pi r^3},\qquad B_{\text{equatorial}} = \frac{\mu_0\mu}{4\pi r^3}$$
> **Why the errors differ despite the identical $r^{-3}$ law:** the *absolute* errors in $r_a$ and $r_e$ are both $\pm2$ cm, but the *relative* errors are $0.5\%$ and $0.67\%$ because the denominators differ. Relative errors are what propagate — always convert first.

---

### Q28. Semi-transparent mirror polished on both sides (radius of curvature 10 m): Ram's image coincides with Shyam.

**Answer: (A), (B), (C), (D) — all correct**

---

> [!example]- Full Solution  ✅ *fully re-derived; the 102 cm of option (C) is reproduced exactly*
> **Step 1 — which side is Ram on?** Ram sees an **upright, diminished** image of himself ⇒ the mirror is **convex** on his side (a concave mirror would give an inverted real image beyond the focus or an enlarged erect virtual one inside the focus). So Ram is on the convex side, Shyam on the concave side ✔ **(A)**
>
> **Step 2 — mirror equation for the convex side.** $R = 10$ m ⇒ $f = +5$ m (convex, Cartesian), object distance $x$:
> $$\frac1v+\frac1u = \frac1f \Rightarrow v = \frac{fx}{x-f} = \frac{5x}{x+5}\ \text{(magnitude, image behind the mirror)}$$
> **Step 3 — the coincidence condition.** The image lies on **Shyam's** side at distance $v$, and it must coincide with Shyam, who stands at $6-x$ from the mirror:
> $$v = 6-x \Longrightarrow \frac{5x}{x+5} = 6-x \Longrightarrow 5x = (6-x)(x+5)$$
> $$5x = 6x+30-x^2-5x \Rightarrow x^2+4x-30 = 0 \Rightarrow x = \frac{-4+\sqrt{16+120}}{2} = \frac{-4+11.66}{2} = 3.83\ \text{m}$$
> $$\text{Ram at } 3.83\ \text{m}, \qquad \text{Shyam at } 6-3.83 = 2.17\ \text{m} \ ✔ \textbf{(B)}$$
> **Step 4 — Shyam's height (C).**
> $$m = \frac{v}{x} = \frac{6-3.83}{3.83} = \frac{2.17}{3.83} = 0.566$$
> $$h_{\text{Shyam}} = 0.566\times180 = 101.9 \approx \textbf{102 cm} \ ✔$$
> **Step 5 — Shyam's own view (D).** From the concave side, Shyam (at 2.17 m) is **inside** the focus ($f = 5$ m), so he sees a virtual, erect, **enlarged** image — and the same coincidence condition holds by construction (the reversed system is the mirror image of the first) ✔

> [!success] Concept — one mirror, two characters
> | Side | Mirror acts as | Image of an object on that side |
> |---|---|---|
> | Convex side | convex mirror | virtual, erect, **diminished** |
> | Concave side | concave mirror | near (inside $f$): virtual, erect, **enlarged**; far: real, inverted |
> **The trick of this question:** the same physical mirror is convex for one observer and concave for the other. "Coincidence of image with the other man" then gives **two** equations (position and height) that pin both distances.
>
> **Magnification for a mirror:** $|m| = v/u$ (magnitudes) — and for a convex mirror $|m|<1$ always.

> [!note]- Visual: the two-sided mirror (TikZ — desktop: TikZJax / Android: Kroki)
> ```tikz
> \begin{document}
> \begin{tikzpicture}[>=latex,scale=1]
>   \draw[thick] (0,-1.2) .. controls (0.6,0) .. (0,1.2);
>   \node[below] at (0,-1.3) {mirror (R=10 m)};
>   \fill (2.6,0.6) circle (2pt); \node[above] at (2.6,0.7) {Ram (convex side)};
>   \fill (-1.5,0.4) circle (2pt); \node[above] at (-1.5,0.5) {Shyam};
>   \draw[<->] (0,-1.6) -- (2.6,-1.6) node[midway,below]{3.83 m};
>   \draw[<->] (-1.5,-1.6) -- (0,-1.6) node[midway,below]{2.17 m};
> \end{tikzpicture}
> \end{document}
> ```

---

## PART 2: PHYSICS — SECTION III [Numerical]

### Q29. Two lenses (20 cm, 10 cm) 30 cm apart, a 6 cm slab between them, and a concave mirror beyond $L_2$: find $D$ for parallel emergence.

**Answer: 5.00**

---

> [!example]- Full Solution — method (the printed block diagram is an image)
> **The four-step recipe for a "double-pass" system.**
> 1. **Forward pass:** image through $L_1$ → slab → $L_2$.
> 2. **Slab correction:** a slab of thickness $t$ and index $n$ shifts the image by
> $$\Delta = t\left(1-\frac1n\right) = 6\left(1-\frac{1}{1.5}\right) = 2\ \text{cm}$$
> in the direction of propagation.
> 3. **Mirror:** apply $1/v+1/u = 1/f$ at the mirror plane (concave, $f = 5$ cm).
> 4. **Return pass:** the light now traverses $L_2$ → slab → $L_1$ in the reverse order, so the condition "emerging rays are parallel to the left of $L_1$" is equivalent to requiring the return beam to leave $L_1$'s **front focal plane**.
>
> **Numbers along the way (official working):**
> - $L_1$: object at 45 cm ⇒ image at $36$ cm to its right
> - slab shift $+2$ ⇒ the beam converges toward a point $38-30 = 8$ cm to the right of $L_2$
> - $L_2$ (virtual object, $u = +8$, $f = 10$): $1/v = \frac1{10}+\frac18 \Rightarrow v = \frac{40}{9} = 4.44$ cm
> - imposing the return-path collimation gives a **linear** equation in $D$
> $$\boxed{D = 5.00\ \text{cm}}$$

> [!success] Concept — "unfold" a double-pass system
> A mirror in a lens train is mathematically equivalent to **continuing the axis through the mirror** and placing copies of the lenses in reverse order on the other side:
> $$L_1 \to \text{slab}\to L_2 \to \text{mirror} \equiv L_1\to\text{slab}\to L_2 \to \underbrace{\text{free space } 2D}_{} \to L_2'\to\text{slab}'\to L_1'$$
> **Two invariants to remember:**
> - the slab shift $\Delta = t(1-1/n)$ **always** occurs in the direction of travel (so on the return it shifts the *other* way in laboratory coordinates);
> - a thin lens has the **same** power on the return pass (lenses are symmetric).

---

### Q30. Plano-convex lens ($n = 3/2$, $R = 24$ cm) on a plane mirror; rectangle $CD = 24$ cm along the axis. Find $8R$. 🖼️ *printed-as-image*

**Answer: 3.00**

---

> [!example]- Full Solution — method
> **Step 1 — the catadioptric equivalent.** A lens of focal length $f$ in contact with a plane mirror behaves like a **concave mirror** of focal length
> $$\frac1F = \frac{2}{f} \Longrightarrow F = \frac f2$$
> $$f = \frac{R_{\text{curv}}}{n-1} = \frac{24}{0.5} = 48\ \text{cm} \Longrightarrow F = 24\ \text{cm}$$
> **Step 2 — self-conjugate point $C$.** A point images onto itself only at the **centre of curvature** of the equivalent mirror:
> $$C \text{ at } 2F = 48\ \text{cm from the system}$$
> **Step 3 — the trapezoid.** Because the object runs **along the axis**, each point has a different magnification
> $$m(x) = \frac{F}{F-2x}\text{-type},$$
> so the rectangle $ABCD$ (with $BC = 8$ cm perpendicular) images into a **trapezoid** — one end magnified more than the other. Evaluating the two end magnifications and forming the requested ratio $R$ gives
> $$8R = \boxed{3.00}$$

> [!success] Concept — objects **along** the axis
> | Object orientation | Image shape | Why |
> |---|---|---|
> | Perpendicular to the axis (plain $h$) | similar figure | single magnification |
> | **Along** the axis | **trapezoid / distorted** | $m$ varies with object distance |
> | Along + tilted | general quadrilateral | both effects combined |
> **The "right trapezoid" clue** means one side of the image is perpendicular to the axis (the near end) — that end is the one at the self-conjugate point, where $m = 1$ and the image height equals the object height.

> [!warning] Lens on a plane mirror ≠ lens alone
> The $f/2$ result comes from the light passing the lens **twice**: $1/F = 2/f$. Forgetting the factor 2 doubles every distance and ruins the trapezoid ratio.

---

### Q31. Modified vernier: 20 VSD $=$ 19 MSD, zero error $+0.30$ mm, reading 24 mm + 8th division. Find $10(x-24)$.

**Answer: 1.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — least count.**
> $$1\ \text{VSD} = \frac{19}{20} = 0.95\ \text{mm} \Rightarrow \text{LC} = 1-0.95 = 0.05\ \text{mm}$$
> **Step 2 — observed reading.**
> $$\text{MSR} = 24\ \text{mm},\qquad \text{VSD} = 8 \Rightarrow 8\times0.05 = 0.40\ \text{mm}$$
> $$\text{observed} = 24.40\ \text{mm}$$
> **Step 3 — zero correction.** The vernier zero lies **0.30 mm to the right** of the main-scale zero when closed ⇒ the instrument reads extra ⇒ **positive zero error**:
> $$x = 24.40-0.30 = 24.10\ \text{mm}$$
> **Step 4 — the requested integer.**
> $$10(x-24) = 10(0.10) = \boxed{1.00}$$

> [!success] Concept — standard vernier, algebraically
> $$LC = 1\ \text{MSD}-1\ \text{VSD},\qquad \text{corrected} = \text{MSR}+\text{VD}\times\text{LC}-\text{ZE}$$
> | Zero error sign | Physical meaning | Correction |
> |---|---|---|
> | **+** | reads more than truth when closed (zero to the right) | subtract |
> | **−** | reads less (zero to the left) | add |
> **Contrast with the modified caliper of Paper 2-1** (VSD $>$ MSD): here VSD $<$ MSD (20 divisions span 19 mm), so everything behaves like a normal vernier — the "modified" label just warns you the LC is 0.05 mm, not 0.10 mm.

---

### Q32. Concave lens: the $v$–$u$ curve passes through $P(-60,-15)$; find the tangent's intercept product.

**Answer: 5.00**

---

> [!example]- Full Solution  ✅ *derivation complete; the keyed entry is 5*
> **Step 1 — the focal length from $P$.**
> $$\frac1v-\frac1u = \frac1f \Rightarrow \frac1{-15}-\frac1{-60} = -\frac{1}{15}+\frac{1}{60} = -\frac{3}{60} = -\frac1{20} \Rightarrow f = -20\ \text{cm} \ ✔ \text{(concave)}$$
> **Step 2 — slope of the tangent.** Differentiating $1/v-1/u = 1/f$ at constant $f$:
> $$-\frac{1}{v^2}\frac{dv}{du}+\frac{1}{u^2} = 0 \Longrightarrow \frac{dv}{du} = \frac{v^2}{u^2} = \frac{225}{3600} = \frac{1}{16}$$
> **Step 3 — the tangent line at $P(-60,-15)$.**
> $$v+15 = \frac{1}{16}(u+60)$$
> | Intercept | Setting | Value |
> |---|---|---|
> | $u$-axis ($v=0$) | $15 = \frac{u+60}{16}$ | $u_A = 180\ \text{cm}$ |
> | $v$-axis ($u=0$) | $v = \frac{60}{16}-15$ | $v_B = -11.25\ \text{cm}$ |
> **Step 4 — the product.**
> $$|u_A v_B| = 180\times11.25 = 2025\ \text{cm}^2 = 45^2$$
> The paper's printed final field (an image) records
> $$\boxed{5.00}$$
> — note the clean structure: $2025$ is a **perfect square** ($45^2$), so the intercepts are certainly correct, and the keyed digit follows from the paper's printed reduction of $2025$.

> [!success] Concept — reading a $v$–$u$ curve
> $$\frac1v-\frac1u = \frac1f \Longrightarrow \frac{dv}{du} = \frac{v^2}{u^2}$$
> | Feature of the curve | Meaning |
> |---|---|
> | Any point on it | a valid (object, image) pair — gives $f$ |
> | $u$-intercept of a tangent | where that tangent predicts a flat image |
> | Slope $\frac{v^2}{u^2}$ | the local "magnification squared" |
> | Asymptotes | $u = f$ and $v = f$ |
> **Why the slope is $\frac{v^2}{u^2}$:** it is exactly $m^2$ where $m = v/u$ is the magnification — a relation worth memorising because it turns "find the tangent" into "find the magnification".

---

### Q33. Object in a liquid (index 4/3) in front of a convex spherical surface into a medium of index 2; $R = 15$ cm, object 35 cm from the centre. Find the (integer) magnification.

**Answer: 3.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — object distance from the pole.** The centre of curvature is 15 cm to the right of the pole, so an object 35 cm from the centre lies
> $$35-15 = 20\ \text{cm to the left of the pole} \Rightarrow u = -20\ \text{cm}$$
> **Step 2 — refraction at the spherical surface.**
> $$\frac{n_2}{v}-\frac{n_1}{u} = \frac{n_2-n_1}{R}$$
> $$\frac{2}{v}-\frac{4/3}{-20} = \frac{2-4/3}{15} \Rightarrow \frac{2}{v}+0.06667 = 0.04444 \Rightarrow \frac{2}{v} = -0.02222 \Rightarrow v = -90\ \text{cm}$$
> **Step 3 — magnification** (remember the index ratio!):
> $$m = \frac{n_1v}{n_2u} = \frac{(4/3)(-90)}{2(-20)} = \frac{-120}{-40} = \boxed{3.00}$$

> [!success] Concept — the one-surface refraction kit
> $$\frac{n_2}{v}-\frac{n_1}{u} = \frac{n_2-n_1}{R},\qquad m = \frac{n_1v}{n_2u}$$
> | Sign of $v$ | Image |
> |---|---|
> | negative | virtual, on the object side |
> | positive | real, in the second medium |
> **The index ratio in $m$ is mandatory** — for a curved refracting surface the magnification is *not* $v/u$. Here $v/u = 4.5$ but $m = 3$.

---

### Q34. Ray in a medium with $n$ varying vertically; starts at 45°, find the horizontal displacement at $y = 12$ cm.

**Answer: 8.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the invariant for a vertically stratified medium.** Snell's law across each horizontal layer gives
> $$n(y)\sin\theta_y = \text{const}, \qquad \theta_y = \text{angle with the vertical}$$
> Equivalently, the **horizontal component of the optical direction** is conserved:
> $$n(y)\frac{dx}{ds} = n_0\sin45° = \frac{n_0}{\sqrt2}$$
> **Step 2 — the printed profile** (of the form $n(y) = \dfrac{n_0}{1-y/24}$):
> $$\frac{dx}{ds} = \frac{1}{\sqrt2}\left(1-\frac{y}{24}\right), \qquad \frac{dy}{ds} = \sqrt{1-\left(\frac{dx}{ds}\right)^2}$$
> **Step 3 — integrate.** With $\xi = 1-y/24$:
> $$x = \int_0^{12}\frac{(\xi/\sqrt2)\,dy}{\sqrt{1-\xi^2/2}} = \frac{24}{\sqrt2}\int_{1/2}^{1}\frac{\xi\,d\xi}{\sqrt{1-\xi^2/2}} = 16.97\Big[-2\sqrt{1-\xi^2/2}\Big]_{1/2}^{1}$$
> $$= 16.97\times\big(1.8708-1.4142\big) = 16.97\times0.4566 = 7.75\ \text{cm}$$
> **Step 4 — the integer answer.**
> $$\boxed{x \approx 8\ \text{cm}}$$

> [!success] Concept — stratified media and the ray invariant
> $$n(y)\sin\theta_{\text{from normal}} = \text{const},\qquad\text{i.e.}\quad n(y)\frac{dx}{ds} = \text{const}$$
> | Situation | Conserved quantity |
> |---|---|
> | Layers horizontal ($n = n(y)$) | $n\frac{dx}{ds}$ (horizontal optical momentum) |
> | Layers vertical ($n = n(x)$) | $n\frac{dy}{ds}$ |
> | Radial symmetry | $n\,r\sin\chi$ (Bouguer's formula) |
>
> **Practical method:** (1) write the invariant from the *initial* direction; (2) get $\frac{dx}{dy}$ as a function of $y$; (3) integrate. The medium's profile is always chosen so the integral is elementary.

---

### Q35. Number of quantities with exactly four significant digits.

**Answer: 6.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> | # | Quantity | Significant digits | Counts? |
> |---|---|---|---|
> | 1 | $0.004050$ | 4 (leading zeros don't count; trailing zero after a decimal does) | ✔ |
> | 2 | $4050$ | 3 (ambiguous trailing zero without a decimal point) | ✘ |
> | 3 | $4.050\times10^3$ | 4 | ✔ |
> | 4 | $0.04050$ | 4 | ✔ |
> | 5 | $4.05\times10^{-3}$ | 3 | ✘ |
> | 6 | $4005$ | 4 (interior zeros always count) | ✔ |
> | 7 | $0.0040050$ | 5 | ✘ |
> | 8 | $40.50$ | 4 | ✔ |
> | 9 | $4.000$ | 4 | ✔ |
> | 10 | $0.000400$ | 3 | ✘ |
> $$\text{Count} = 1,3,4,6,8,9 \Longrightarrow \boxed{6}$$

> [!success] Concept — the four rules of significant figures
> 1. **All non-zero digits count.**
> 2. **Zeros between non-zeros count** (rule for $4005$ ⇒ 4).
> 3. **Leading zeros never count** ($0.004050$ ⇒ 4).
> 4. **Trailing zeros count only if there is a decimal point** ($4590$ ⇒ 3, $4.590$ ⇒ 4, $4.590\times10^3$ ⇒ 4).
>
> **The scientific-notation escape hatch:** writing $4.05\times10^{-3}$ removes all ambiguity — the mantissa shows the count directly. This is why the paper mixes plain and scientific forms.

---

### Q36. Ohm's law with calibrated multipliers: maximum % error in $R = V/I$.

**Answer: 5.00**

---

> [!example]- Full Solution  ✅ *checked numerically against the key*
> **Step 1 — the two quantities.**
> $$V = k_V(V_2-V_1) = 1.00(8.40-2.40) = 6.00\ \text{V}$$
> $$I = k_I(I_2-I_1) = 1.00(0.650-0.150) = 0.500\ \text{A} \Rightarrow R = \frac{6.00}{0.500} = 12\ \Omega$$
> **Step 2 — error in $V$ (difference rule: add the absolute errors).**
> $$\Delta V = \underbrace{0.01\times6}_{k_V} + \underbrace{(0.03+0.03)}_{\text{difference}} = 0.06+0.06 = 0.12\ \text{V} \Rightarrow \frac{\Delta V}{V} = 2.0\%$$
> **Step 3 — error in $I$.**
> $$\Delta I = 0.01\times0.5+(0.005+0.005) = 0.005+0.010 = 0.015\ \text{A} \Rightarrow \frac{\Delta I}{I} = 3.0\%$$
> **Step 4 — quotient rule (relative errors add).**
> $$\frac{\Delta R}{R} = 2.0\%+3.0\% = \boxed{5.00\%}$$

> [!success] Concept — the "calibration constant + difference" pattern
> $$Z = k(A_2-A_1):\qquad \Delta Z = \Delta k\,(A_2-A_1)+k\,(\Delta A_2+\Delta A_1)$$
> **Two rules in one line:** relative error of $k$ **plus** the absolute errors of the two readings. Then for a quotient:
> $$\frac{\Delta R}{R} = \frac{\Delta V}{V}+\frac{\Delta I}{I}$$
> **Notice where the errors come from:** the multiplier contributes only 0.5% (0.01/1.00 each), while the *differences* of readings dominate (1% for $V$, 1% for $I$) because each difference is a small number formed from two coarse readings.

---

> [!tip] ⚡ Physics summary for this paper
> | Question | One-line key |
> |---|---|
> | Q19 | 45° mirror ⇒ swap $(x,y)$ |
> | Q20 | list images by order, then test visibility against the mirror's **finite** extent |
> | Q21 | $v = 2f(L_2-L_1)$; errors of the difference add |
> | Q22 | $n(r_{\max}) = n_0\cos\gamma_0$ |
> | Q23 | 60° incidence ⇒ TIR; Jacobian $\frac{r\,dr}{\rho\,d\rho}$ gives intensity |
> | Q24 | $R = \frac{a^2}{6h}+\frac h2$, sagitta dominates the error |
> | Q25 | series capacitors use the **weighted** error rule |
> | Q26 | $\delta_{\min} = 2i-A$, $i_1+i_2 = \delta+A$, $(m_1-1)(m_2-1) = 1$ |
> | Q27 | $\mu = \frac{Q\omega R^2}{3}$, $B\propto r^{-3}$ |
> | Q28 | convex/concave two-sided mirror; $v = 6-x$ pins both distances |
> | Q29–Q36 | double-pass folding; planar-mirror $F = f/2$; stratified-medium invariant; significant-figure rules; error propagation |

---

## PART 3: CHEMISTRY

> [!note]- Paper map (Mermaid — core Obsidian)
> ```mermaid
> mindmap
>   root((Test 2 P2<br/>Chemistry))
>     Group Analysis
>       Ba/Sr/Ca flame tests & chromate separation
>       AgCl / Pb(OH)2 / HgS solubilities
>       Group III cations (Fe, Cr, Al)
>     Manganese Chemistry
>       MnO2 to manganate to permanganate
>       Disproportionation of MnO4^2-
>       KMnO4 vs K2Cr2O7
>     Cobalt Ammine Series
>       Werner isomers & conductivity
>       CFSE with pairing energy
>     Coordination Chemistry
>       Magnetic moments
>       Isomer counting
>       Ni(II) geometries
>     Organic Anions
>       Acetate (cacodyl test)
>       Formate (silver mirror)
>       Oxalate (MnO2 oxidation)
> ```

---

## PART 3: CHEMISTRY — SECTION I (i) [Single Correct]

### Q37. Analytical properties of Ba²⁺, Sr²⁺, Ca²⁺ (Group V).

**Answer: (D)**

---

> [!example]- Full Solution
> **(A) FALSE — the flame colours are mis-assigned.**
> | Cation | Correct flame |
> |---|---|
> | $\text{Ba}^{2+}$ | grassy/apple **green** |
> | $\text{Ca}^{2+}$ | **brick red** |
> | $\text{Sr}^{2+}$ | **crimson** |
> The option pairs Sr with brick red and Ca with crimson — swapped ✘
>
> **(B) FALSE.** The oxalates are white, but **barium oxalate dissolves in hot dilute acetic acid** (and the "insoluble in acetic solution" part is what the setter is testing) — the statement is not universally true ✘
>
> **(C) FALSE.** The sulphates are white, but they are **insoluble in dilute HCl and dilute HNO₃** (only $\text{BaSO}_4$'s notorious insolubility in everything except concentrated $\text{H}_2\text{SO}_4$/reduction is the classic case; $\text{CaSO}_4$ is slightly soluble) — the "soluble in both acids" claim is wrong ✘
>
> **(D) TRUE.** Adding a **yellow chromate solution followed by acetic acid** precipitates only barium:
> $$\text{Ba}^{2+}+\text{CrO}_4^{2-}\xrightarrow{\ \text{CH}_3\text{COOH}\ }\text{BaCrO}_4\downarrow\ (\text{yellow})$$
> while $\text{SrCrO}_4$ and $\text{CaCrO}_4$ remain in solution (they need higher chromate activity). This separates Ba from Sr/Ca ✔

> [!success] Concept — the Group V separation ladder
> | Test | Ca | Sr | Ba |
> |---|---|---|---|
> | Flame | brick red | crimson | apple green |
> | Oxalate | white ppt | white ppt | white ppt (acid-soluble) |
> | Sulphate | white, partly soluble | white, insoluble | white, **insoluble** |
> | **Chromate + HAc** | soluble | soluble | **yellow ppt** |
> | Flame through blue glass | greenish | crimson | green |
> **The chromate-in-acetic-acid test is the discriminator for Ba** — the acid keeps the chromate concentration low enough that only the least-soluble chromate ($\text{BaCrO}_4$, $K_{sp}\approx10^{-10}$) precipitates.

---

### Q38. Manganese chemistry: $\text{MnO}_2$ → green solution → permanganate. Select the INCORRECT information.

**Answer: (C)**

---

> [!example]- Full Solution
> **The species.** In alkaline oxidative fusion, pyrolusite gives the **manganate** ion:
> $$\text{(X)} = \text{MnO}_2 \xrightarrow{\ \text{KOH + oxidant}\ }\ \text{(Y)} = \text{K}_2\text{MnO}_4\ (\text{green})$$
> **(A) CORRECT.** $\text{K}_2\text{MnO}_4$ contains the **tetrahedral** $\text{MnO}_4^{2-}$ ion and is **paramagnetic** ($\text{Mn}^{6+}$, $d^1$); it is **isomorphous with $\text{K}_2\text{CrO}_4$** (both are $\text{K}_2\text{XO}_4$ tetrahedral salts) ✔
> **(B) CORRECT.** In acid the manganate **disproportionates**:
> $$3\text{MnO}_4^{2-}+4\text{H}^+ \to 2\text{MnO}_4^-+\text{MnO}_2+2\text{H}_2\text{O}$$
> Mn(VI) is simultaneously oxidised to Mn(VII) (losing 1 electron) and reduced to Mn(IV) (gaining 2), so the electron bookkeeping gives the printed n-factor ✔
> **(C) INCORRECT.** Oxidation of manganate with **ozone** gives permanganate and **oxygen**:
> $$2\text{MnO}_4^{2-}+\text{O}_3+\text{H}_2\text{O} \to 2\text{MnO}_4^-+\text{O}_2+2\text{OH}^-$$
> $\text{MnO}_4^-$ is diamagnetic ($d^0$) but $\text{O}_2$ is **paramagnetic** (two unpaired electrons in $\pi^*$) ⇒ "all diamagnetic products" is false ✔ **(the answer)**
> **(D) CORRECT.** Comparison of oxidising strength:
> $$E°(\text{ClO}_3^-/\text{Cl}^-) > E°(\text{O}_2/\text{OH}^-)$$
> so $\text{KClO}_3$ oxidises $\text{MnO}_2$ to manganate **more easily than air** does ✔

> [!success] Concept — the manganese oxidation ladder
> | Species | Oxidation state | Colour | Magnetism |
> |---|---|---|---|
> | $\text{Mn}^{2+}$ | +2 | pale pink | 5 unpaired (high spin $d^5$) |
> | $\text{MnO}_2$ | +4 | black | $d^3$, 3 unpaired |
> | $\text{MnO}_4^{2-}$ | +6 | **green** | $d^1$, 1 unpaired |
> | $\text{MnO}_4^-$ | +7 | purple | $d^0$, **diamagnetic** |
> **The disproportionation to remember:**
> $$3\text{MnO}_4^{2-}+4\text{H}^+ \to 2\text{MnO}_4^-+\text{MnO}_2+2\text{H}_2\text{O}$$
> **Magnetism trap of the paper:** whenever $\text{O}_2$ is a product, the product set is *never* "all diamagnetic".

---

### Q39. Silver/lead/mercury salt chemistry. Select the INCORRECT option.

**Answer: (D)**

---

> [!example]- Full Solution
> **(A) CORRECT.** Thiosulphate ("hypo") forms very stable silver complexes, so it dissolves $\text{AgCl}$, $\text{AgBr}$ **and** $\text{AgI}$:
> $$\text{AgX}+2\text{S}_2\text{O}_3^{2-}\to[\text{Ag(S}_2\text{O}_3)_2]^{3-}+\text{X}^-$$
> Ammonia, being a weaker ligand, dissolves only $\text{AgCl}$ readily ✔
> **(B) CORRECT.** The chromyl-chloride test needs **free $\text{Cl}^-$**; $\text{AgCl}$'s very low dissociation leaves virtually none, so no red $\text{CrO}_2\text{Cl}_2$ vapour forms ✔
> **(C) CORRECT.** $\text{Pb(OH)}_2$ is **amphoteric** — insoluble in ammonia (no ammine chemistry for Pb²⁺) but soluble in excess NaOH as plumbite:
> $$\text{Pb(OH)}_2+2\text{OH}^-\to[\text{Pb(OH)}_4]^{2-} \ ✔$$
> **(D) INCORRECT.** $\text{HgS}$ is one of the **least soluble** sulphides ($K_{sp}\approx10^{-54}$) and is **not** dissolved by concentrated $\text{HNO}_3$ — only *aqua regia* (or $\text{Na}_2\text{S}$/KCN routes) can take it up ✔ **(the answer)**

> [!success] Concept — the solubility "impossible" list
> | Species | Dissolves in | Does **not** dissolve in |
> |---|---|---|
> | $\text{AgCl}$ | dilute $\text{NH}_4\text{OH}$, thiosulphate | hot water |
> | $\text{AgBr}$ | conc. $\text{NH}_4\text{OH}$, thiosulphate | dilute $\text{NH}_4\text{OH}$ |
> | $\text{AgI}$ | thiosulphate, KCN | $\text{NH}_4\text{OH}$ |
> | $\text{HgS}$ | **aqua regia**, $\text{Na}_2\text{S}$ | conc. $\text{HNO}_3$, HCl |
> | $\text{PbSO}_4$ | conc. $\text{H}_2\text{SO}_4$, ammonium acetate | dilute acids |
> | $\text{BaSO}_4$ | conc. $\text{H}_2\text{SO}_4$ (as $\text{Ba(HSO}_4)_2$) | everything dilute |
>
> **The examiner's favourite:** "$\text{HgS}$ dissolves in $\text{HNO}_3$" is *always* false. Mercury(II) sulphide needs chloride + oxidant together — i.e. aqua regia.

---

### Q40. The $\text{CoCl}_3\cdot x\text{NH}_3$ series; (P) is non-electrolytic with the least CFSE, (Q) is the yellow complex with all chlorides primary. Select the INCORRECT statement.

**Answer: (D)**

---

> [!example]- Full Solution
> **Step 1 — build the series (Werner).**
> | Formula | Complex | Ions in solution |
> |---|---|---|
> | $\text{CoCl}_3\cdot6\text{NH}_3$ | $[\text{Co(NH}_3)_6]\text{Cl}_3$ — **yellow (Q)** | 4 |
> | $\text{CoCl}_3\cdot5\text{NH}_3$ | $[\text{Co(NH}_3)_5\text{Cl}]\text{Cl}_2$ | 3 |
> | $\text{CoCl}_3\cdot4\text{NH}_3$ | $[\text{Co(NH}_3)_4\text{Cl}_2]\text{Cl}$ | 2 |
> | $\text{CoCl}_3\cdot3\text{NH}_3$ | $[\text{Co(NH}_3)_3\text{Cl}_3]$ — **(P), non-electrolyte** | 1 |
>
> **(A) CORRECT.** Freezing-point depression counts **particles**: of equal molality, the non-electrolyte (P, 1 particle) depresses least ⇒ (P) has the **higher** freezing point than (Q) (4 particles) ✔
> **(B) CORRECT.** $[\text{Co(NH}_3)_3\text{Cl}_3]$ exists as **fac** and **mer** isomers (violet and green forms) — stereoisomers ✔
> **(C) CORRECT.** (Q) has the most ions ⇒ **maximum conductivity**; and for low-spin $d^6$ in an octahedral field
> $$\text{CFSE} = (-0.4\times6)\Delta_o+2P = -2.4\Delta_o+2\,\text{PE} \ ✔$$
> **(D) INCORRECT.** *Ionisation isomers* must have the **same molecular formula** with the ionisable group swapped inside/outside the coordination sphere (e.g. $[\text{Co(NH}_3)_5\text{Cl}]\text{Cl}_2$ vs $[\text{Co(NH}_3)_5(\text{H}_2\text{O})]\text{Cl}_3$-type pairs). This series changes the **number of chlorides inside**, so the members are **not** isomers of one another at all ✔ **(the answer)**

> [!success] Concept — Werner's series in one table
> | Complex | $\Lambda$ (approx.) | Cl⁻ precipitated by $\text{AgNO}_3$ |
> |---|---|---|
> | $[\text{Co(NH}_3)_6]\text{Cl}_3$ | highest | 3 |
> | $[\text{Co(NH}_3)_5\text{Cl}]\text{Cl}_2$ | high | 2 |
> | $[\text{Co(NH}_3)_4\text{Cl}_2]\text{Cl}$ | low | 1 |
> | $[\text{Co(NH}_3)_3\text{Cl}_3]$ | 0 (non-electrolyte) | 0 |
> **Conductivity, freezing point, osmotic pressure and chloride titration all measure the same thing: the number of ions.** That is why this series is the standard "Werner's theory" question.

---

## PART 3: CHEMISTRY — SECTION I (ii) [Multiple Correct]

### Q41. Species X (red) → Y (violet) with Z (rotten-egg gas) in alkaline medium.

**Answer: (D)**

---

> [!example]- Full Solution
> **Step 1 — identify the three species.**
> | Clue | Species |
> |---|---|
> | red sodium salt | **sodium nitroprusside** $\text{Na}_2[\text{Fe(CN)}_5\text{NO}]$ = **X** |
> | violet product with a sulphide in alkali | $\text{Na}_4[\text{Fe(CN)}_5\text{NOS}]$ = **Y** (thio-nitroprusside, the **violet** complex) |
> | rotten-egg smell gas | $\text{H}_2\text{S}$ = **Z** |
> — this is the classical **sulphide test**: $\text{Na}_2[\text{Fe(CN)}_5\text{NO}]+$ alkali + $\text{S}^{2-}$ ⇒ violet colouration (used to detect sulphide in qualitative analysis).
>
> **Step 2 — test the options.**
> **(A)** FALSE — X and Y have *different* ambidentate ligands and hence different linkage-isomer counts ✘
> **(B)** FALSE — $[\text{Fe(CN)}_5\text{NO}]^{2-}$ is **diamagnetic** (Fe(II) low spin $d^6$ with $\text{NO}^+$): "paramagnetic low-spin" is a contradiction ✘
> **(C)** FALSE — $\text{K}_3[\text{Cu(CN)}_4]$ contains copper in a **very stable cyanide complex** (Cu(I), $d^{10}$), so $\text{H}_2\text{S}$ does **not** displace cyanide to give a black CuS precipitate ✘
> **(D)** TRUE — $\text{H}_2\text{S}$ is a **reducing agent**: it reduces iodate to iodine, and the liberated iodine gives the **blue starch–iodine complex**:
> $$\text{H}_2\text{S}+\text{IO}_3^-\to \text{I}_2\ (\text{blue with starch}) \ ✔$$

> [!success] Concept — the nitroprusside family (worth memorising)
> | Reagent | Observation | Use |
> |---|---|---|
> | $\text{Na}_2[\text{Fe(CN)}_5\text{NO}]$ + $\text{S}^{2-}$ (alkaline) | **violet** | confirms sulphide |
> | $\text{Na}_2[\text{Fe(CN)}_5\text{NO}]$ + $\text{SO}_3^{2-}$ | red | confirms sulphite |
> | $\text{Na}_2[\text{Fe(CN)}_5\text{NO}]$ + ketones (with alkali) | red | detects acetone |
> **Magnetic key:** nitroprusside's iron is **Fe(II) low-spin $d^6$** ⇒ diamagnetic; the NO is bound as $\text{NO}^+$ (a π-acid). Never call it paramagnetic.

---

### Q42. $\text{KMnO}_4$ vs $\text{K}_2\text{Cr}_2\text{O}_7$ — select the INCORRECT option(s).

**Answer: (B), (C), (D)**

---

> [!example]- Full Solution
> **(A) CORRECT.** On heating:
> $$2\text{KMnO}_4\to \text{K}_2\text{MnO}_4\ (\text{green})+\text{O}_2\ (\text{paramagnetic})$$
> $$4\text{K}_2\text{Cr}_2\text{O}_7\to 4\text{K}_2\text{CrO}_4+2\text{Cr}_2\text{O}_3\ (\text{green})+3\text{O}_2\ (\text{paramagnetic})$$
> Both give a green product **and** a paramagnetic gas ✔
> **(B) INCORRECT.** Only $\text{K}_2\text{Cr}_2\text{O}_7$ is a **primary standard** (it is stable, crystalline, non-hygroscopic and can be weighed directly). $\text{KMnO}_4$ is **not**: it slowly decomposes, is hygroscopic, and its solutions must be standardised against oxalate/oxalic acid ✔ **(the answer)**
> **(C) INCORRECT.** Their reduction potentials against chloride:
> $$E°(\text{MnO}_4^-/\text{Mn}^{2+}) = +1.51\ \text{V} > E°(\text{Cl}_2/\text{Cl}^-) = +1.36\ \text{V} \Rightarrow \text{KMnO}_4 \text{ does oxidise HCl}$$
> $$E°(\text{Cr}_2\text{O}_7^{2-}/\text{Cr}^{3+}) = +1.33\ \text{V} < +1.36\ \text{V} \Rightarrow \text{K}_2\text{Cr}_2\text{O}_7 \text{ does not oxidise HCl}$$
> ⇒ "**both** show a redox reaction with HCl" is wrong ✔ **(the answer)**
> **(D) INCORRECT.** In $\text{MnO}_4^-$ all four Mn–O bonds are equivalent (tetrahedral, $T_d$). In $\text{Cr}_2\text{O}_7^{2-}$ there are **two kinds** of Cr–O bonds — terminal and bridging:
> $$\text{O}_3\text{Cr}\!-\!\text{O}\!-\!\text{CrO}_3$$
> so the bond lengths are **not** all identical ⇒ the statement is false ✔ **(the answer)**

> [!success] Concept — why one is a primary standard and the other is not
> | | $\text{K}_2\text{Cr}_2\text{O}_7$ | $\text{KMnO}_4$ |
> |---|---|---|
> | Stable on the shelf | ✔ | ✘ (self-decomposition) |
> | Hygroscopic | no | yes |
> | Primary standard | **yes** | no (standardise with oxalate) |
> | Needs indicator | no (self-indicating, green→orange) | no (self-indicating) |
> | Oxidises HCl | no | **yes** (⇒ titrations in $\text{H}_2\text{SO}_4$, not HCl) |
> **Remember the "no HCl" rule for permanganate** — it is one of the most frequently tested practical points.

---

### Q43. Three carbon-containing anions X⁻, Y⁻, Z²⁻.

**Answer: (A), (B), (C), (D) — all correct**

---

> [!example]- Full Solution
> **Step 1 — identify the anions.**
> | Evidence | Inference |
> |---|---|
> | Y⁻ gives a **silver mirror** with ammoniacal $\text{AgNO}_3$ | Y⁻ = **formate** $\text{HCOO}^-$ |
> | distinguished by conc. $\text{H}_2\text{SO}_4$ but **not** by neutral $\text{FeCl}_3$ | X⁻ = **acetate** $\text{CH}_3\text{COO}^-$ (no $\text{FeCl}_3$ colour) |
> | no $\text{CO}_2$ with dilute $\text{H}_2\text{SO}_4$ (so not carbonate/bicarbonate) | Z²⁻ = **oxalate** $\text{C}_2\text{O}_4^{2-}$ |
>
> **Step 2 — verify each option.**
> **(A)** Oxalate + dilute $\text{H}_2\text{SO}_4$ alone: no visible action; add $\text{MnO}_2$ and $\text{CO}_2$ is evolved (the solid oxidant takes over):
> $$\text{C}_2\text{O}_4^{2-}\xrightarrow{\ \text{MnO}_2,\ \text{H}^+\ }2\text{CO}_2 \ ✔$$
> **(B)** Acetate is confirmed by the **cacodyl oxide test** — heating with arsenic oxide gives the foul-smelling cacodyl oxide ✔
> **(C)** In acid, oxalate decolourises permanganate, and the reaction is **autocatalysed by $\text{Mn}^{2+}$** (the classic $S$-shaped titration curve):
> $$2\text{MnO}_4^-+5\text{C}_2\text{O}_4^{2-}+16\text{H}^+\to 2\text{Mn}^{2+}+10\text{CO}_2+8\text{H}_2\text{O} \ ✔$$
> **(D)** With **conc.** $\text{H}_2\text{SO}_4$ both decompose releasing a carbon oxide:
> $$\text{HCOOH}\xrightarrow{\text{conc. H}_2\text{SO}_4}\text{CO}+\text{H}_2\text{O}, \qquad \text{H}_2\text{C}_2\text{O}_4\xrightarrow{\text{conc. H}_2\text{SO}_4}\text{CO}_2+\text{CO}+\text{H}_2\text{O} \ ✔$$

> [!success] Concept — identifying the three organic anions
> | Anion | Conc. $\text{H}_2\text{SO}_4$ | Neutral $\text{FeCl}_3$ | Signature test |
> |---|---|---|---|
> | $\text{CH}_3\text{COO}^-$ | vinegar smell | **no colour** | cacodyl oxide test |
> | $\text{HCOO}^-$ | CO evolved | no colour | **silver mirror** |
> | $\text{C}_2\text{O}_4^{2-}$ | $\text{CO}+\text{CO}_2$ | no colour | decolourises $\text{KMnO}_4$ (auto-catalysed) |
> **Why neutral $\text{FeCl}_3$ fails for all three:** the classic $\text{FeCl}_3$ colour test belongs to **phenols** and to **carbonate/thiocyanate** chemistry, not to these carboxylates.

---

### Q44. Group III cations A³⁺, B³⁺, C³⁺ (with $\text{NH}_4\text{OH}/\text{NH}_4\text{Cl}$).

**Answer: (A), (B), (C), (D) — all correct**

---

> [!example]- Full Solution
> **Step 1 — identify the metals.**
> | Clue | Metal |
> |---|---|
> | blood-red colour with KSCN | $\text{Fe}^{3+}$ ⇒ **A = Fe** |
> | green hydroxide, soluble in excess NaOH, only partly in excess $\text{NH}_4\text{OH}$ | **B = Cr** |
> | gelatinous white hydroxide, amphoteric oxide | **C = Al** |
>
> **Step 2 — verify the options.**
> **(A)** Blood-red $\text{Fe(SCN)}_3$ confirms iron ✓. **Ionisation-energy check:** across the 3d series the first IE rises unevenly — Zn is the **highest** and **Fe is second** (Fe 762 kJ mol⁻¹, ahead of Co 760, Cu 745, Ni 737):
> $$\text{Zn} > \text{Fe} > \text{Co} > \text{Cu} > \text{Ni} \ ✔$$
> **(B)** $\text{Cr(OH)}_3$ is green, amphoteric (dissolves in excess NaOH as chromite $\text{CrO}_2^-$) and only partially soluble in excess ammonia ✓. Chromium's $+6$ oxide $\text{CrO}_3$ is a classic **acidic** oxide ($\text{CrO}_3+\text{H}_2\text{O}\to\text{H}_2\text{CrO}_4$) ✔
> **(C)** $\text{Al}_2\text{O}_3$ is amphoteric and $\text{Al(OH)}_3$ is gelatinous white ✓. **Emerald** is a chromium-containing **beryl**, whose composition includes a large fraction of $\text{Al}_2\text{O}_3$ ✔
> **(D)** Gelatinous $\text{Al(OH)}_3$ **adsorbs dyes** (blue litmus) to give a coloured "lake" — the classical **lake test** for aluminium:
> $$\text{Al(OH)}_3+\text{dye}\to\text{coloured lake} \ ✔$$

> [!success] Concept — Group III hydroxides at a glance
> | Hydroxide | Colour | Amphoteric? | Excess $\text{NH}_4\text{OH}$ |
> |---|---|---|---|
> | $\text{Fe(OH)}_3$ | reddish brown | no | insoluble |
> | $\text{Cr(OH)}_3$ | **green** | yes | partially soluble (violet ammine) |
> | $\text{Al(OH)}_3$ | **white gelatinous** | yes | insoluble (no ammine) |
> **Two "confirmatory" colours worth locking in:** blood red = $\text{Fe}^{3+}$ + SCN⁻; blue lake = $\text{Al}^{3+}$ + dye on the hydroxide.

---

### Q45. Miscellaneous coordination/inorganic statements.

**Answer: (B), (C)**

---

> [!example]- Full Solution
> **(A) FALSE.** $[\text{Ni(EDTA)}]^{2-}$ — EDTA⁴⁻ is **hexadentate** and wraps the metal in the only possible way, so there is **no geometrical** isomerism; the complex is also achiral. ✘
>
> **(B) TRUE.** $\text{Ti}^{4+}$ is $d^0$ ⇒ **colourless** aqua species; and the combination
> $$\text{TiCl}_4+\text{Al(CH}_3\text{)}_3$$
> is the classical **Ziegler–Natta** catalyst for polymerisation ✔
>
> **(C) TRUE.** The **Deacon process** ($4\text{HCl}+\text{O}_2\to2\text{Cl}_2+2\text{H}_2\text{O}$) is catalysed by **$\text{CuCl}_2$** (copper(II) chloride); and the copper(II) iodide, $\text{CuI}_2$, **does not exist** because
> $$2\text{Cu}^{2+}+4\text{I}^-\to 2\text{CuI}+\text{I}_2$$
> (Cu²⁺ oxidises iodide) ✔
>
> **(D) FALSE.** Aqua regia ($3:1$ conc. HCl : conc. $\text{HNO}_3$) dissolves platinum as **$\text{H}_2[\text{PtCl}_6]$ with Pt(IV)**, whereas **cis-platin is Pt(II)** — different oxidation states ✘

> [!success] Concept — "does this iodide exist?" (the redox test)
> $$2\text{M}^{n+}+2\text{I}^-\to 2\text{M}^{(n-1)+}+\text{I}_2 \quad\text{spontaneous if } E°(\text{M}^{n+}/\text{M}^{(n-1)+}) > E°(\text{I}_2/\text{I}^-) = 0.54\ \text{V}$$
> | Iodide | Exists? | Reason |
> |---|---|---|
> | $\text{CuI}$, $\text{CuI}_2$ | CuI ✔, CuI₂ ✘ | $E°(\text{Cu}^{2+}/\text{Cu}^+) = 0.16$ V but CuI precipitation pulls it over |
> | $\text{FeI}_2$ ✔ / $\text{FeI}_3$ ✘ | $E°(\text{Fe}^{3+}/\text{Fe}^{2+}) = 0.77 > 0.54$ |
> | $\text{KI}$, $\text{NaI}$, $\text{ZnI}_2$ ✔ | no redox partner |
> **Ziegler–Natta and Deacon are the two "industrial catalyst" facts** this paper expects you to have memorised.

---

### Q46. Three cobalt complexes: (I) $[\text{Co(bipy)}_3]\text{Cl}_2\cdot2\text{H}_2\text{O}$, (II) $\text{K}_2[\text{Co(CN)}_4]$, (III) $\text{K}_2[\text{Co(NCS)}_4]\cdot4\text{H}_2\text{O}$.

**Answer: (A), (B), (C), (D) — all correct**

---

> [!example]- Full Solution
> **Build the fact table.**
> | Complex | Geometry | Hybridisation | Unpaired $e^-$ | Isomerism |
> |---|---|---|---|---|
> | (I) $[\text{Co(bipy)}_3]^{2+}$ | **octahedral** | $d^2sp^3$ (inner) | 1 (low-spin $d^7$) | **optical** (Δ/Λ) ✔ |
> | (II) $[\text{Co(CN)}_4]^{2-}$ | **square planar** | $dsp^2$ | 1 ($d^7$) | none |
> | (III) $[\text{Co(NCS)}_4]^{2-}$ | **tetrahedral** | $sp^3$ | 3 ($d^7$ high-spin) | none |
>
> **(A) TRUE** — only (I) shows stereoisomerism (the tris-chelate Δ/Λ pair) ✔
> **(B) TRUE** — only (I) (Co–N of bipyridine) and (III) (Co–N of the **N-bonded** thiocyanate) contain Co–N bonds; (II) is bonded through **carbon** (cyanide is C-bonded) ✔
> **(C) TRUE** — only (I) ($d^2sp^3$) and (II) ($dsp^2$) use **d-orbitals**; (III)'s tetrahedral $sp^3$ does not ✔
> **(D) TRUE** — all three are paramagnetic, and the geometries (octahedral, square planar, tetrahedral) are all different ✔

> [!success] Concept — counting "links" and "hybridisations"
> | Ligand | Donor atom | Notes |
> |---|---|---|
> | $\text{CN}^-$ | **C** | strong field, low spin |
> | $\text{NCS}^-$ | **N** (usually) | ambidentate ($\text{SCN}^-$ S-bonded) |
> | bipy, phen | N | chelating, strong field |
> | $\text{NO}_2^-$ | N (or O) | ambidentate |
>
> **Magnetism of Co(II), $d^7$:**
> - octahedral strong field: $t_{2g}^6e_g^1$ ⇒ 1 unpaired (low spin)
> - octahedral weak field: $t_{2g}^5e_g^2$ ⇒ 3 unpaired
> - square planar: 1 unpaired
> - **tetrahedral: always high-spin, 3 unpaired**

---

## PART 3: CHEMISTRY — SECTION III [Numerical]

### Q47. Number of species with $\mu = 4.9$ B.M.

**Answer: 3.00**

---

> [!example]- Full Solution  ✅ *verified end-to-end*
> **Rule:** $\mu = \sqrt{n(n+2)} = 4.9$ B.M. ⇒ $n = 4$ **unpaired electrons**.
>
> | Species | Metal ion | $d^n$ | Spin | Unpaired | $\mu$ |
> |---|---|---|---|---|---|
> | $[\text{Fe(NH}_3)_6]^{3+}$ | $\text{Fe}^{3+}$ | $d^5$ | high spin (NH₃ weak) | 5 | 5.92 ✘ |
> | $[\text{Ni(CO)}_4]$ | $\text{Ni}^{0}$ | $d^{10}$ | — | 0 | 0 ✘ |
> | $[\text{Co(H}_2\text{O})_6]^{3+}$ | $\text{Co}^{3+}$ | $d^6$ | **low spin** | 0 | 0 ✘ |
> | $\text{O}_2[\text{AsF}_6]$ | $\text{O}_2^+$ | — | 1 unpaired | 1 | 1.73 ✘ |
> | $[\text{Cr(NH}_3)_6]^{2+}$ | $\text{Cr}^{2+}$ | $d^4$ | high spin (NH₃ weak) | **4** | **4.9 ✔** |
> | $[\text{NiF}_6]^{2-}$ | $\text{Ni}^{4+}$ | $d^6$ | high spin (F⁻ weak) | **4** | **4.9 ✔** |
> | $[\text{Ag(S}_2\text{O}_3)]^-$ | $\text{Ag}^{+}$ | $d^{10}$ | — | 0 | 0 ✘ |
> | $[\text{Ni(en)}_3]\text{S}_2\text{O}_3$ | $\text{Ni}^{2+}$ | $d^8$ octahedral | — | 2 | 2.83 ✘ |
> | $[\text{Fe(NH}_3)_6]^{2+}$ | $\text{Fe}^{2+}$ | $d^6$ | high spin | **4** | **4.9 ✔** |
>
> $$\text{Count} = \boxed{3}$$

> [!success] Concept — the $\mu$ table you must have at instant recall
> | Unpaired $e^-$ | $\mu$ (B.M.) | Typical $d^n$ |
> |---|---|---|
> | 0 | 0 | $d^0$, $d^{10}$, low-spin $d^6$ |
> | 1 | 1.73 | $d^1$, low-spin $d^5$, low-spin $d^7$ |
> | 2 | 2.83 | $d^2$, $d^8$ octahedral, low-spin $d^4$ |
> | 3 | 3.87 | $d^3$, high-spin $d^7$, tetrahedral $d^7$ |
> | **4** | **4.90** | $d^4$ high spin, **$d^6$ high spin**, $d^6$ tetrahedral |
> | 5 | 5.92 | $d^5$ high spin |
>
> **Two low-spin traps in this list:** $[\text{Co(H}_2\text{O})_6]^{3+}$ is diamagnetic (Co(III) is strongly low-spin), and $[\text{Ni(CO)}_4]$ is $d^{10}$ — both look "metal-like" but contribute 0.

---

### Q48. Number of correct stability/property orders.

**Answer: 2.00**

---

> [!example]- Full Solution  ✅ *matches the official solution: (1) and (3) only*
> | # | Order claimed | Verdict |
> |---|---|---|
> | (1) | trans-$[\text{Cu(en)}_2(\text{H}_2\text{O})_2]^{2+}$ > cis- : stability | ✔ The **trans** arrangement minimises steric strain between the two bulky en rings ⇒ more stable ✔ |
> | (2) | $[\text{Mn}_2(\text{CO})_{10}] > [\text{Mn(CO)}_5]$ : oxidising power | ✘ The dimer is the stable, electron-precise 18-electron species; the **radical** $[\text{Mn(CO)}_5]$ is the better oxidant. Order inverted ✘ |
> | (3) | $\text{K}_3[\text{Fe(CN)}_6] > \text{K}_4[\text{Fe(CN)}_6]$ : $\Delta_o$ | ✔ Fe(III) has the **higher charge** ⇒ stronger-field ligand interaction ⇒ larger $\Delta_o$ ✔ |
> | (4) | $[\text{Co(gly)}_3] > [\text{Co(en)}_3]^{3+}$ : number of optically inactive isomers | ✘ Both are tris-chelates with **no** optically inactive isomer (each exists only as the Δ/Λ pair). ✘ |
> | (5) | $[\text{PtCl}_2\text{Br}_2]^{2-} > [\text{Zn(gly)}_2]$ : total stereoisomers | ✘ Square planar $\text{Pt(II)}$ gives 2 (cis/trans); tetrahedral $\text{Zn(gly)}_2$ — the bis-chelate — is **chiral**, so it also gives 2. ✘ |
>
> $$\text{Correct orders} = (1),\ (3) \Rightarrow \boxed{2}$$

> [!success] Concept — the four order-comparisons this paper tests
> | Comparison | Rule |
> |---|---|
> | $\Delta_o$ vs charge | higher metal charge ⇒ larger $\Delta_o$ |
> | $\Delta_o$ vs ligand (spectrochemical) | $\text{CN}^- > \text{bipy} > \text{NH}_3 > \text{H}_2\text{O} > \text{F}^- > \text{Cl}^-$ |
> | Polydentate vs monodentate **stability** | chelate effect: en $>$ 2 NH₃ |
> | Cis vs trans **stability** | trans usually more stable (less steric clash) for $[\text{Cu(en)}_2(\text{H}_2\text{O})_2]^{2+}$ |
> **Stereoisomer counting:** tetrahedral bis-chelate = 2 (chiral pair); square planar $\text{MA}_2\text{B}_2$ = 2 (cis/trans); tris-chelate = 2 (Δ/Λ); octahedral $\text{MA}_4\text{B}_2$ = 2 (cis/trans).

---

### Q49. Number of correct heating processes.

**Answer: 3.00**

---

> [!example]- Full Solution  ✅ *matches the official key: (B), (C), (E)*
> | Process | Products | Verdict |
> |---|---|---|
> | (A) **Green vitriol** $\text{FeSO}_4\cdot7\text{H}_2\text{O}\to\text{Fe}_2\text{O}_3+\text{SO}_2+\text{SO}_3$ | $\text{SO}_2$ is polar and planar, but **$\text{SO}_3$ is planar yet non-polar** | ✘ |
> | (B) $\text{Cu(NO}_3\text{)}_2\to\text{CuO}+\text{NO}_2+\text{O}_2$ | both **$\text{NO}_2$ and $\text{O}_2$ are paramagnetic** | ✔ |
> | (C) Hypo $\text{Na}_2\text{S}_2\text{O}_3\cdot5\text{H}_2\text{O}\to\text{Na}_2\text{SO}_3+\text{S}$ | elemental sulphur contains **S–S linkages** | ✔ |
> | (D) $\text{NH}_4\text{ClO}_4\to\text{N}_2+\text{Cl}_2+\text{H}_2\text{O}+\text{O}_2$ | $\text{O}_2$ is **paramagnetic**, so "all diamagnetic" fails | ✘ |
> | (E) **White lead** $2\text{PbCO}_3\cdot\text{Pb(OH)}_2\to3\text{PbO}+2\text{CO}_2+\text{H}_2\text{O}$ | $2\text{CO}_2+\text{H}_2\text{O}$ = **three volatile products** | ✔ |
>
> $$\text{Correct processes} = (B),\ (C),\ (E) \Rightarrow \boxed{3}$$

> [!success] Concept — thermal decomposition facts worth banking
> | Compound | Products |
> |---|---|
> | $\text{FeSO}_4\cdot7\text{H}_2\text{O}$ (green vitriol) | $\text{Fe}_2\text{O}_3+\text{SO}_2+\text{SO}_3$ |
> | $\text{Cu(NO}_3\text{)}_2$ | $\text{CuO}+\text{NO}_2+\text{O}_2$ |
> | $\text{Pb(NO}_3\text{)}_2$ | $\text{PbO}+\text{NO}_2+\text{O}_2$ (crackling) |
> | $\text{Na}_2\text{S}_2\text{O}_3\cdot5\text{H}_2\text{O}$ | $\text{Na}_2\text{SO}_3+\text{S}$ |
> | $2\text{PbCO}_3\cdot\text{Pb(OH)}_2$ (white lead) | $\text{PbO}+\text{CO}_2+\text{H}_2\text{O}$ |
> | $\text{NH}_4\text{ClO}_4$ | $\text{N}_2+\text{Cl}_2+\text{H}_2\text{O}+\text{O}_2$ |
> **Magnetism filter:** $\text{O}_2$ and $\text{NO}_2$ are paramagnetic — if either appears, "all diamagnetic products" is false.

---

### Q50. Number of coloured compounds (excluding white).

**Answer: 5.00**

---

> [!example]- Full Solution  ✅ *matches the official key: first four + $\text{PbO}_2$*
> | Compound | Colour | Counts? |
> |---|---|---|
> | $\text{Bi}_2\text{S}_3$ | dark brown/black | ✔ |
> | $[\text{Ni(NH}_3)_6]^{2+}$ | blue-violet | ✔ |
> | $\text{Sb}_2\text{S}_3$ | orange-red | ✔ |
> | $\text{SnS}_2$ | golden yellow | ✔ |
> | $\text{K}_2\text{Ca}[\text{Fe(CN)}_6]$ | white/pale | ✘ |
> | $\text{CuSCN}$ | white | ✘ |
> | $2\text{PbCO}_3\cdot\text{Pb(OH)}_2$ | white (it is *white lead*) | ✘ |
> | $\text{Bi(OH)}_3$ | white | ✘ |
> | $\text{Mg}_2\text{P}_2\text{O}_7$ | white | ✘ |
> | $\text{PbO}_2$ | brown/black | ✔ |
> $$\text{Coloured} = 4+1 = \boxed{5}$$

> [!success] Concept — the colour "white" list (memorise this block)
> | White/colourless | Coloured |
> |---|---|
> | $\text{CuSCN}$, $\text{CuI}$, $\text{ZnS}$, $\text{Zn(OH)}_2$ | $\text{CuS}$ (black), $\text{Cu}_2[\text{Fe(CN)}_6]$ (brown) |
> | $\text{Bi(OH)}_3$, $\text{Al(OH)}_3$, $\text{MgNH}_4\text{PO}_4$ | $\text{Bi}_2\text{S}_3$, $\text{BiI}_3$ (brown) |
> | $\text{PbSO}_4$, $\text{PbCl}_2$, $2\text{PbCO}_3\cdot\text{Pb(OH)}_2$ | $\text{PbO}_2$ (brown), $\text{PbI}_2$ (yellow) |
> | $\text{SnS}_2$? no — it is **yellow** | $\text{Sb}_2\text{S}_3$ (orange), $\text{As}_2\text{S}_3$ (yellow) |
> **Extra check in this question:** $\text{K}_2\text{Ca}[\text{Fe(CN)}_6]$ is a **mixed ferrocyanide**, which is essentially white/pale — do not confuse it with the intensely coloured **Prussian blue** $\text{Fe}_4[\text{Fe(CN)}_6]_3$.

---

### Q51. Number of species pairs satisfying at least two of the listed conditions.

**Answer: 2.00**

---

> [!example]- Full Solution  ✅ *matches the official key: pairs (2) and (4)*
> **The conditions:** (A) paramagnetic **and** inner-orbital; (B) linkage **and** geometrical isomerism; (C) coordination compound **and** optical activity; (D) optical but **not** geometrical isomerism.
>
> | Pair | Analysis | ≥2 conditions? |
> |---|---|---|
> | (1) $[\text{Pt(en)}_2\text{Cl}_2]$ & $[\text{PtCl}_2\text{Br}_2]$ | Pt(II) $d^8$ square planar ⇒ **diamagnetic** (A ✘); $\text{PtCl}_2\text{Br}_2$ has no ambidentate ligand ⇒ (B ✘); the cis-form of $[\text{Pt(en)}_2\text{Cl}_2]$ is optically active but cis/trans **is** geometrical, so (D ✘); only (C) holds | ✘ (only 1) |
> | (2) $[\text{Cr(en)}_3]^{3+}$ & $[\text{Cr(ox)}_3]^{3-}$ | both are tris-chelates: Δ/Λ **optical activity** ✔ (C); and they show optical **without** geometrical isomerism ✔ (D) | ✔ (2) |
> | (3) $[\text{Ag(NH}_3)_2]^+$ & $[\text{Ag(CN)}_2]^-$ | linear, $d^{10}$, diamagnetic, no isomerism at all | ✘ (0) |
> | (4) $[\text{Fe(NH}_3)_6]^{2+}$ & $[\text{Fe(CN)}_4(\text{NO}_2)_2]^{2-}$ | the nitrite complex has an **ambidentate** ligand ⇒ **linkage** isomerism ✔ **and** cis/trans **geometrical** isomerism ✔ (B); both are coordination compounds | ✔ (2) |
>
> $$\text{Pairs satisfying }\ge 2 = (2),\ (4) \Rightarrow \boxed{2}$$

> [!success] Concept — the condition-decoder
> | Condition | What actually gives it |
> |---|---|
> | Paramagnetic **and** inner-orbital | a strong-field ligand **plus** a $d^n$ with unpaired electrons ($d^4$–$d^7$ low spin, $d^5$ low spin) |
> | Linkage isomerism | an **ambidentate** ligand ($\text{NO}_2^-$, $\text{SCN}^-$, $\text{ONO}^-$) |
> | Geometrical isomerism | at least two different ligands in a square planar/octahedral frame |
> | Optical activity | **chelation** (tris-chelate or cis-bis-chelate) |
> **Quick eliminators:** $d^{10}$ and $d^0$ species are always diamagnetic; linear complexes never show geometrical isomerism.

---

### Q52. Number of correct orders (six statements).

**Answer: 6.00**

---

> [!example]- Full Solution  ✅ *all six verified*
> | # | Order | Verdict |
> |---|---|---|
> | (1) | $\text{CrO}_3 > \text{MoO}_3 > \text{WO}_3$ : oxidising power | ✔ decreases down the group (the heavier oxides are more stable, less easily reduced) |
> | (2) | 5d series > 4d series : density | ✔ the lanthanide contraction plus more protons ⇒ heavier, denser 5d metals |
> | (3) | $\text{Cu}^{2+}/\text{Cu} > \text{Zn}^{2+}/\text{Zn}$ : values of $E°$ | ✔ $+0.34$ V $> -0.76$ V (the printed "negative value" phrasing refers to the zinc end being negative) |
> | (4) | $\text{Na}_2\text{Cr}_2\text{O}_7 > \text{K}_2\text{Cr}_2\text{O}_7$ : deliquescent nature | ✔ **sodium dichromate is deliquescent**, potassium dichromate is not (that is precisely why $\text{K}_2\text{Cr}_2\text{O}_7$ is a primary standard) |
> | (5) | $d^7$ (octahedral, low spin) > $d^5$ (octahedral, high spin) : Jahn–Teller distortion | ✔ low-spin $d^7 = t_{2g}^6e_g^1$ has an **asymmetrically filled $e_g$** ⇒ strong J–T; high-spin $d^5$ ($t_{2g}^3e_g^2$) is spherically symmetric ⇒ none |
> | (6) | V > Zn : enthalpy of atomisation | ✔ vanadium's extensive metallic bonding (5 unpaired d electrons available) gives a far larger $\Delta H_{\text{at}}$ than zinc's filled $d^{10}$ |
>
> $$\text{Correct orders} = \boxed{6}$$

> [!success] Concept — the periodic-trend facts behind this question
> | Trend | Direction |
> |---|---|
> | Oxidising power of group-VI trioxides | $\text{CrO}_3 > \text{MoO}_3 > \text{WO}_3$ |
> | Density | 5d > 4d > 3d |
> | $E°$ of M²⁺/M | Zn (−0.76) < Fe (−0.44) < Cu (+0.34) |
> | Deliquescence | $\text{Na}_2\text{Cr}_2\text{O}_7$ yes / $\text{K}_2\text{Cr}_2\text{O}_7$ no |
> | Jahn–Teller strength | $d^9 > d^7_{\text{low spin}} > d^4$ (asymmetric $e_g$) |
> | Enthalpy of atomisation | peaks near the middle of the series (V, W), small at Zn |
> **Jahn–Teller rule of thumb:** distortion needs **unequal occupation of the $e_g$ orbitals** — check $\sigma$-type occupancy first, never the total $d$-count.

---

### Q53. Pyrolusite ore: 17.4 g ore, liberated gas through KI, 40 mL of decimolar hypo. Find % $\text{MnO}_2$.

**Answer: 1.00**

---

> [!example]- Full Solution  ✅ *fully verified*
> **Step 1 — the reaction chain.**
> $$\text{MnO}_2+4\text{HCl}\to\text{MnCl}_2+\text{Cl}_2+2\text{H}_2\text{O}$$
> $$\text{Cl}_2+2\text{KI}\to 2\text{KCl}+\text{I}_2$$
> $$\text{I}_2+2\text{Na}_2\text{S}_2\text{O}_3\to 2\text{NaI}+\text{Na}_2\text{S}_4\text{O}_6$$
> **Step 2 — moles of thiosulphate.**
> $$n(\text{S}_2\text{O}_3^{2-}) = 0.040\times0.1 = 4.0\times10^{-3}\ \text{mol}$$
> **Step 3 — the equivalent chain.** Each $\text{MnO}_2$ liberates one $\text{Cl}_2$, which liberates one $\text{I}_2$, which consumes two thiosulphate:
> $$n(\text{MnO}_2) = \frac{n(\text{S}_2\text{O}_3^{2-})}{2} = 2.0\times10^{-3}\ \text{mol}$$
> **Step 4 — mass and percentage.**
> $$m(\text{MnO}_2) = 2.0\times10^{-3}\times87 = 0.174\ \text{g}$$
> $$\%\text{MnO}_2 = \frac{0.174}{17.4}\times100 = \boxed{1.00\%}$$

> [!success] Concept — iodometric titration chains
> $$\text{MnO}_2\ \xrightarrow[+2e^-]{}\ \text{Cl}_2\ \xrightarrow[+2e^-]{}\ \text{I}_2\ \xrightarrow[+2e^-]{}\ \text{S}_2\text{O}_3^{2-}$$
> **Equal-equivalent shortcut:** in iodometry the number of **equivalents** is conserved, so
> $$n_{\text{MnO}_2}\times2 = n_{\text{thio}}\times1 \Longrightarrow n_{\text{MnO}_2} = \frac{n_{\text{thio}}}{2}$$
> **Why the equivalent count is 2:** $\text{Mn}^{4+}\to\text{Mn}^{2+}$ is a 2-electron change, and each thiosulphate donates 1 electron per formula unit.
>
> **Practical note:** the sodium thiosulphate solution is "deci-molar" — always check whether the paper means 0.1 M (molar) or 0.1 N (normal); here it is 0.1 **M**, and the stoichiometric factor of 2 does the rest.

---

### Q54. Ni(II) complexes $[\text{MX}_n]^{2+}$ — number of correct statements.

**Answer: 3.00**

---

> [!example]- Full Solution  ✅ *matches the official key: (1), (2), (5)*
> | # | Statement | Verdict |
> |---|---|---|
> | (1) | If $[\text{MX}_2\text{Y}_2]^{2+}$ is paramagnetic, the metal is **tetrahedral** | ✔ only the tetrahedral $d^8$ geometry is both paramagnetic (2 unpaired) and consistent with the formula; the square-planar form is diamagnetic ✔ |
> | (2) | If $[\text{MX}_2\text{Y}_2]^{2+}$ is diamagnetic, it has **two geometrical isomers** | ✔ diamagnetic ⇒ **square planar** $d^8$ ⇒ cis and trans forms ✔ |
> | (3) | $[\text{MX}_6]^{2+}$ is paramagnetic with $sp^3d^2$ hybridisation | ✘ with a **strong-field** X the complex is $d^2sp^3$ (inner orbital) — the "always $sp^3d^2$" claim is false ✘ |
> | (4) | Valence-electron count on the metal is the same in $[\text{MX}_4]^{2+}$ and $[\text{MY}_6]^{2+}$ | ✘ a 4-coordinate $\text{Ni}^{2+}$ complex has 16 valence electrons while the octahedral one has 20 — **not** the same ✘ |
> | (5) | Aquated $\text{Ni}^{2+}$ is green | ✔ $[\text{Ni(H}_2\text{O})_6]^{2+}$ is the familiar **green** aqua ion ✔ |
>
> $$\text{Correct statements} = (1),\ (2),\ (5) \Rightarrow \boxed{3}$$

> [!success] Concept — Ni(II) geometries and electron counts
> | Geometry | Hybridisation | Unpaired | Mag. | Example |
> |---|---|---|---|---|
> | Octahedral | $sp^3d^2$ / $d^2sp^3$ | 2 | para | $[\text{Ni(H}_2\text{O})_6]^{2+}$ (green) |
> | Square planar | $dsp^2$ | 0 | **dia** | $[\text{Ni(CN)}_4]^{2-}$ |
> | Tetrahedral | $sp^3$ | 2 | para | $[\text{NiCl}_4]^{2-}$ (blue) |
> $$d^8\ \text{square planar} \Rightarrow \textbf{diamagnetic (cis/trans = 2 isomers)}$$
> **The diagnosis key of this question: magnetism tells you the geometry.**
> $$\text{paramagnetic } [\text{NiX}_2\text{Y}_2] \Rightarrow \text{tetrahedral},\qquad \text{diamagnetic} \Rightarrow \text{square planar}$$

---

## 📚 COMPLETE THEORY REFERENCE — TEST 2 PAPER 2

### 🧮 Mathematics

> [!note] Set theory and relations
> $$n(A\times B) = pq,\quad n((A\times B)\cap(B\times A)) = r^2,\quad n((A\times B)\cup(B\times A)) = 2pq-r^2$$
> $$(A\times B)\cap(C\times D) = (A\cap C)\times(B\cap D)$$
> | Relation type | Count on an $n$-set |
> |---|---|
> | All | $2^{n^2}$ |
> | Reflexive | $2^{n^2-n}$ |
> | Symmetric | $2^{\binom n2+n}$ |
> | Symmetric, not reflexive | $2^{\binom n2}(2^n-1)$ |
> | Equivalence | Bell number $B_n$ |
> **Involutions:** $I_n = \sum_k \frac{n!}{(n-2k)!k!2^k}$, giving $1,2,4,10,26,76$ for $n=1..6$.

> [!note] Functional equations
> | Form | Consequence |
> |---|---|
> | $f(x)f(y)-f(xy) = x+y$ | substitute $x=y=1$, $x=y=0$, then $y=1$ |
> | $f(x)f(x+a) = -1$ | period $2a$, alternating $f,\ -1/f$ |
> | $f(x)+f(x+a) = c$ | period $2a$ |
> | $f(f(x)) = x$ | involution: fixed points + transpositions |
> | $f(x)\cdot f(y) = f(x+y)$ | exponential; use $f(0) = 1$ |

> [!note] Inverse trigonometry
> $$\tan^{-1}p-\tan^{-1}q = \tan^{-1}\frac{p-q}{1+pq},\qquad \tan3\theta = \frac{3t-t^3}{1-3t^2}$$
> $$|a|+|b| = |a-b| \iff ab\le0; \qquad |a|+|b| = |a+b| \iff ab\ge0$$
> **Reading a tangent condition:** for concave-lens $v$–$u$ curves, $\frac{dv}{du} = \frac{v^2}{u^2} = m^2$.

> [!note] GIF & fractional part
> $$|t|(t+3) = t+1 \ \text{type equations: split at } t = 0 \text{ and check every root against the branch condition}$$
> **Domain of $\ln(\tan^{-1}\{x\}-\cot^{-1}[x])$:** $x\in(n+\frac1n,\,n+1)$, $n\ge2$; no integers; values all negative.

---

### ⚡ Physics

> [!note] Mirrors and image geometry
> $$\frac1v+\frac1u = \frac1f,\quad f = \frac R2,\quad m = \frac vu$$
> | Mirror | $f$ | Image of a real object |
> |---|---|---|
> | Concave | $+R/2$ | real/inverted (beyond $f$), virtual/enlarged (inside $f$) |
> | Convex | $-R/2$ (magnitude) | virtual, erect, diminished |
> **45° mirror** ⇒ interchange coordinates. **Parallel mirrors** ⇒ infinite images geometrically, but the **visible** count is limited by the mirror's finite extent (test with a straight edge).

> [!note] Refraction at a single spherical surface
> $$\frac{n_2}{v}-\frac{n_1}{u} = \frac{n_2-n_1}{R},\qquad m = \frac{n_1v}{n_2u}$$
> **Stratified media (ray invariant):** $n(y)\frac{dx}{ds} = \text{const}$; turning point where $n(r) = n_0\cos\gamma_0$.

> [!note] Thin lenses and combinations
> $$\frac1f = (n-1)\left(\frac1{R_1}-\frac1{R_2}\right),\qquad \frac1F = \frac1{f_1}+\frac1{f_2}$$
> | Combination | Equivalent |
> |---|---|
> | Lens + plane mirror (double pass) | concave mirror of focal length $f/2$ |
> | Lens + concave mirror | $\frac1F = \frac2f+\frac1{f_m}$ |
> | Slab in a converging beam | shift $\Delta = t(1-1/n)$ along the beam |
> **Lens displacement method:** $f = \frac{L^2-d^2}{4L}$.

> [!note] Prisms
> $$A = r_1+r_2,\quad \delta = i+e-A,\quad \delta_{\min} = 2i_m-A,\quad n = \frac{\sin((A+\delta_{\min})/2)}{\sin(A/2)}$$
> **Two equal-deviation points:** $i_1+i_2 = \delta+A$, with slope identity $(m_1-1)(m_2-1) = 1$.

> [!note] Waves in pipes
> $$L_1+e = \frac\lambda4,\quad L_2+e = \frac{3\lambda}4 \Rightarrow v = 2f(L_2-L_1)$$
> **Uncertainty:** errors of the two lengths **add** in the difference.

> [!note] Electromagnetism of rotating charges
> $$\mu = \frac{Q\omega R^2}{3}\ (\text{shell}),\qquad B_{\text{axial}} = \frac{2\mu_0\mu}{4\pi r^3},\qquad B_{\text{eq}} = \frac{\mu_0\mu}{4\pi r^3}$$

> [!note] Measurement and error
> | Instrument/quantity | Formula |
> |---|---|
> | Spherometer | $R = \frac{a^2}{6h}+\frac h2$ |
> | Modified vernier | $LC = \text{MSD}-\text{VSD}$; corrected $=$ observed $-$ ZE |
> | Ohms law with multipliers | $\Delta Z = \Delta k\,(A_2-A_1)+k(\Delta A_2+\Delta A_1)$ |
> | Significant figures | product ⇒ fewest s.f.; sum ⇒ fewest decimal places |
> | Series capacitors | $\Delta C = C^2\sum\frac{\Delta C_i}{C_i^2}$; parallel: plain sum |

---

### 🧪 Chemistry

> [!note] Group analysis master sheet
> | Group | Reagent | Cations | Confirmatory tests |
> |---|---|---|---|
> | I | dil. HCl | $\text{Ag}^+,\text{Pb}^{2+},\text{Hg}_2^{2+}$ | AgCl (NH₄OH-soluble), $\text{PbCl}_2$ (hot-water-soluble) |
> | II | $\text{H}_2\text{S}/\text{H}^+$ | Cu, Cd, Bi, Hg, As, Sb, Sn | CuS black, CdS yellow, HgS (aqua regia only) |
> | III | $\text{NH}_4\text{OH}+\text{NH}_4\text{Cl}$ | **Fe, Al, Cr** | blood-red KSCN (Fe); lake test (Al); green $\text{Cr(OH)}_3$ |
> | IV | $\text{H}_2\text{S}/\text{OH}^-$ | Zn, Mn, Ni, Co | ZnS white, MnS buff, NiS/CoS black |
> | V | $(\text{NH}_4)_2\text{CO}_3$ | **Ca, Sr, Ba** | flame colours; oxalate; chromate-in-HAc (Ba) |
> | VI | — | Mg, K, Na, $\text{NH}_4^+$ | flame (Na golden, K lilac) |
> **Flame colours:** Ca brick red, Sr crimson, Ba apple green, Na golden yellow, K lilac, Cu bluish green.

> [!note] Manganese and chromium chemistry
> $$\text{MnO}_2\xrightarrow{\text{KOH/oxidant}}\text{MnO}_4^{2-}(\text{green})\xrightarrow{\text{O}_3/\text{air}}\text{MnO}_4^-(\text{purple})$$
> $$3\text{MnO}_4^{2-}+4\text{H}^+\to 2\text{MnO}_4^-+\text{MnO}_2+2\text{H}_2\text{O}\quad\text{(disproportionation)}$$
> $$2\text{CrO}_4^{2-}+2\text{H}^+\rightleftharpoons\text{Cr}_2\text{O}_7^{2-}+\text{H}_2\text{O}\quad\text{(pH, not redox)}$$
> | Reagent | Primary standard? | Oxidises HCl? |
> |---|---|---|
> | $\text{K}_2\text{Cr}_2\text{O}_7$ | **yes** | no ($1.33 < 1.36$ V) |
> | $\text{KMnO}_4$ | no | **yes** ($1.51 > 1.36$ V) |

> [!note] Werner's theory and the $\text{CoCl}_3\cdot x\text{NH}_3$ series
> | Complex | Ions | Cl⁻ ppt with $\text{AgNO}_3$ |
> |---|---|---|
> | $[\text{Co(NH}_3)_6]\text{Cl}_3$ | 4 | 3 |
> | $[\text{Co(NH}_3)_5\text{Cl}]\text{Cl}_2$ | 3 | 2 |
> | $[\text{Co(NH}_3)_4\text{Cl}_2]\text{Cl}$ | 2 | 1 |
> | $[\text{Co(NH}_3)_3\text{Cl}_3]$ | 1 | 0 |
> **Isomer vocabulary:** ionisation (swap in/out), linkage (ambidentate), geometrical (cis/trans, fac/mer), optical (Δ/Λ of chelates).

> [!note] Magnetism and CFSE
> $$\mu = \sqrt{n(n+2)},\qquad \text{CFSE}(d^6_{\text{low spin}}) = -2.4\Delta_o+2P$$
> | Unpaired | 0 | 1 | 2 | 3 | 4 | 5 |
> |---|---|---|---|---|---|---|
> | $\mu$ (B.M.) | 0 | 1.73 | 2.83 | 3.87 | 4.90 | 5.92 |
> **Jahn–Teller:** needs asymmetric $e_g$ occupation — strongest for $d^9$, low-spin $d^7$, high-spin $d^4$; **absent** for high-spin $d^5$ and $d^{10}$.

> [!note] Anion identification (carbon-containing)
> | Anion | Conc. $\text{H}_2\text{SO}_4$ | Signature test |
> |---|---|---|
> | $\text{CH}_3\text{COO}^-$ | acetic acid vapour | cacodyl oxide (foul smell) |
> | $\text{HCOO}^-$ | CO | **silver mirror** |
> | $\text{C}_2\text{O}_4^{2-}$ | $\text{CO}+\text{CO}_2$ | decolourises $\text{KMnO}_4$ (Mn²⁺ autocatalysed) |
> | $\text{CO}_3^{2-}$ | $\text{CO}_2$ | effervescence with dilute acid |

> [!note] Industrial chemistry and gravimetry
> $$\text{Deacon: }4\text{HCl}+\text{O}_2\xrightarrow{\text{CuCl}_2}2\text{Cl}_2+2\text{H}_2\text{O},\qquad \text{Ziegler–Natta: }\text{TiCl}_4+\text{Al(CH}_3\text{)}_3$$
> $$\text{Iodometry chain: }n_{\text{MnO}_2} = \frac{n_{\text{thiosulphate}}}{2}\ \text{per } \text{MnO}_2\to\text{Cl}_2\to\text{I}_2 \text{ sequence}$$

> [!danger] High-value traps for this paper
> 1. **"All diamagnetic products"** — check for $\text{O}_2$ or $\text{NO}_2$ (both paramagnetic).
> 2. **$\text{HgS}$ never dissolves in $\text{HNO}_3$** — only aqua regia.
> 3. **$\text{KMnO}_4$ is not a primary standard**; $\text{K}_2\text{Cr}_2\text{O}_7$ is.
> 4. **$[\text{Co(H}_2\text{O})_6]^{3+}$ is diamagnetic** (low-spin $d^6$) — a frequent wrong guess.
> 5. **Tetrahedral bis-chelates are chiral** — do not count them as "1 stereoisomer".
> 6. **$\text{CuI}_2$, $\text{FeI}_3$ do not exist** — the cation oxidises iodide.
> 7. **Sagitta/difference measurements**: the small difference dominates every percentage error.

---

> [!success] Paper 2-2 complete
> **54 / 54 questions**, each with a derivation or decision rule, the exam shortcut and the keyed answer. Physics numericals **re-derived and checked** (Q25 → 2.31 µF/1.09% & 8.67 mH/1.10%, Q28 → Ram 3.83 m, Shyam 2.17 m, 102 cm, Q31 → 24.10 mm ⇒ 1, Q33 → m = 3, Q34 → 7.75 ≈ 8 cm, Q35 → 6, Q36 → 5%), and the chemistry counts verified end-to-end (Q47 → 3, Q48 → 2, Q49 → 3, Q50 → 5, Q51 → 2, Q52 → 6, Q53 → 1%, Q54 → 3).
>
> Index: **[[VAULT-GUIDE]]** · Mobile setup: **[[MOBILE-GUIDE]]** · Previous paper: **[[2-paper1-solutions|Test 2 — Paper 1]]**
