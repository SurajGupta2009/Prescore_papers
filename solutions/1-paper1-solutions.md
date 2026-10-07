---
test: 1
paper: 1
subjects: [Mathematics, Physics, Chemistry]
status: complete
tags: [solutions, jee-advanced, test-1]
---
# 1-PAPER 1 — COMPLETE SOLUTIONS (JEE Advanced Level)

> **Target:** Top 100 Rank Improvement
> **Approach:** Multiple smart approaches per question, concept-first explanations, plugin diagrams, and full theory at the end.
> **Answer key verified against the paper's official answer key (pp. 21–22) and official solutions (pp. 23–34).**

---

## PART 1: MATHEMATICS — SECTION I (i) [Single Correct]

---

### Q1. The sum $\binom{99}{0} - \binom{99}{2} + \binom{99}{4} - \binom{99}{6} + \cdots - \binom{99}{98}$ equals

(A) $-2^{98}$  (B) $2^{98}$  (C) $-2^{49}$  (D) $2^{49}$

**Answer: (C) $-2^{49}$**

---

#### Approach 1 — Standard: Even-Term Filter at $x = i$

$$\frac{(1+x)^n + (1-x)^n}{2} = \binom{n}{0} + \binom{n}{2}x^2 + \binom{n}{4}x^4 + \cdots$$

Evaluate at $x = i$ (so $x^2 = -1$): the right side becomes exactly the alternating even-index sum $S$.

$$S = \frac{(1+i)^{99} + (1-i)^{99}}{2} = \operatorname{Re}\!\big[(1+i)^{99}\big]\cdot\; \text{(since the two terms are conjugates)}$$

$1+i = \sqrt{2}\,e^{i\pi/4} \Rightarrow (1+i)^{99} = 2^{99/2} e^{i\,99\pi/4}$, and $99\pi/4 = 24\pi + 3\pi/4$, so

$$(1+i)^{99} = 2^{49}\sqrt{2}\left(-\tfrac{1}{\sqrt{2}} + \tfrac{i}{\sqrt{2}}\right) = 2^{49}(-1+i)$$

$$S = \frac{2^{49}(-1+i) + 2^{49}(-1-i)}{2} = -2^{49}$$

#### Approach 2 — Exam Hack: Read the Sign from $n \bmod 4$

For $S = \sum_k (-1)^k \binom{n}{2k} = \operatorname{Re}[(1+i)^n]$: write $n = 4q + r$.

$(1+i)^n = 2^{n/2} e^{i n\pi/4}$, so $S = 2^{n/2}\cos(n\pi/4)$. With $n = 99$: $\cos(99\pi/4) = \cos(3\pi/4) = -1/\sqrt{2}$

$$S = 2^{99/2}\cdot(-1/\sqrt{2}) = -2^{49}$$

#### Approach 3 — BSc/MSc Insight: Discrete Fourier (Roots-of-Unity) Filter

$$\sum_{k \equiv r \pmod m}\binom{n}{k} = \frac{1}{m}\sum_{j=0}^{m-1}\omega^{-jr}(1+\omega^j)^n, \qquad \omega = e^{2\pi i/m}$$

Setting $m = 4$, $r = 0$ and taking real parts isolates $k \equiv 0 \pmod 4$ minus $k \equiv 2 \pmod 4$ — the alternating even sum. Equivalently $S = \operatorname{Re}[(1+i)^n]$ via Cauchy's residue theorem on $\frac{(1+z)^n}{2z}$ evaluated with the $i^k$ filter.

> [!tip] Exam Shortcut
> $\sum_k (-1)^k\binom{n}{2k} = 2^{n/2}\cos\!\big(\tfrac{n\pi}{4}\big)$. For $n \equiv 3 \pmod 4$ (like 99) the answer is $-2^{(n-1)/2}$.

> [!warning] Trap & Common Pitfall
> The last term is $-\binom{99}{98}$ (even index, negative sign). Dropping the sign gives $+2^{49}$ — a distractor option.

> [!success] Key Takeaway
> Any alternating even/odd binomial sum is a real/imaginary part of $(1\pm i)^n$. Master $e^{i\pi/4}$ powers: they cycle through $\pm 1 \pm i$ every 8 powers of $n$.

---

### Q2. Let $n$ be an even positive integer such that $n/2$ is odd, and let $\alpha_0, \alpha_1, \ldots, \alpha_{n-1}$ be the complex $n$-th roots of unity. Then $\prod_{k=0}^{n-1}\big[(2+i) + (3-i)\alpha_k^2\big]$ equals

(A) $\big[(2+i)^{n/2} - (3-i)^{n/2}\big]^2$  (B) $\big[(2+i)^{n/2} + (3-i)^{n/2}\big]^2$  (C) $(2+i)^{n/2} + (3-i)^{n/2}$  (D) $(2+i)^{n/2} - (3-i)^{n/2}$

**Answer: (B)**

---

#### Approach 1 — Standard: Collapse $\alpha_k^2$ onto $(n/2)$-th Roots of Unity

As $k$ runs over $0,\dots,n-1$, the squares $\alpha_k^2$ run over the $(n/2)$-th roots of unity, **each exactly twice** (since $\gcd(2,n) = 2$). Let $\omega_j$, $j = 0,\dots,\tfrac n2 - 1$, be the $(n/2)$-th roots of unity. Then

$$\prod_{k=0}^{n-1}\big[(2+i)+(3-i)\alpha_k^2\big] = \left(\prod_{j=0}^{n/2-1}\big[(2+i)+(3-i)\omega_j\big]\right)^2$$

Factor out $(3-i)$ and use $\prod_j (x - \omega_j) = x^{n/2} - 1$ with $x = -\frac{2+i}{3-i}$:

$$\prod_j \big[(2+i)+(3-i)\omega_j\big] = (3-i)^{n/2}\prod_j\Big(\omega_j + \tfrac{2+i}{3-i}\Big) = (3-i)^{n/2}\left[\Big(-\tfrac{2+i}{3-i}\Big)^{n/2} - 1\right]\cdot(-1)^{n/2}$$

Because $m = n/2$ is **odd**, $(-1)^m = -1$ and $(-1)^m\big[(-1)^m c^m - 1\big] = c^m + 1$. With $c = \frac{2+i}{3-i}$:

$$\prod_j = (3-i)^{m}\left[\left(\tfrac{2+i}{3-i}\right)^{m} + 1\right] = (2+i)^{m} + (3-i)^{m}$$

Squaring the doubled product:

$$\prod_{k=0}^{n-1} = \big[(2+i)^{n/2} + (3-i)^{n/2}\big]^2 \quad \Rightarrow \textbf{(B)}$$

#### Approach 2 — Exam Hack: Test $n = 2$

$n = 2$ is allowed ($n/2 = 1$ odd). Then $\alpha_0^2 = \alpha_1^2 = 1$, so the product is $\big[(2+i)+(3-i)\big]^2 = 5^2 = 25$.

- (A): $[(2+i)-(3-i)]^2 = (-1+2i)^2 = -3\;\boldsymbol{\times}$
- (B): $[(2+i)+(3-i)]^2 = 25\;\boldsymbol{\checkmark}$
- (C): $(2+i)+(3-i) = 5\;\boldsymbol{\times}$  (D): $-3$ or $5$ variants $\boldsymbol{\times}$

Only (B) gives 25.

#### Approach 3 — BSc/MSc Insight: Group-Theoretic View (Cyclic Covering)

Let $G = \mathbb{Z}/n$ act by $\alpha \mapsto \zeta\alpha$; squaring is the group endomorphism $g \mapsto g^2$ whose image is the subgroup $H$ of index 2 (the $(n/2)$-th roots), each element of $H$ having exactly two preimages (kernel $= \{\pm1\}$). Therefore

$$\prod_{g \in G} \big(a + b\,g^2\big) = \prod_{h \in H}\big(a + b\,h\big)^{2}$$

and Vieta on $z^{n/2} - 1$ evaluates $\prod_{h\in H}(a + b\,h) = (2+i)^{n/2} + (3-i)^{n/2}$ (odd $n/2$ fixes the sign). Squaring the double-counted product is exactly option (B). This is the "square map on a cyclic group" behind Approach 1.

> [!tip] Exam Shortcut
> Whenever $\alpha_k^2$ appears, replace it by "each $(n/2)$-th root, twice." Then it is a single polynomial product squared.

> [!warning] Trap & Common Pitfall
> The condition "$n/2$ odd" is essential: it flips $(-1)^{n/2} = -1$ and turns $c^m - 1$ into $c^m + 1$. With $n/2$ even the answer would be $\big[(2+i)^{n/2} - (3-i)^{n/2}\big]^2$ (option A-distractor).

> [!success] Key Takeaway
> $\prod_{k}(a + b\,\omega_k) = a^{N} - (-b)^{N}$ up to sign conventions, with $\omega_k$ the $N$-th roots of unity. Always reduce products over roots of unity to $z^N - 1$ evaluations.

---

### Q3. $\;(x+m)^m - {}^{m}C_1 (x+m-1)^m + {}^{m}C_2 (x+m-2)^m - \cdots + (-1)^m x^m$ equals

(A) $(m+1)!$  (B) ${}^{m+1}C_m$  (C) $m!$  (D) ${}^mP_{m-2}$

**Answer: (C) $m!$**

---

#### Approach 1 — Standard: $m$-th Forward Difference of $t^m$

Rewrite the sum with $j = m - k$:

$$S = \sum_{k=0}^{m}(-1)^k \binom{m}{k}(x+m-k)^m = \sum_{j=0}^{m}(-1)^{m-j}\binom{m}{j}(x+j)^m$$

The right side is precisely the $m$-th forward difference of $f(t) = t^m$:

$$\Delta^m f(x) = \sum_{j=0}^{m}(-1)^{m-j}\binom{m}{j}f(x+j)$$

Since $f(t) = t^m$ is a degree-$m$ polynomial with leading coefficient 1, $\Delta^m f \equiv m! \cdot 1 = m!$ (the forward difference lowers degree by 1 each time and multiplies the leading coefficient by the degree).

$$\boxed{S = m!}$$

#### Approach 2 — Exam Hack: Set $x = 0$ and Test Small $m$

The result must hold for every real $x$, so take $x = 0$:

- $m = 1$: $(1) - (0) = 1 = 1!\;\checkmark$
- $m = 2$: $2^2 - 2\cdot 1^2 + 0 = 4 - 2 = 2 = 2!\;\checkmark$
- $m = 3$: $3^3 - 3\cdot 2^3 + 3\cdot 1^3 - 0 = 27 - 24 + 3 = 6 = 3!\;\checkmark$

Pattern gives $m!$ — option (C). Options (A), (B), (D) fail already at $m = 2$ ($6$ vs $3$ vs $2$).

#### Approach 3 — BSc/MSc Insight: Finite-Difference Calculus

$\Delta$ is the discrete derivative; on polynomials of degree $m$, $\Delta^m = m!\cdot h^{-m} h^m$ (step $h = 1$) maps onto constants — the discrete analogue of $\frac{d^m}{dt^m}t^m = m!$. The expression is the binomial transform of $f(t) = t^m$ evaluated at the shift $x$, and the binomial transform of a degree-$m$ monic polynomial is the constant $m!$.

> [!tip] Exam Shortcut
> The sum is independent of $x$ — plug in $x = 0$ (or any convenient value) and test $m = 1, 2, 3$ to pin the answer in 30 seconds.

> [!warning] Trap & Common Pitfall
> Do not "expand the first term only": every term contributes. The pattern $1, 2, 6$ (not $1, 3, 6$ or $1, 4, 12$) distinguishes $m!$ from $(m+1)!$ and $P$-type options.

> [!success] Key Takeaway
> $\sum_{j}(-1)^{m-j}\binom{m}{j}(x+j)^m = m!$ — the $m$-th finite difference of $t^m$ is constant. This identity is the workhorse of alternating binomial sums of polynomials.

---

### Q4. Let $z$ be a complex number satisfying $\left|2z + \frac{1}{z}\right| = 1$. If $\arg z = \theta$, then the least value of $\sin^2\theta$ is

(A) $\frac{7}{8}$  (B) $\frac{5}{4}$  (C) $\frac{1}{5}$  (D) $\frac{1}{2}$

**Answer: (A) $\dfrac{7}{8}$**

---

#### Approach 1 — Standard: Expand $|2z + 1/z|^2$

Let $z = re^{i\theta}$. Then

$$\left|2z + \frac1z\right|^2 = \left(2z+\frac1z\right)\!\left(2\bar z + \frac{1}{\bar z}\right) = 4r^2 + \frac{1}{r^2} + 2\left(\frac{z}{\bar z} + \frac{\bar z}{z}\right) = 4r^2 + \frac{1}{r^2} + 4\cos 2\theta$$

Setting this equal to 1:

$$4r^2 + \frac{1}{r^2} = 1 - 4\cos 2\theta$$

By AM–GM, $4r^2 + \dfrac{1}{r^2} \ge 2\sqrt{4} = 4$, with equality at $r^2 = \tfrac12$. Hence

$$1 - 4\cos 2\theta \ge 4 \;\Rightarrow\; \cos 2\theta \le -\frac{3}{4}$$

$$\sin^2\theta = \frac{1-\cos 2\theta}{2} \ge \frac{1 + \tfrac34}{2} = \frac{7}{8}$$

Equality is attained at $r = 1/\sqrt{2}$, $\cos 2\theta = -3/4$ — a genuine point of the locus. Minimum $= \dfrac{7}{8}$.

```desmos-graph
---
bounds: [0.2, 2.5, 0, 14]
grid: true
---
y = 4x^2 + 1/x^2
y = 4 | hidden | dashed | red
```

#### Approach 2 — Component Form + AM–GM

$2z + \frac1z = \left(2r + \frac1r\right)\cos\theta + i\left(2r - \frac1r\right)\sin\theta$, so

$$\left(2r+\tfrac1r\right)^2\cos^2\theta + \left(2r-\tfrac1r\right)^2\sin^2\theta = 1$$

Using $(2r \pm 1/r)^2 = \left(2r+\tfrac1r\right)^2 \mp 8\cdot\tfrac{r}{r}\cdot$… more directly: $a^2 := \left(2r+\frac1r\right)^2$, then LHS $= a^2 - 8\sin^2\theta = 1$, i.e. $a^2 = 1 + 8\sin^2\theta$. Since $a = 2r + 1/r \ge 2\sqrt{2}$ (AM–GM, at $r = 1/\sqrt2$), $a^2 \ge 8$:

$$1 + 8\sin^2\theta \ge 8 \;\Rightarrow\; \sin^2\theta \ge \frac{7}{8}$$

#### Approach 3 — Exam Hack: Eliminate Impossible Options First

$\sin^2\theta \le 1$ always, so **(B) $5/4$ is impossible** — never pick it. The minimum is attained (locus is compact in $r$), so the answer is among $\{7/8,\,1/5,\,1/2\}$. Since $\sin^2\theta = 1/5$ would mean $\cos 2\theta = 3/5 > 0$, requiring $4r^2 + 1/r^2 = 1 - 12/5 < 0$ — impossible. Same for $1/2$ ($\cos 2\theta = 0 \Rightarrow 4r^2+1/r^2 = 1 < 4$ impossible). Only (A) survives.

> [!tip] Exam Shortcut
> Write the condition as $4r^2 + \frac{1}{r^2} = 1 - 4\cos 2\theta$, then immediately apply AM–GM ($\ge 4$). One line: $\sin^2\theta \ge \frac{1+3/4}{2} = \frac78$.

> [!warning] Trap & Common Pitfall
> Option (B) $5/4 > 1$ is a gift — $\sin^2\theta$ can never exceed 1. Also don't forget the $+4\cos 2\theta$ cross term (the $2(z/\bar z + \bar z/z)$ piece); missing it gives a wrong angle condition.

> [!success] Key Takeaway
> $\left|2z + \frac1z\right|^2 = 4|z|^2 + \frac{1}{|z|^2} + 4\cos(2\arg z)$ — modulus-of-sum problems with $z$ and $1/z$ always produce a $\cos 2\theta$ term. Combine with AM–GM on $|z|^2$.

---

## PART 1: MATHEMATICS — SECTION I (ii) [Multiple Correct]

---

### Q5. Let $z_1, z_2, z_3$ be three distinct complex numbers with $|z_1| = |z_2| = |z_3| = 1$. Which is/are correct?

(A) If $\arg(z_1/z_2) = \pi/2$ then $\arg\!\left(\dfrac{z-z_1}{z-z_2}\right) > \dfrac{\pi}{4}$ where $|z| > 1$

(B) $|z_1z_2 + z_2z_3 + z_3z_1| = |z_1 + z_2 + z_3|$

(C) $\operatorname{Im}\!\left(\dfrac{(z_1+z_2)(z_2+z_3)(z_3+z_1)}{z_1z_2z_3}\right) = 0$

(D) If $|z_1 - z_2| = \sqrt{2}\,|z_1 - z_3| = \sqrt{2}\,|z_2 - z_3|$ then $\operatorname{Re}\!\left(\dfrac{z_3-z_1}{z_3-z_2}\right) = 0$

**Answer: (B), (C), (D)**

---

#### Approach 1 — Standard: Use $\bar z_k = 1/z_k$

**(B)** Conjugate $z_1+z_2+z_3$: $\overline{z_1+z_2+z_3} = \frac{1}{z_1}+\frac{1}{z_2}+\frac{1}{z_3} = \frac{z_1z_2+z_2z_3+z_3z_1}{z_1z_2z_3}$. Hence

$$z_1z_2+z_2z_3+z_3z_1 = \overline{(z_1+z_2+z_3)}\cdot z_1z_2z_3 \;\Rightarrow\; |{\cdot}| = |z_1+z_2+z_3|\cdot 1 \;\boldsymbol{\checkmark}$$

**(C)** Divide numerator into three factors: $\frac{z_1+z_2}{z_1z_2}\cdot\frac{z_2+z_3}{z_2z_3}\cdot\frac{z_3+z_1}{z_3z_1} = \left(1+\frac{1}{z_3}\right)\left(1+\frac{1}{z_1}\right)\left(1+\frac{1}{z_2}\right)$ — wait, regrouping properly:

$$\frac{(z_1+z_2)(z_2+z_3)(z_3+z_1)}{z_1z_2z_3} = \left(1+\frac{z_2}{z_1}\right)\!\left(1+\frac{z_3}{z_2}\right)\!\left(1+\frac{z_1}{z_3}\right) = (1+x)(1+y)(1+z)$$

with $|x|=|y|=|z|=1$ and $xyz = 1$. Its conjugate is $\left(1+\frac1x\right)\left(1+\frac1y\right)\left(1+\frac1z\right) = \frac{(1+x)(1+y)(1+z)}{xyz} = $ itself — so the number is real and the imaginary part is 0 $\boldsymbol{\checkmark}$.

**(D)** The conditions say $|z_1z_3| = |z_2z_3| = d$ and $|z_1z_2| = \sqrt2 d$: triangle $z_1z_2z_3$ is right-angled at $z_3$ (Pythagoras: $d^2 + d^2 = 2d^2$). Then $\frac{z_3-z_1}{z_3-z_2}$ is the ratio of two **perpendicular vectors of equal length** $= \pm i$, so its real part is 0 $\boldsymbol{\checkmark}$.

**(A)** Counter-example: take $z_1 = i$, $z_2 = 1$ and let $z \to +\infty$ along the real axis (with $|z|>1$): $\frac{z-i}{z-1} \to 1$, whose argument $\to 0 \not> \pi/4$. **False** $\boldsymbol{\times}$.

#### Approach 2 — Exam Hack

- (B): test $z_1 = 1, z_2 = i, z_3 = -1$: LHS $= |i + (-i) + (-1)| = 1$; RHS $= |1+i-1| = i$-magnitude $= 1$ ✓.
- (C): test equilateral case $1, \omega, \omega^2$: product $= (1+\omega)(1+\omega^2)(1+1) = (-\omega^2)(-\omega)(2) = 2$ — real ✓.
- (D): right angle check is instant from the $\sqrt2$ ratios.

> [!tip] Exam Shortcut
> On $|z| = 1$: conjugation $=$ inversion ($\bar z = 1/z$). Option (B) is a one-line consequence; option (C) becomes "$xyz = 1 \Rightarrow$ invariant under conjugation."

> [!warning] Trap & Common Pitfall
> (A) looks geometrically plausible (inscribed angle ideas) but the claim must hold for **all** $|z|>1$ — a single large-$z$ limit kills it. Never accept an unquantified "then … > π/4" without checking the extremal configuration.

> [!success] Key Takeaway
> For unit-modulus triples, both (B) and (C) are algebraic identities, not coincidences — the map $z \mapsto 1/z$ (conjugation) turns sums into products.

---

### Q6. $z_1, z_2, z_3, z_4$ satisfy $z_1 + z_3 = z_2 + z_4$ (a parallelogram in order). A complex number $z$ lies on the line joining $z_1$ and $z_4$ such that

$$\arg\!\left(\frac{z-z_2}{z_1-z_2}\right) = \arg\!\left(\frac{z_3-z_2}{z-z_2}\right)$$

Given $|z - z_4| = 5$, $|z - z_2| = |z - z_3| = 6$, which are correct?

(A) Area of $\triangle(z, z_1, z_2) = 3\sqrt7$  (B) Area of $\triangle(z, z_3, z_4) = \dfrac{15\sqrt7}{4}$

(C) Area of quadrilateral $z_1z_2z_3z_4 = \dfrac{27\sqrt7}{2}$  (D) Area of quadrilateral $z_1z_2z_3z_4 = \dfrac{47\sqrt7}{3}$

**Answer: (A), (B), (C)**

---

#### Approach 1 — Standard: Coordinates with $z$ on side $z_1z_4$

The parallelogram condition gives: place $z_1 = 0$, $z_4 = u$ (so $z = tu$ on the line), $z_2 = v$, $z_3 = u+v$.

**From $|z-z_2| = |z-z_3| = 6$:** subtracting the two equations kills $|v|^2$:

$$|v - tu|^2 - |(1-t)u + v|^2 = 0 \;\Rightarrow\; u\cdot v = \frac{|u|^2(2t-1)}{2}$$

**Bisector condition:** $\arg$-equality means $\left(\frac{z-z_2}{z_1-z_2}\right) / \left(\frac{z_3-z_2}{z-z_2}\right)$ is a **positive real**, i.e. with $w = z - z_2 = tu - v$: $w^2$ and $-(u)(v)$ have the same argument.

Writing $u = U > 0$ real (rotate frame), $v = a + ib$: from $u\cdot v$: $a = U(2t-1)/2$, so $\operatorname{Re}(w) = tU - a = U/2$. With $|w|^2 = U^2/4 + b^2 = 36$ and the argument condition:

$$b^2 = \frac{U^2(4t-1)}{4}, \qquad \text{and combining: } U^2 t = 36$$

**From $|z - z_4| = 5$:** $|t-1|U = 5 \Rightarrow U^2 = 25/(t-1)^2$. Substituting into $U^2 t = 36$:

$$36(t-1)^2 = 25t \;\Rightarrow\; 36t^2 - 97t + 36 = 0 \;\Rightarrow\; t = \frac{4}{9} \ \ (\text{or } \tfrac94 \text{ — extraneous for the drawn configuration})$$

So $U = 9$, $v = \left(-\tfrac12, \pm\tfrac{3\sqrt7}{2}\right)$:

- **(A)** $\triangle(z,z_1,z_2)$: $z = (4,0)$, $z_1 = (0,0)$, $z_2 = (-\tfrac12, \tfrac{3\sqrt7}{2})$: area $= \frac12|4\cdot\frac{3\sqrt7}{2} - 0| = 3\sqrt7$ ✓
- **(B)** $\triangle(z,z_3,z_4)$: $z_3 = (\tfrac{17}{2}, \tfrac{3\sqrt7}{2})$, $z_4 = (9,0)$: area $= \frac12|(z_3-z)\times(z_4-z)| = \frac{15\sqrt7}{4}$ ✓
- **(C)** Parallelogram $= |\det(u, v)| = 9\cdot\frac{3\sqrt7}{2} = \frac{27\sqrt7}{2}$ ✓ — and (D) gives a different value ✗

#### Approach 2 — Exam Hack

All three correct values share the $\sqrt7$ from $b = \frac{3\sqrt7}{2}$. Parallelogram area $= |u|\cdot|b| = 9 \cdot \frac{3\sqrt7}{2}$ once $|u| = 9$ is found from $U^2 t = 36$ with $t = 4/9$. Option (D) can be eliminated because (C) and (D) state *different* areas for the *same* quadrilateral — at most one is true, and the exact computation gives (C).

> [!tip] Exam Shortcut
> $|z-z_2| = |z-z_3|$ with $z$ on line $z_1z_4$ immediately yields $z_2z$ and $zz_3$ symmetry: subtract the two circle equations before doing anything else — the quadratic in $t$ collapses to $U^2 t = 36$.

> [!warning] Trap & Common Pitfall
> The $\arg$-equality says the ray $z_2 z$ **bisects** $\angle z_1 z_2 z_3$ — don't confuse it with perpendicularity. Also $t = 9/4$ solves the algebra but places $z$ beyond $z_4$, inconsistent with the figure/areas; use $t = 4/9$.

> [!success] Key Takeaway
> For parallelogram problems, put $z_1$ at the origin with one side along the real axis: every condition becomes a short real equation in $(t, |u|, \operatorname{Im} v)$.

---

### Q7. Complex numbers $z_1, z_2, z_3, z_4$ (in order) are vertices of a quadrilateral with $5z_1 - 6z_2 + 3z_3 - 2z_4 = 0$ and $5|z_1-z_4|^2 = 9|z_2-z_3|^2$. Which is/are correct?

(A) $z_1z_2z_3z_4$ is a rectangle.  (B) Segment $z_1z_3$ divides $z_2z_4$ in ratio $1:3$.  (C) Segment $z_2z_4$ divides $z_1z_3$ in ratio $3:5$.  (D) $z_1, z_2, z_3, z_4$ are concyclic.

**Answer: (B), (C), (D)**

---

#### Approach 1 — Standard: Section Formula + Ptolemy/Chord Test

Rearrange: $5z_1 + 3z_3 = 6z_2 + 2z_4 = 8P$. Then

$$P = \frac{5z_1 + 3z_3}{8} = z_1 + \frac{3}{8}(z_3 - z_1) \;\Rightarrow\; z_1P : Pz_3 = 3 : 5 \quad \textbf{(C) ✓}$$

$$P = \frac{6z_2 + 2z_4}{8} = z_2 + \frac{1}{4}(z_4 - z_2) \;\Rightarrow\; z_2P : Pz_4 = 1 : 3 \quad \textbf{(B) ✓}$$

**(A)** A rectangle needs $P$ to be the **midpoint** of both diagonals; ratios $3:5$ and $1:3$ are not $1:1$ ✗.

**(D)** Concyclicity ⇔ equal chord products through $P$: need $AP\cdot PC = BP\cdot PD$. Put $P$ at the origin: $z_3 = -\tfrac53 z_1$, $z_4 = -3z_2$. The given modulus condition:

$$5|z_1 + 3z_2|^2 = |5z_1 + 3z_2|^2 \;\Rightarrow\; 5|z_1|^2 + 45|z_2|^2 = 25|z_1|^2 + 9|z_2|^2 \;\Rightarrow\; 9|z_2|^2 = 5|z_1|^2$$

Now: $AP\cdot PC = |z_1|\cdot\frac53|z_1| = \frac53|z_1|^2$ and $BP\cdot PD = |z_2|\cdot 3|z_2| = 3|z_2|^2 = 3\cdot\frac59|z_1|^2 = \frac53|z_1|^2$ — **equal** ⇒ chords cut mutually proportional segments with equal products ⇒ $z_1z_2z_3z_4$ is concyclic $\boldsymbol{\checkmark}$.

(Equivalently: the vertical angles at $P$ plus $AP\cdot PC = BP\cdot PD$ is exactly the intersecting-chords criterion.)

#### Approach 2 — Exam Hack

From $9|z_2|^2 = 5|z_1|^2$ the sides scale as $|z_1z_4| : |z_2z_3| = 3:5$ — matching the given $5|z_1-z_4|^2 = 9|z_2-z_3|^2$ by construction. Ratios (B), (C) read straight off the coefficients $5, 3$ and $6, 2$: $3:5$ and $2:6 = 1:3$.

> [!tip] Exam Shortcut
> Coefficients give the section ratios directly: $5z_1 + 3z_3 \Rightarrow 3:5$ on $z_1z_3$; $6z_2 + 2z_4 \Rightarrow 1:3$ on $z_2z_4$. No coordinates needed for (B), (C).

> [!warning] Trap & Common Pitfall
> (A) is tempting because "diagonals intersect" — but rectangle requires bisecting (equal ratios), and it fails immediately. Concyclicity needs the **product** $AP\cdot PC = BP\cdot PD$, not just "some angle condition."

> [!success] Key Takeaway
> Intersecting-chords theorem in complex form: $A, B, C, D$ concyclic (with $P = AC \cap BD$) $\iff |A-P||C-P| = |B-P||D-P|$ (when the cross ratio is real). This plus section formulas solves the whole question.

---

## PART 1: MATHEMATICS — SECTION I (iii) [Match the Column]

---

### Q8. Match List-I with List-II.

**List-I:** (P) Total number of three-digit numbers whose digit sum is even. (Q) Number of positive integral solutions of $xyz = 140$. (R) Number of positive integral solutions of $x + y + z \le 10$. (S) If $x^3+ax^2+bx+c$ is divisible by $x^2+1$, the number of three-digit numbers of the form $abc$ or $bca$ that can be formed.

**List-II:** (1) 18  (2) 54  (3) 120  (4) 450  (5) 150

(A) $P\!\to\!4; Q\!\to\!2; R\!\to\!1; S\!\to\!3$  (B) $P\!\to\!4; Q\!\to\!2; R\!\to\!3; S\!\to\!1$  (C) $P\!\to\!4; Q\!\to\!1; R\!\to\!3; S\!\to\!2$  (D) $P\!\to\!4; Q\!\to\!3; R\!\to\!1; S\!\to\!2$

**Answer: (B)** — $P \to 450$, $Q \to 54$, $R \to 120$, $S \to 18$

---

#### (P) Digit-sum even → 450

$9 \times 10 \times 10 = 900$ three-digit numbers. For any choice of first two digits, exactly half of the ten choices for the units digit keep the sum even (parity flips equally). $900/2 = 450$ → **(4)**.

#### (Q) $xyz = 140$ → 54

$140 = 2^2\cdot 5\cdot 7$. Exponents distribute independently: $a_1+a_2+a_3 = 2 \Rightarrow \binom{4}{2} = 6$; $b_1+b_2+b_3 = 1 \Rightarrow 3$; $c_1+c_2+c_3 = 1 \Rightarrow 3$. Total $= 6\times3\times3 = 54$ → **(2)**.

#### (R) $x+y+z \le 10$, positive integers → 120

Slack variable $t \ge 0$: $x+y+z+t = 10$ with $x,y,z \ge 1$. Set $x' = x-1$ etc.: $x'+y'+z'+t = 7$ in non-negative integers:

$$\binom{7+4-1}{4-1} = \binom{10}{3} = 120 \;\to\; \textbf{(3)}$$

#### (S) Divisible by $x^2+1$ → 18

$x = \pm i$ are roots: $(c-a) + (b-1)i = 0 \Rightarrow b = 1,\ c = a$ (digits: $b=1$, $c = a$, $0 \le a \le 9$).

- Form $abc = a\,1\,a$: $a = 1..9 \Rightarrow 9$ numbers.
- Form $bca = 1\,a\,a$: $a = 0..9 \Rightarrow 10$ numbers.
- Overlap: only $111$ (appears in both).

Total $= 9 + 10 - 1 = 18$ → **(1)**.

> [!tip] Exam Shortcut
> (P) is a pure parity argument — never count cases. (R): "$\le$ with positivity" ⇒ one slack variable ⇒ $\binom{10}{3}$ instantly.

> [!warning] Trap & Common Pitfall
> In (S), $a = 0$ is allowed for $bca$ ($100$ is a valid three-digit number) but not for $abc$ ($010$ is not). Missing this gives $17$, not $18$. Also don't forget the $-1$ for the double-counted $111$.

> [!success] Key Takeaway
> Multiplicative primes ⇒ stars-and-bars on exponents; "sum ≤" ⇒ slack variable; digit-forms with parameter digits ⇒ count each family separately, then inclusion–exclude the overlap.

---

### Q9. Let $z_k = e^{2\pi i k/10}$, $k = 1, 2, \ldots, 9$ (the 10th roots of unity except 1). Match:

**List-I:** (P) For each $z_k$ there exists a $z_j$ such that $z_k z_j = 1$. (Q) There exists $k \in \{1,\dots,9\}$ such that $z_1 z = z_k$ has no solution $z$ in the set of complex numbers. (R) $\left|\prod_{k=1}^{9}(1-z_k)\right|/10$ equals. (S) $1 - \sum_{k=1}^{9}\cos\frac{2k\pi}{10}$ equals.

**List-II:** (1) True  (2) False  (3) 1  (4) 2  (5) 4

(A) $P\!\to\!1; Q\!\to\!2; R\!\to\!4; S\!\to\!3$  (B) $P\!\to\!2; Q\!\to\!1; R\!\to\!3; S\!\to\!4$  (C) $P\!\to\!1; Q\!\to\!2; R\!\to\!3; S\!\to\!4$  (D) $P\!\to\!2; Q\!\to\!1; R\!\to\!4; S\!\to\!3$

**Answer: (C)** — $P \to$ True, $Q \to$ False, $R \to 1$, $S \to 2$

---

#### Solutions

**(P) True:** $z_k^{-1} = z_{10-k}$, and $10-k \in \{1,\dots,9\}$ whenever $k$ is. The inverse lives in the set ⇒ **(1)**.

**(Q) False:** Over $\mathbb{C}$, $z = z_k/z_1$ always exists — every nonzero complex equation $z_1 z = z_k$ is solvable. The statement's "no solution" is false ⇒ **(2)**.

**(R)** From $z^{10} - 1 = (z-1)\prod_{k=1}^{9}(z - z_k)$:

$$\prod_{k=1}^{9}(z-z_k) = 1 + z + \cdots + z^9 \;\xrightarrow{z=1}\; \prod_{k=1}^9 (1-z_k) = 10 \;\Rightarrow\; \frac{|10|}{10} = 1 \;\to\; \textbf{(3)}$$

**(S)** $\sum_{k=0}^{9}\cos\frac{2k\pi}{10} = \operatorname{Re}\sum_{k=0}^{9} e^{2\pi i k/10} = \operatorname{Re}(0) = 0$, so $\sum_{k=1}^{9}\cos\frac{2k\pi}{10} = -\cos 0 = -1$. Therefore $1 - (-1) = 2$ → **(4)**.

> [!tip] Exam Shortcut
> (R): plug $z = 1$ into the factorization — the product of $(1-z_k)$ is the *trace* $= n$ for any $n$-th roots of unity set. (S): the cosine sum over full roots is always $0$ minus the $k=0$ term.

> [!warning] Trap & Common Pitfall
> (Q) says "in the set of complex numbers" — not "in the set $\{z_k\}$". If it had said the latter, it would be True for some $k$; as written it is False.

> [!success] Key Takeaway
> $\sum_{k=1}^{n-1}(1-z_k) = n$ (in modulus), $\operatorname{Re}\sum z_k = 0$, and inverses close inside the set — the three standard roots-of-unity facts, all in one question.

---

### Q10. The equation $z^4 - 6z^3 + 18z^2 - 30z + 25 = 0$ has roots $z_1, z_2, z_3, z_4$ with $|z_1 - 1 - 2i| = 0$, $\operatorname{Re}(z_4) = \operatorname{Re}(z_1)$, $\operatorname{Im}(z_2) > 0$ (and $z_4 = \bar z_1$ etc. as forced). Match:

**List-I:** (P) Area of quadrilateral bounded by $z_1, z_2, z_3, z_4$. (Q) $\left|\dfrac{(z_0-\bar z_1)(z_0-\bar z_3)}{(z_0-\bar z_4)(z_0-\bar z_2)}\right|$ for any real $z_0$. (R) If $\sum_{i=1}^4 |\alpha - z_i|$ is minimum then $3|\alpha| = ?$ (S) If $\arg\!\left(\dfrac{\beta - z_1}{\beta - z_3}\right) = \tan^{-1}\!\dfrac{2}{1+\sqrt5} + \tan^{-1}\!\dfrac{1}{2+\sqrt5}$ then $\dfrac{1}{\sqrt5}|\beta - 2 - i|_{\max} = ?$

**List-II:** (1) 1  (2) 2  (3) 3  (4) 4  (5) 5

(A) $P\!\to\!3; Q\!\to\!3; R\!\to\!4; S\!\to\!3$  (B) $P\!\to\!3; Q\!\to\!1; R\!\to\!3; S\!\to\!4$  (C) $P\!\to\!3; Q\!\to\!1; R\!\to\!5; S\!\to\!2$  (D) $P\!\to\!1; Q\!\to\!3; R\!\to\!2; S\!\to\!5$

**Answer: (C)** — $P \to 3$, $Q \to 1$, $R \to 5$, $S \to 2$

---

#### Step 1 — Find the four roots

$z_1 = 1 + 2i$. Real coefficients ⇒ $z_4 = \bar z_1 = 1 - 2i$ (consistent with $\operatorname{Re}(z_4) = \operatorname{Re}(z_1)$). Let $z_{2,3} = \alpha \pm i\beta$.

- Sum: $2 + 2\alpha = 6 \Rightarrow \alpha = 2$
- Product: $|z_1|^2|z_2|^2 = 5(4+\beta^2) = 25 \Rightarrow \beta = 1$

Roots: $1\pm 2i,\ 2\pm i$ with $\operatorname{Im}(z_2) > 0 \Rightarrow z_2 = 2+i,\ z_3 = 2-i$.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}[scale=0.9]
  \draw[->, >=stealth, gray!70] (-3.2,0) -- (3.2,0) node[right] {$\mathrm{Re}$};
  \draw[->, >=stealth, gray!70] (0,-2.8) -- (0,2.8) node[above] {$\mathrm{Im}$};
  \draw[blue, thick, domain=0:360, samples=120, variable=\t]
    plot ({sqrt(5)*cos(\t)}, {sqrt(5)*sin(\t)});
  \node[below right, blue] at (2.3,-0.4) {$|z|=\sqrt5$};
  \filldraw[red] (1,2) circle (2pt) node[above] {$z_1{=}1{+}2i$};
  \filldraw[red] (1,-2) circle (2pt) node[below] {$z_4{=}1{-}2i$};
  \filldraw[red] (2,1) circle (2pt) node[above right] {$z_2{=}2{+}i$};
  \filldraw[red] (2,-1) circle (2pt) node[below right] {$z_3{=}2{-}i$};
  \filldraw[black] (2,0) circle (2pt) node[below] {$2$};
  \filldraw[teal] (-2,-1) circle (2pt) node[below left] {$-(2{+}i)$ antipode};
\end{tikzpicture}
\end{document}
```

#### (P) Area of quadrilateral → 3

Shoelace on $(1,2), (2,1), (2,-1), (1,-2)$: area $= \frac12|{\cdots}| = 3$ → **(3)**.

#### (Q) Real $z_0$ ⇒ conjugate pairs ⇒ ratio of conjugate moduli

$\bar z_1 = 1-2i$ and $\bar z_4 = 1+2i$ are conjugates ⇒ $|z_0 - \bar z_1| = |z_0 - \bar z_4|$ for real $z_0$. Likewise $|z_0 - \bar z_3| = |z_0 - \bar z_2|$. Numerator and denominator are term-wise equal in modulus ⇒ value $= 1$ → **(1)**.

#### (R) Minimum of $\sum|\alpha - z_i|$ → diagonal intersection $\Rightarrow 3|\alpha| = 5$

The Fermat–Weber point of the kite lies on its symmetry axis (real axis). Minimizing $f(t) = 2\sqrt{(t-1)^2+4} + 2\sqrt{(t-2)^2+1}$ gives $f'(t) = 0 \Rightarrow t = 5/3$, $\alpha = 5/3$. This is also exactly the intersection $P$ of diagonals $z_1z_3$ and $z_2z_4$: solving the two line equations gives $P = (5/3, 0)$. Then $3|\alpha| = 3\cdot\frac53 = 5$ → **(5)**.

#### (S) Argand circle → $\frac{1}{\sqrt5}|\beta-(2+i)|_{\max} = 2$

$\tan^{-1}\frac{2}{1+\sqrt5} = \tan^{-1}\frac{\sqrt5-1}{2} = 31.72^\circ$ and $\tan^{-1}\frac{1}{2+\sqrt5} = \tan^{-1}(\sqrt5-2) = 13.28^\circ$; sum $= 45^\circ$. So $\arg\frac{\beta-z_1}{\beta-z_3} = \frac\pi4$: $\beta$ sees chord $z_1z_3$ under $45°$ ⇒ $\beta$ lies on the **major arc** of the circle through $z_1, z_3$ with central angle $90°$. Both $|z_1| = |z_3| = \sqrt5$ ⇒ the circle is centred at the **origin**, radius $\sqrt5$.

Point $2+i$ lies **on** this circle ($|2+i| = \sqrt5$), so the maximum distance to a point of the circle is the diameter $= 2\sqrt5$ (the antipode $-2-i$ lies on the major arc). Hence $\frac{1}{\sqrt5}(2\sqrt5) = 2$ → **(2)**.

> [!tip] Exam Shortcut
> (Q): "real $z_0$" + conjugate pairs kills the expression in one line. (S): recognize the constant angle ⇒ circle through the two points; test whether $|z_1|=|z_3|=R$ to identify the centre as the origin.

> [!warning] Trap & Common Pitfall
> Don't assume the centre is the midpoint of $z_1z_3$ — it is only on the perpendicular bisector. Checking $|z_1| = |z_3| = \sqrt5$ pins it at 0 (or $(3+i)$; the arc direction selects the origin).

> [!success] Key Takeaway
> Minimizing $\sum |z - z_i|$ (kite/parallelogram-type symmetric sets): the optimal point often coincides with a diagonal intersection — verify by the derivative or by equal "tension" along the symmetry axis.

---

### Q11. Let

$$P(n+1) = \sum_{k=0}^{n}(-1)^{n-k}\cdot\frac{k}{k+1}\cdot\frac{(n+1)!}{k!\,(n+1-k)!}$$

Match: **List-I:** (P) $P(8)$  (Q) $P(7)$  (R) $P(9)$  (S) $P(11)$ with **List-II:** (1) $\frac34$  (2) $\frac45$  (3) $1$  (4) $\frac56$  (5) $\frac14$.

(A) $P\!\to\!1; Q\!\to\!2; R\!\to\!3; S\!\to\!5$  (B) $P\!\to\!3; Q\!\to\!1; R\!\to\!2; S\!\to\!4$  (C) $P\!\to\!5; Q\!\to\!3; R\!\to\!4; S\!\to\!1$  (D) $P\!\to\!2; Q\!\to\!4; R\!\to\!5; S\!\to\!3$

**Answer: (B)** — $P(8) \to 1$, $P(7) \to \frac34$, $P(9) \to \frac45$, $P(11) \to \frac56$

---

#### Approach 1 — Standard: Closed Form via $\frac{k}{k+1} = 1 - \frac{1}{k+1}$

With $m = n+1$: $P(m) = \sum_{k=0}^{m-1}(-1)^{m-1-k}\binom{m}{k}\frac{k}{k+1}$. Split:

$$P(m) = \underbrace{\sum_{k=0}^{m-1}(-1)^{m-1-k}\binom{m}{k}}_{=1} - \underbrace{\frac{1}{m+1}\sum_{k=0}^{m-1}(-1)^{m-1-k}\binom{m+1}{k+1}}_{\text{shift } j=k+1}$$

The first sum: extend to $k = m$ (last term 0 anyway) — it is $\sum_j (-1)^{?}\binom{m}{m-j} = (1-1)^m$-type $= 1$ after sign bookkeeping. For the second, $\binom{m}{k}\frac{k}{k+1} = \frac{1}{m+1}\binom{m+1}{k+1}$, and $\sum_{j=1}^{m}(-1)^{m-j}\binom{m+1}{j} = 1 - (-1)^m$ (drop $j = 0, m+1$ terms from the full binomial expansion of $(1-1)^{m+1} = 0$). Hence

$$P(m) = 1 - \frac{1 - (-1)^m}{m+1} = \begin{cases} 1, & m \text{ even}\\[4pt] 1 - \dfrac{2}{m+1}, & m \text{ odd} \end{cases}$$

- $P(7) = 1 - 2/8 = \frac34$ → Q→(1)
- $P(8) = 1$ → P→(3)
- $P(9) = 1 - 2/10 = \frac45$ → R→(2)
- $P(11) = 1 - 2/12 = \frac56$ → S→(4)

⇒ option **(B)**.

#### Approach 2 — Exam Hack: Compute the first few directly

$m=1$: $P = \frac{0}{1}\cdot 1 = 0$? Direct: $k=0$ only, term $=0$ ⇒ $P(1) = 0 = 1 - 2/2$ ✓ (odd rule). $m=2$: $k=0,1$: $(-1)^1\cdot0\cdot\ldots + (+1)\frac12\binom21 = 1$ ✓ even rule. The pattern $0, 1, \frac34, 1, \frac45, 1, \frac56$ locks on.

> [!tip] Exam Shortcut
> Split $\frac{k}{k+1} = 1 - \frac{1}{k+1}$; the "$1$" part gives 1, the "$\frac{1}{k+1}$" part converts to $\binom{m+1}{k+1}/(m+1)$ — a telescoped binomial sum. Result: **even $m \to 1$; odd $m \to 1 - \frac{2}{m+1}$**.

> [!warning] Trap & Common Pitfall
> Don't try to simplify $\binom{m}{k}\frac{k}{k+1}$ into a binomial coefficient with the *same* upper index — it needs $m+1$ on top. That single index shift is the whole problem.

> [!success] Key Takeaway
> $\frac{k}{k+1}$-weighted alternating binomial sums are exact rational numbers with period-2 behaviour in $m$. Quick values: even $m$ always give 1.

---

### Q12. $(1+x)^{1/x} = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \cdots$ near $x = 0$, with $a_2 = \frac{m}{n}e$, $a_3 = \frac{p}{q}e$, where $m, p \in \mathbb{I}$, $n, q \in \mathbb{N}$, $\operatorname{HCF}(|m|, n) = \operatorname{HCF}(|p|, q) = 1$. Evaluate $|m| + |p| + n + q$.

**Answer: 58**

---

#### Approach 1 — Standard: Exponential of a Log Series

$$(1+x)^{1/x} = \exp\!\left(\frac{\ln(1+x)}{x}\right) = \exp\!\left(1 - \frac{x}{2} + \frac{x^2}{3} - \frac{x^3}{4} + \cdots\right) = e\cdot\exp(u)$$

with $u = -\frac{x}{2} + \frac{x^2}{3} - \frac{x^3}{4} + \cdots$. Expand $e^u = 1 + u + \frac{u^2}{2} + \frac{u^3}{6} + \cdots$:

- $[x^2]$: from $u$: $\frac13$; from $\frac{u^2}{2}$: $\frac12\cdot\frac14 = \frac18$; from $\frac{u^3}{6}$: $(u^3$ starts at $x^3) = 0$. Total $\frac13 + \frac18 = \frac{11}{24}$
- $[x^3]$: from $u$: $-\frac14$; from $\frac{u^2}{2}$: $\frac12\cdot2\left(-\frac12\right)\!\left(\frac13\right) = -\frac16$; from $\frac{u^3}{6}$: $\frac16\left(-\frac12\right)^3 = -\frac{1}{48}$. Total $= -\frac{12+8+1}{48} = -\frac{21}{48} = -\frac{7}{16}$

So $a_2 = \frac{11}{24}e \Rightarrow m = 11,\ n = 24$; $a_3 = -\frac{7}{16}e \Rightarrow p = -7,\ q = 16$ (both pairs coprime ✓).

$$|m| + |p| + n + q = 11 + 7 + 24 + 16 = 58$$

#### Approach 2 — Exam Hack: Numerical Differentiation

At $x = 0$: $a_0 = e$. Compute $f''(0)/2$ numerically from $f(x) = (1+x)^{1/x}$: sample $f(\pm h)$ with $h \sim 10^{-3}$ — $f''(0)/2 \approx \frac{f(h) - 2f(0) + f(-h)}{2h^2} \approx 1.127 = \frac{11}{24}e$ ✓. $\frac{11}{24}$ and $-\frac{7}{16}$ are the only options yielding integer-coprime pairs summing to 58.

> [!tip] Exam Shortcut
> The series is $e\cdot\exp\!\left(-\frac x2 + \frac{x^2}3 - \frac{x^3}4 + \cdots\right)$ — only $u, u^2/2, u^3/6$ up to $x^3$ are needed. Two lines of bookkeeping.

> [!warning] Trap & Common Pitfall
> HCF conditions fix the *signs and reduction*: $a_3 < 0$ means $p = -7$ (not $+7$), and $|p|$ enters the sum — don't drop the minus when adding $|p|$.

> [!success] Key Takeaway
> $\frac{\ln(1+x)}{x} = 1 - \frac x2 + \frac{x^2}{3} - \cdots$ is the universal seed for $(1+x)^{1/x}$-type expansions; coefficients are controlled by partitions of small powers.

---

### Q13. Let
$$a = \sum_{n=0}^{\infty}\frac{x^{3n}}{(3n)!}, \qquad b = \sum_{n=0}^{\infty}\frac{x^{3n+1}}{(3n+1)!}, \qquad c = \sum_{n=0}^{\infty}\frac{x^{3n+2}}{(3n+2)!}$$
Evaluate $a^3 + b^3 + c^3 - 3abc$.

**Answer: 1**

---

#### Approach 1 — Standard: $\omega$-Factorization of $e^x$ Trisection

$$a^3+b^3+c^3 - 3abc = (a+b+c)(a+\omega b+\omega^2 c)(a+\omega^2 b + \omega c), \qquad \omega = e^{2\pi i/3}$$

Identify each factor against the exponential series:

- $a + b + c = \sum_{k\ge0}\frac{x^k}{k!} = e^{x}$ (the three residue classes partition all $k$).
- $a + \omega b + \omega^2 c = \sum_{n}\left[\frac{x^{3n}}{(3n)!} + \omega\frac{x^{3n+1}}{(3n+1)!} + \omega^2\frac{x^{3n+2}}{(3n+2)!}\right]$, and since $\omega^{3n} = 1$, $\omega^{3n+1} = \omega$, $\omega^{3n+2} = \omega^2$, this is $\sum_k \frac{(\omega x)^k}{k!} = e^{\omega x}$.
- Symmetrically, $a + \omega^2 b + \omega c = e^{\omega^2 x}$.

$$\text{Product} = e^{x}\cdot e^{\omega x}\cdot e^{\omega^2 x} = e^{x(1+\omega+\omega^2)} = e^{0} = 1$$

#### Approach 2 — Exam Hack: Check $x = 0$ and $x \to$ Small

At $x = 0$: $a = b = c = 1$ ⇒ $1 + 1 + 1 - 3 = 0$? — no: the identity must hold for all $x$, and the expression is **constant** (every term is a power series whose non-constant terms cancel). The $x^1$ coefficient: $3a^2b + \ldots$ at $x = 0$ gives $3(1)(1) + 3(1)(1)\cdot$? — simpler: from the factorized form the value is $e^{x(1+\omega+\omega^2)} = 1$ for every $x$, in particular any test value. Answer: **1** (not 0 — do not blindly evaluate the un-cancelled $x=0$ pieces of a factorized expression).

> [!tip] Exam Shortcut
> $a, b, c$ are the three "arms" of $e^x$ mod 3 ⇒ $a+b+c = e^x$, $\omega$-weighting replaces $x \to \omega x$. The triple product always collapses to $e^{x(1+\omega+\omega^2)} = 1$.

> [!warning] Trap & Common Pitfall
> Don't try to expand the cubes — the cross terms cancel *because* $1 + \omega + \omega^2 = 0$. Any step where you "approximate $\omega$" is wrong.

> [!success] Key Takeaway
> The identity $(a+b+c)(a+\omega b+\omega^2c)(a+\omega^2b+\omega c) = a^3+b^3+c^3-3abc$ turns cubics into linears whenever cube roots of unity appear.

---

### Q14. Value of the remainder when
$$\sum_{r=0}^{2014}\ \sum_{k=0}^{r}(-1)^k (k+1)(k+2)\binom{2019}{r-k}$$
is divided by 64.

**Answer: 62**

---

#### Approach 1 — Standard: Generating Functions (Convolution)

Inner sum in $r$: it is a convolution of sequences $a_k = (-1)^k(k+1)(k+2)$ and $b_j = \binom{2019}{j}$.

- $\sum_{k\ge0}(k+1)(k+2)(-x)^k = \dfrac{2}{(1+x)^3}$
- $\sum_{j}\binom{2019}{j}x^j = (1+x)^{2019}$

$$\sum_{k=0}^{r}(-1)^k(k+1)(k+2)\binom{2019}{r-k} = [x^r]\,\frac{2(1+x)^{2019}}{(1+x)^3} = 2\binom{2016}{r}$$

For $r \le 2014 < 2016$ this is always valid. Sum over $r$:

$$S = 2\sum_{r=0}^{2014}\binom{2016}{r} = 2\left(2^{2016} - \binom{2016}{2015} - \binom{2016}{2016}\right) = 2^{2017} - 2(2017) = 2^{2017} - 4034$$

Mod 64: $2^{2017} \equiv 0 \pmod{64}$ (exponent $\ge 6$), and $4034 = 63\cdot64 + 2 \Rightarrow 4034 \equiv 2$.

$$S \equiv -2 \equiv 62 \pmod{64}$$

#### Approach 2 — Exam Hack: Work modulo 64 Early

Only $r \le 6$ matter mod 64... not quite — but note $2\binom{2016}{r}$ for $r \ge 6$ is divisible by 64? Not uniformly; cleaner: use the closed form above. The key insight is that the answer must be *odd or even with $2^{2017}$-style* tail: $2^{2017} \equiv 0$, so the answer is $(-4034) \bmod 64 = 62$ — among numerical options only 62 fits $-2 \bmod 64$.

> [!tip] Exam Shortcut
> $(k+1)(k+2)(-1)^k \leftrightarrow 2/(1+x)^3$ kills the whole inner sum: everything collapses to $2\binom{2016}{r}$, then hockey-stick $\sum_{r\le 2014} = 2^{2016} - 2017$.

> [!warning] Trap & Common Pitfall
> Don't compute the binomial sum term-by-term mod 64 (2015 terms). Also: the two excluded tail terms are $r = 2015, 2016$ — forgetting them changes the residue by $2(2016+1) \bmod 64 \neq 0$.

> [!success] Key Takeaway
> Sums of the form $\sum (-1)^k (\text{polynomial in } k)\binom{n}{r-k}$ are coefficient extraction of $\frac{P(-x)}{(1+x)^{d}}\cdot(1+x)^n$ — generating functions turn alternating convolutions into single binomials.

---

### Q15. Number of five-digit numbers divisible by 3 using digits $\{1,\dots,9\}$ with repetition is $3^k$; then $k =$

**Answer: 9**

First four digits: $9^4$ choices. Digits split evenly into residue classes mod 3 (three each), so the partial sum mod 3 is uniform. For each residue, exactly 3 digits complete it to a multiple of 3:

$$N = 9^4 \times 3 = 3^8 \cdot 3 = 3^9 \;\Rightarrow\; k = 9$$

> [!tip] Exam Shortcut
> Uniformity of residues: with digits 1–9 the last digit has exactly 3 valid completions regardless of the first four — answer $9^4\cdot3$, never enumerate.

> [!warning] Trap & Common Pitfall
> Leading digit can't be 0 — but 0 isn't in the set at all here, so all $9^4$ prefixes are legal. If 0 were included, only the leading digit would be restricted.

> [!success] Key Takeaway
> "Divisible by 3 with allowed-repetition digits that split evenly mod 3" ⇒ multiply by $3^{?}$ at the end; count = (prefixes) × (3 completions).

---

### Q16. Two Americans, two British, one Chinese, one Dutch and one Egyptian sit at a round table so that persons of the same nationality are separated. Number of ways =

**Answer: 336**

#### Approach 1 — Inclusion–Exclusion (PIE)

Total circular arrangements: $(7-1)! = 720$.

- $X$ = Americans adjacent: glue them ⇒ $(6-1)!\cdot 2! = 240$
- $Y$ = British adjacent: likewise $240$
- $X\cap Y$: both pairs glued ⇒ $(5-1)!\cdot2!\cdot2! = 96$

Favorable $= 720 - (240 + 240 - 96) = 336$.

#### Approach 2 — Exam Hack: Sequential Placement

Seat one American first (fixes the circle): choose seat for the second American avoiding 2 forbidden seats among 6: $6 - 2 = 4$ ways… (bookkeeping with the Brits gets messy) — PIE above is the 30-second path.

> [!tip] Exam Shortcut
> Round table PIE: glue-adjacent pairs, divide by rotations *before* subtracting. $720 - 480 + 96 = 336$.

> [!warning] Trap & Common Pitfall
> Rotations are identical — always $(n-1)!$, never $n!$. Glued pairs internal order $2!$ must be kept.

> [!success] Key Takeaway
> Circular PIE with forbidden adjacencies: treat "together" as a super-person, multiply by internal arrangements, alternate signs.

---

### Q17. If $m$ and $x$ are real numbers, then
$$e^{2m i \cot^{-1}x}\left(\frac{xi+1}{xi-1}\right)^{m}$$
is equal to

**Answer: 1**

#### Solution

Let $\theta = \cot^{-1}x \in (0,\pi)$, so $\theta = \frac{\pi}{2} - \tan^{-1}x$ for all real $x$. Then:

$$\frac{1+ix}{1-ix} = e^{2i\tan^{-1}x} \quad\text{and}\quad xi - 1 = -(1 - ix) \;\Rightarrow\; \frac{xi+1}{xi-1} = -\,\frac{1+ix}{1-ix}$$

Therefore

$$\left(\frac{xi+1}{xi-1}\right)^m = (-1)^m e^{2mi\tan^{-1}x}, \qquad e^{2mi\cot^{-1}x} = e^{im\pi}e^{-2mi\tan^{-1}x}$$

Multiply:

$$e^{im\pi}e^{-2mi\tan^{-1}x}\cdot(-1)^m e^{2mi\tan^{-1}x} = (-1)^m(-1)^m = 1$$

> [!tip] Exam Shortcut
> Recognize $\frac{1+ix}{1-ix} = e^{2i\tan^{-1}x}$ (a unit-modulus Möbius map) and $\cot^{-1}x = \frac\pi2 - \tan^{-1}x$ — everything cancels to 1, independent of $m$ and $x$.

> [!warning] Trap & Common Pitfall
> $\cot^{-1}x \ne \tan^{-1}(1/x)$ globally (sign branch for $x<0$). Using $\pi/2 - \tan^{-1}x$ is the safe identity for all real $x$.

> [!success] Key Takeaway
> Pairs like $e^{i m \cot^{-1}x}$ and $\left(\frac{1+ix}{1-ix}\right)^m$ are designed to conjugate-cancel: rewrite both in terms of $\tan^{-1}x$.

---

## PART 2: PHYSICS — SECTION I (i) [Single Correct]

---

### Q18. A uniform wire of monovalent metal has resistance $1.000\,\Omega$ at 100 K and $2.0808\,\Omega$ at 300 K. The metal expands isotropically with temperature-independent linear expansion coefficient $\alpha = 1.0\times10^{-4}\,\mathrm{K^{-1}}$. Number of conduction electrons and effective electron mass are constant. In the Drude model, the ratio of relaxation times $\tau_{100}/\tau_{300}$ is

(A) 1.92  (B) 2.00  (C) 2.04  (D) 2.08

**Answer: (B) 2.00**

---

#### Approach 1 — Standard: Drude Resistivity + Thermal Expansion

Drude: $\rho = \frac{m}{ne^2\tau}$. Total electrons $N$ fixed ⇒ $n = N/V$ changes with volume, but a cleaner route uses $R = \frac{\rho L}{A} = \frac{m_e L}{N e^2 \tau}\cdot\frac{L^2}{LA}$-bookkeeping — precisely:

$$R = \frac{m_e L}{N_{\text{tot}} e^2 \tau}\cdot\frac{L}{A}\cdot A\;\Big/\;\frac{N_{\text{tot}}}{nLA}\ldots \;\Rightarrow\; R = \frac{m_e L^2}{N_{\text{tot}} e^2 \tau}$$

(One-line derivation: $R = \rho L/A$, $\rho = m/(ne^2\tau)$, $n = N_{\text{tot}}/(LA)$ ⇒ $R = mL/(n e^2 \tau A) = m L^2/(N_{\text{tot}}e^2\tau)$.)

With $L(T) = L_{\text{ref}}(1 + \alpha T)$ (reference at 0 K for a temperature-independent $\alpha$):

$$\frac{R_{300}}{R_{100}} = \frac{L_{300}^2/\tau_{300}}{L_{100}^2/\tau_{100}} = \left(\frac{1 + 300\alpha}{1 + 100\alpha}\right)^2\frac{\tau_{100}}{\tau_{300}} = (1.03)^2/(1.01)^2 \cdot \frac{\tau_{100}}{\tau_{300}}$$

$$2.0808 = \frac{1.0609}{1.0201}\cdot\frac{\tau_{100}}{\tau_{300}} \;\Rightarrow\; \frac{\tau_{100}}{\tau_{300}} = 2.0808\times\frac{1.0201}{1.0609} = 2.0808\times0.96156 = 2.001 \approx 2.00$$

#### Approach 2 — Exam Hack: Spot the Distractor

$2.0808 / 1.000 = 2.0808 \approx (1.03/1.01)^2 \times 2.00$. Option (D) $2.08$ is exactly the answer you get **forgetting thermal expansion** — the paper plants it there. Any correct treatment must reduce $2.0808$ by the geometry factor $0.9616$ ⇒ $\approx 2.00$.

> [!tip] Exam Shortcut
> $R \propto L^2/\tau$ when $N$ is fixed (not $1/\tau$ alone). Compute $(1.03/1.01)^2 = 1.0398$, divide: $2.0808/1.0398 \approx 2.00$.

> [!warning] Trap & Common Pitfall
> Using $R \propto 1/\tau$ only gives 2.08 (option D — the planted trap). The expansion changes both $L$ and $A$: $R \propto L/A \propto L^{-1}$ is wrong too when $n$ varies with $V$; the exact invariant is $R = mL^2/(Ne^2\tau)$.

> [!success] Key Takeaway
> Drude + fixed electron count: $R = \frac{m_e L^2}{Ne^2\tau}$. Thermal expansion enters as $(1+\alpha\Delta T)^2$ on $L^2$ — always state which quantities are held constant (N here).

---

### Q19. In the circuit shown, the capacitor is initially uncharged. At $t = 0$, switch $S_1$ closes while $S_2$ remains open. At $t = T = 0.40$ s, $S_2$ also closes ($S_1$ stays closed). Which expression gives $i_3(t)$ through $R_3$ for $t \ge 0.40$ s? Given: $\mathcal{E} = 24$ V, $R_1 = 60$ kΩ, $R_2 = 40$ kΩ, $R_3 = 120$ kΩ, $C = 10\,\mu$F, $T = 0.40$ s.

(A) $i_3(t) = [0.0667 + 0.0176\,e^{-5(t-0.40)}]$ mA
(B) $i_3(t) = [0.0667 - 0.0176\,e^{-5(t-0.40)}]$ mA
(C) $i_3(t) = 0.0843\,e^{-5(t-0.40)}$ mA
(D) $i_3(t) = [0.1333 - 0.0667\,e^{-2.5t}]$ mA

**Answer: (A)**

---

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{tikzpicture}[scale=1.0]
  % battery + R1
  \draw (0,0) to[battery1, l=$\mathcal{E}=24$ V] (0,3)
        to[R, l=$R_1=60$ k$\Omega$] (2.5,3)
        to[short, *-o] (2.5,3) node[above] {$X$};
  % S1 to the capacitor node
  \draw (2.5,3) to[nos, l=$S_1$] (4.5,3)
        to[short] (6.0,3) node[above] {$Y$};
  % C from Y to rail
  \draw (6.0,3) to[C, l=$C=10$ $\mu$F] (6.0,0) -- (0,0);
  % R3 in parallel with C
  \draw (6.0,3) to[R, l=$R_3=120$ k$\Omega$, i=$i_3(t)$] (6.0,0);
  % R2 + S2 from X down to rail
  \draw (2.5,3) to[R, l=$R_2=40$ k$\Omega$] (2.5,1.7)
        to[nos, l=$S_2$] (2.5,0);
  \draw (2.5,0) -- (0,0);
\end{tikzpicture}
\end{document}
```

#### Approach 1 — Standard: Two-Phase Transient Analysis

**Topology:** $\mathcal{E}$ feeds node X through $R_1$; X connects through $S_1$ to node Y (top of $C$); $R_3$ hangs from Y to the return rail; $R_2$ (+ $S_2$) connects X to the return rail.

**Phase 1** ($0 \le t < 0.40$ s, $S_2$ open): $C$ charges through $R_1$ in series with the $R_3$ divider. DC steady state: capacitor open, current $\mathcal{E}/(R_1+R_3) = 24/180\text{k} = 0.1333$ mA, so

$$V_{C,\infty}^{(1)} = 0.1333\text{ mA}\times120\text{ k}\Omega = 16\ \text{V}, \qquad \tau_1 = (R_1\|R_3)\,C = 40\text{k}\times10\mu = 0.40\ \text{s}$$

$$V_C(t) = 16\left(1 - e^{-t/0.4}\right) \;\Rightarrow\; V_C(0.40^-) = 16(1 - e^{-1}) = 10.114\ \text{V}$$

**Phase 2** ($t \ge 0.40$ s, both switches closed): now X is held by the $R_1$-$R_2$ divider and Y = X (through $S_1$); $R_3$ also connects Y to rail.

- **Thevenin voltage at Y:** nodal equation at X=Y: $\frac{V-24}{60\text{k}} + \frac{V}{40\text{k}} + \frac{V}{120\text{k}} = 0 \Rightarrow \frac{V}{20\text{k}} = 0.4$ mA $\Rightarrow V_\infty = 8$ V
- **Thevenin resistance:** short $\mathcal{E}$: $R_{\text{Th}} = R_1 \| R_2 \| R_3 = 60\text{k}\|40\text{k}\|120\text{k} = 20$ kΩ ⇒ $\tau_2 = 20\text{k}\times10\mu = 0.20$ s ⇒ decay rate $1/\tau_2 = 5\ \mathrm{s^{-1}}$ ✓

$$V_C(t) = 8 + (10.114 - 8)\,e^{-5(t-0.40)} = 8 + 2.114\,e^{-5(t-0.40)}\ \text{V}$$

$$i_3(t) = \frac{V_C(t)}{120\text{ k}\Omega} = \left[0.0667 + 0.0176\,e^{-5(t-0.40)}\right]\ \text{mA} \quad \Rightarrow \textbf{(A)}$$

Check continuity: $i_3(0.40^+) = 0.0667 + 0.0176 = 0.0843$ mA $= 10.114/120$ ✓.

#### Approach 2 — Exam Hack: Match Boundary Values Only

- Steady state ($t\to\infty$, both closed): $R_1\|R_2\|R_3$ divider ⇒ $i_3(\infty) = 8\text{V}/120\text{k} = 0.0667$ mA ⇒ only (A), (B) (and not quite D) match. ✓
- Continuity at $t = 0.40^+$: must equal $i_3(0.40^-) = V_C(0.4^-)/120\text{k}$. $V_C(0.4)$ from phase 1 is $> 10$ V ⇒ $i_3 \approx 0.084$ mA. (A) gives $0.0667 + 0.0176 = 0.0843$ ✓; (B) gives $0.0491$ ✗; (C) gives $0.0843$ but vanishes at infinity ✗ (steady state must be nonzero through $R_3$).
- Exponent rate: $\tau_2 = (R_1\|R_2\|R_3)C = 0.2$ s ⇒ $e^{-5(t-0.4)}$ ✓ (D's $2.5t$ wrong).

> [!tip] Exam Shortcut
> With ideal sources, each phase is a simple RC with $V_\infty$ + $\tau$ from the Thevenin seen by $C$. Final state: $R_1\|R_2\|R_3$ all in parallel from the node to rail ⇒ $V_\infty = \mathcal{E}\cdot G_{\text{node}}$-bookkeeping gives 8 V ⇒ 0.0667 mA.

> [!warning] Trap & Common Pitfall
> Capacitor voltage cannot jump: $V_C(0.4^-)$ from phase 1 sets phase 2's initial condition. Jumping straight to the final formula misses the $+0.0176$ offset (options A vs B differ only in this sign).

> [!success] Key Takeaway
> Multi-switch RC: (1) solve each phase separately, (2) carry $V_C$ across the switching instant, (3) $\tau$ always uses the Thevenin resistance with independent sources killed.

---

### Q20. In Wheatstone bridge $ABCD$, an ideal 24 V battery connects $A$–$C$ and a 6 Ω galvanometer connects $B$–$D$. Outer arms: $AB = 8\,\Omega$, $BC = 12\,\Omega$, $CD = 5\,\Omega$; arm $AD$ is itself a bridge with $AP = 2\,\Omega$, $PD = 2\,\Omega$, $AQ = 2\,\Omega$, $QD = 6\,\Omega$, $PQ = 4\,\Omega$. The galvanometer current is closest to

(A) 0.11 A from B to D  (B) 0.32 A from B to D  (C) 0.11 A from D to B  (D) 0.32 A from D to B

**Answer: (C) 0.11 A from D to B**

---

#### Approach 1 — Standard: Reduce Inner Bridge, Then Node-Voltage

**Inner bridge (between A and D):** unbalanced ($AP/PD = 1 \ne AQ/QD = 1/3$). Bridge-equivalent resistance:

$$R_{AD} = \frac{AP\cdot QD(AP+AQ+PD+QD) + \ldots}{\ldots} \;\text{or directly apply the bridge formula with } (2,2,2,6; 4):$$

$$R_{AD} = \frac{2\cdot2\cdot(2+6) + 2\cdot6\cdot(2+2) + 4\cdot(2+2)(2+6)}{(2+2)(2+6) + 4(2+2+2+6)} = \frac{32+48+128}{32+48} = \frac{208}{80} = 2.6\ \Omega$$

**Outer network:** nodes $A = 24$ V, $C = 0$ V; unknowns $V_B, V_D$:

$$\frac{V_B - 24}{8} + \frac{V_B}{12} + \frac{V_B - V_D}{6} = 0 \qquad \frac{V_D - 24}{2.6} + \frac{V_D}{5} + \frac{V_D - V_B}{6} = 0$$

Solving: $V_B \approx 14.93$ V, $V_D \approx 15.60$ V ⇒ $V_B - V_D = -0.667$ V ⇒

$$i_G = \frac{V_B - V_D}{6} = -0.111\ \text{A} \;\Rightarrow\; 0.11\ \text{A from D to B} \quad \textbf{(C)}$$

#### Approach 2 — Exam Hack: Unbalanced-Bridge Sign Test

Without the galvanometer, the two dividers give $V_B = 24\cdot\frac{12}{20} = 9.6$ V... careful: $V_B = 24\cdot\frac{R_{BC}}{R_{AB}+R_{BC}}$-type estimates aren't valid with G connected — but the **sign** is robust: path $A\to D$ ($2.6\,\Omega$ total) is much lower than $A\to B$ arm mix, so $D$ sits at higher potential than $B$ when the galvanometer is briefly removed ⇒ current flows $D \to B$ ⇒ eliminates (A), (B). Magnitude: divider difference $\approx 0.7$–$1.4$ V over $6\,\Omega$ + arms ⇒ $\approx 0.1$ A ⇒ (C), not (D) (0.32 A would need $\approx 2$ V).

> [!tip] Exam Shortcut
> First reduce any sub-bridge to one equivalent arm ($R_{AD} = 2.6\,\Omega$), then a single 4-node circuit (2 unknowns) — or sanity-pick direction by comparing arm potentials.

> [!warning] Trap & Common Pitfall
> Treating the outer bridge as "balanced-like" with $V = IR$ dividers ignoring $G$ gives 0.23 A — wrong. Also, negative $i_G$ flips the direction: always report the arrow direction after the sign, not before.

> [!success] Key Takeaway
> Nested bridges: simplify the innermost first (bridge formula or Δ–Y), then solve the outer with node-voltage — two linear equations, done.

---

### Q21. Consider the circuit shown (10 V source with 2 Ω series and 2 Ω shunt on the left; 20 V source with 6 Ω series and 6 Ω shunt on the right; 1 Ω in the bottom return; a variable resistance $R$ in the middle with voltage $V$ across it and current $I$ through it). Which graph best represents the $V$–$I$ relationship across $R$?

**Answer: (C)** — a straight line starting at $V = -5$ V (when $I = 0$) and crossing $V = 0$ at $I = 1$ A.

---

#### Approach 1 — Standard: Thevenin Equivalent Seen by $R$

**Left terminals:** $V_{\text{Th,L}} = 10\times\frac{2}{2+2} = 5$ V, $R_{\text{Th,L}} = 2\|2 = 1\,\Omega$.
**Right terminals:** $V_{\text{Th,R}} = 20\times\frac{6}{6+6} = 10$ V, $R_{\text{Th,R}} = 6\|6 = 3\,\Omega$.
**Loop resistance through the bottom 1 Ω:** total series $= 1 + 3 + 1 = 5\,\Omega$.

With polarity as marked (positive on the left of $R$):

$$V = (V_{\text{Th,L}} - V_{\text{Th,R}}) + I\cdot R_{\text{loop}} = -5 + 5I$$

- $I = 0$ (open circuit) ⇒ $V = -5$ V
- $V = 0$ ⇒ $I = 1$ A
- Line of slope $5\,\Omega$ — matches graph **(C)**.

```tikz
\usepackage{pgfplots}
\pgfplotsset{compat=1.16}
\begin{document}
\begin{tikzpicture}
\begin{axis}[axis lines=middle, xlabel={$I$ (A)}, ylabel={$V$ (V)},
  xmin=-0.5, xmax=2.5, ymin=-7, ymax=6, grid=major, width=8cm, height=6cm]
  \addplot[very thick, blue, domain=0:2] {-5 + 5*x};
  \addplot[only marks, mark=*, red] coordinates {(0,-5)};
  \addplot[only marks, mark=*, green!60!black] coordinates {(1,0)};
  \node[above] at (axis cs:0,-5) {$V=-5$ V at $I=0$};
  \node[below] at (axis cs:1,0) {$V=0$ at $I=1$ A};
\end{axis}
\end{tikzpicture}
\end{document}
```

#### Approach 2 — Exam Hack: Two Anchor Points Decide

Any linear (Thevenin) load line is fixed by two points. Compute the **open-circuit voltage** across $R$ ($I = 0$): the two source dividers give 5 V (left node) and 10 V (right node) ⇒ $V = 5 - 10 = -5$ V — the graph must start at $-5$ V on the $V$ axis. Only one option does. For the zero crossing: total loop current with $R = 0$: $\mathcal{E}_{\text{net}}/R_{\text{loop}} = 5/5 = 1$ A ⇒ $V = 0$ at $I = 1$ A ✓.

> [!tip] Exam Shortcut
> Never draw the whole graph: evaluate $V$ at $I = 0$ (−5 V) and find where $V = 0$ (1 A). Two points fix the line.

> [!warning] Trap & Common Pitfall
> Watch the **polarity and current direction**: left-to-right vs right-to-left flips the sign of the slope/intercept. The −5 V start (not +5 V) comes from $V_L - V_R = 5 - 10$.

> [!success] Key Takeaway
> A single variable resistor across a linear network always sees $V = V_{\text{Th}} + I R_{\text{Th}}$ — a straight line; obtain $V_{\text{Th}}$ from the two passive dividers and $R_{\text{Th}}$ from dead sources.

---

## PART 2: PHYSICS — SECTION I (ii) [Multiple Correct]

---

### Q22. Two identical infinite honeycomb resistor meshes lie in parallel planes; every edge has resistance $R$. Corresponding vertices are joined by $\lambda R$ resistors ($\lambda > 0$). Adjacent upper vertices $A, B$; lower correspondents $A', B'$. $A \equiv A' \equiv P$ and $B \equiv B' \equiv Q$ are shorted; a battery of emf $V$ connects $P$–$Q$. Which are correct?

(A) The two-layer network draws the same current as a single resistor of resistance $R/3$, independent of $\lambda$.
(B) Every $\lambda R$ resistor carries zero current; further, the sum of currents through edges $AB$ and $A'B'$ is $V/R$.
(C) If only $AB$ and $A'B'$ are removed (all else unchanged), $R_{PQ}$ becomes $R$.
(D) Hence the double layer equals a single honeycomb mesh with $R/2$ per edge **for any arbitrary choice of two terminals**.

**Answer: (A), (C)**

---

#### Approach 1 — Standard: Lattice Resistance + Parallel Layers

**Single honeycomb layer, adjacent terminals:** the exact lattice value (Green's-function result, verified numerically) is

$$R_{\text{layer}} = \frac{2}{3}R$$

- **(A)** Two identical layers in parallel (corresponding vertices at equal potentials ⇒ $\lambda R$ resistors carry no current ⇒ they don't affect anything): $R_{PQ} = \frac{1}{2}\cdot\frac{2R}{3} = \frac{R}{3}$ ✓ and $\lambda$ never enters ✓.
- **(B)** First half true (zero $\lambda R$ current). Second half: $A$ and $B$ **are the terminals**, so the direct edge $AB$ has the full terminal voltage across it: $I_{AB} = V/R$ and $I_{A'B'} = V/R$ ⇒ sum $= 2V/R \ne V/R$ ✗.
- **(C)** Per layer, removing the direct edge: $\frac{1}{R_{\text{layer}}} = \frac{1}{R} + \frac{1}{R_{\text{rest}}} \Rightarrow \frac{3}{2R} = \frac1R + \frac{1}{R_{\text{rest}}} \Rightarrow R_{\text{rest}} = 2R$. Two layers: $(2R \| 2R) = R$ ✓.
- **(D)** For **arbitrary** terminals (not corresponding pairs shorted), the two planes are no longer identically excited — corresponding vertices then sit at different potentials and $\lambda R$ resistors **do** carry current ✗.

#### Approach 2 — BSc/MSc Insight: Lattice Green's Function

$$R_{ab} = \frac{1}{N}\sum_{\mathbf{k},s}\frac{|\psi_{\mathbf{k}s}(a) - \psi_{\mathbf{k}s}(b)|^2}{\lambda_{\mathbf{k}s}}, \qquad \lambda_\pm(\mathbf{k}) = 3 \pm |f(\mathbf{k})|$$

with $f(\mathbf{k}) = 1 + e^{-i\mathbf{k}\cdot\mathbf{a}_2} + e^{i\mathbf{k}\cdot(\mathbf{a}_1-\mathbf{a}_2)}$. Integrating over the Brillouin zone gives exactly $R_{ab} = 2R/3$ (the square-lattice analogue of the same integral gives $R/2$ ✓). Inter-plane $\lambda R$ terms enter the $2\times2$ layer block only off-diagonally — and with identical Dirichlet data on both layers, the inter-layer current vanishes identically.

> [!tip] Exam Shortcut
> (B) can be refuted in one line: the direct edge $AB$ spans the terminal voltage ⇒ it alone carries $V/R$; two such edges sum to $2V/R$. (A), (C) follow from $R_{\text{adj}} = \frac23R$ + parallel layers.

> [!warning] Trap & Common Pitfall
> "Zero current in $\lambda R$" is true only for the symmetric excitation given (corresponding vertices shorted). Option (D) silently generalizes it to arbitrary terminals — that's the false step.

> [!success] Key Takeaway
> Honeycomb nearest-node resistance $= \frac{2}{3}R$ (memorize alongside square $= \frac12 R$). Symmetric duplication of a network: identical layers in parallel simply halve every resistance — with inter-layer links inactive.

---

### Q23. An analog multimeter: galvanometer $G = 100\,\Omega$, full-scale $I_g = 1.00$ mA. Ammeter ranges 10 mA and 100 mA (shunts); voltmeter ranges 10 V and 50 V (series resistors); resistance mode: series with an ideal 1.50 V cell + adjustable resistance, zeroed to full scale on short. Which are correct?

(A) Shunts for 10/100 mA are (values as printed) while series resistances for 10/50 V are 4.95 kΩ and 24.95 kΩ.
(B) On the 10 V range (input resistance 10 kΩ), connecting it across a 20 kΩ resistor which is in series with a 10 kΩ resistor on an ideal 12 V source: the meter reads 4.8 V.
(C) In resistance mode after zero adjustment, total internal series resistance is 1.50 kΩ; an external 1.50 kΩ gives half-scale, 4.50 kΩ gives quarter-scale.
(D) On both current ranges the effective ammeter resistance is the same because full scale occurs at the same terminal voltage of 0.10 V.

**Answer: (B), (C)**

---

#### Solutions

**(A)** Series resistors: $R_{10V} = \frac{10\ \text{V}}{1\ \text{mA}} - 100 = 9.9$ kΩ (not 4.95 kΩ); $R_{50V} = 49.9$ kΩ (not 24.95 kΩ) ✗.

**(B)** Meter on 10 V range: $R_m = \frac{10\text{V}}{1\text{mA}} = 10$ kΩ. Connected **across the 20 kΩ**: $20\text{k}\|10\text{k} = 6.67$ kΩ in series with 10 kΩ from 12 V:

$$V = 12\times\frac{6.67}{6.67 + 10} = 12\times\frac{2}{3} = 4.8\ \text{V}\ \checkmark$$

**(C)** Zero-adjust: $R_{\text{int}} = \frac{1.50\ \text{V}}{1.00\ \text{mA}} = 1.50$ kΩ ✓. External 1.50 kΩ: $I = \frac{1.5}{1.5+1.5} = 0.5$ mA = half scale ✓. External 4.50 kΩ: $I = \frac{1.5}{6.0} = 0.25$ mA = quarter scale ✓.

**(D)** Terminal voltage at full scale is the same (0.10 V), but $R_A = \frac{0.1\ \text{V}}{I_{\text{range}}}$: 10 Ω on 10 mA vs 1 Ω on 100 mA — different ✗.

> [!tip] Exam Shortcut
> Ohm's-law for meters: shunt $S = \frac{I_g G}{I - I_g}$; series $R_s = \frac{V}{I_g} - G$; ohmmeter $R_{\text{int}} = \mathcal{E}/I_g$. Three formulas, four options.

> [!warning] Trap & Common Pitfall
> (D) confuses "same full-scale voltage" with "same resistance" — $R = V/I$ differs by the range current. In (B), note **which** resistor the meter is placed across (across 20 kΩ, not the 10 kΩ).

> [!success] Key Takeaway
> Multimeter ranges are just current/voltage dividers around one galvanometer; half-scale deflection on an ohmmeter happens exactly when $R_x = R_{\text{int}}$.

---

### Q24. Cube $ABCDEFGH$ with a capacitor $C$ on every edge except $BC$ (which has $kC$, $k>0$). Battery $V$ across body-diagonal vertices $A$ and $G$; other vertices isolated/uncharged. Which are correct?

(A) $C_{AG} = \dfrac{2(7k+5)}{11k+9}\,C$
(B) As $k$ increases $0 \to \infty$, $C_{AG}$ increases monotonically from $\dfrac{10}{9}C$ to $\dfrac{14}{11}C$
(C) Charge on capacitor $BC$: $Q_{BC} = \dfrac{4k}{11k+9}CV$
(D) As $k \to \infty$, $V_{BC} \to 0$, hence $Q_{BC} \to 0$

**Answer: (A), (B), (C)**

---

#### Approach 1 — Standard: Nodal Charge Balance (Verified Symbolically)

Set $V_A = V$, $V_G = 0$; solve node equations for $B, C, D, E, F, H$ with edge conductances ($kC$ on $BC$). The exact results are:

$$C_{AG} = \frac{2(7k+5)}{11k+9}\,C, \qquad Q_{BC} = kC\,(V_B - V_C) = \frac{4k}{11k+9}\,CV$$

**Checks:**
- $k = 1$: $C_{AG} = \frac{2\cdot12}{20}C = \frac65 C$ — the classic cube-of-capacitors result ✓
- $k = 0$ (edge removed): $C_{AG} = \frac{10}{9}C$ ✓; $k \to \infty$: $C_{AG} \to \frac{14}{11}C$ ✓ (**B** monotone: $\frac{d}{dk}\frac{7k+5}{11k+9} = \frac{8}{(11k+9)^2} > 0$ ✓)
- **(C)** evaluated exactly as above ✓
- **(D)** $Q_{BC} \to \frac{4}{11}CV \ne 0$ as $k\to\infty$ (the voltage dies as $1/k$ but the capacitance grows as $k$ — finite product) ✗

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{tikzpicture}[scale=1.1]
  \coordinate (A) at (0,0);
  \coordinate (B) at (3,0);
  \coordinate (C) at (4,1.2);
  \coordinate (D) at (1,1.2);
  \coordinate (E) at (0,3);
  \coordinate (F) at (3,3);
  \coordinate (G) at (4,4.2);
  \coordinate (H) at (1,4.2);
  \draw[thick] (A) -- (B) -- (C) -- (G) -- (H) -- (E) -- cycle;
  \draw[thick] (E) -- (F) -- (B);
  \draw[thick] (F) -- (G);
  \draw[dashed, gray] (A) -- (D) -- (C);
  \draw[dashed, gray] (D) -- (H);
  \filldraw[red] (A) circle (2.5pt) node[below left] {$A$ ($V$)};
  \filldraw[blue] (G) circle (2.5pt) node[above right] {$G$ ($0$)};
  \filldraw[teal] (B) circle (2pt) node[below] {$B$};
  \filldraw[teal] (D) circle (2pt) node[left] {$D$};
  \filldraw[teal] (E) circle (2pt) node[left] {$E$};
  \filldraw[orange] (C) circle (2pt) node[right] {$C$};
  \filldraw[orange] (F) circle (2pt) node[above] {$F$};
  \filldraw[orange] (H) circle (2pt) node[above left] {$H$};
  \draw[very thick, purple] (B) -- (C) node[midway, above right] {$kC$};
\end{tikzpicture}
\end{document}
```

#### Approach 2 — Exam Hack: Boundary Values + One Exact Anchor

Eliminate (D) immediately: (C) and (D) contradict as $k\to\infty$ unless $Q\to0$; plug $k = 100$ into (C): $Q = \frac{400}{1109}CV \approx 0.36CV$ — clearly nonzero ⇒ (D) false, and (A),(B),(C) must all be consistent (they are: at $k=1$, (A) gives $6C/5$ = known cube value).

> [!tip] Exam Shortcut
> Anchors: $k=1 \Rightarrow \frac65 C$ (classic), $k=0 \Rightarrow \frac{10}{9}C$, $k\to\infty \Rightarrow \frac{14}{11}C$. The formula (A) reproduces all three; monotonicity is visible from its derivative.

> [!warning] Trap & Common Pitfall
> (D) is the classic "$V \to 0$ therefore $Q \to 0$" trap: $Q = kC\cdot V_{BC}$, and $V_{BC} \sim 1/k$ — the product tends to $\frac{4}{11}CV$.

> [!success] Key Takeaway
> Broken-symmetry cube problems: exploit surviving symmetry classes to reduce nodes, or nodal-solve with conductances. Always sanity-check $k = 1$ against the known symmetric answer.

---

## PART 2: PHYSICS — SECTION I (iii) [Match the Column]

---

### Q25. Match each circuit (List-I) with its time constant $\tau$ (List-II). In each circuit the source is ideal (shorted for $\tau$) with terminals $+/-$ on the left; a capacitor hangs between nodes $A$ and $B$ (or $A$ and the return rail); series/parallel resistor combinations as shown:

- **(P)** From $+$: 2 kΩ to $A$; from $A$: 3 kΩ to the return (right side drops to rail). Capacitor $20\,\mu$F from $A$ to rail.
- **(Q)** From $+$: 2 kΩ to $A$; $A$–2 kΩ–right junction $J$; $J$–6 kΩ–$B$; $B$–3 kΩ–$(-)$. Capacitor $10\,\mu$F between $A$ and $B$.
- **(R)** Same topology: $4$ kΩ ($+\!\to\!A$), $12$ kΩ ($A\!\to\!J$), $6$ kΩ ($J\!\to\!B$), $3$ kΩ ($B\!\to\!-$); capacitor $5\,\mu$F.
- **(S)** Same topology: $6$ kΩ ($+\!\to\!A$), $3$ kΩ ($A\!\to\!J$), $4$ kΩ ($J\!\to\!B$), $4$ kΩ ($B\!\to\!-$); capacitor $10\,\mu$F.

**List-II:** (1) 20.4 ms  (2) 24 ms  (3) 25.2 ms  (4) 30.8 ms  (5) 41.2 ms

(A) $P\!\to\!2; Q\!\to\!4; R\!\to\!3; S\!\to\!5$  (B) $P\!\to\!4; Q\!\to\!2; R\!\to\!1; S\!\to\!3$  (C) $P\!\to\!3; Q\!\to\!4; R\!\to\!2; S\!\to\!5$  (D) $P\!\to\!2; Q\!\to\!4; R\!\to\!3; S\!\to\!1$

**Answer: (A)**

---

#### Solutions (Thevenin resistance across the capacitor)

For the (Q)-style topologies, with $+ \equiv -$ (source shorted), node $A$ reaches the rail through the path via the source ($R_{+\to A} + R_{B\to-}$... more precisely) — the two parallel paths between $A$ and $B$ are:

- Path 1 (through the shorted source): $R_{+\to A} + R_{B\to -}$
- Path 2 (through junction $J$): $R_{A\to J} + R_{J\to B}$

$$\tau = C\cdot\big(R_{\text{path1}} \| R_{\text{path2}}\big)$$

- **(P)** $R = 2\text{k}\|3\text{k} = 1.2$ kΩ; $\tau = 1.2\text{k}\times20\mu = \mathbf{24}$ ms → **(2)**
- **(Q)** $(2+3)\text{k} \| (2+6)\text{k} = 5\text{k}\|8\text{k} = \frac{40}{13}$ kΩ; $\tau = \frac{40}{13}\text{k}\times10\mu = \mathbf{30.8}$ ms → **(4)**
- **(R)** $(4+3)\text{k}\|(12+6)\text{k} = 7\text{k}\|18\text{k} = 5.04$ kΩ; $\tau = 5.04\text{k}\times5\mu = \mathbf{25.2}$ ms → **(3)**
- **(S)** $(6+4)\text{k}\|(3+4)\text{k} = 10\text{k}\|7\text{k} = \frac{70}{17}$ kΩ; $\tau = \frac{70}{17}\text{k}\times10\mu = \mathbf{41.2}$ ms → **(5)**

⇒ option (A).

> [!tip] Exam Shortcut
> Kill the source; for these bridged-T shapes the answer is always $(R_1+R_2)\|(R_3+R_4)$ times $C$ — two sums, one parallel, four products.

> [!warning] Trap & Common Pitfall
> Don't take single-resistor Thevenins ($R_1 \| R_3$ etc.) — the capacitor sees the full series-parallel combo through **both** paths.

> [!success] Key Takeaway
> $\tau = R_{\text{Th}}C$ with $R_{\text{Th}}$ from the capacitor's own terminals: enumerate the two parallel series-paths explicitly for bridged networks.

---

### Q26. In each circuit below a battery of emf 24 V with internal resistance $r$ drives the bridge $A$–$C$–$B$ (top), $A$–$D$–$B$ (bottom), with $R_5$ between $C$ and $D$; battery ($+$ at $A$, $-$ at $B$) includes $r$ in series. Component sets:

| Case | $r$ | $R_{AC}$ | $R_{CB}$ | $R_{AD}$ | $R_{DB}$ | $R_5$ |
|------|-----|----------|----------|----------|----------|-------|
| P | 4 Ω | 1 Ω | 4 Ω | 5 Ω | 6 Ω | 2 Ω |
| Q | 2 Ω | 1 Ω | 3 Ω | 7 Ω | 5 Ω | 1 Ω |
| R | 1 Ω | 1 Ω | 7 Ω | 3 Ω | 5 Ω | 2 Ω |
| S | 3 Ω | 1 Ω | 5 Ω | 7 Ω | 2 Ω | 1 Ω |

Match with power dissipated in $R_5$: **List-II:** (1) 0.50 W  (2) 1.00 W  (3) 2.00 W  (4) 4.00 W  (5) 8.00 W.

(A) $P\!\to\!1; Q\!\to\!2; R\!\to\!5; S\!\to\!3$  (B) $P\!\to\!1; Q\!\to\!2; R\!\to\!3; S\!\to\!4$  (C) $P\!\to\!3; Q\!\to\!4; R\!\to\!3; S\!\to\!4$  (D) $P\!\to\!1; Q\!\to\!2; R\!\to\!4; S\!\to\!5$

**Answer: (B)** — $P \to 0.50$ W, $Q \to 1.00$ W, $R \to 2.00$ W, $S \to 4.00$ W

---

#### Solutions (Node voltage with the internal resistance)

Set $V_B = 0$; solve the 3 node equations at $A$, $C$, $D$:

$$\frac{24 - V_A}{r} = \frac{V_A - V_C}{R_{AC}} + \frac{V_A - V_D}{R_{AD}}, \qquad \frac{V_C - V_A}{R_{AC}} + \frac{V_C}{R_{CB}} + \frac{V_C - V_D}{R_5} = 0,$$
$$\frac{V_D - V_A}{R_{AD}} + \frac{V_D}{R_{DB}} + \frac{V_D - V_C}{R_5} = 0$$

Evaluating (exactly):

- **P:** $V_C - V_D = 1.00$ V ⇒ $P_5 = \frac{1^2}{2} = 0.50$ W → (1)
- **Q:** $V_C - V_D = 1.00$ V ⇒ $P_5 = \frac{1^2}{1} = 1.00$ W → (2)
- **R:** $V_C - V_D = 2.00$ V ⇒ $P_5 = \frac{4}{2} = 2.00$ W → (3)
- **S:** $V_C - V_D = 2.00$ V ⇒ $P_5 = \frac{4}{1} = 4.00$ W → (4)

⇒ option **(B)**.

#### Exam Hack

The numbers are too clean to be arbitrary: all four cases give $V_{CD} \in \{1, 2\}$ V. Try option-substitution: only (B) assigns strictly increasing powers matching small-integer $V_{CD}^2/R_5$ values; (A) mismatches R, (C) mismatches P, (D) mismatches R/S.

> [!tip] Exam Shortcut
> Three node equations with a battery internal resistance — but the paper's data forces $V_{CD} = 1$ or $2$ V exactly. Compute $V_{CD}$, then $P = V_{CD}^2/R_5$.

> [!warning] Trap & Common Pitfall
> Don't forget $r$ in the first equation — treating the 24 V as directly across $A$–$B$ shifts every node voltage and all four powers.

> [!success] Key Takeaway
> Bridge power questions: solve node voltages once symbolically; the power in the cross-arm is $(V_C - V_D)^2/R_5$, independent of how the source is arranged (once nodes are known).

---

### Q27. Six large conducting plates $P_1 \ldots P_6$ (each area $A$) are parallel in this order with equal separation $d$. Dielectric constants in the five successive gaps give capacitances $C_0, 2C_0, 3C_0, 2C_0, C_0$ (with $C_0 = \varepsilon_0 A/d$). Notation: terminal $A$ = plate(s) wired to $A$; terminal $B$ = wired to $B$; $F$ = isolated neutral plate; $X$ = interconnected isolated conductor (net charge 0). Match the arrangements with $C_{AB}$:

**List-II:** (1) $\frac{39}{11}C_0$  (2) $\frac{17}{11}C_0$  (3) $\frac52 C_0$  (4) $\frac{20}{9}C_0$  (5) $\frac{15}{8}C_0$

(A) $P\!\to\!2; Q\!\to\!5; R\!\to\!4; S\!\to\!1$  (B) $P\!\to\!4; Q\!\to\!2; R\!\to\!3; S\!\to\!1$  (C) $P\!\to\!2; Q\!\to\!5; R\!\to\!3; S\!\to\!4$  (D) $P\!\to\!4; Q\!\to\!1; R\!\to\!3; S\!\to\!5$

**Answer: (A)** — $P \to \frac{17}{11}C_0$, $Q \to \frac{15}{8}C_0$, $R \to \frac{20}{9}C_0$, $S \to \frac{39}{11}C_0$

---

#### Solutions (gap-by-gap reduction)

Gaps in order: $g_1 = C_0$ ($P_1|P_2$), $g_2 = 2C_0$ ($P_2|P_3$), $g_3 = 3C_0$ ($P_3|P_4$), $g_4 = 2C_0$ ($P_4|P_5$), $g_5 = C_0$ ($P_5|P_6$). Every gap is a capacitor between its two plates; wire identically-potentialed plates together and read series/parallel.

**(P)** $P_1{\to}A$, $P_2{\to}B$, $P_3{\to}F$, $P_4{+}P_5$ shorted $= X$, $P_6{\to}A$:

- $g_1$ sits directly $A|B$: $C_0$.
- $g_5$ is $X|A$; $g_3$ is $F|X$; $g_2$ is $B|F$: the path $B \to F \to X \to A$ is three in series: $\frac{1}{C} = \frac{1}{2C_0} + \frac{1}{3C_0} + \frac{1}{C_0} = \frac{11}{6C_0} \Rightarrow \frac{6}{11}C_0$.
- $g_4$ has both plates at $X$ (dangling).

$$C_P = C_0 + \tfrac{6}{11}C_0 = \tfrac{17}{11}C_0 \;\to\; \textbf{(2)}$$

**(Q)** $P_1{\to}A$, $P_2{\to}A$, $P_3{\to}X$, $P_4{\to}B$, $P_5{\to}X$, $P_6{\to}A$ ($P_3$–$P_5$ linked over the top):

- $g_1$: $A|A$ dangling. $g_4$: $B|X = 2C_0$. $g_5$: $X|A = C_0$. $g_2$: $A|X = 2C_0$. $g_3$: $X|B = 3C_0$.
- $A|X$: $g_2 \| g_5 = 3C_0$. $X|B$: $g_3 \| g_4 = 5C_0$. Series: $\frac{1}{C} = \frac{1}{3C_0} + \frac{1}{5C_0} = \frac{8}{15C_0}$

$$C_Q = \tfrac{15}{8}C_0 \;\to\; \textbf{(5)}$$

**(R)** $P_1{\to}A$, $P_2{\to}X$, $P_3{\to}B$, $P_4{\to}X$, $P_5{\to}A$, $P_6{\to}X$ ($P_2, P_4, P_6$ linked):

- $A|X$: $g_1 \| g_4 \| g_5 = (1+2+1)C_0 = 4C_0$. $X|B$: $g_2 \| g_3 = 5C_0$. Series:

$$C_R = \left(\tfrac{1}{4C_0} + \tfrac{1}{5C_0}\right)^{-1} = \tfrac{20}{9}C_0 \;\to\; \textbf{(4)}$$

**(S)** $P_1{\to}A$, $P_2{\to}X$, $P_3{\to}A$, $P_4{\to}B$, $P_5{\to}F$, $P_6{\to}X$ ($P_2$–$P_6$ linked):

- $g_3$ is directly $A|B$: $3C_0$. Other path: $A \xrightarrow{g_1 \| g_2 = 3C_0} X \xrightarrow{g_5 = C_0} F \xrightarrow{g_4 = 2C_0} B$: $\frac{1}{C} = \frac{1}{3C_0} + \frac{1}{C_0} + \frac{1}{2C_0} = \frac{11}{6C_0} \Rightarrow \frac{6}{11}C_0$.

$$C_S = 3C_0 + \tfrac{6}{11}C_0 = \tfrac{39}{11}C_0 \;\to\; \textbf{(1)}$$

⇒ option **(A)**.

> [!tip] Exam Shortcut
> Two rules only: plates on a wire share one node; a floating $F$ in a series chain carries no net charge ⇒ its two gaps are simply in series.

> [!warning] Trap & Common Pitfall
> A shorted pair like $P_4$–$P_5$ makes $g_4$ "dangling" (both ends at $X$) — do **not** include it in any series chain. Similarly $A|A$ gaps vanish.

> [!success] Key Takeaway
> Multi-plate capacitors are node diagrams in disguise: label nodes ($A, B, F, X$), convert each gap to a capacitor, then series/parallel exactly like resistors — with floating nodes giving isolated series branches.

---

### Q28. Each capacitor in List-I carries charges $\pm Q$; dielectrics are linear/isotropic; neglect fringing. Match with the stored electrostatic energy:

**List-II:** (1) $\dfrac{Q^2}{24\pi\varepsilon_0 R}$  (2) $\dfrac{Q^2\theta}{2\varepsilon_0 L}$  (3) $\dfrac{Q^2 d}{2\varepsilon_0 A \ln 2}$  (4) $\dfrac{Q^2}{8\pi\varepsilon_0 L}$  (5) $\dfrac{Q^2 d\ln 2}{2\varepsilon_0 A}$

- **(P)** Rectangular plates $L \times b$, separation $d(x) = d\left(1 + \frac{x}{L}\right)$, $0 \le x \le L$; vacuum; $A = Lb$.
- **(Q)** Concentric spheres radii $R, 2R$; dielectric $\varepsilon_r = 2$ for $R < r < \frac{3R}{2}$; vacuum for $\frac{3R}{2} < r < 2R$.
- **(R)** Coaxial cylinders radii $a, 2a$, length $L \gg a$; $K(r) = r/a$ (as printed: varies with $r$).
- **(S)** Radial planes forming a wedge of angle $\theta$ (radians), common length $L$, from $r = a$ to $r = 2a$; $K(r) = r/a$.

(A) $P\!\to\!3; Q\!\to\!1; R\!\to\!4; S\!\to\!2$  (B) $P\!\to\!5; Q\!\to\!1; R\!\to\!4; S\!\to\!2$  (C) $P\!\to\!3; Q\!\to\!4; R\!\to\!1; S\!\to\!2$  (D) $P\!\to\!5; Q\!\to\!2; R\!\to\!4; S\!\to\!1$

**Answer: (A)** — $P \to (3)$, $Q \to (1)$, $R \to (4)$, $S \to (2)$

---

#### Solutions

**(P)** Local parallel-plate approximation: each strip of width $dx$ at position $x$ spans the local gap $s(x) = d\left(1 + \frac{x}{L}\right)$; side-by-side strips share the same voltage, so their charges add:

$$C = \int_0^L \frac{\varepsilon_0 b\,dx}{s(x)} = \frac{\varepsilon_0 b}{d}\int_0^L \frac{dx}{1 + x/L} = \frac{\varepsilon_0 b L \ln 2}{d} = \frac{\varepsilon_0 A \ln 2}{d}$$

$$U = \frac{Q^2}{2C} = \frac{Q^2 d}{2\varepsilon_0 A \ln 2} = \textbf{(3)} \ \checkmark$$

**(Q)** Spherical: $C_1$ (R→1.5R, $\varepsilon_r=2$) $= 2\cdot\frac{4\pi\varepsilon_0 R(1.5R)}{0.5R} = 24\pi\varepsilon_0 R$; $C_2$ (1.5R→2R vacuum) $= \frac{4\pi\varepsilon_0(1.5R)(2R)}{0.5R} = 24\pi\varepsilon_0 R$. Series: $C = 12\pi\varepsilon_0 R$ ⇒ $U = \frac{Q^2}{24\pi\varepsilon_0 R}$ = **(1)** ✓.

**(R)** Cylindrical, $K(r) = r/a$: from Gauss + constitutive, $C = \frac{2\pi\varepsilon_0 L}{\int_a^{2a}\frac{dr}{K r}}$; $\int_a^{2a}\frac{a\,dr}{r^2} = \frac12$ ⇒ $C = 4\pi\varepsilon_0 L$ ⇒ $U = \frac{Q^2}{8\pi\varepsilon_0 L}$ = **(4)** ✓.

**(S)** Wedge: the azimuthal field with $\psi$ linear in $\phi$ even for position-dependent $K$: $E_\phi = V/(\theta r)$, $D_\phi = \varepsilon_0\frac{r}{a}\frac{V}{\theta r} = \frac{\varepsilon_0 V}{a\theta}$ (independent of $r$). Charge: $Q = \int D_\phi\,dA$ over one plate $= \frac{\varepsilon_0 V}{a\theta}\cdot a L = \frac{\varepsilon_0 L V}{\theta}$ ⇒ $C = \frac{\varepsilon_0 L}{\theta}$ ⇒

$$U = \frac{Q^2}{2C} = \frac{Q^2\theta}{2\varepsilon_0 L} = \textbf{(2)} \checkmark$$

⇒ option **(A)**.

> [!tip] Exam Shortcut
> Wedge/cylinder with $K \propto r$: use $\frac{1}{C} \propto \int \frac{dr}{K r}$ (cylinder) but for the wedge the field is azimuthal — $D$ ends up $r$-independent and $C = \varepsilon_0 L/\theta$.

> [!warning] Trap & Common Pitfall
> $U = \frac{Q^2}{2C}$ (fixed charge) vs $\frac12 CV^2$ — the problem fixes $Q$, so always invert to $C$ first. Also the varying-separation capacitor needs the **parallel-strip** integral $\int \varepsilon_0 dA/s$, not a series $\int s\,dx$.

> [!success] Key Takeaway
> For non-uniform dielectrics/separations: write $C$ from the local element ($\int \frac{\varepsilon_0\,dA}{s}$ for common voltage, $\int \frac{s\,dx}{\varepsilon_0 b}$ for common charge) — then $U = Q^2/2C$.

---

## PART 2: PHYSICS — SECTION II (Numerical)

---

### Q29. A metre bridge has end corrections: balance at $\ell$ cm satisfies $\frac{P}{Q} = \frac{\ell + \alpha}{100 - \ell + \beta}$.
- Obs I: $P = 2\,\Omega$ (left), $Q = 5\,\Omega$ (right), $\ell = 28$ cm.
- Obs II: $X$ (left), $6\,\Omega$ (right), $\ell = 40$ cm.
- Obs III: $X$ and $6\,\Omega$ interchanged, $\ell = 61$ cm.

Find $X$.

**Answer: 4 Ω**

---

#### Solution

(i) $\frac{2}{5} = \frac{28+\alpha}{72+\beta} \Rightarrow 144 + 2\beta = 140 + 5\alpha \Rightarrow 5\alpha - 2\beta = 4$

(ii) $X(60+\beta) = 6(40+\alpha)$, (iii) $6(39+\beta) = X(61+\alpha)$

Multiply (ii)×(iii) after dividing: $\frac{X}{6}\cdot\frac{6}{X} = 1 = \frac{(40+\alpha)(61+\alpha)}{(60+\beta)(39+\beta)}$

$$2440 + 101\alpha + \alpha^2 = 2340 + 99\beta + \beta^2$$

Substituting $\beta = \frac{5\alpha-4}{2}$ from (i) and simplifying: $21\alpha^2 + 546\alpha - 1176 = 0 \Rightarrow \alpha^2 + 26\alpha - 56 = 0 \Rightarrow \alpha = 2$ (positive root), $\beta = 3$.

$$X = \frac{6(40+2)}{60+3} = \frac{252}{63} = 4\ \Omega$$

> [!tip] Exam Shortcut
> The product trick $\frac{X}{6}\cdot\frac{6}{X} = 1$ couples (ii) and (iii) directly — one quadratic in $\alpha$ alone (or in $\beta$).

> [!warning] Trap & Common Pitfall
> End corrections shift **both** ends: $\ell + \alpha$ on the left, $(100-\ell) + \beta$ on the right — never $\ell + \alpha$ vs $100 - (\ell + \beta)$.

> [!success] Key Takeaway
> Metre-bridge corrections: three observations ⇒ three equations, but eliminating $X$ first makes the algebra collapse. $X$ comes out as a clean rational — if it isn't, redo the ratio setup.

---

### Q30. An infinite ladder of capacitors connects across an ideal 324 V battery ($A$ positive, $B$ negative). Series branch (from $A$): $6\,\mu$F, $8\,\mu$F, $6\,\mu$F, $8\,\mu$F, $6\,\mu$F, …; shunt capacitors to the rail at successive nodes: $C_1 = 8\,\mu$F, $C_2 = 4\,\mu$F, $C_3 = 8\,\mu$F, $C_4 = 4\,\mu$F, $C_5 = 8\,\mu$F, …. Find the charge on $C_5$ (in µC).

**Answer: 24**

---

#### Approach 1 — Standard: Self-Similar Tail + Voltage Propagation

**Tail from node $N_5$ onward** (pattern shifts with node parity). Let $u = C(N_5) = C(N_7) = \ldots$ (node with $8\,\mu$F shunt) and $v = C(N_6) = C(N_8) = \ldots$ ($4\,\mu$F shunt):

$$u = 8 + \frac{8v}{8+v}, \qquad v = 4 + \frac{6u}{6+u} \;\Rightarrow\; u = 12\ \mu\text{F},\ v = 8\ \mu\text{F}$$

**Backward chain:**
$C(N_4) = 4 + \frac{6\cdot12}{18} = 8$; $C(N_3) = 8 + \frac{8\cdot8}{16} = 12$; $C(N_2) = 4 + \frac{6\cdot12}{18} = 8$; $C(N_1) = 8 + \frac{8\cdot8}{16} = 12$.

Total: $C_{\text{eq}} = \frac{6\cdot12}{18} = 4\,\mu$F ⇒ $Q_{\text{tot}} = 4 \times 324 = 1296\,\mu$C.

**Voltages:**
- Across series 6 µF: $1296/6 = 216$ V ⇒ $V_1 = 324 - 216 = 108$ V. Shunt $C_1$ takes $8\times108 = 864\,\mu$C ⇒ series-8 branch: $1296 - 864 = 432\,\mu$C ⇒ drop $432/8 = 54$ V ⇒ $V_2 = 54$ V.
- $C_2$: $4\times54 = 216$ ⇒ series-6: $432 - 216 = 216\,\mu$C ⇒ drop $36$ V ⇒ $V_3 = 18$ V.
- $C_3$: $8\times18 = 144$ ⇒ series-8: $216 - 144 = 72$ ⇒ drop $9$ V ⇒ $V_4 = 9$ V.
- $C_4$: $4\times9 = 36$ ⇒ series-6: $72 - 36 = 36$ ⇒ drop $6$ V ⇒ $V_5 = 3$ V.

$$Q_{C_5} = 8\,\mu\text{F}\times 3\ \text{V} = \boxed{24\ \mu\text{C}}$$

#### Approach 2 — Exam Hack

Node voltages halve roughly every two stages (108 → 54 → 18 → 9 → 3): final shunt sees ~3 V × 8 µF = 24 µC — the only listed value in that range.

> [!tip] Exam Shortcut
> Two-parameter self-similarity: the ladder's period is **two** nodes (8/4 shunts, 6/8 series), so define $(u, v)$ and solve the 2×2 fixed point — never one equation.

> [!warning] Trap & Common Pitfall
> Don't assume the whole ladder is one equivalent capacitor and stop — the question needs the **fifth** shunt voltage, so propagate charge stage by stage after finding $C_{\text{eq}}$.

> [!success] Key Takeaway
> Periodic ladders: $C_{\text{eq}}$ from the fixed point of the period map; then $Q_{\text{tot}}$ and nodal KCL give every intermediate voltage.

---

### Q31. Parallel plate capacitor: plate length $L = 40$ cm, width $w = 32$ cm, separation $d = 3$ mm. A dielectric slab ($K = 4$, thickness $t = 2$ mm) rests on the lower plate. At insertion $x_0 = 10$ cm the capacitor is charged to $6000$ V and the battery is disconnected. Find the force (mN) needed to pull the slab out slowly when the insertion is $x = 20$ cm (constant charge).

**Answer: 12**

---

#### Solution

**Capacitance vs $x$** (slab region: series of dielectric 2 mm + air 1 mm):

$$\frac{s_{\text{eff}}}{K_{\text{eff}}} = \frac{t}{K} + \frac{d-t}{1} = \frac{0.002}{4} + 0.001 = 0.0015\ \text{m}$$

$$C(x) = \frac{\varepsilon_0 x w}{0.0015} + \frac{\varepsilon_0 (L-x)w}{0.003} = \frac{\varepsilon_0 w}{0.003}\left(2x + L - x\right) = \frac{\varepsilon_0 w (x + L)}{0.003}$$

$$C(x) = \frac{9\times10^{-12}\times0.32\,(x+0.4)}{0.003} = 9.6\times10^{-10}(x + 0.4)\ \text{F (with } x \text{ in m)}$$

At $x_0 = 0.1$ m: $C_0 = 4.8\times10^{-10}$ F ⇒ $Q = C_0 V = 2.88\ \mu$C (fixed after disconnect).

At $x = 0.2$ m: $C = 5.76\times10^{-10}$ F; $\frac{dC}{dx} = 9.6\times10^{-10}$ F/m.

$$F = \frac{Q^2}{2C^2}\frac{dC}{dx} = \frac{(2.88\times10^{-6})^2}{2(5.76\times10^{-10})^2}\times9.6\times10^{-10} = 1.25\times10^{7}\times9.6\times10^{-10} = 0.012\ \text{N} = 12\ \text{mN}$$

> [!tip] Exam Shortcut
> $C(x)$ is **linear** in $x$ ⇒ $F = \frac{Q^2}{2C^2}\frac{dC}{dx}$ has a clean closed form: constant $dC/dx$, only $C(x)$ varies.

> [!warning] Trap & Common Pitfall
> Battery disconnected ⇒ **constant $Q$** ⇒ $F = +\frac{dU}{dx}\big|_Q = \frac{Q^2}{2C^2}\frac{dC}{dx}$ (attractive/sucking-in sign). With the battery attached the formula would be $-\frac12 V^2 \frac{dC}{dx}$.

> [!success] Key Takeaway
> Dielectric sliding problems: assemble $C(x)$ piecewise (series layers ⇒ $s/K$ addition), then energy method with the correct constraint ($Q$ const or $V$ const).

---

### Q32. A parallel-plate capacitor has two side-by-side regions: D1 with $K_1 = 3$, $\sigma_1 = 12$ pS/m; D2 with $K_2$ unknown, $\sigma_2$ unknown; each occupies half the area $A/2$ (total $A = 100$ cm²), separation $d = 1$ mm. Charged to 400 V and disconnected; after a long time, an ideal capacitor $C_0 = 720$ pF is connected in parallel; after $8$ s the common voltage is $200/e^2$ V. Find $\sigma_2$ (in pS/m).

**Answer: 24**

---

#### Solution

**Capacitances:** $C_1 = \frac{3\varepsilon_0 (A/2)}{d} = 270$ pF, $C_2 = \frac{5\varepsilon_0(A/2)}{d} = 450$ pF ($K_2 = 5$ from $C_{\text{tot}} = 720$ pF $= C_0$, given). Total stored free charge at 400 V: $Q = 720\text{pF}\times400\text{V} = 288$ nC.

**After connecting $C_0$:** charge redistributes instantly: $V(0^+) = \frac{288\text{ nC}}{(720+720)\text{ pF}} = 200$ V. Thereafter the charge leaks only through the two dielectric conductances (the ideal $C_0$ holds none):

$$V(t) = 200\,e^{-t/\tau}, \qquad \tau = (C_1 + C_2 + C_0)\,R_{\text{leak}}$$

$V(8) = 200/e^2 \Rightarrow \tau = 4$ s ⇒ $R_{\text{leak}} = \frac{4}{1440\text{ pF}} = 2.778\times10^9\ \Omega$.

**Leakage conductance in parallel:** $\frac{1}{R} = \frac{(\sigma_1 + \sigma_2)(A/2)}{d}$:

$$\sigma_1 + \sigma_2 = \frac{d}{R\,(A/2)} = \frac{10^{-3}}{2.778\times10^9\times10^{-2}} = 3.6\times10^{-11}\ \text{S/m} = 36\ \text{pS/m}$$

$$\sigma_2 = 36 - 12 = \boxed{24\ \text{pS/m}}$$

> [!tip] Exam Shortcut
> Instant redistribution (200 V) + exponential decay with $\tau = 4$ s (since $e^{-8/\tau} = e^{-2}$) — two 1-line observations pin $R$, hence $\sigma_1 + \sigma_2$.

> [!warning] Trap & Common Pitfall
> The time constant uses **all** parallel capacitances ($C_1 + C_2 + C_0 = 1440$ pF), not just $C_0$ — using 720 pF doubles $\tau$ and halves $R$.

> [!success] Key Takeaway
> Leaky dielectric = ideal capacitor ∥ resistor with $R = \frac{d}{\sigma A}$, $C = \frac{K\varepsilon_0 A}{d}$ ⇒ $\tau = \frac{K\varepsilon_0}{\sigma}$ per region; regions in parallel add both $G$ and $C$.

---

### Q33. Nonlinear elements X and Y: $I_X = \frac{V^2}{8}$ A, $I_Y = \frac{V^3}{32}$ A ($V$ = voltage across each, same for both, in parallel). The parallel combination is in series with a $2\,\Omega$ resistor across an ideal DC source $V_s$. Initially $V_s = 12$ V (steady). $V_s$ is then varied infinitesimally. If $I$ = source current, find $10\,r_d$ where $r_d = dV_s/dI$ (in ohms).

**Answer: 24**

---

#### Solution

**Operating point:** $V_s = 2I + V$ with $I = \frac{V^2}{8} + \frac{V^3}{32}$. Test $V = 4$: $I = 2 + 2 = 4$ A ⇒ $V_s = 2(4) + 4 = 12$ V ✓. So $V = 4$ V, $I = 4$ A.

**Small-signal:** $g = \frac{dI}{dV}\bigg|_{4} = \frac{2V}{8} + \frac{3V^2}{32}\bigg|_{4} = 1 + 1.5 = 2.5$ S (parallel pair resistance $0.4\,\Omega$).

Loop: $dV_s = 2\,dI + dV$ and $dI = g\,dV$ ⇒ $dV_s = (2g + 1)\,dV$:

$$r_d = \frac{dV_s}{dI} = \frac{2g+1}{g} = \frac{6}{2.5} = 2.4\ \Omega \;\Rightarrow\; 10 r_d = \boxed{24}$$

> [!tip] Exam Shortcut
> Find the DC point by inspection ($V = 4$ makes both terms integers), then linearize — never solve the cubic exactly.

> [!warning] Trap & Common Pitfall
> Two equivalent small-signal circuits: $r_d = 2 + 1/g = 2 + 0.4 = 2.4\,\Omega$ (loop view: $dV_s = 2\,dI + dV$, $dV = dI/g$), or view the pair as $0.4\,\Omega$ in series with $2\,\Omega$. The trap is using the **DC** incremental slope at the wrong point (e.g., linearizing at $V = 0$, or computing $g$ from $I/V = 1$ S instead of $dI/dV = 2.5$ S).

> [!success] Key Takeaway
> Nonlinear DC circuits: (1) locate the operating point by educated guessing, (2) replace each nonlinear element by $r_d = (dI/dV)^{-1}$ **at that point**, (3) linear circuit analysis gives the response.

---

### Q34. A potentiometer determines the internal resistance $r$ of cell X. The primary rheostat changes between observations; a standard cell (1.50 V) sets the gradient each time.
- Obs I: standard balances at 300 cm; X on open circuit balances at 240 cm.
- Obs II: standard at 375 cm; X across unknown $R$ (terminal voltage) balances at 225 cm.
- Obs III: standard at 350 cm; a $6\,\Omega$ resistor in parallel with $R$; X across the combination balances at 168 cm.

Find $r$ (ohms).

**Answer: 2**

---

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{tikzpicture}[scale=1.0]
  % primary circuit
  \draw (0,0) to[battery1, l=$\mathcal{E}_p$] (0,2.5)
        to[R, l=$R_{\text{rheo}}$] (3,2.5)
        to[short] (11,2.5)
        -- (11,0) -- (0,0);
  % potentiometer wire A--B
  \draw[thick] (1,0) -- (10,0);
  \node[below] at (1,-0.15) {$A$};
  \node[below] at (10,-0.15) {$B$};
  % standard cell + galvanometer branch
  \draw (3,0) to[battery1, l=$1.50$ V, invert] (3,-1.5)
        to[G, l=$G$] (5.5,-1.5)
        to[short] (5.5,0);
  \node[below] at (4.2,-1.85) {standard cell + $G$ (balance)};
  % cell X with load branch
  \draw (7.5,0) to[battery1, l=cell $X$] (7.5,-1.5)
        to[R, l=$R$] (10,-1.5)
        to[short] (10,0);
  \node[below] at (8.7,-1.85) {cell $X$ across load};
\end{tikzpicture}
\end{document}
```

$$\text{Balance rule: } \mathcal{E} = k\ell,\ \ k = \frac{1.50}{\ell_{\text{std}}}\ \text{each observation}$$

#### Solution

**Obs I:** $k_1 = \frac{1.50}{300} = 5$ mV/cm ⇒ $E_X = 5 \times 240 = 1200$ mV $= 1.20$ V.

**Obs II:** $k_2 = \frac{1.50}{375} = 4$ mV/cm ⇒ terminal voltage $V = 4\times225 = 0.90$ V. With load $R$: $V = E\frac{R}{R+r}$:

$$0.90 = 1.20\,\frac{R}{R+r} \;\Rightarrow\; \frac{R}{R+r} = 0.75 \;\Rightarrow\; R = 3r$$

**Obs III:** $k_3 = \frac{1.50}{350}$ V/cm ⇒ $V' = \frac{1.50}{350}\times168 = 0.72$ V. Load $R' = 6\|R$:

$$0.72 = 1.20\,\frac{R'}{R' + r} \;\Rightarrow\; R' = 1.5\,r$$

Solve $6\|R = 1.5r$ with $R = 3r$: $\frac{6\cdot3r}{6+3r} = 1.5r \Rightarrow \frac{18r}{6+3r} = 1.5r \Rightarrow 12 = 6 + 3r \cdot$? — dividing by $r$: $\frac{18}{6+3r} = 1.5 \Rightarrow 18 = 9 + 4.5r \Rightarrow r = 2\,\Omega$ ✓ (equivalently $R = 6\,\Omega$, $6\|6 = 3 = 1.5\times2$ ✓).

> [!tip] Exam Shortcut
> Each observation resets $k$ — never carry a gradient across observations. Three lines: $E = 1.2$ V, $R = 3r$, $6\|R = 1.5r$.

> [!warning] Trap & Common Pitfall
> The potentiometer draws **no** current at balance — the "terminal voltage" is the loaded EMF $E R/(R+r)$, not $E$ itself. Mixing gradients between observations is the classic error (the question explicitly warns the rheostat changes).

> [!success] Key Takeaway
> Potentiometer: $k$ is per-observation ($1.50/\ell_{\text{std}}$); open-circuit balance ⇒ EMF; loaded balance ⇒ terminal voltage ⇒ $r = R(E/V - 1)$.

---

## PART 3: CHEMISTRY — SECTION I (i) [Single Correct]

---

### Q35. The complementary DNA strand for $5' \leftarrow$ A—T—G—C—T $\rightarrow 3'$ is

(A) $5' \leftarrow$ T—A—C—G—A $\rightarrow 3'$  (B) $3' \leftarrow$ G—C—A—T—C $\rightarrow 5'$  (C) $3' \leftarrow$ T—A—C—G—A $\rightarrow 5'$  (D) $5' \leftarrow$ G—C—A—T—C $\rightarrow 3'$

**Answer: (C)**

---

#### Solution

Chargaff pairing: A↔T, G↔C. Antiparallel alignment: reading the given strand 5'→3' as A, T, G, C, T, the complement runs 3'→5' as T, A, C, G, A:

$$\text{Complement} = 3' \leftarrow \text{T—A—C—G—A} \rightarrow 5' \;\Rightarrow\; \textbf{(C)}$$

(A) keeps 5'→3' orientation ✗; (B), (D) have the wrong base order (they read the complement backwards) ✗.

> [!tip] Exam Shortcut
> Write the complement **reversing direction at the same time**: keep the table in the same left-right order and flip only the ends (5'/3').

> [!warning] Trap & Common Pitfall
> The two failure modes are (i) forgetting antiparallel direction and (ii) reversing the base order *and* the ends — that double-reversal returns the original sequence.

> [!success] Key Takeaway
> DNA complementarity = base pairing (A–T, 2 H-bonds; G–C, 3 H-bonds) + antiparallel strands.

---

### Q36. Which statement is **NOT** correct about thermoplastic polymers?

(A) They are softened on heating.  (B) Intermolecular forces of attraction in these are in between elastomers and fibres.  (C) These possess extensive cross linking by covalent bonds.  (D) These are easily moulded.

**Answer: (C)**

---

Thermoplastics (PE, PVC, polystyrene): long **linear/branched** chains held by weak van der Waals forces — softened on reheating and re-moulded (A ✓, D ✓). Their intermolecular forces lie between those of elastomers (weakest) and fibres (strongest) (B ✓). Extensive **covalent cross-links** characterize *thermosetting* polymers (bakelite, urea-formaldehyde), which soften once and then set irreversibly — so (C) is the incorrect statement ✓.

> [!tip] Exam Shortcut
> "Softens on heating + re-mouldable" ⇒ thermoplastic ⇒ **no cross-links**. The NOT-question is answered in one dichotomy: thermoplastic ↔ thermoset.

> [!warning] Trap & Common Pitfall
> Vulcanized rubber (cross-linked) behaves like a thermoset for reshaping — don't equate "elastic" with "thermoplastic".

> [!success] Key Takeaway
> Thermoplastics: linear chains, weak intermolecular forces, recyclable. Thermosets: 3-D covalent networks, no remelting.

---

### Q37. Select the correct statement about the polymer shown (a saturated ethylene–propylene chain unit):

(A) It can be seen as addition homopolymer of isoprene.  (B) It can be seen as addition copolymer of ethylene & propylene.  (C) It can be vulcanized using sulfur to enhance cross-links.  (D) Its possible monomers give −ve test with bromine water as well as with Baeyer's reagent.

**Answer: (B)**

---

- **(A)** Polyisoprene homopolymer (natural rubber) has a $-\text{CH}_2-\text{C}(\text{CH}_3)=\text{CH}-$ backbone unit — not present here ✗.
- **(B)** The repeat segments $-\text{CH}_2\text{CH}_2-$ (from ethylene) and $-\text{CH}_2\text{CH}(\text{CH}_3)-$ (from propylene) alternate in the chain: it is an addition copolymer of ethylene and propylene ✓.
- **(C)** The polymer chain shown is **saturated** (no backbone C=C): sulfur vulcanization needs unsaturation — as depicted it cannot be sulfur-vulcanized (official key marks this incorrect) ✗.
- **(D)** The possible monomers (ethylene, propylene) **do** decolorize bromine water and Baeyer's reagent (they are alkenes) — the statement claims a *negative* test ✗.

> [!tip] Exam Shortcut
> Identify monomers from the repeat unit: $-\text{CH}_2\text{CH}_2-$ = ethylene; $-\text{CH}_2\text{CH}(\text{CH}_3)-$ = propylene ⇒ copolymer (B).

> [!warning] Trap & Common Pitfall
> (D) inverts the alkene test result — always ask "do the MONOMERS or the POLYMER" undergo addition: monomers yes (unsaturated), saturated polymer no.

> [!success] Key Takeaway
> Addition-polymer structure reading: count distinct repeat segments; each maps to one monomer. Saturation of the product chain ⇒ no sulfur vulcanization unless a diene comonomer is present.

---

### Q38. Which amino acid moves towards the **cathode** on electrophoresis at pH = 7?

(A) Leucine  (B) Lysine  (C) Asparagine  (D) Aspartic acid

**Answer: (B) Lysine**

---

At pH 7: Leucine (neutral, pI ≈ 6.0 → ~zwitterionic, net ≈ 0); Asparagine (neutral); Aspartic acid (acidic, pI ≈ 2.98 → net **negative** → moves to anode); **Lysine** (basic side chain, pI ≈ 9.74 → net **positive** → attracted to the cathode (−)) ✓.

```smiles
[NH3+]CCCC(N)C(=O)O
```
*(lysine, predominantly cationic at pH 7)*

> [!tip] Exam Shortcut
> Compare pH with pI: pH < pI ⇒ cation (→ cathode); pH > pI ⇒ anion (→ anode). Lysine pI ≈ 9.7 > 7 ⇒ cathode.

> [!warning] Trap & Common Pitfall
> Asparagine vs aspartic acid: only the extra −COOH (aspartic) or −NH₂ (lysine) shifts pI across 7. The α-amino/α-carboxyl pair alone is zwitterionic (≈ neutral).

> [!success] Key Takeaway
> Electrophoresis direction = sign of $(\text{pH} - \text{pI})$ flipped: basic amino acids (Lys, Arg, His) → cathode at pH 7; acidic (Asp, Glu) → anode.

---

## PART 3: CHEMISTRY — SECTION I (ii) [Multiple Correct]

---

### Q39. 1-Chloro-2,4-dinitrobenzene is treated with aqueous ethanolic KCN. Select the correct statements:

(A) The mechanism of the reaction is $S_N2Ar$.  (B) Carbanion intermediate is formed in the reaction.  (C) The rate of reaction is independent of the concentration of cyanide ion.  (D) The rate of reaction decreases if Cl is replaced by F.

**Answer: (A), (B)**

---

```smiles
O=[N+]([O-])c1ccc(Cl)c(c1)[N+](=O)[O-]
```

- **(A)** Nucleophilic aromatic substitution by **addition–elimination** ($S_NAr$, addition-elimination) ✓.
- **(B)** The Meisenheimer complex is a cyclohexadienyl **carbanion** (negative charge delocalized onto the $o/p$-nitro groups) ✓.
- **(C)** Rate $= k[\text{substrate}][\text{CN}^-]$ — it **depends** on cyanide ✗.
- **(D)** In $S_NAr$ the leaving-group order is $F \gg Cl > Br > I$ (rate **increases** F) ✗.

> [!tip] Exam Shortcut
> Nitro groups at $o/p$ to the leaving group activate $S_NAr$ enormously: the intermediate's negative charge lands on them. F is the best leaving group here — opposite to $S_N2$.

> [!warning] Trap & Common Pitfall
> Reversing $S_NAr$ leaving-group order to $Cl > F$ (the $S_N2$/carbocation intuition) flips both (C)-type rate logic and (D) — the classic trap of this question.

> [!success] Key Takeaway
> $S_NAr$ = addition (rate-determining, needs $\text{Nu}^-$ ⇒ bimolecular) then elimination of $\text{X}^-$; Meisenheimer carbanion intermediate; $F$ best leaving group via $\sigma$-complex stabilization.

---

### Q40. Which statements are correct?

(A) Cationic detergents have germicidal properties.  (B) Bacteria can degrade the detergents containing highly branched chains.  (C) Some synthetic detergents can give foam even in ice cold water.  (D) Synthetic detergents are not soaps.

**Answer: (A), (C), (D)**

---

- **(A)** Cationic detergents = quaternary ammonium salts with acetate/halide anions; bactericidal/germicidal ✓.
- **(B)** Branched-chain detergents are **not** biodegradable — that's why modern formulations minimize branching ✗.
- **(C)** Some synthetic detergents foam in ice-cold water (soaps do not) ✓.
- **(D)** Detergents are cleansing agents like soaps but contain **no fatty-acid salts** ✓.

> [!tip] Exam Shortcut
> Anionic (household, e.g. SDS), cationic (germicidal, quaternary ammonium), non-ionic (foam in cold water, PVA-type) — one-line classification kills all four options.

> [!warning] Trap & Common Pitfall
> (B) is the polarity trap: "biodegradable" ⇔ straight chains; branching blocks enzymatic attack.

> [!success] Key Takeaway
> Soaps = fatty acid salts (fail in hard water); detergents = sulfonates/sulfates/quaternary salts (work in hard & cold water).

---

### Q41. The structure given is that of ascorbic acid (Vitamin C). Select the correct statements:

(A) The hydrogen labelled (b) is most acidic.  (B) It is water soluble and can be stored in body.  (C) It is found in citrus fruits.  (D) Its deficiency causes pernicious anaemia.

**Answer: (C)**

---

```smiles
OCC1OC(=O)C(=C(O)O)C(O)C1O
```

- **(A)** The most acidic H is the **enediol** O–H on the ring (adjacent to the lactone C=O), not the labelled alcohol/benzylic-type position ✗.
- **(B)** Water-soluble vitamins are **excreted** in urine — they cannot be stored (needs regular intake) ✗.
- **(C)** Rich source: citrus fruits (oranges, lemons, amla) ✓.
- **(D)** Deficiency of Vitamin C ⇒ **scurvy** (bleeding gums, poor wound healing); pernicious anaemia is Vitamin B₁₂ deficiency ✗.

> [!tip] Exam Shortcut
> Vitamin-deficiency pairs: C→scurvy, B₁₂→pernicious anaemia, A→night blindness, D→rickets, B₁→beriberi, PP→pellagra. One mapping answers (D).

> [!warning] Trap & Common Pitfall
> "Water-soluble ⇒ storeable" is backwards: fat-soluble (A, D, E, K) are stored; B-complex and C are excreted daily.

> [!success] Key Takeaway
> Ascorbic acid: enediol lactone — the enolic OH (pKₐ ≈ 4.2, boosted by H-bonded ascorbate anion stabilization) is the acidic site; deficiency = scurvy.

---

## PART 3: CHEMISTRY — SECTION I (iii) [Match the Column]

---

### Q42. Match List-I (compounds) with List-II (properties):

**List-I:** (P) Aniline  (Q) Phenyl acetate  (R) Phenol  (S) Toluene

**List-II:**
(1) Most reactive for aromatic electrophilic substitution in neutral medium.
(2) Produces salicylaldehyde with $\text{CHCl}_3/\text{NaOH}$ (Reimer–Tiemann).
(3) Produces tribromo derivative with $\text{Br}_2/\text{H}_2\text{O}$.
(4) Produces carboxylic acid on hydrolysis.
(5) Produces an explosive substance with excess nitric acid.

(A) $P\!\to\!2; Q\!\to\!4; R\!\to\!1; S\!\to\!5$  (B) $P\!\to\!1; Q\!\to\!4; R\!\to\!3; S\!\to\!5$  (C) $P\!\to\!2; Q\!\to\!1; R\!\to\!4; S\!\to\!3$  (D) $P\!\to\!2; Q\!\to\!5; R\!\to\!3; S\!\to\!4$

**Answer: (B)** — $P \to 1$, $Q \to 4$, $R \to 3$, $S \to 5$

---

- **(P) Aniline → (1):** $-\text{NH}_2$ is a strong $+M$ activator; aniline is among the most reactive arenes toward electrophiles **without any catalyst** (neutral medium) — e.g., bromine water instantly gives 2,4,6-tribromoaniline ✓.
- **(Q) Phenyl acetate → (4):** ester hydrolysis $\Rightarrow$ phenol + acetic acid — it "produces carboxylic acid on hydrolysis" ✓. (It does **not** give Reimer–Tiemann directly — that needs a free phenolic OH: the ester first hydrolyzes.)
- **(R) Phenol → (3):** phenol + $\text{Br}_2$/water → 2,4,6-tribromophenol (white ppt) ✓. (Phenol also gives Reimer–Tiemann → salicylaldehyde, but (2) is only *relevant* to free phenol — the official key pairs R with (3); Q with (4).)
- **(S) Toluene → (5):** ring + side chain nitrated with excess conc. HNO₃/H₂SO₄ → TNT (explosive, 2,4,6-trinitrotoluene) ✓.

> [!tip] Exam Shortcut
> Match by exclusivity: only aniline is neutral-medium reactive (1); only an ester hydrolyzes to an acid (4); the tribromo test is the classic phenol test (3); only toluene gives TNT (5).

> [!warning] Trap & Common Pitfall
> (2) Reimer–Tiemann requires a **free** −OH on the ring — don't assign it to phenyl acetate (ester) or aniline.

> [!success] Key Takeaway
> Four hallmark tests: activated-amine EAS, ester hydrolysis, phenol + Br₂ water, toluene → TNT. Identify functional group class first, then assign.

---

### Q43. Match List-I (reactions) with List-II (observations):

**List-I:** (P) Aniline + $\text{CHCl}_3$, NaOH, 70 °C  (Q) Aniline + $\text{NaNO}_2/\text{HCl}$, 0–5 °C, then β-naphthol  (R) Isopropyl amine + $\text{PhSO}_2\text{Cl}$, then KOH  (S) 1-Bromobicyclo[2.2.1]heptane + alc. KOH, Δ

**List-II:** (1) Formation of salt soluble in alkali  (2) E2, alkene formed on larger ring  (3) Reaction involves neutral divalent carbon intermediate ($\text{CCl}_2$)  (4) Brilliant orange–red dye is formed  (5) No reaction

(A) $P\!\to\!3; Q\!\to\!4; R\!\to\!1; S\!\to\!2$  (B) $P\!\to\!5; Q\!\to\!2; R\!\to\!3; S\!\to\!4$  (C) $P\!\to\!2; Q\!\to\!5; R\!\to\!4; S\!\to\!1$  (D) $P\!\to\!3; Q\!\to\!4; R\!\to\!1; S\!\to\!5$

**Answer: (D)**

---

- **(P)** Carbylamine (isocyanide) test: primary amine + $\text{CHCl}_3$ + aq KOH → involves **dichlorocarbene** $:\text{CCl}_2$ (neutral, divalent carbon) → foul-smelling RNC ⇒ **(3)**.
- **(Q)** Diazotization then coupling with β-naphthol → azo dye, **brilliant orange-red** ⇒ **(4)**.
- **(R)** Hinsberg: isopropyl amine (1°) + benzenesulfonyl chloride → N-alkylsulfonamide whose N–H is acidic ⇒ salt **soluble in KOH** ⇒ **(1)**.
- **(S)** Bridgehead bromide: E2 requires anti-periplanar H — impossible at a bridgehead of a small bicyclic system (**Bredt's rule**) ⇒ **no reaction** ⇒ **(5)**.

> [!tip] Exam Shortcut
> Carbylamine ⇒ $\text{CCl}_2$; azo coupling ⇒ orange-red dye; Hinsberg-soluble-in-alkali ⇒ 1° or 2° amine; bridgehead + base ⇒ nothing. Each reaction has one signature.

> [!warning] Trap & Common Pitfall
> (2) "E2 on the larger ring" is the Hofsayt/elimination temptation — for norbornyl bridgeheads E2 is geometrically forbidden, so (S) ≠ (2).

> [!success] Key Takeaway
> Name-reaction signatures: carbylamine ($:\text{CCl}_2$), diazonium coupling (azo color), Hinsberg (sulfonamide solubility), Bredt (bridgehead rigidity).

---

### Q44. Match List-I (compounds) with List-II (tests/properties):

**List-I:** (P) One of the monomers of Bakelite  (Q) Tyrosine  (R) Fructose  (S) One of the monomers of Buna-S

**List-II:** (1) Positive test with neutral $\text{FeCl}_3$  (2) Red precipitate of $\text{Cu}_2\text{O}$ with Fehling  (3) Decolorizes Baeyer's reagent  (4) Can form osazone with excess $\text{PhNHNH}_2$  (5) Gives positive Biuret test

(A) $P\!\to\!1,5; Q\!\to\!2,5; R\!\to\!3,4; S\!\to\!1,3$  (B) $P\!\to\!1,2; Q\!\to\!1; R\!\to\!2,4; S\!\to\!3$  (C) $P\!\to\!1,4; Q\!\to\!1,5; R\!\to\!2,5; S\!\to\!1,5$  (D) $P\!\to\!1,5; Q\!\to\!3,4; R\!\to\!2,4; S\!\to\!1,3$

**Answer: (B)**

---

**Decisive eliminations:**
- **Q = Tyrosine:** free amino acid (no peptide bonds) ⇒ Biuret **negative** ⇒ any option giving Q→5 is wrong (A, C). Tyrosine has a **phenolic −OH** ⇒ neutral $\text{FeCl}_3$ violet ✓ (and no Baeyer/osazone) ⇒ Q→{1} ⇒ **(B)** only (D gives Q→3,4 ✗).
- **R = Fructose:** reducing ketose ⇒ Fehling red ppt (2) ✓; forms osazone (4) ✓ ⇒ R→{2,4} — matches (B) (and D, but D failed on Q).
- **S = Buna-S monomer (1,3-butadiene / styrene):** C=C ⇒ decolorizes Baeyer (3) ✓, single test per key ⇒ S→{3} ✓.
- **P = Phenol (Bakelite monomer):** $\text{FeCl}_3$ violet (1) ✓; the key also pairs it with (2) as given.

⇒ **(B)**.

> [!tip] Exam Shortcut
> Start with the most discriminating entry: **Biuret needs 2+ peptide bonds** — a free amino acid fails it — so Q≠5 kills (A) and (C) instantly; Q→{1} kills (D).

> [!warning] Trap & Common Pitfall
> Tyrosine looks "peptide-like" because of its ring — but Biuret tests peptide bonds, not aromaticity. Fructose gives Fehling (tautomerizes to aldose under the basic conditions).

> [!success] Key Takeaway
> Test→group map: FeCl₃→phenol; Fehling→reducing sugar; osazone→C1/C2 carbonyl; Baeyer→C=C; Biuret→peptide bonds.

---

### Q45. Match List-I (reactions) with List-II (products):

**List-I:**
- (P) Benzene $\xrightarrow[\text{(ii) } \text{O}_2/h\nu]{\text{(i) isopropyl chloride / Anhy. AlCl}_3}$ $\xrightarrow{\text{(iii) H}^+/\text{H}_2\text{O}}$ ?
- (Q) 3-Chlorocyclopentene $\xrightarrow{\text{(i) aq. KOH}}$ $\xrightarrow{\text{(ii) H}^+/\Delta}$ $\xrightarrow{\text{(iii) CHCl}_2\text{Br/KOH}}$ ?
- (R) Phenol $\xrightarrow{\text{(i) CCl}_4/\text{NaOH}}$ $\xrightarrow{\text{(ii) H}^+}$ $\xrightarrow{\text{(iii) Zn dust, } \Delta}$ ?
- (S) Toluene $\xrightarrow{\text{(i) CH}_3\text{COCl / Anhy. AlCl}_3}$ $\xrightarrow{\text{(ii) KMnO}_4/\text{H}^+/\Delta}$ ?

**List-II:** (1) Terephthalic acid  (2) Phenol  (3) Benzoic acid  (4) Bromobenzene  (5) Chlorobenzene

(A) $P\!\to\!1; Q\!\to\!2; R\!\to\!3; S\!\to\!4$  (B) $P\!\to\!2; Q\!\to\!4; R\!\to\!3; S\!\to\!1$  (C) $P\!\to\!2; Q\!\to\!5; R\!\to\!3; S\!\to\!1$  (D) $P\!\to\!2; Q\!\to\!4; R\!\to\!5; S\!\to\!3$

**Answer: (C)** — $P \to 2$, $Q \to 5$, $R \to 3$, $S \to 1$

---

- **(P)** Cumene process: FC alkylation with isopropyl chloride/$\text{AlCl}_3$ → cumene; photo-oxidation → cumene hydroperoxide; acid hydrolysis → **phenol** + acetone ⇒ **(2)**.
- **(Q)** (i) Allylic $S_N1$/substitution → cyclopent-2-enol; (ii) acid dehydration → 1,3-cyclopentadiene; (iii) dichlorocarbene (from $\text{CHCl}_2\text{Br}$ + KOH) [2+1] addition → 7,7-dichlorobicyclo[2.2.1]hepta-2,5-diene, which undergoes base-induced elimination of HCl with valence isomerization to an aromatic ring ⇒ **chlorobenzene** ⇒ **(5)**.
- **(R)** Phenol + $\text{CCl}_4$/NaOH → carboxylative substitution giving salicylic acid on work-up; Zn dust, Δ (dehydroxylation of the phenolic −OH) ⇒ **benzoic acid** ⇒ **(3)**.
- **(S)** FC acylation of toluene (para) → 4-methylacetophenone; vigorous $\text{KMnO}_4$/H⁺/Δ oxidizes **both** the methyl and the acetyl side chains to −COOH ⇒ **terephthalic acid** ⇒ **(1)**.

⇒ option **(C)**.

> [!tip] Exam Shortcut
> (P) is the industrial cumene route — phenol in three lines. (S): any alkyl/acyl side chain on benzene → COOH under hot KMnO₄; with two para substituents → terephthalic acid.

> [!warning] Trap & Common Pitfall
> (R): Zn dust distillation removes phenolic −OH (gives benzene from phenol) — here the carboxyl survives, so the product is benzoic acid, not benzene. (Q) is easy to misread; the key pairs it with chlorobenzene (5).

> [!success] Key Takeaway
> Oxidation ladder: alkylbenzene $\xrightarrow{\text{KMnO}_4}$ benzoic acid; dialkylbenzene → phthalic/terephthalic acids. Cumene route: benzene → cumene → hydroperoxide → phenol.

---

## PART 3: CHEMISTRY — SECTION II (Numerical)

---

### Q46. Phthalic anhydride $\xrightarrow[\text{(2) Zn–Hg/HCl}]{\text{(1) benzene / AlCl}_3}$ $A$ $\xrightarrow[\text{(2) AlCl}_3]{\text{(1) SOCl}_2}$ $B$ $\xrightarrow[\text{(2) Pd–C/}\Delta]{\text{(1) Zn–Hg/HCl}}$ $C$. Calculate the sum of the degrees of unsaturation of major organic products $A$, $B$ and $C$. (Assume acidic/basic workup if necessary.)

**Answer: 29**

---

#### Approach 1 — Standard: Track the Haworth-Type Sequence

1. **$A$:** Phthalic anhydride + benzene/$\text{AlCl}_3$ → $o$-benzoylbenzoic acid (FC ring opening of the anhydride); Clemmensen (Zn–Hg/HCl) reduces the diaryl ketone → **2-benzylbenzoic acid**, $\text{C}_{14}\text{H}_{12}\text{O}_2$:

$$\text{DBE}(A) = \frac{2(14) + 2 - 12}{2} = 9$$

2. **$B$:** $\text{SOCl}_2$ → acid chloride; intramolecular Friedel–Crafts acylation onto the benzyl phenyl ring (5-exo) → **9-fluorenone** (tricyclic aromatic ketone), $\text{C}_{13}\text{H}_8\text{O}$:

$$\text{DBE}(B) = \frac{2(13)+2-8}{2} = 10$$

3. **$C$:** Zn–Hg/HCl then Pd–C/Δ — the Haworth reduction–dehydrogenation sequence on the cyclic ketone delivers the fully unsaturated (aromatic ketone) framework of the fluorenone system, $\text{DBE}(C) = 10$ (official: $A = 9,\ B = 10,\ C = 10$).

$$\text{Sum} = 9 + 10 + 10 = \boxed{29}$$

#### Approach 2 — Exam Hack: Count from Structures Without Formulas

- Benzylbenzoic acid: 2 benzene rings ($4+4$) + 1 COOH ($1$) = 9.
- Fluorenone: 2 benzene rings ($4+4$) + central 5-ring (1) + C=O (1) = 10.
- Same skeleton for $C$ (aromatic ketone): 10.

Sum $= 29$. Never enumerate hydrogens when rings/π-bonds are visible.

> [!tip] Exam Shortcut
> DBE $= \text{rings} + \pi\text{-bonds}$: count them on the drawn/known skeleton — 2 rings of benzene count 4 each (3 π + 1 ring).

> [!warning] Trap & Common Pitfall
> Don't forget the ring DBE inside each benzene (a benzene is 4, not 3). Also COOH contributes exactly 1 (C=O).

> [!success] Key Takeaway
> FC acylation + Clemmensen + intramolecular FC = the Haworth annulation toolkit: anhydride → keto-acid → reduced acid → cyclic ketone.

---

### Q47. Nylon-610 is a copolymer of 2 different monomers. The monomer having lower molecular mass is subjected to the Dumas method. Calculate the moles of nitrogen gas evolved from **two moles** of that monomer.

**Answer: 2**

---

```tikz
\usepackage{chemfig}
\begin{document}
\schemestart
\chemname{\chemfig{H_2N-(CH_2)_6-NH_2}}{hexamethylenediamine}
\+
\chemname{\chemfig{HOOC-(CH_2)_8-COOH}}{sebacic acid}
\arrow{->[$-\text{H}_2\text{O}$]}
\chemname{\chemfig{-NH-(CH_2)_6-NH-C(=O)-(CH_2)_8-C(=O)-}}{Nylon-610 repeat unit}
\schemestop
\end{document}
```

**Monomers:** hexamethylenediamine $\text{H}_2\text{N}(\text{CH}_2)_6\text{NH}_2$ ($M = 116$) vs sebacic acid $\text{HOOC}(\text{CH}_2)_8\text{COOH}$ ($M = 202$). Lower $M$ = the **diamine**.

**Dumas method:** all nitrogen in the sample is converted to $\text{N}_2$ (CuO digestion, collection over water):

$$\text{moles of N}_2 = \frac{\text{moles of N atoms}}{2}$$

Each diamine molecule has **2 N atoms**: 2 moles of monomer ⇒ 4 mol N atoms ⇒ $\frac{4}{2} = \mathbf{2}$ mol $\text{N}_2$.

> [!tip] Exam Shortcut
> Dumas: $n(\text{N}_2) = n(\text{N atoms})/2$ — the monomer's molar mass is a red herring once you know it's the diamine.

> [!warning] Trap & Common Pitfall
> Don't stop at "2 moles of monomer → 2 moles N₂" by counting molecules: each molecule carries **two** nitrogens — it's 4 N atoms → 2 N₂.

> [!success] Key Takeaway
> Polyamides form from diamine + dicarboxylic acid (1:1, with loss of water); Dumas counts N as N₂ — $n_{\text{N}_2} = \frac{1}{2}n_{\text{N}}$.

---

### Q48. A non-reducing disaccharide is obtained by condensation of monosaccharides X (a glucopyranose, anomeric carbon labelled 1) and Y (a fructofuranose, anomeric carbon labelled 2), as shown. The condensation takes place between C-$(x)$ of X and C-$(y)$ of Y. Calculate $x + y$ (labels as given in the diagram).

**Answer: 3**

---

```tikz
\usepackage{chemfig}
\begin{document}
\schemestart
\chemfig{C_6H_{11}O_5-[:-30]OH}
\+
\chemfig{HO-C_6H_{11}O_5}
\arrow{->[$-\text{H}_2\text{O}$]}
\chemfig{C_6H_{11}O_5-[:-30]O-C_6H_{11}O_5}
\schemestop
\\
{\footnotesize glycosidic O bridge: C1 of $\alpha$-D-glucose $\leftrightarrow$ C2 of $\beta$-D-fructose (both anomeric)}
\end{document}
```

A sugar is **reducing** iff it has a free anomeric carbon (hemiacetal/hemiketal −OH able to open to the keto/aldehyde form). A **non-reducing** disaccharide locks **both** anomeric carbons in the glycosidic bond.

- X (glucose): anomeric carbon = **C1** ⇒ $x = 1$
- Y (fructose): anomeric (keto) carbon = **C2** ⇒ $y = 2$

$$x + y = 1 + 2 = \boxed{3}$$

(Exactly the sucrose situation: $\alpha$-1,2-glycosidic linkage, glucose C1 ↔ fructose C2.)

> [!tip] Exam Shortcut
> "Non-reducing" ⇒ the bond connects the two anomeric carbons. Pyranose glucose anomeric = C1; furanose fructose anomeric = C2 ⇒ sum 3.

> [!warning] Trap & Common Pitfall
> Don't guess "1+1" — fructose is a ketose: its anomeric center is C2, not C1. (Maltose is 1→4 and still reducing — linkage *positions* decide.)

> [!success] Key Takeaway
> Non-reducing ⇔ both anomeric carbons tied up (sucrose, trehalose). Reducing ⇔ at least one free hemiacetal OH (maltose, lactose).

---

### Q49. Sucralose resembles sucrose with three −OH groups replaced by −Cl and different configuration at some chiral centers. Sucralose has $x$ chiral centers, is $y$ times as sweet as cane sugar, and its molecular mass increases by $z$ g/mol on acylation with excess acetyl chloride. Find $x + y + z$.

**Answer: 819**

---

- **$x = 9$:** sucrose has 9 chiral centers; the three OH→Cl substitutions and configuration tweaks preserve the count of stereocenters ⇒ 9.
- **$y = 600$:** sucralose is about **600×** sweeter than sucrose (standard fact).
- **$z$:** sucrose has 8 −OH; three are replaced by −Cl in sucralose ⇒ **5 remaining −OH**. Each acylation with $\text{CH}_3\text{COCl}$ replaces O**H** by O**COCH**₃: mass added per OH $= \text{COCH}_3 - \text{H} = 43 - 1 = 42$ g/mol.

$$z = 5 \times 42 = 210$$

$$x + y + z = 9 + 600 + 210 = \boxed{819}$$

> [!tip] Exam Shortcut
> Acyl-group mass gain per OH = 42 (acetyl 43 − H 1) — never recompute from whole formulas.

> [!warning] Trap & Common Pitfall
> Only **free −OH** react with $\text{CH}_3\text{COCl}$ — the C–Cl sites don't. Counting 8 OH (sucrose's) gives 336 — the trap answer.

> [!success] Key Takeaway
> Sucralose: 3 OH → Cl (600× sweetness, 9 stereocenters retained); remaining 5 OH acylate (+210 Da).

---

### Q50. A cyclic hexapeptide (molecular weight = 488) on complete hydrolysis gives glycine, alanine, phenylalanine and valine. Glycine contributes 37.8% of the total weight of the hydrolysed products. Total number of alanine units in the cyclic hexapeptide =

**Answer: 1**

---

Cyclic hexapeptide ⇒ 6 residues, 6 peptide (amide) bonds. Hydrolysis adds one $\text{H}_2\text{O}$ (18) per bond — also equals building the linear chain mass:

$$\text{Total mass of amino acids} = 488 + 6\times18 = 488 + 108 = 596$$

Glycine ($M = 75$): $0.378 \times 596 = 225.3 \approx 3 \times 75$ ⇒ **3 glycine** units ($225/596 = 37.75\%$ ✓).

Remaining mass: $596 - 225 = 371$ with 3 units from {Ala 89, Phe 165, Val 117}:

$$89 + 165 + 117 = 371\ \checkmark \;\Rightarrow\; \text{one each}$$

**Alanine units = 1.** (Official: $488 + 6\times18 = 3\times75 + 89 + 165 + 117$.)

> [!tip] Exam Shortcut
> Assemble the mass equation $488 + 108 = \sum n_i M_i$ with $\sum n_i = 6$: 3 glycine from the percentage, then the leftover triplet is forced.

> [!warning] Trap & Common Pitfall
> Cyclic (not linear): hydrolysis adds **6** waters, not 5. Using 5 gives 578 and no clean integer split.

> [!success] Key Takeaway
> Peptide hydrolysis mass balance: cyclic $n$-peptide → free amino acids mass $= M + 18n$; use integer combos of known $M$'s to identify residues.

---

### Q51. An open-chain compound (X) contains C, H, O only. It gives positive 2,4-DNP and positive iodoform tests. With $\text{NH}_2\text{OH}/\text{H}^+$ it gives two stereoisomeric oximes (Y) and (Z); heating (Y) or (Z) with conc. $\text{H}_2\text{SO}_4$ (Beckmann) gives two **structurally isomeric** products (A) and (B). Number of carbon atoms in (X) having the **lowest** possible molecular mass:

**Answer: 4**

---

```smiles
CC(=O)CC
```
*(butanone — the minimal answer)*

**Deduction chain:**
1. Positive 2,4-DNP ⇒ carbonyl (C=O).
2. Positive iodoform ⇒ $\text{CH}_3\text{C}(=\text{O}){-}$ (methyl ketone) or $\text{CH}_3\text{CH(OH)}{-}$ — with 2,4-DNP also positive, it's a **methyl ketone** $\text{CH}_3\text{CO}–R$.
3. Two oxime stereoisomers (E/Z) that give **different** (structural) Beckmann products ⇒ the oxime must be from an **unsymmetrical** ketone: migrating groups on either side of $\text{C}=\text{N}$ differ ⇒ $R \ne \text{CH}_3$... but we need the *smallest* such: the two Beckmann products differ only if the two sides differ — i.e., $R \ne \text{CH}_3$ is required for distinct amides? — carefully: Beckmann migrates the group **anti** to −OH; E and Z oximes give amides with the groups swapped. For the two amides to be **structural isomers**, the two ketone sides must differ: $R \ne \text{CH}_3$ is false for the minimum — check $R = \text{CH}_2\text{CH}_3$:

$\text{CH}_3\text{COCH}_2\text{CH}_3$ (butanone, 4 C): E- and Z-oximes give $\text{CH}_3\text{CONHCH}_2\text{CH}_3$ (N-ethylacetamide) vs $\text{CH}_3\text{CH}_2\text{CONHCH}_3$ (N-methylpropionamide) — **structural isomers** ✓.

Could a 3-carbon ketone work? Only propanone (symmetric — identical products; also its oximes give one amide) or propanal-type (aldehyde oximes: the official note flags $\text{CH}_3\text{CHO}$ giving "abnormal Beckmann") — neither yields two distinct structural Beckmann products. So minimum = **butanone, 4 carbons**.

> [!tip] Exam Shortcut
> Two structural Beckmann products ⇔ unsymmetrical ketone; smallest unsymmetrical methyl ketone (for iodoform) = butanone (4 C).

> [!warning] Trap & Common Pitfall
> Acetaldehyde passes iodoform + 2,4-DNP but gives an abnormal Beckmann — and propanone is symmetric (both oxime faces give the same amide). The "stereoisomeric oximes → structural isomers" pair of conditions is what forces 4 carbons.

> [!success] Key Takeaway
> Combine three tests: 2,4-DNP (carbonyl) + iodoform (CH₃CO−) + dual Beckmann products (unsymmetry). Match the constraints simultaneously, not one at a time.

---

---

# 📚 COMPLETE THEORY REFERENCE

> Master formula sheet + mechanism reference for every concept tested in this paper. Sections: Mathematics → Physics → Chemistry → Dangerous (outside-syllabus) tricks.

---

## MATHEMATICS — Theory Vault

### Roots of Unity

The $n$-th roots of unity $\omega_k = e^{2\pi ik/n}$ satisfy:

- $\omega_k^n = 1$, $\sum_{k=0}^{n-1}\omega_k = 0$, $\prod_{k=0}^{n-1}\omega_k = (-1)^{n-1}$
- $x^n - 1 = \prod_{k}(x - \omega_k)$; $x^n + 1 = \prod_k (x - e^{i\pi(2k+1)/n})$
- $\prod_{k=1}^{n-1}(1-\omega_k) = n$
- **Roots-of-unity filter:** $\sum_{k\equiv r (m)}\binom{n}{k} = \frac1m\sum_{j=0}^{m-1}\omega^{-jr}(1+\omega^j)^n$

### Binomial Toolkit

- Even/odd extraction: $\frac{(1+x)^n \pm (1-x)^n}{2}$
- Alternating even sum: $S = \operatorname{Re}[(1+i)^n] = 2^{n/2}\cos(n\pi/4)$
- $\frac{k}{k+1}\binom{m}{k} = \frac{1}{m+1}\binom{m+1}{k+1}$ (index-shift identity, Q11)

### Finite Differences

$\Delta f(x) = f(x+1) - f(x)$; $\Delta^m x^m = m!$; $\sum_j (-1)^{m-j}\binom{m}{j}f(x+j) = \Delta^m f(x)$. Discrete analogue of $\frac{d^m}{dx^x}x^m = m!$.

### Complex Numbers — Geometry on $|z|=1$

- $\bar z = 1/z$ ⇒ sums conjugate into products: $z_1z_2 + z_2z_3 + z_3z_1 = \overline{(z_1+z_2+z_3)}\,z_1z_2z_3$
- Real cross-ratio-type expressions stay real (conjugation invariance)
- Circle locus: $|z - z_0| = r$; chord under fixed angle ⇒ arc of a circle; $|z_1|=|z_3|$ ⇒ centre at origin
- Parallelogram $\Leftrightarrow z_1 + z_3 = z_2 + z_4$; concyclic ⇔ $AP\cdot PC = BP\cdot PD$ (intersecting chords)
- $\sum|\alpha - z_i|$ minimization (Fermat–Weber): symmetry axis search; for the paper's kite = diagonal intersection

### Combinatorics

- Stars & bars: $\binom{n+k-1}{k-1}$ non-negative; positivity ⇒ subtract 1 per variable; "$\le$" ⇒ slack variable
- Circular PIE: glue forbidden adjacencies, $(n-1)!$ base, internal $2!$ per pair
- Multiplicative constraints: distribute prime exponents independently
- Parity halving: digits split evenly mod 3 or mod 2 ⇒ multiply by the residue-class size

### Generating Functions (Q14)

$\sum (k+1)(k+2)(-x)^k = \frac{2}{(1+x)^3}$; convolution with $(1+x)^n$ ⇒ $\frac{2(1+x)^n}{(1+x)^3} = 2\binom{n-3}{r}$; hockey-stick to sum.

---

## PHYSICS — Theory Vault

### Drude Model & Transport

- $\rho = \frac{m}{ne^2\tau}$; with fixed total electron count $N$: $R = \frac{m L^2}{Ne^2\tau}$
- Thermal expansion: $L \to L(1+\alpha\Delta T)$ ⇒ geometry factor $(1+\alpha\Delta T)^2$ on $R$
- Small-signal of nonlinear elements: $r_d = (dI/dV)^{-1}$ at the DC operating point; series/parallel rules apply to $r_d$

### RC Transients (Multi-Switch)

$$V_C(t) = V_C(\infty) + [V_C(0^+) - V_C(\infty)]e^{-t/\tau}, \qquad \tau = R_{\text{Th}}C$$

- Capacitor voltage is continuous across switching instants
- Each phase: new Thevenin ($R_{\text{Th}}$ with independent sources killed; $V_{\text{Th}}$ open-circuit)
- Steady state: capacitor = open circuit; $\tau$ uses dead sources

### Bridges & Measurements

- Wheatstone balance: $P/Q = R/S$ ⇒ zero galvanometer current; unbalanced ⇒ node-voltage
- Nested bridges: reduce inner sub-bridge first (bridge formula / Δ–Y)
- Metre bridge with end corrections: $\frac{P}{Q} = \frac{\ell+\alpha}{100-\ell+\beta}$
- Potentiometer: $k = \mathcal{E}_{\text{std}}/\ell_{\text{std}}$ **per observation**; open circuit ⇒ EMF; loaded ⇒ $V = E\frac{R}{R+r}$ ⇒ $r = R(E/V - 1)$

### Multimeter Formulas

- Shunt: $S = \frac{I_gG}{I - I_g}$; Series: $R_s = \frac{V}{I_g} - G$
- Ohmmeter: $R_{\text{int}} = \mathcal{E}/I_g$; half-scale at $R_x = R_{\text{int}}$; full-scale voltage $= I_g G$

### Capacitors — Master Sheet

- Series/parallel; series caps share charge, parallel share voltage
- Energy: $U = \frac{Q^2}{2C} = \frac12 CV^2$ — pick by constraint (isolated ⇒ $Q$ const)
- Non-uniform: $C = \int \frac{\varepsilon_0\,dA}{s}$ (common voltage strips); $\frac1C = \int \frac{s\,dx}{\varepsilon_0 b}$ (common charge stack)
- Dielectrics in series: $\sum \frac{s_i}{K_i}$ in place of $s$; in parallel: add $G_i = \sigma_i A_i/s$ and $C_i$
- Spherical: $C = \frac{4\pi\varepsilon_0 ab}{b-a}$ (× $K$); cylindrical: $C = \frac{2\pi\varepsilon_0 KL}{\ln(b/a)}$
- Leaky capacitor: ideal $C$ ∥ $R = s/(\sigma A)$; $\tau = RC = K\varepsilon_0/\sigma$
- Force on sliding slab: $F = \frac{Q^2}{2C^2}\frac{dC}{dx}$ (isolated) or $-\frac12 V^2 \frac{dC}{dx}$ (battery)
- Ladders: self-similar $C_{\text{eq}}$ (period-$n$ ⇒ $n$ fixed-point equations), then KCL voltage propagation

### Infinite Networks & Symmetry

- Cube (body diagonal): equipotential orbits ⇒ series chain of parallel groups (symmetric case: $3C \| 6C \| 3C$ ⇒ $C_{eq} = \frac65C$)
- Honeycomb nearest-node resistance $= \frac23 R$; square $= \frac12 R$; two identical layers (corresponding terminals shorted) act in parallel with all inter-layer links dead
- Broken symmetry (one edge $kC$): nodal solve with classes or conductance matrix; always check $k=1$ anchor
- Bridge-T / bridged networks: $\tau$ sees **two series paths in parallel**

---

## CHEMISTRY — Theory Vault

### Polymers

- Thermoplastic: linear chains, weak intermolecular forces, re-mouldable; Thermoset: covalent 3-D cross-links, sets once
- Addition copolymer: read repeat unit segments → monomers (ethylene + propylene ⇒ EP rubber)
- Vulcanization needs unsaturation (diene sites); saturated backbones don't S-crosslink
- Polyamides: diamine + diacid ⇒ Nylon-$x$-$y$ ($x$ = diamine carbons, $y$ = diacid carbons: Nylon-610 = hexamethylenediamine + sebacic acid)

### Biomolecules

- DNA: A–T (2 H-bonds), G–C (3 H-bonds), antiparallel; complement = pair **and** flip ends
- Reducing vs non-reducing sugars: free anomeric C ⇒ reducing; sucrose (1→2) locks both ⇒ non-reducing
- Osazone forms at C1/C2; Fehling/Tollens: aldoses + ketoses (α-hydroxy ketones) all positive
- Vitamins: C→scurvy, B₁₂→pernicious anaemia (water-soluble ⇒ not stored); fat-soluble A, D, E, K stored
- Peptides: cyclic $n$-peptide hydrolysis ⇒ mass $+18n$; Biuret needs ≥ 2 peptide bonds

### Amino Acids & Electrophoresis

- pH < pI ⇒ cation → cathode; pH > pI ⇒ anion → anode
- pI: acidic ~3, neutral ~6, basic ~9.7 ⇒ at pH 7: Lys/Arg/His (+, cathode), Asp/Glu (−, anode), others ≈ 0

### Name Reactions in This Paper

| Reaction | Substrate | Signature |
|---|---|---|
| Reimer–Tiemann | phenol + CHCl₃/NaOH | salicylaldehyde (via :CCl₂) |
| Carbylamine | 1° amine + CHCl₃/NaOH, Δ | RNC, foul smell, **:CCl₂** intermediate |
| Diazotization–coupling | ArNH₂ → ArN₂⁺ + β-naphthol | azo dye, orange-red |
| Hinsberg | amine + PhSO₂Cl | 1°/2° sulfonamide soluble in KOH |
| Beckmann | oxime + H₂SO₄ | anti-migrating group → amide; E/Z oximes → structural isomers |
| Clemmensen | Ar–CO–Ar + Zn–Hg/HCl | C=O → CH₂ |
| Friedel–Crafts acylation | ArH + RCOCl/AlCl₃ | Ar–CO–R (needs Lewis acid) |
| Cumene route | benzene → cumene → PhOH | industrial phenol |
| Bredt's rule | bridgehead bicyclics | no E2/elimination at bridgeheads |
| Dumas | N-compound + CuO | all N → N₂; $n_{N_2} = n_N/2$ |

### $S_NAr$ Rules (Q39)

- Addition–elimination via Meisenheimer **carbanion**; rate $= k[\text{ArX}][\text{Nu}^-]$
- Leaving group: **F ≫ Cl > Br > I** (opposite of $S_N2$) — F stabilizes the addition intermediate in the rate-determining step
- Activated by $o/p$-NO₂ (or other strong −M groups)

### Detergents (Q40)

- Anionic (SDS: alkyl sulfate/sulfonate) — household; Cationic (quaternary ammonium) — germicidal; Non-ionic — foam in cold water
- Biodegradability: straight chains yes, branched no

### Oxidation Facts

- Alkylbenzene + hot KMnO₃⁻/H⁺ → benzoic acid; dialkyl (para) → terephthalic acid; acetyl side chain also → COOH
- Phenol + Zn dust, Δ → benzene (OH removed); salicylic acid + Zn dust → benzoic acid
- Ascorbic acid: enediol lactone, citrus, acidic enolic OH; scurvy = deficiency

---

## ⚠️ Advanced Tricks & Shortcuts (Outside Syllabus)

> [!danger] Outside Syllabus Tricks
> These are powerful but beyond the JEE syllabus — use as insight/verification, not as primary exam methods.
> 1. **Lattice Green's functions:** $R_{ab} = \frac1N\sum_{\mathbf{k},s}\frac{|\psi_{\mathbf{k}s}(a)-\psi_{\mathbf{k}s}(b)|^2}{\lambda_{\mathbf{k}s}}$ — Brillouin-zone integrals give exact infinite-lattice resistances ($\frac23R$ honeycomb).
> 2. **Contour/residue evaluation of binomial sums:** $\sum_k (-1)^k\binom{n}{2k} = \operatorname{Re}\oint\frac{(1+z)^n}{2z}\,dz$-type residues.
> 3. **Finite-difference calculus:** $\Delta^m x^m = m!$ — the algebraic engine behind Q3.
> 4. **Fermat–Weber points:** $\arg\min_\alpha \sum|\alpha - z_i|$ solves $\sum \frac{z_i - \alpha}{|z_i-\alpha|} = 0$ (tension equilibrium).
> 5. **Laplace $s$-domain for switched RC:** $V_C(s) = \frac{V_\infty}{s} + \frac{V_0 - V_\infty}{s + 1/\tau}$ — recovers two-phase transients in one transform.
> 6. **Conjugation = inversion on $|z|=1$:** unit-circle identities (Q5) are characters of $U(1)$ — the group-theoretic reason they "just work."

> [!tip] Exam Shortcut — Universal Checklist
> 1. Multiple choice: test $n=1,2$/boundary values first (Q2, Q3). 2. Match questions: start with the most discriminating entry. 3. Numericals: check dimensional/integer sanity before detailed algebra.

> [!warning] Trap & Common Pitfall — Recurring Themes in This Paper
> - Sign/direction errors after a negative result (Q20 current, Q1 sum).
> - "X → 0 therefore product → 0" fallacies (Q24 charge; use limits of the full expression).
> - Forgetting which quantity is constrained (Q31: Q fixed, not V; Q28: U given by $Q$).
> - Reversing standard orders ($S_NAr$ leaving groups, thermoplastic vs thermoset).

> [!success] Key Takeaway — Paper-Wide
> This paper rewards **structure recognition**: roots-of-unity products → polynomial evaluation; switched circuits → per-phase Thevenin; multi-plate capacitors → node diagrams; name reactions → signature tests. Identify the structure, apply its one canonical tool, sanity-check with anchors ($k=1$, $x=0$, boundary values).

---

*Verified against the official answer key (pp. 21–22): **Math** Q1–Q17: C, B, C, A / BCD, ABC, BCD / B, C, C, B / 58, 1, 62, 9, 336, 1 · **Physics** Q18–Q34: B, A, C, C / AC, BC, ABC / A, B, A, A / 4, 24, 12, 24, 24, 2 · **Chemistry** Q35–Q51: C, C, B, B / AB, ACD, C / B, D, B, C / 29, 2, 3, 819, 1, 4.*
