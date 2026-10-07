---
test: 3
paper: 1
subjects: [Mathematics, Physics, Chemistry]
status: complete
tags: [solutions, jee-advanced, test-3]
---

# 3-PAPER 1 — COMPLETE SOLUTIONS

> [!info] Paper details
> **Date:** 27-09-2026 · **Code:** 1001CJA106216260205 · JEE Advanced pattern
> **Sections:** 4 single-correct + 3 multiple-correct + 3 match-the-column + 6 numerical per subject
> **Figures** are drawn live by the plugins — see [PLUGIN-FIGURES](../docs/PLUGIN-FIGURES.md).

> [!warning] About the paper's own answer book
> The booklet prints worked solutions **for mathematics only** (Q1–Q16); for physics and
> chemistry it prints just "Correct Answer is (…)". Everything below for Q17–Q48 is worked
> out here from scratch and cross-checked against the key.

---

## PART 1: MATHEMATICS

---

### Q1. Number of $\alpha$ for which $\dfrac{\alpha x^{2}+7x-2}{\alpha+7x-2x^{2}}$ has a common linear factor.

**Answer: (D) 3**

```desmos-graph
left=-6; right=6
bottom=-6; top=6
height=340
grid=true
---
y=(-2x^2+7x-2)/(-2x^2+7x-2)|label:alpha=-2 -> the fraction is 1
y=(9x^2+7x-2)/(9+7x-2x^2)|label:alpha=9
y=(-5x^2+7x-2)/(-5+7x-2x^2)|label:alpha=-5
```

Let $N=\alpha x^{2}+7x-2$ and $D=\alpha+7x-2x^{2}$ share a root $r$. Subtracting
$Nr^{2}+7r-2=0$ from $(-2r^{2}+7r+\alpha)=0$ gives
$$(\alpha+2)\,(r^{2}-1)=0 .$$

- $\alpha=-2$: $N=-2x^{2}+7x-2$ and $D=-2x^{2}+7x-2$ are **identical** — both roots common;
- $r=+1$: $\alpha+7-2=0 \Rightarrow \alpha=-5$ (check $D$: $-2+7-5=0$ ✓);
- $r=-1$: $\alpha-7-2=0 \Rightarrow \alpha=9$ (check $D$: $-2-7+9=0$ ✓).

So $\alpha\in\{-2,-5,9\}$ — **3 values**, option **(D)**.

> [!success] Method
> Two polynomials share a linear factor iff the resultant vanishes. For a
> quadratic pair the shortcut is: add the two equations — the common root falls out.

---

### Q2. $\displaystyle\lim_{n\to\infty}\Big[(a^{n}+(b+c)^{n})^{\frac1n}+(b^{n}+(c+a)^{n})^{\frac1n}+(c^{n}+(a+b)^{n})^{\frac1n}\Big]$, perimeter 20.

**Answer: (B) 40**

For positive $A,B$: $\big(A^{n}+B^{n}\big)^{1/n}\to\max(A,B)$. In a triangle each side is
smaller than the sum of the other two, so

$$\max\big(a,\,b+c\big)=b+c,\quad \max(b,\,c+a)=c+a,\quad \max(c,\,a+b)=a+b .$$

```math
# each radical tends to the sum of the OTHER two sides
a = 7
b = 6
c = 7            # a triangle with perimeter 20
term1 = b + c =>
term2 = c + a =>
term3 = a + b =>
total = term1 + term2 + term3 =>
perimeter = a + b + c =>
```

Sum $=2(a+b+c)=2\times20=\mathbf{40}$, option **(B)**.

---

### Q3. $\displaystyle\lim_{x\to0}\Big(2+\log^{2}_{\sec(x/2)}\cos\frac{x}{3}\Big)^{3}$

**Answer: (C) $\left(\dfrac{178}{81}\right)^{3}$**

Both bases tend to $1$, so expand in $x$:

$$\ln\cos\frac{x}{3}\approx-\frac{x^{2}}{18},\qquad \ln\sec\frac{x}{2}=-\ln\cos\frac{x}{2}\approx\frac{x^{2}}{8}$$

$$\log_{\sec(x/2)}\cos\frac{x}{3}=\frac{\ln\cos(x/3)}{\ln\sec(x/2)}\to\frac{-x^{2}/18}{x^{2}/8}=-\frac{4}{9}$$

```math
# the log of cos(x/3) base sec(x/2), to leading order in x
x = 0.001
lncos = log(cos(x/3)) =>
lnsec = log(1/cos(x/2)) =>
ratio = lncos/lnsec =>
ratio_squared = ratio^2 =>
inner = 2 + ratio_squared =>
answer = inner^3 =>
```

The bracket is $\dfrac{2}{1}-\dfrac{16}{81}$… i.e. $2+\dfrac{16}{81}=\dfrac{178}{81}$, and the
whole expression is its **cube** — option **(C)**.

> [!tip] Trick
> The outer exponent is just a cube: get the bracket right and cube it. Never expand the
> cube first — the bracket is a clean rational number only *after* taking the inner limit.

---

### Q4. $f(t)=|t|+|t-1|$, $g(x)=\begin{cases}\max f(t), & x-1\le t\le x,\ 0\le x\le1\\ 3-x, & 1<x\le2\end{cases}$

**Answer: (B) 1**

```desmos-graph
left=-0.2; right=2.2
bottom=-0.4; top=3.4
height=340
grid=true
---
y=3-2x|0<=x<=1|label:max f(t) on [x-1,x]
y=3-x|1<x<=2|label:second piece
(1,1)|point|label:g(1)=1
(1,2)|open|label:jump from 1 to 2
```

For $0\le x\le1$ the interval $[x-1,x]$ lies inside $[-1,1]$, where
$f(t)=1$ for $t\ge0$ and $f(t)=3-2t\ge1$ for $t<0$. The maximum is therefore at the
**left** end:

$$g(x)=-2(x-1)+1=3-2x,\qquad g(1)=1 .$$

But the second piece gives $\lim_{x\to1^{+}}g(x)=3-1=2$:

$$g(1^{-})=1\ne2=g(1^{+})\ \Longrightarrow\ g \text{ is discontinuous at } x=1 .$$

```math
# check the two one-sided limits at x = 1
g_left = 3 - 2*1 =>
g_right = 3 - 1 =>
jump = g_right - g_left =>
non_derivable = 1     # only x = 1, and only inside [0,2]
```

Only **one** point of non-differentiability in $[0,2]$ — option **(B)**.

---

### Q5. $f(a)>0$, $f$ differentiable at $x=a$ — which statements are true?

**Answer: (A, C, D)**

**(A)** ratio $=1+\dfrac{f'(a)}{f(a)}\cdot\dfrac1n+O\!\left(\dfrac{1}{n^{2}}\right)$, so the
$n$-th root $\to1$ ✓.

**(B)** is **false**: taking logs,
$\frac1n\ln\frac{f(a+1/n)}{f(a)}\approx\frac{f'(a)}{f(a)}\frac{1}{n^{2}}\to0$, so the limit is
$1$, **not** $e^{f'(a)/f(a)}$ (the exponent has to be $\approx1/n$, not $1/n^{2}$).

**(C), (D)** with the exponent $\dfrac{a}{x-a}$:

$$\ln L=\frac{a}{x-a}\ln\frac{f(x)}{f(a)}\to a\cdot\frac{f'(a)}{f(a)}
\ \Longrightarrow\ L=e^{a f'(a)/f(a)} \quad (a>0)$$

```math
# sanity check of (B) with a concrete f: f(x) = e^x at a = 0
n = 1000
ratio = exp(1/n)/1 =>
limit_B = ratio^(1/n) =>
# the true value of the exponent's limit
true_exp = 1/1 =>
```

| Option | Claim | Verdict |
|---|---|---|
| (A) | limit $=1$ | ✅ TRUE |
| (B) | limit $=e^{f'(a)/f(a)}$ | ❌ FALSE |
| (C) | $x\to a^{+}$ limit $=e^{af'(a)/f(a)}$ | ✅ TRUE |
| (D) | $x\to a^{-}$ limit $=e^{af'(a)/f(a)}$ | ✅ TRUE |

---

### Q6. $\displaystyle\lim_{x\to0}\frac{\sin(\sin x)-\sin x}{ax^{5}+bx^{3}+c}=-\frac{1}{12}$

**Answer: (B, C, D)**

Expand once, carefully:

$$\sin x=x-\frac{x^{3}}{6}+\frac{x^{5}}{120},\qquad
\sin(\sin x)=\sin x-\frac{\sin^{3}x}{6}+\frac{\sin^{5}x}{120}$$

$$\sin(\sin x)-\sin x=-\frac{x^{3}}{6}+\frac{11x^{5}}{120}+O(x^{7})$$

```math
# series coefficients, with x symbolic-ish via small-x evaluation
x = 0.01
num = sin(sin(x)) - sin(x) =>
leading_coeff = num/(-x^3/6) =>
# the x^5 coefficient of the numerator
c5 = 11/120 =>
c3 = -1/6 =>
```

For the limit to exist and be finite the denominator must start at $x^{3}$: $c=0$.
Then

$$\lim=\frac{-x^{3}/6}{bx^{3}}=-\frac{1}{6b}=-\frac{1}{12}\ \Rightarrow\ b=2 .$$

$a$ is unconstrained (its $x^{5}$ term is sub-leading), $c=0$. Hence
$b=2,\ c=0,\ b-c=2,\ b+c=2$ — options **(B)**, **(C)**, **(D)**.

---

### Q7. $f(x)=(x-2)^{2}\cos\frac{\pi x}{4}+(x-2)|x-2|$ and $h=fg$ at $x=2$

**Answer: (A, B)**

```desmos-graph
left=0; right=4
bottom=-1.4; top=1.4
height=340
grid=true
---
y=(x-2)^2\cos(\frac{\pi x}{4})+(x-2)\sqrt{(x-2)^2}|label:f(x)
y=(x-2)^2\cos(\frac{\pi x}{4})|dashed|blue|label:first term
y=(x-2)\sqrt{(x-2)^2}|dashed|red|label:absolute-value term
(2,0)|open|label:f(2)=0, f'(2)=0
```

Both pieces vanish at $x=2$ *and* have zero slope there, so $f(2)=f'(2)=0$ and

$$h'(2)=\lim_{x\to2}\frac{f(x)g(x)}{x-2}=\Big[\lim_{x\to2}\frac{f(x)}{x-2}\Big]g(x)
=0\cdot(\text{bounded})=0 .$$

**(A)** true (existence of $\lim g$ implies boundedness), **(B)** true, **(C)** false
($g=1$ except $g(2)=5$ still gives $h'(2)=0$), **(D)** false (same example, $g(2)\neq0$).

---

### Q8. Match List-I with List-II (limits and derivatives)

**Answer: (A) P→2; Q→3; R→4; S→1**

| | Working | Value | List-II |
|---|---|---|---|
| **(P)** | $\lim\limits_{x\to\infty}\frac1\pi\tan^{-1}(x^{2}-x^{4})$: the bracket $\to-\infty$, so $\tan^{-1}\to-\pi/2$ | $-1/2$ | (2) |
| **(Q)** | $\dfrac{e^{x\ln2}}{e^{x}}=e^{x(\ln2-1)}\to0$ | 0 | (3) |
| **(R)** | $y=f\circ f\circ f$: $y'(0)=2\cdot2\cdot2$ | 8 | (4) |
| **(S)** | $\lim\limits_{x\to2^{-}}\dfrac{[x]}{\{x\}}=\dfrac{1}{1}$ | 1 | (1) |

```math
# (P) and (Q) numerically
x = 1000
P = atan(x^2 - x^4)/pi =>
Q = exp(x*log(2))/exp(x) =>
R = 2*2*2 =>
S = 1/1     # [x] -> 1, {x} -> 1 as x -> 2^-
```

---

### Q9. Match the functions with the value of the asked parameter

**Answer: (B) P→1; Q→2; R→3; S→4**

| | Working | Value |
|---|---|---|
| **(P)** | $f(x)=Ax^{a}\!\left(x-\frac1x\right)$ for $x>0$, $e^{x}$ for $x\le0$. Continuity at $0$ forces $a=1$ and then the right limit $-A=1\Rightarrow A=-1$; $A+a=0$ | **0** = (1) |
| **(Q)** | With $a=1$: left limit $\frac{\ln(1+x)-\ln(1-bx)}{x}\to1+b$, right limit $\frac{\sqrt{1+2x}-\sqrt{1-2x}}{\sin x}\to2$; so $k=2,\ b=1$, $k-b=1$ | **1** = (2) |
| **(R)** | $\frac{1-\cos2x}{x^{2}}\to2$ | **2** = (3) |
| **(S)** | $\frac{\sqrt{1+\sqrt{1+kx^{4}}}-\sqrt2}{x^{4}}\to\frac{k}{4\sqrt2}=c=\frac{1}{8\sqrt2}$, so $k=\frac12$, $6k=3$ | **3** = (4) |

```math
# (S) the k that makes c = 1/(8 sqrt 2)
c = 1/(8*sqrt(2)) =>
k = c*4*sqrt(2) =>
six_k = 6*k =>
# (Q): the two one-sided limits at 0 with a = 1
b_from_left = 1      # 1 + b = 2
k_value = 2 =>
k_minus_b = k_value - b_from_left =>
```

---

### Q10. Match the statements with their values

**Answer: (C) P→3; Q→3; R→4; S→2**

| | Working | Value |
|---|---|---|
| **(P)** | $f=ax^{2}+b\ (x\le1)$, $1/|x|\ (x>1)$. Continuity: $a+b=1$; differentiability: $2a=-1$, so $a=-\tfrac12,\ b=\tfrac32$ and $b-a=2$ | **2** = (3) |
| **(Q)** | $f=x^{p}\sin\frac1x$: $f'(0)=\lim x^{p-1}\sin\frac1x$ exists iff $p>1$ — smallest integer $p=2$ | **2** = (3) |
| **(R)** | $f=\max\{|x|,x^{2},x^{3}\}$ has corners where the winner changes: $x=-1,\,0,\,1$ | **3** = (4) |
| **(S)** | $f=\cos\pi x+ax\ (x<0)$, $b(1-x^{2})^{1/3}\ (x\ge0)$: continuity gives $b=1$, differentiability gives $a=0$; $a+b=1$ | **1** = (2) |

```desmos-graph
left=-2.2; right=2.2
bottom=-0.3; top=4.3
height=330
grid=true
---
y=\sqrt{x^2}|label:abs(x)
y=x^2|dashed|red|label:x^2
y=x^3|dashed|blue|label:x^3
(1,1)|point|label:the three corners
(0,0)|point
(-1,1)|point
```

> [!tip] Why $x=-1$ is a corner too
> Just left of $-1$, $|x|\approx1+\epsilon$ beats $x^{2}\approx1-2\epsilon$; just right of $0$
> $|x|$ beats $x^{2}$ again. A change of *winner* between two branches is a kink unless the
> slopes happen to agree — they do not here.

---

### Q11. Integral values of $x$: $\Big|1-\log_{1/6}x\Big|+|\log_{2}x|+2=\Big|3-\log_{1/6}x-\log_{2}x\Big|$

**Answer: 1.00**

Write $t=\log_{2}x$. Then $\log_{1/6}x=\dfrac{t\ln2}{-\ln6}=-\dfrac{t}{\log_26}=-\dfrac{t}{k}$
with $k=\log_26\approx2.585$. The equation becomes a one-variable relation:

$$\Big|1+\frac tk\Big|+|t|+2=\Big|3+\frac tk-t\Big|$$

```desmos-graph
left=-3; right=3
bottom=-1; top=14
height=340
grid=true
---
y=\sqrt{(1+x/2.585)^2}+\sqrt{x^2}+2|label:LHS
y=\sqrt{(3+x/2.585-x)^2}|label:RHS
(0,3)|label:equal at t=0 (x=1)
(-2.585,4.585)|open|label:equal at t=-k (x=1/6)
```

The two sides agree exactly at $t=0$ ($x=1$) and at $t=-k$ ($x=\tfrac16$). Of these only
$x=1$ is an integer. Hence **one** integral value — answer **1.00**.

> [!warning] Why not more
> Away from those two points the LHS grows like $2|t|$ while the RHS grows like
> $|1-\frac1k||t|\approx0.61|t|$; the difference is strictly increasing in $|t|$, so no other
> solution exists. The tempting $x=1/6$ is a solution but **not an integer**.

---

### Q12. $\sqrt{\Big\lfloor x+\big\lfloor \frac x2\big\rfloor\Big\rfloor}+\Big\lfloor\sqrt{\{x\}}+\big\lfloor\frac x3\big\rfloor\Big\rfloor=3$; solution set $[a,b)$, find $a+b$

**Answer: 7.00**

For an integer $m$ and a number $\theta\in[0,1)$, $\lfloor m+\theta\rfloor=m$. Hence

$$\Big\lfloor\sqrt{\{x\}}+\Big\lfloor\frac x3\Big\rfloor\Big\rfloor=\Big\lfloor\frac x3\Big\rfloor,
\qquad
\Big\lfloor x+\Big\lfloor\frac x2\Big\rfloor\Big\rfloor=\lfloor x\rfloor+\Big\lfloor\frac x2\Big\rfloor .$$

The equation becomes $\sqrt{\lfloor x\rfloor+\lfloor x/2\rfloor}=3-\lfloor x/3\rfloor$.
The right side must be a non-negative integer:

| $\lfloor x/3\rfloor$ | RHS | needs $\lfloor x\rfloor+\lfloor x/2\rfloor$ | satisfied by |
|---|---|---|---|
| 0 | 3 | 9 | $x<3$ gives at most $2+1=3$ — no |
| 1 | 2 | 4 | $x\in[3,4)$: $3+1=4$ ✓; $[4,5)$: $4+2=6$ ✗; $[5,6)$: $5+2=7$ ✗ |
| 2 | 1 | 1 | $x\ge6$ gives at least $6+3$ — no |

```math
# brute-force the same count over a few periods
x = 3.0
lhs = sqrt(floor(x + floor(x/2))) + floor(sqrt(x - floor(x)) + floor(x/3)) =>
x = 3.5
lhs2 = sqrt(floor(x + floor(x/2))) + floor(sqrt(x - floor(x)) + floor(x/3)) =>
a = 3
b = 4
a_plus_b = a + b =>
```

So the solution set is $[3,4)$: $a=3$, $b=4$, $a+b=\mathbf{7.00}$.

---

### Q13. $f(x)=\dfrac{1-\sin x}{(\pi-2x)^{2}}\cdot\dfrac{\log\sin x}{\log(1+\pi^{2}-4\pi x+4x^{2})}$, continuity at $x=\frac\pi2$ gives $f(\frac\pi2)=\frac{-1}{\lambda}$

**Answer: 64.00**

Put $u=\pi-2x\to0$. Then $x=\frac{\pi-u}{2}$,

$$1-\sin x=1-\cos\frac u2\approx\frac{u^{2}}{8},\qquad
\log\sin x=\log\cos\frac u2\approx-\frac{u^{2}}{8},$$

and $1+\pi^{2}-4\pi x+4x^{2}=1+u^{2}$, so $\log(1+u^{2})\approx u^{2}$. Hence

$$f\Big(\frac\pi2\Big)=\frac{\frac{u^{2}}{8}\cdot\left(-\frac{u^{2}}{8}\right)}{u^{2}\cdot u^{2}}
=-\frac{1}{64}=-\frac{1}{\lambda}\ \Longrightarrow\ \lambda=\mathbf{64.00}.$$

```math
# evaluate numerically as u -> 0
u = 0.0001
x = (pi - u)/2
f = (1 - sin(x))*log(sin(x))/((pi-2*x)^2 * log(1 + pi^2 - 4*pi*x + 4*x^2)) =>
minus_one_over_f = -1/f =>
```

---

### Q14. $y=\left(1+\frac1x\right)^{x}$; evaluate $\dfrac{2\sqrt{y_{2}(2)+\frac18}}{\log\frac32-\frac13}$

**Answer: 3.00**

With $A(x)=\ln\!\left(1+\frac1x\right)-\frac{1}{x+1}$ we have $y'=yA$ and $y''=y(A^{2}+A')$,
where $A'=-\frac{1}{x(x+1)}+\frac{1}{(x+1)^{2}}$.

At $x=2$: $y=\frac94$, $A=\ln\frac32-\frac13$, $A'=-\frac16+\frac19=-\frac1{18}$.

```math
# all the pieces at x = 2
y2 = (1 + 1/2)^2 =>
A = log(3/2) - 1/3 =>
Aprime = -1/(2*3) + 1/9 =>
y2doubleprime = y2*A^2 + y2*Aprime =>
plus_eighth = y2doubleprime + 1/8 =>
root = sqrt(plus_eighth) =>
numerator = 2*root =>
answer = numerator/A =>
```

Since $y''(2)=\frac94 A^{2}-\frac18$,

$$\sqrt{y''(2)+\tfrac18}=\tfrac32 A\ \Rightarrow\ \text{numerator}=3A
\ \Rightarrow\ \frac{3A}{A}=\mathbf{3.00}.$$

---

### Q15. $y=\dfrac{\sqrt{1+2x}\;\sqrt[4]{1+4x}\;\sqrt[6]{1+6x}\cdots\sqrt[100]{1+100x}}{\sqrt[3]{1+3x}\;\sqrt[5]{1+5x}\;\sqrt[7]{1+7x}\cdots\sqrt[101]{1+101x}}$; find $y'(0)$

**Answer: 0.00**

Take logs — each $k$-th root turns into $\frac1k\ln(1+kx)$:

$$\ln y=\sum_{\substack{k\ \text{even}\\k=2}}^{100}\frac{\ln(1+kx)}{k}
-\sum_{\substack{k\ \text{odd}\\k=3}}^{101}\frac{\ln(1+kx)}{k}$$

$$\frac{y'}{y}=\sum_{\text{even}}\frac{1}{1+kx}-\sum_{\text{odd}}\frac{1}{1+kx}
\ \xrightarrow[x\to0]{}\ \#_{\text{even}}-\#_{\text{odd}}=50-50=0$$

```math
# how many roots on each side?
evens = (100 - 2)/2 + 1 =>
odds = (101 - 3)/2 + 1 =>
log_derivative_at_0 = evens - odds =>
y0 = 1        # every factor is 1 at x = 0
y_prime_0 = y0*log_derivative_at_0 =>
```

$y(0)=1$ and $y'(0)=y(0)\times0=\mathbf{0.00}$.

> [!tip] The whole trick
> The numerator and denominator have the **same number** of factors whose
> $x$-derivatives at $0$ are exactly $1$ each. The sums cancel before any algebra.

---

### Q16. Two cubics with two common roots; $f$ continuous at $0$ gives $a+b$

**Answer: 20.00**

Let the common roots be $x_{1},x_{2}$ and the third roots $\alpha,\beta$:

$$x^{3}-5x^{2}+px+q=0:\quad x_{1}+x_{2}+\alpha=5$$
$$x^{3}-2x^{2}+(p-3)x+r=0:\quad x_{1}+x_{2}+\beta=2$$

Subtracting the equations leaves a **quadratic** whose roots are the common pair:
$-3x^{2}+3x+(q-r)=0$, i.e. $x_{1}+x_{2}=1$. Therefore

$$\alpha=4,\qquad \beta=1 .$$

The continuity pieces then give
$\;2^{\sin(\alpha x)/(\beta x)}\big|_{x\to0^-}=2^{\alpha/\beta}=2^{4}=16=a\;$ and
$\;b\cdot\dfrac{\ln\!\big(e^{x^{2}}+\alpha\beta\sqrt x\big)}{\tan\sqrt x}\to
b\cdot\alpha\beta=4b=16$… wait — see the check below.

```math
# third roots from the sum relations
x1_plus_x2 = 1
alpha = 5 - x1_plus_x2 =>
beta = 2 - x1_plus_x2 =>
# left piece: exponent sin(alpha x)/(beta x) -> alpha/beta
left_limit = 2^(alpha/beta) =>
a = left_limit =>
# right piece: ln(e^x2 + alpha*beta*sqrt(x))/tan(sqrt(x)) -> alpha*beta = 4
right_factor = alpha*beta =>
b = a/right_factor =>
a_plus_b = a + b =>
```

So $a=16$, $b=4$ and $\mathbf{a+b=20.00}$ — matching the key.

> [!warning] Typo in the printed paper
> The booklet's own solution prints "$\beta=2$" while also printing $x_{1}+x_{2}=1$ and
> "$\alpha=4$". The consistent set is $\alpha=4,\ \beta=1$; it is this pair that makes the
> quoted limits $16$ and $4$ and reproduces the keyed answer 20.

---

## PART 2: PHYSICS

---

### Q17. Standing/travelling wave $y=3\cos(4\pi t-2\pi x)+4\sin(4\pi t-2\pi x)$ mm — distance $PQ$ and acceleration of $Q$

**Answer: (A) $\dfrac{1}{2\pi}\tan^{-1}\!\left(\dfrac34\right)$ m, $-80\pi^{2}$ mm/s²**

```desmos-graph
left=0; right=1
bottom=-6; top=6
height=330
grid=true
---
y=3\cos(2\pi x)-4\sin(2\pi x)|label:y(x,0)
y=5\cos(2\pi x+0.6435)|dashed|red|label:y = 5cos(2pi x + phi)
(0.1013,4)|point|label:P
(0.0,3.98)|open|label:Q (nearest zero of sin)
```

Combine the two components into one sinusoid:
$3\cos\theta+4\sin\theta=5\cos(\theta-\phi)$ with $\tan\phi=4/3$. So

$$y=5\cos(4\pi t-2\pi x-\phi),\qquad v_y=-20\pi\sin(4\pi t-2\pi x-\phi) .$$

At $t=0$: $\cos(2\pi x+\phi)=\frac{4}{5}$ **and** $v_y>0$. Since
$v_y=+20\pi\sin(2\pi x+\phi)>0$ we need $\sin>0$, i.e.

$$2\pi x_P+\phi=\theta,\qquad \theta=\cos^{-1}\tfrac45=\tan^{-1}\tfrac34 .$$

$Q$ has zero transverse velocity $\Rightarrow\sin(2\pi x+\phi)=0$; the **nearest such point to
the left** is $2\pi x_Q+\phi=0$, so

$$PQ=\frac{\theta}{2\pi}=\frac{1}{2\pi}\tan^{-1}\frac34 .$$

Its acceleration is $a_y=-80\pi^{2}\cos(2\pi x+\phi)\big|_{Q}=-80\pi^{2}\cos 0=\mathbf{-80\pi^{2}}$ mm/s².

```math
# the key numbers
theta = atan(3/4) to deg =>
distance = theta_deg/360          # fraction of a wavelength
amp = sqrt(3^2 + 4^2) =>
acc_q = -amp*(4*pi)^2 * cos(0) =>
check = 5*cos(2*pi*0.1013 + 0.6435) =>   # y at P
```

---

### Q18. Two sound sources + a third one; sound level of $S_3$ alone

**Answer: (C) 83 dB**

$S_2$ has $4\times$ the power of $S_1$ but sits at twice the distance, so its intensity at $P$
is $\dfrac{4P_1}{4\pi(2r)^{2}}=\dfrac{P_1}{4\pi r^{2}}$ — **identical** to $S_1$'s, i.e.
$80$ dB as well.

They are incoherent, so intensities add: $2I\Rightarrow 80+3=83$ dB.

Switching on $S_3$ raises the total by another $3$ dB: $4I$ — which means $I_3=2I$, i.e.

$$L_3=10\log\frac{2I}{I_0}=83\ \text{dB}$$

```math
# decibel bookkeeping (relative to I0 = 1)
I1 = 1
L1 = 10*log(10, I1/1) =>
I2 = I1                # 4x power at 2x distance cancels exactly
L12 = 10*log(10, (I1+I2)/1) =>
Ltotal = L12 + 3 =>
I3 = I1                # solutions: total 4I needs I3 = 2I? check below
L3 = 10*log(10, 2/1) + 80 =>
total_check = 10*log(10, 4/1) + 80 =>
```

> [!warning] Trap
> "$4\times$ power at twice the distance" is exactly a wash — many students keep the factor
> 4 and get 86 dB for the pair, then 83 dB for $S_3$ by accident. Do the division first.

---

### Q19. Standing EM wave; energy densities equal at $t=\frac{\pi}{6\omega}$, Poynting along $-x$

**Answer: (A) $\dfrac{\pi}{6}$**

For $\vec E=2E_0\sin(kx)\cos(\omega t)\,\hat y$ the companion magnetic field of a standing wave is
$\vec B=\dfrac{2E_0}{c}\cos(kx)\sin(\omega t)\,\hat z$ (sign fixed below by the Poynting vector).

```desmos-graph
left=0; right=1.6
bottom=-0.4; top=1.05
height=320
grid=true
---
y=\sin(x)^2*\cos(pi/6)^2|label:uE (in units)
y=\cos(x)^2*\sin(pi/6)^2|dashed|red|label:uB (in units)
(0.5236,0.5625)|open|label:kx = pi/6 (both = 0.5625)
```

Equality of energy densities:
$\tfrac12\epsilon_0(2E_0)^{2}\sin^{2}(kx)\cos^{2}(\omega t)
=\tfrac{1}{2\mu_0}\frac{4E_0^{2}}{c^{2}}\cos^{2}(kx)\sin^{2}(\omega t)$, and
$1/(\mu_0c^{2})=\epsilon_0$, so

$$\sin^{2}(kx)\cos^{2}(\omega t)=\cos^{2}(kx)\sin^{2}(\omega t)
\ \Longrightarrow\ \tan^{2}(kx)=\tan^{2}(\omega t) .$$

At $\omega t=\pi/6$: $\tan(\omega t)=1/\sqrt3$, so $kx=\pi/6$ (the root inside $0<kx<\pi/2$).

**Direction check:** $\vec S=\vec E\times\vec B/\mu_0\propto
\hat y\times\hat z=+\hat x$; for $\vec S$ along $-\vec x$ we need $B$ along $-\hat z$, which is
consistent with $\sin(\omega t)>0$ at that instant ✓.

```math
# both sides at the instant given
omega_t = 30 deg
tan2_wt = (tan(omega_t))^2 =>
kx = atan(sqrt(tan2_wt)) to deg =>
uE = sin(kx)^2*cos(omega_t)^2 =>
uB = cos(kx)^2*sin(omega_t)^2 =>
equal = uE - uB =>
```

---

### Q20. Diffraction-limited telescope: two LEDs 2.0 cm apart, objective 5.0 cm, $\lambda=550$ nm

**Answer: (B) 1.49 km**

```tikz
\begin{document}
\begin{tikzpicture}[line width=0.9pt, scale=1.0]
% telescope aperture and the two LEDs at distance L
\draw[very thick] (0,-1.0) -- (0,1.0);
\node at (0,-1.35) [below, font=\small]{objective, $D=5.0$ cm};
\foreach \y in {-0.3,0.3} { \draw[->, >=stealth, blue] (0,\y) -- (2.6,\y*3.2); }
\draw[fill, red] (5.5,0.96) circle (2.6pt);
\draw[fill, red] (5.5,-0.96) circle (2.6pt);
\node at (5.6,0.96) [right, font=\small]{LED};
\node at (5.6,-0.96) [right, font=\small]{LED};
\draw[<->, >=stealth] (5.15,0.96) -- (5.15,-0.96);
\node at (5.0,0) [left, font=\small]{$2.0$ cm};
\draw[<->, >=stealth] (0,-1.7) -- (5.5,-1.7);
\node at (2.7,-1.9) [below, font=\small]{$L$ (just resolved)};
\node at (0.6,1.3) [right, font=\small]{$\theta_{\min}=1.22\lambda/D$};
\end{tikzpicture}
\end{document}
```

Rayleigh's criterion: two objects are just resolved when their angular separation is

$$\theta_{\min}=1.22\frac{\lambda}{D}=1.22\frac{550\times10^{-9}}{5.0\times10^{-2}}
=1.342\times10^{-5}\ \text{rad}.$$

```math
# angular resolution and the maximum resolvable distance
lamb = 550 nm
D = 5.0 cm
theta = 1.22*lamb/D =>
s = 2.0 cm
L = s/theta to km =>
```

The separation is $2.0$ cm, so $L=\dfrac{2.0\times10^{-2}}{1.342\times10^{-5}}
\approx1.49\times10^{3}$ m = **1.49 km** — option **(B)**.

---

### Q21. Sonometer wire — which changes keep the stated frequency?

**Answer: (A, B, C, D)** — all four

With $f_n=\dfrac{n}{2L}\sqrt{\dfrac{T}{\mu}}$:

| | New value | Check |
|---|---|---|
| **(A)** | $f_1'=\dfrac{1}{2(3L/2)}\sqrt{\dfrac{9T}{\mu}}=\dfrac{1}{3L}\cdot\dfrac{3v}{1}=2f$ | ✅ |
| **(B)** | fundamental $=\dfrac{2}{3}\cdot\dfrac{2v}{1}=\dfrac{4f}{3}$; second harmonic $=\dfrac{8f}{3}$ | ✅ |
| **(C)** | radius $\times2$ ⟹ $\mu\times4$ ⟹ $f\to f/2$; third harmonic $=\dfrac{3f}{2}$ | ✅ |
| **(D)** | $f_1'=\dfrac{1}{2(2L)}\cdot2v=f$; second harmonic $=2f$ | ✅ |

```math
# verify each claim with a normalised wire: L = 1, T = 1, mu = 1
v = 1
f1 = v/(2*1) =>
A = (1/(2*1.5))*sqrt(9)/1 =>
A_expected = 2*f1 =>
B = 2*(1/(2*1.5))*sqrt(4)/1 =>
B_expected = 8*f1/3 =>
C = 3*(1/(2*1))*sqrt(1)/2 =>
C_expected = 3*f1/2 =>
D = 2*(1/(2*2))*sqrt(4)/1 =>
D_expected = 2*f1 =>
```

---

### Q22. Thin film $\mu=\frac43$, $t=450$ nm on glass $n_g=\frac32$

**Answer: (A, B, C)**

Both reflections are "denser → rarer" reflections, so both carry a $\pi$ shift and the phase
difference comes purely from the path:

$$\Delta=2\mu t=2\cdot\tfrac43\cdot450=1200\ \text{nm}$$

```math
# phase bookkeeping
mu = 4/3
t = 450 nm
opd = 2*mu*t =>
lambda1 = 600 nm
order1 = opd/lambda1 =>
lambda2 = 480 nm
order2 = opd/lambda2 =>
# thickness change to turn a maximum into a minimum
dt = lambda1/(4*mu) =>
# with ng = 1.20 the lower reflection loses its pi shift
opd_needed = (2 + 0.5)*600 nm =>
mismatch = opd_needed - opd =>
```

- **(A)** $\Delta/\lambda_1=1200/600=2$ — **integer** ⟹ constructive ✅
- **(B)** $\Delta/\lambda_2=1200/480=2.5$ — **half-integer** ⟹ destructive ✅
- **(C)** to go from maximum to minimum we need an extra $\lambda/2$ of path:
  $\Delta t=\dfrac{\lambda}{4\mu}=\dfrac{600}{4\times 4/3}=112.5$ nm ✅
- **(D)** with $n_g=1.20<\mu$ the lower reflection has **no** $\pi$ shift, so the two shifts
  no longer cancel and the condition flips to $\Delta=(m+\tfrac12)\lambda$; $1200/600=2$ is an
  integer, so the maximum turns into a **minimum** ⟹ (D) ❌

---

### Q23. Two strings joined at $x=0$ with $\mu_2=4\mu_1$

**Answer: (B)**

$Z=\sqrt{T\mu}$, so $Z_2=2Z_1$ and

$$r=\frac{Z_1-Z_2}{Z_1+Z_2}=-\frac13,\qquad t=\frac{2Z_1}{Z_1+Z_2}=\frac23 .$$

Hence the reflected amplitude is $6\times\frac13=2$ mm **with a phase reversal** and the
transmitted amplitude is $6\times\frac23=4$ mm.

Wave numbers: $v_1=\omega/k_1=40/8=5$ m/s, $v_2=v_1/2=2.5$ m/s, so
$k_2=40/2.5=16$ — twice $k_1$, i.e. **half the wavelength** ✓.

```tikz
\begin{document}
\begin{tikzpicture}[line width=0.9pt, scale=1.0]
% heavy string on the left, light string on the right
\draw[line width=2.4pt, gray] (-5,0) -- (0,0);
\draw[line width=1.2pt, gray] (0,0) -- (5,0);
\node at (-2.6,-0.5) [below, font=\small]{string 1: $\mu_1$};
\node at (2.6,-0.5) [below, font=\small]{string 2: $\mu_2=4\mu_1$};
\draw[dashed] (0,-1.2) -- (0,1.2);
\node at (0,1.35) [above, font=\small]{junction $x=0$};
% incident and reflected on the left; transmitted (shorter wavelength) on the right
\draw[->, very thick, blue] (-4.6,0.75) -- (-2.2,0.75);
\node at (-3.4,0.95) [above, font=\small]{$y_i=6\cos(40t-8x+\pi/6)$};
\draw[<-, very thick, red] (-4.6,-0.75) -- (-2.2,-0.75);
\node at (-3.4,-1.0) [below, font=\small]{$y_r=2\cos(40t+8x+\pi/6+\pi)$};
\draw[->, very thick, purple] (1.0,0.75) -- (4.2,0.75);
\node at (2.6,0.95) [above, font=\small]{$y_t=4\cos(40t-16x+\pi/6)$};
\node at (2.6,-1.0) [below, font=\small]{amplitude $4$ mm, $\lambda$ halved};
\end{tikzpicture}
\end{document}
```

- **(A)** ❌ the printed form omits the extra $\pi$ of the phase reversal (the statement of
  reversal itself is right, the formula is not);
- **(B)** ✅ amplitude 4 mm, $k$ doubled;
- **(C)** ❌ $y(0,t)=6\cos\left(40t+\frac\pi6\right)-2\cos\left(40t+\frac\pi6\right)
  =4\cos\left(40t+\frac\pi6\right)$ is right, but the maximum speed is
  $4\times40=160$ mm/s, not 40;
- **(D)** ❌ the reflected power fraction is $r^{2}=\frac19$, not $\frac13$.

---

### Q24. Match four two-beam interference arrangements with their fringe widths

**Answer: (A) P→4; Q→2; R→3; S→1**

$$P:\ d=2aA(\mu-1)=2(0.25)(10^{-3})(0.5)=2.5\times10^{-4}\ \text{m},\ D=1.0\ \text{m}$$
$$Q:\ d=2h=4\times10^{-4}\ \text{m},\ D=0.8\ \text{m}$$
$$R:\ d\approx2a\theta=2(0.30)(0.75\times10^{-3})=4.5\times10^{-4}\ \text{m},\ D=0.30+0.90=1.20\ \text{m}$$
$$S:\ d=2\times0.10\times3=0.60\ \text{mm}\ (\text{image separation}),\ D=0.80\ \text{m}$$

```math
# beta = lambda D / d for each arrangement
lamb = 600 nm
betaP = lamb*1.0/(2.5e-4) to mm =>
betaQ = lamb*0.8/(4e-4) to mm =>
betaR = lamb*1.2/(4.5e-4) to mm =>
betaS = lamb*0.8/(6e-4) to mm =>
```

$\beta_P=2.40$ mm → (4); $\beta_Q=1.20$ mm → (2); $\beta_R=1.60$ mm → (3);
$\beta_S=0.80$ mm → (1). Answer **(A)**.

> [!note] Why $D=1.20$ m for the Fresnel mirrors
> The two virtual images sit *behind* the mirrors, about as far from the intersection as the
> source is in front of it. So image → screen distance is $0.30+0.90=1.20$ m, not $0.90$ m.

---

### Q25. Match each magnetic-field pair with its polarisation

**Answer: (A) P→1; Q→2; R→3; S→4,5**

```tikz
\begin{document}
\begin{tikzpicture}[line width=0.9pt, scale=1.0]
% Lissajous figures for the four cases, drawn as phasor pairs
\begin{scope}[shift={(0,0)}]
  \draw[->] (-0.2,0) -- (2.4,0); \draw[->] (0,-1.2) -- (0,1.2);
  \draw[thick, blue] (1.1,0) circle (0.9);
  \node at (1.1,-1.5) [below, font=\small]{(P) circle: circular};
\end{scope}
\begin{scope}[shift={(3.4,0)}]
  \draw[->] (-0.2,0) -- (2.4,0); \draw[->] (0,-1.2) -- (0,1.2);
  \draw[thick, red] (1.1,0) ellipse [x radius=0.7, y radius=1.1];
  \node at (1.1,-1.5) [below, font=\small]{(Q) axes along $x,y$};
\end{scope}
\begin{scope}[shift={(6.8,0)}]
  \draw[->] (-0.2,0) -- (2.4,0); \draw[->] (0,-1.2) -- (0,1.2);
  \draw[thick, purple, rotate=45] (1.1,0) ellipse [x radius=0.85, y radius=0.6];
  \node at (1.1,-1.5) [below, font=\small]{(R) axes at $45°$};
\end{scope}
\end{tikzpicture}
\end{document}
```

With $\vec B=(B_x,B_y)$:

| | Data | Reading |
|---|---|---|
| **(P)** | $B_x=-B_0\sin\omega t,\ B_y=B_0\cos\omega t$ | equal amplitudes, $\pi/2$ apart ⟹ **circle** (1) |
| **(Q)** | $B_x=-B_0\sin\omega t,\ B_y=2B_0\cos\omega t$ | in quadrature, unequal ⟹ ellipse with **axes along $x,y$** (2) |
| **(R)** | $B_x=-B_0\cos(\omega t+\pi/3),\ B_y=B_0\cos\omega t$ | equal amplitudes, $60°$ apart ⟹ ellipse with **axes at $45°$** (3) |
| **(S)** | $B_x=-B_0\cos(\omega t+\pi/3),\ B_y=\sqrt3B_0\cos\omega t$ | $\tan 2\theta=\dfrac{2(1)(\sqrt3)\cos60°}{1-3}=\dfrac{\sqrt3}{-2}$… see below → (4) and (5) |

```math
# (S): major-axis direction and axial ratio
ax = 1
ay = sqrt(3)
delta = 60 deg
num = 2*ax*ay*cos(delta) =>
den = ax^2 - ay^2 =>
tan2theta = num/den =>
minor = 0.5*(ax^2+ay^2 - sqrt((ax^2-ay^2)^2 + 4*ax^2*ay^2*cos(delta)^2)) =>
major = 0.5*(ax^2+ay^2 + sqrt((ax^2-ay^2)^2 + 4*ax^2*ay^2*cos(delta)^2)) =>
axial_ratio_sq = major/minor =>
# the option quotes sqrt((4+sqrt7)/(4-sqrt7)) = 2.44
option_value = sqrt((4+sqrt(7))/(4-sqrt(7))) =>
```

The principal axes of (S) are *not* along $x,y$, so it matches both (4) (axis direction) and
(5) (axial ratio) — answer **(A)**.

---

### Q26. Match the Doppler situations with the wavelength reaching the observer

**Answer: (A) P→2; Q→3; R→4; S→2**

$f_0=680$ Hz, $v=340$ m/s.

| | Working | $\lambda$ reaching the observer |
|---|---|---|
| **(P)** | $f'=f\dfrac{v}{v-v_s}=680\dfrac{340}{272}=850$ Hz, $\lambda'=v/f'=0.400$ m | (2) |
| **(Q)** | source still: the **wavelength in air** stays $v/f_0=0.500$ m; the observer merely sweeps more of it | (3) |
| **(R)** | $f'=680\dfrac{340}{425}=544$ Hz, $\lambda'=0.625$ m | (4) |
| **(S)** | source 68 m/s toward, observer 34 m/s away: $f'=680\dfrac{340-34}{340-68}=765$ Hz, $\lambda'=\dfrac{340-34}{765}=0.400$ m | (2) |

```math
# the four wavelengths
f0 = 680 Hz
v = 340 m/s
lambdaP = v/(f0*v/(v-68 m/s)) to m =>
lambdaQ = v/f0 to m =>
lambdaR = v/(f0*v/(v+85 m/s)) to m =>
lambdaS = (v-34 m/s)/(f0*(v-34 m/s)/(v-68 m/s)) to m =>
```

---

## PART 2: PHYSICS — SECTION II (Numerical)

---

### Q27. Kundt's tube: rod clamped at its midpoint, third allowed mode

**Answer: 220.44**

```desmos-graph
left=0; right=1.5
bottom=-1.2; top=1.2
height=270
---
y=\sin(5*pi*x/1.5)|label:third allowed mode (n=5)
(0.75,0)|point|label:clamp (node)
```

A rod clamped at its centre has nodes there; the allowed modes are $n=1,3,5,\dots$ with
$\lambda_{\text{rod}}=2L/n$. "Third allowed" means $n=5$:

$$f=\frac{c}{2L/5}=\frac{5c}{2L},\qquad
\lambda_{\text{gas}}=\frac{v_{\text{gas}}}{f}=\frac{2L\,v_{\text{gas}}}{5c}.$$

Initially $\lambda_{\text{gas}}/2=2.00$ cm. After heating the gas 10 % faster and stretching the
rod 0.20 % (its wave speed unchanged, same mode):

$$f'=\frac{f}{1.002},\qquad \lambda'_{\text{gas}}=1.10\,\lambda_{\text{gas}}\cdot1.002 .$$

```math
# dust-heap separation = lambda_gas/2
sep = 2.00 cm
speed_factor = 1.10
length_factor = 1.002
new_sep = sep*speed_factor*length_factor =>
hundred_x = new_sep to cm =>     # this is already in cm, factor 100 applied below
answer = sep*speed_factor*length_factor*100/1 =>   # in units of 0.01 cm
check = 2.00*1.10*1.002*100 =>
```

$$x=2.00\times1.10\times1.002=2.2044\ \text{cm},\qquad \mathbf{100x=220.44}.$$

---

### Q28. Newton's rings with a trapped dust particle, air then liquid

**Answer: 18.00**

With a central film thickness $t_0$, the $n$-th dark ring satisfies
$2(t_0+e)=n\lambda$ in air and $2\mu(t_0+e')=n\lambda$ in liquid, so

$$r^{2}=n\lambda R-2Rt_0,\qquad r'^{2}=\frac{n\lambda R}{\mu}-2Rt_0 .$$

```math
# dark-ring radii with a central air-gap offset t0
R = 1.20 m
lamb = 600 nm
n = 14
r = 4.80 mm/2 =>
n_lambda_R = n*lamb*R =>
two_R_t0 = n_lambda_R - r^2 =>
t0 = two_R_t0/(2*R) =>
mu = 4/3
r_prime = 3.60 mm/2 =>
two_R_t0_check = n*lamb*R/mu - r_prime^2 =>
t0_check = two_R_t0_check/(2*R) =>
x = t0*1e7 =>
```

Both rings give the same $t_0\approx1.8\times10^{-6}$ m, so $t_0=18\times10^{-7}$ m and
$\mathbf{x=18.00}$.

---

### Q29. Compound microscope: limit of resolution with an immersion liquid

**Answer: 407.40**

$$M=m_o M_e,\quad M_e=\frac{D}{f_e}=\frac{25}{6},\quad m_o=\frac{90}{25/6}=21.6,
\quad f_o=\frac{L}{m_o}=\frac{18}{21.6}=0.833\ \text{cm}$$

$$\alpha_{\text{eff}}=0.8\times0.60=0.48\ \text{cm},\qquad
\sin\theta=\frac{\alpha_{\text{eff}}}{\sqrt{\alpha_{\text{eff}}^{2}+f_o^{2}}}
=\frac{0.48}{\sqrt{0.2304+0.6944}}=0.4991$$

```math
# from M = mo * Me to the numerical aperture and d_min
L = 18 cm
fe = 6 cm
Dvision = 25 cm
M = 90
Me = Dvision/fe =>
fo = L/(M/Me) =>
alpha = 0.8*0.60 cm =>
sintheta = alpha/sqrt(alpha^2 + fo^2) =>
mu = 1.50
lamb = 500 nm
dmin = 1.22*lamb/(2*mu*sintheta) to nm =>
```

$$d_{\min}=\frac{1.22\lambda}{2n\sin\theta}=407.4\ \text{nm}\ \Rightarrow\ \mathbf{x=407.40}$$

---

### Q30. Two coherent sound sources, unequal powers, complete destructive interference

**Answer: N = 2**

```tikz
\begin{document}
\begin{tikzpicture}[line width=0.9pt, scale=1.0]
% two sources 3 m apart, point P above the line with the projection marked
\draw[ultra thick] (0,0) -- (6,0);
\draw[fill, blue] (0,0) circle (3.2pt); \node at (0,0) [below left, font=\small]{$S_1$};
\draw[fill, blue] (6,0) circle (3.2pt); \node at (6,0) [below right, font=\small]{$S_2$};
\node at (3,-0.55) [below, font=\small]{$3.0$ m};
\coordinate (P) at (2.2,2.6);
\draw[fill, red] (P) circle (3.2pt); \node at (P) [above, font=\small]{$P$};
\draw[thick] (0,0) -- (P); \node at (1.0,1.45) [left, font=\small]{$r_1$};
\draw[thick] (6,0) -- (P); \node at (4.3,1.6) [right, font=\small]{$r_2$};
\draw[dashed] (P) -- (2.2,0); \node at (2.35,1.3) [right, font=\small]{$h$};
\draw[<->, >=stealth] (0,-1.0) -- (2.2,-1.0); \node at (1.1,-1.2) [below, font=\small]{$x$};
\node at (4.6,-1.2) [below, font=\small]{$r_1<2$ m and $r_2=2r_1$};
\end{tikzpicture}
\end{document}
```

**Amplitudes must be equal for *complete* cancellation.** Since amplitude
$\propto\sqrt{P}/r$: $\dfrac{\sqrt{P_1}}{r_1}=\dfrac{\sqrt{4P_1}}{r_2}\Rightarrow r_2=2r_1$.

**Phases.** $S_2$ leads by $\pi/3$; the phase difference at $P$ is
$\Delta=\dfrac{\pi}{3}+\dfrac{2\pi}{\lambda}(r_1-r_2)$. Destructive means $\Delta=(2m+1)\pi$:

$$\frac{\pi}{3}-2\pi r_1=(2m+1)\pi\ \Rightarrow\ r_1=-m-\frac13
\ \Rightarrow\ r_1=\frac53\ \text{m}\ (\text{or } \frac23\ \text{m}).$$

The geometry $r_1^{2}=x^{2}+h^{2}$, $r_2^{2}=(3-x)^{2}+h^{2}$ with $r_2=2r_1$ gives
$9-6x=3r_1^{2}$, i.e. $x=\dfrac{3-r_1^{2}}{2}$.

```math
# amplitudes equal -> r2 = 2 r1 ; destructive -> r1 = 5/3 or 2/3
r1 = 5/3 m
x1 = (3 - r1^2)/2 to m =>
N1 = x1*18 =>
r2_inner = 2/3 m
x2 = (3 - r2_inner^2)/2 to m =>
N2 = x2*18 =>
# check r1 < 2 m and the phase condition
phase_diff = (pi/3) + 2*pi*(r1 - 2*r1) =>
phase_over_pi = phase_diff/pi =>
```

$r_1=\frac53$ m (which is $<2$) gives $x=\frac{1}{9}$ m $=\frac{2}{18}$ m ⟹ $\mathbf{N=2}$.

---

### Q31. Two waves of intensities $9I_0$ and $4I_0$ — beat frequency from the intensity record

**Answer: N = 8**

$$I=I_1+I_2+2\sqrt{I_1I_2}\cos\delta=13I_0+12I_0\cos\delta,\qquad \delta=\Delta\omega\,t+\delta_0$$

```desmos-graph
left=0; right=2
bottom=0; top=26
height=330
grid=true
---
y=13+12\cos(4\pi x+4.18879)|label:I(t)/I0
y=19|dashed|red|label:I = 19I0
y=7|dashed|green|label:I = 7I0 at t = 0, rising
(0,7)|point|label:endpoints are not 19
(2,7)|point
```

- $t=0$: $13+12\cos\delta_0=7\Rightarrow\cos\delta_0=-\tfrac12$, and the intensity is **rising**
  ⟹ $\sin\delta_0<0$ ⟹ $\delta_0=4\pi/3$.
- $I=19I_0$ needs $\cos\delta=+\tfrac12$, i.e. $\delta=\pm\tfrac{\pi}{3}+2k\pi$ — **twice per
  beat period**.
- Eight hits happen in $2.0$ s, and neither endpoint is a hit, so the phase must advance by
  exactly $4$ full beat cycles in $2$ s:

$$\Delta\omega\times2.0=4\times2\pi\ \Rightarrow\ f_b=\frac{2}{1}=2\ \text{Hz}
=\frac{N}{4}\ \Rightarrow\ \mathbf{N=8}.$$

```math
# counts per beat period and the phase advance
hits_per_period = 2
hits = 8
periods = hits/hits_per_period =>
fb = periods/2.0 Hz =>
N = fb*4 =>
delta0 = 4*pi/3 =>
I_at_0 = 13 + 12*cos(delta0) =>
I_at_2 = 13 + 12*cos(delta0 + 2*pi*fb*2.0) =>
```

---

### Q32. Radiation force on a plate (reflection 72 %, absorption 18 %, transmission 10 %)

**Answer: 64.69 nN**

```tikz
\begin{document}
\begin{tikzpicture}[line width=0.9pt, scale=1.0]
% plate at 37 degrees with the three outgoing beams
\draw[very thick] (-2.6,-1.6) -- (2.6,1.6);
\node at (2.75,1.7) [right, font=\small]{plate};
\draw[->, very thick, red] (-3.6,1.0) -- (0,0);
\node at (-3.5,1.2) [above, font=\small]{$P=15$ W, $37°$ to normal};
\draw[<-, very thick, orange] (0,0) -- (2.4,0.62);
\node at (2.5,0.85) [right, font=\small]{reflected $0.72P$ (specular)};
\draw[<-, very thick, purple] (0,0) -- (3.3,-1.9);
\node at (2.0,-1.6) [below, font=\small]{transmitted $0.10P$};
\node at (0.55,-0.5) [font=\small]{absorbed $0.18P$};
\draw[dashed] (0,-0.9) -- (0,0.9);
\node at (0.1,0.95) [above, font=\small]{normal};
\end{tikzpicture}
\end{document}
```

The momentum flux normal to the plate is $\dfrac{P\cos\theta}{c}$:

- incident beam delivers it **in**, reflected beam returns it **out**: factor $(1+R)$;
- transmitted beam carries it **away** through the plate: subtract $T$;
- the absorbed $18\%$ simply stops, contributing $\times1$.

$$F_\perp=\frac{P\cos\theta}{c}\big[(1+0.72)-0.10\big]=\frac{P\cos\theta}{c}(1.62)$$

```math
# normal force from momentum flux
P = 15 W
c = 3e8 m/s
theta = 37 deg
R = 0.72
T = 0.10
A = 0.18
factor = (1 + R) - T =>
F = P*cos(theta)/c*factor =>
F_nN = F*1e9 =>
```

$$F=\frac{15\times0.7986}{3\times10^{8}}\times1.62=6.469\times10^{-8}\ \text{N}
=\mathbf{64.69\ nN}$$

> [!tip] The three momentum books
> Reflected light hands the surface $2\cos\theta$ of momentum per unit path-length factor;
> transmitted light takes its momentum with it; absorbed light leaves all of it behind. Written
> as fluxes, that is the single bracket $(1+R)-T$ above.

---

## PART 3: CHEMISTRY

---

### Q33. Sparingly soluble salt — identify the correct statement

**Answer: (A)**

```tikz
\begin{document}
\begin{tikzpicture}[line width=0.9pt, scale=1.0]
% dissolution equilibrium with a complexing agent removing the cation
\node at (-3.4,0.9) [font=\small]{solid salt};
\draw[very thick] (-3.4,0.4) -- (-2.4,0.4);
\draw[->, >=stealth, thick] (-2.2,0.4) -- (-0.6,0.4);
\node at (-1.4,0.65) [above, font=\small]{dissolve};
\node at (0.1,0.4) [font=\small]{$M^{+}$};
\node at (1.5,0.4) [font=\small]{$+$};
\node at (2.6,0.4) [font=\small]{$X^{-}$};
% complexation pulls the cation out of the equilibrium
\draw[->, >=stealth, thick, red] (0.35,0.75) -- (1.4,1.5);
\node at (2.2,1.6) [right, font=\small]{$+$ ligand $\rightarrow [ML_n]^{+}$ (removed)};
\node at (0.4,-0.35) [font=\small]{Le Chatelier: removing $M^{+}$ drives dissolution $\rightarrow$ solubility $\uparrow$};
% the things that do NOT matter
\draw[thick, gray] (-4.0,-1.1) -- (4.4,-1.1);
\node at (0.2,-1.36) [font=\small]{$K_{sp}$ changes \emph{only} with temperature; common-ion shifts it, never changes it};
\end{tikzpicture}
\end{document}
```

| Statement | Verdict |
|---|---|
| **(A)** complexation of an ion increases solubility | ✅ (it removes free $M^{+}$, pulling the equilibrium right) |
| **(B)** hydrolysis decreases solubility | ❌ hydrolysis removes the ion too, so it *increases* solubility |
| **(C)** solubility decreases on dilution | ❌ dilution dissolves *more* total salt |
| **(D)** $K_{sp}$ decreases by the common-ion effect | ❌ $K_{sp}$ is a function of temperature only |

---

### Q34. Which statement about corrosion is **incorrect**?

**Answer: (B)**

- **(A)** ✅ dissolved $\text{CO}_2$ makes $\text{H}_2\text{CO}_3$, and the $\text{H}^{+}$ it
  supplies promotes the cathodic reduction $\text{O}_2+4\text{H}^{+}+4e^{-}\to2\text{H}_2\text{O}$;
- **(B)** ❌ **alkaline media suppress rusting** — $\text{OH}^{-}$ neutralises the $\text{H}^{+}$
  the cathodic reaction needs. (This is exactly why rusty metal is kept dry and why
  sacrificial zinc, which makes a basic surface film, protects iron.)
- **(C)** ✅ for $\text{Pt,H}_2(P_1)|\text{H}^{+}(C_1)\|\text{H}^{+}(C_2)|\text{H}_2(P_1),\text{Pt}$,
  $E=\dfrac{0.059}{1}\log\dfrac{C_2}{C_1}>0$ when $C_2>C_1$;
- **(D)** ✅ chrome/nickel electroplating keeps the metal away from $\text{O}_2$ and moisture.

```math
# the hydrogen-concentration cell that statement (C) refers to
C1 = 0.01 M
C2 = 0.10 M
E = 0.059*log(10, C2/C1) =>
E_reverse = 0.059*log(10, C1/C2) =>
```

---

### Q35. Which statement about electrochemical cells is **incorrect**?

**Answer: (A)**

In a Leclanché (dry) cell the cathode reaction is
$\text{MnO}_2+\text{NH}_4^{+}+e^{-}\to\text{MnO(OH)}+\text{NH}_3$ — the booklet prints it as
happening *at the anode*, which is wrong: zinc is oxidised at the anode.

| | Statement | Verdict |
|---|---|---|
| **(A)** | $\text{MnO}_2$ reduction "occurs at the anode" | ❌ it is the **cathode** reaction |
| **(B)** | mercury cell is concentration-independent | ✅ no ion concentration changes ⟹ flat voltage |
| **(C)** | Ni–Cd outlives lead-acid in cycles | ✅ |
| **(D)** | $\text{Zn}\to\text{Zn}^{2+}+2e^{-}$ at the anode of a Leclanché cell | ✅ |

---

### Q36. Two dissociation equilibria sharing the gas $Z$ — select the **incorrect** statement

**Answer: (D)**

$$\underbrace{X(s)\rightleftharpoons Y(g)+2Z(g)}_{K_{p1}},\qquad
\underbrace{V(s)\rightleftharpoons W(g)+2Z(g)}_{K_{p2}}$$

**Experiment 1.** $P_Y=p_1,\ P_Z=2p_1$ and $P_{\text{tot}}=3p_1$, so
$K_{p1}=p_1(2p_1)^{2}=4p_1^{3}$.

**Experiment 2.** $P_{\text{tot}}=6p_1=3p_2\Rightarrow p_2=2p_1$, so
$K_{p2}=4p_2^{3}=32p_1^{3}=8K_{p1}$ ⟹ **(A) is true**.

**Together.** With both solids present, $P_Z=2p_x+2p_v$ and

$$K_{p1}=4p_x(p_x+p_v)^{2},\qquad K_{p2}=4p_v(p_x+p_v)^{2}
\ \Longrightarrow\ \frac{p_v}{p_x}=8 .$$

```math
# the shared partial pressure of Z ties the two equilibria together
p1 = 1
Kp1 = 4*p1^3 =>
Kp2 = 4*(2*p1)^3 =>
ratio_Kp = Kp2/Kp1 =>
# with both solids present, pv = 8 px
px = 1
pv = 8*px =>
Kp1_check = 4*px*(px+pv)^2 =>
Kp2_check = 4*pv*(px+pv)^2 =>
ratio_check = Kp2_check/Kp1_check =>
# the ratio the option quotes
PW_to_PZ = pv/(2*(px+pv)) =>
PW_to_PZ_as_fraction = 8/18 =>
```

- **(B)** is true (the division above gives $P_W/P_Y=8$);
- **(C)** is true — $P_Y$ depends only on $K_{p1}$ and $P_Z$, and $K_{p1}$ is fixed;
- **(D)** claims $P_W:P_Z=3:8$, whereas the same algebra gives
  $8p_x:2(9p_x)=4:9$ ⟹ **(D) is the incorrect statement**.

---

### Q37. $\text{Na}_2\text{CO}_3+\text{NaHCO}_3$ mixture titrated with HCl (two indicators)

**Answer: (A, B, C)**

**Phenolphthalein** stops at $\text{CO}_3^{2-}\to\text{HCO}_3^{-}$, so

$$\#\text{mol Na}_2\text{CO}_3=\#\text{mol HCl}=1.0\times0.0150=0.0150
\Rightarrow m=0.0150\times106=\mathbf{1.59\ g}\ \text{(A ✓)}$$

$m_{\text{NaHCO}_3}=2.00-1.59=0.41$ g $\Rightarrow20.5\%$ **(B ✓)** and
$0.41/84=4.9\times10^{-3}$ mol — so **(D) ✗** (it claims $8\times10^{-3}$).

**Methyl orange** completes both: $V=\underbrace{2(15.0)}_{\text{carbonate}}
+\underbrace{\dfrac{4.9\times10^{-3}}{1.0}\times10^{3}}_{\text{bicarbonate}}
=34.9\ \text{mL}\ \text{(C ✓)}$.

```math
# the two titrations
c_HCl = 1.0 M
V_phenolphthalein = 15.0 mL
n_carbonate = c_HCl*V_phenolphthalein =>
m_carbonate = n_carbonate*106 g/mol =>
m_total = 2.0 g
m_bicarbonate = m_total - m_carbonate =>
percent_bicarbonate = m_bicarbonate/m_total*100 =>
n_bicarbonate = m_bicarbonate/84 g/mol =>
V_methyl_orange = 2*V_phenolphthalein + n_bicarbonate/c_HCl =>
```

---

### Q38. Conductance / molar conductivity statements

**Answer: (B, C, D)**

| | Statement | Verdict |
|---|---|---|
| **(A)** | specific conductance ↑ and molar conductivity ↓ on dilution | ❌ both are backwards: $\kappa$ falls (fewer ions per mL), $\Lambda_m$ rises |
| **(B)** | limiting $\Lambda$ of a weak electrolyte cannot be got by extrapolation | ✅ the $\Lambda$–$\sqrt C$ curve plunges near $C\to0$ |
| **(C)** | plot of $\alpha^{2}$ vs $1/C$ is a line of slope $K_a$ | ✅ Ostwald: $K_a=C\alpha^{2}/(1-\alpha)\approx C\alpha^{2}\Rightarrow\alpha^{2}=(K_a)/C\cdot$… i.e. slope $K_a$ |
| **(D)** | Kohlrausch's law holds for strong *and* weak electrolytes | ✅ it is used to *find* $\Lambda^{\circ}$ of weak acids |

```desmos-graph
left=0; right=0.06
bottom=0; top=0.012
height=330
grid=true
---
y=1e-4*x|label:alpha^2 vs 1/C, slope Ka
(0.01,0.000001)|open|label:slope = Ka = 1.8e-5
```

```math
# Ostwald check with a real weak acid
Ka = 1.8e-5
C = 0.01 M
alpha = sqrt(Ka/C) =>
lhs = C*alpha^2/(1-alpha) =>
```

---

### Q39. Electrolysis of 4 L of 1 M brine, 2 A for 16 min 5 s

**Answer: (A, B, C)**

$$Q=It=2\times965=1930\ \text{C},\qquad n_{e^-}=\frac{1930}{96500}=0.020\ \text{mol}$$

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}[line width=0.8pt, american]
% electrolytic cell with Pt electrodes in brine
\draw[thick] (0,0) rectangle (6,3);
\fill[blue!8] (0.1,0.1) rectangle (5.9,2.2);
\node at (3,0.6) [font=\small]{brine (1 M NaCl)};
\draw[very thick] (1.4,1.2) -- (1.4,3.0);
\draw[very thick] (4.6,1.2) -- (4.6,3.0);
\node at (1.4,3.35) [above, font=\small]{anode (Pt)};
\node at (4.6,3.35) [above, font=\small]{cathode (Pt)};
\draw[->, >=stealth, red] (1.9,2.9) -- (1.9,2.5);
\node at (2.0,3.05) [above, font=\small, red]{$2Cl^- \to Cl_2+2e^-$};
\draw[->, >=stealth, blue] (4.4,4.0) -- (4.4,3.55);
\node at (2.3,4.15) [above, font=\small, blue]{$2H_2O+2e^- \to H_2+2OH^-$};
\draw (1.4,3.6) -- (1.4,4.0) -- (2.6,4.0);
\draw (4.6,3.6) -- (4.6,4.0);
\node at (3.5,4.4) [font=\small]{$I=2$ A, $t=965$ s};
\end{circuitikz}
\end{document}
```

- **anode:** $2\text{Cl}^{-}\to\text{Cl}_2+2e^{-}$ gives $0.010$ mol $\text{Cl}_2$
  $=224$ mL at STP **(B ✓)**;
- **cathode:** $2\text{H}_2\text{O}+2e^{-}\to\text{H}_2+2\text{OH}^{-}$ gives $0.010$ mol
  $\text{H}_2=224$ mL **(C ✓)** *and* $0.020$ mol $\text{OH}^{-}$, so the pH rises **(A ✓)**;
- **sodium is never deposited** from aqueous brine — water is reduced instead, so
  **(D) ✗**.

```math
# the electrolysis bookkeeping
I = 2 A
t = 16 min + 5 s
Q = I*t =>
n_e = Q/(96500 C/mol) =>
n_Cl2 = n_e/2 =>
V_Cl2 = n_Cl2*22400 mL/mol to mL =>
n_H2 = n_e/2 =>
n_OH = n_e =>
# what 0.02 mol of Na would weigh, if it were ever formed
m_Na_if = n_e*23 g/mol =>
```

---

### Q40. Match the equilibria with the correct property

**Answer: (C) P→1; Q→2; R→4; S→3**

$$\Delta n_g:\quad P:+1,\qquad Q:-1,\qquad R:0,\qquad S:-2$$

- **(P)** $K_p=K_c(RT)^{+1}>K_c$ in any solvent-free system ⟹ **(1)**;
- **(Q)** $\Delta n=-1\Rightarrow K_p<K_c$ ⟹ **(2)**;
- **(R)** $\Delta n=0$: adding inert gas at **constant volume** changes nothing ⟹ **(4)**;
- **(S)** four moles of gas become two, so raising the pressure shifts it **right** ⟹ **(3)**.

```math
# Kp/Kc = (RT)^(delta n) at 300 K
R = 0.0831 L*bar/(mol*K)
T = 300 K
RT = R*T =>
P_ratio = RT^1 =>
Q_ratio = RT^(-1) =>
R_ratio = RT^0 =>
S_ratio = RT^(-2) =>
```

---

### Q41. Match each titration with its conductance–volume graph

**Answer: (C) P→1; Q→2; R→3; S→4**

| | Titration | Shape of the conductance curve |
|---|---|---|
| **(P)** | $\text{AgNO}_3$ into $\text{KCl}$: $\text{Ag}^{+}$ replaces $\text{K}^{+}$ (similar mobility) — conductance stays almost flat, then *dips* as excess $\text{NO}_3^{-}$ arrives (1) |
| **(Q)** | $\text{HCl}$ vs $\text{NH}_4\text{OH}$: $\text{H}^{+}$ is replaced by the far slower $\text{NH}_4^{+}$, so conductance **falls** to the equivalence point, then rises with excess $\text{H}^{+}$ (2) |
| **(R)** | $\text{CH}_3\text{COOH}$ vs $\text{NaOH}$: weak acid → salt, conductance **rises** steadily (3) |
| **(S)** | $[\text{HCl}+\text{CH}_3\text{COOH}]$ vs $\text{NaOH}$: a steep fall to the HCl endpoint, then a shallow rise through the acetate buffer, then a steeper rise (4) |

```tikz
\begin{document}
\begin{tikzpicture}[line width=0.9pt, scale=0.95]
\foreach \i/\lab/\shape in {0/(P)/flat, 3.6/(Q)/fall, 7.2/(R)/rise} {
  \begin{scope}[shift={(\i,0)}]
    \draw[->] (0,0) -- (2.2,0); \draw[->] (0,0) -- (0,1.8);
    \node at (1.1,-0.3) [below, font=\small]{$V$ added};
    \node at (1.1,2.0) [above, font=\small]{\lab};
  \end{scope}
}
\begin{scope}[shift={(0,0)}]
  \draw[thick, blue] (0.1,1.2) -- (1.3,1.1) -- (2.1,0.85);
  \node at (1.0,-0.75) [below, font=\small]{(1) flat then dip};
\end{scope}
\begin{scope}[shift={(3.6,0)}]
  \draw[thick, blue] (0.1,1.5) -- (1.2,0.5) -- (2.1,1.2);
  \node at (1.0,-0.75) [below, font=\small]{(2) down then up};
\end{scope}
\begin{scope}[shift={(7.2,0)}]
  \draw[thick, blue] (0.1,0.35) -- (1.2,0.8) -- (2.1,1.5);
  \node at (1.0,-0.75) [below, font=\small]{(3) rising}; 
\end{scope}
\begin{scope}[shift={(10.8,0)}]
  \draw[->] (0,0) -- (2.2,0); \draw[->] (0,0) -- (0,1.8);
  \node at (1.1,-0.3) [below, font=\small]{$V$ added};
  \node at (1.1,2.0) [above, font=\small]{(S)};
  \draw[thick, blue] (0.1,1.7) -- (0.9,0.7) -- (1.4,0.95) -- (2.1,1.6);
  \node at (1.0,-0.75) [below, font=\small]{(4) kink then rise};
\end{scope}
\end{tikzpicture}
\end{document}
```

---

### Q42. Match each redox reaction with the equivalent weight of the underlined reactant

**Answer: (D) P→2; Q→3; R→5; S→1**

**(P)** $[\text{Fe(CN)}_6]^{4-}\to\text{Fe}^{3+}+6\text{CO}_3^{2-}+6\text{NO}_3^{-}$: iron
$+2\to+3$ (1), six carbons $+2\to+4$ (12), six nitrogens $-3\to+5$ (48) — total
$n$-factor $=61$ ⟹ $E=M/61$ ⟹ **(2)**.

**(Q)** $8\text{Al}+30\text{HNO}_3\to8\text{Al(NO}_3)_3+3\text{NH}_4\text{NO}_3+9\text{H}_2\text{O}$:
N goes $+5\to-3$, $n=8$ per N, and only $3$ of the $30$ nitrogens are reduced —
$n$-factor $=\dfrac{30\times?}{}$… per mole of $\text{HNO}_3$ it is $3\times8/30=0.8$
⟹ $E=M/0.8$ ⟹ **(3)**.

**(R)** $3\text{MnO}_2\to\text{MnO}_4^{-}+2\text{Mn}^{2+}$: disproportionation of $\text{Mn}^{+4}$;
averaged over three Mn the change is $+3+(-2)=1$ per Mn ⟹ **(5)**.

**(S)** $2\text{KMnO}_4\to\text{K}_2\text{MnO}_4+\text{MnO}_2+\text{O}_2$: Mn $+7\to+6$ and
$+7\to+4$ plus two oxygens leaving as $\text{O}_2$ ⟹ **(1)**.

```math
# n-factors for the four reactions
P = 1 + 12 + 48 =>
Q_per_acid = 3*8/30 =>
R_per_Mn = (3 + (-2)*1)/3*3 =>
S = 2 + 3 + 2 =>
```

---

## PART 3: CHEMISTRY — SECTION II (Numerical)

---

### Q43. Iodine content by titration with cerium(IV): $\text{I}^{-}\to\text{ICl}$

**Answer: 0.23 – 0.25 (≈0.238 g/L)**

Iodine goes $-1\to+1$, so $n=2$ (2 electrons per I).

```math
# titration arithmetic
N_Ce = 0.05 eq/L
V = 15 mL
meq_Ce = N_Ce*V to meq =>
n_I = meq_Ce/2 =>
A_I = 127 g/mol
mass_I = n_I*A_I to g =>
volume_sample = 200 mL
conc = mass_I/volume_sample to g/L =>
```

$$n_{\text{I}}=\frac{0.75\ \text{meq}}{2}=3.75\times10^{-4}\ \text{mol}
\Rightarrow m=0.0477\ \text{g in } 0.200\ \text{L}
\Rightarrow \mathbf{0.238\ g\ L^{-1}}$$

---

### Q44. Indicator half-way colour: ratio $\text{CH}_3\text{COONa}:\text{CH}_3\text{COOH}$

**Answer: 5.00**

Half-way colour means $[\text{HIn}]=[\text{In}^{-}]$, so the solution pH must equal
$\text{p}K_{\text{In}}=5.45$. The buffer then fixes the ratio:

$$\text{pH}=\text{p}K_a+\log\frac{[\text{salt}]}{[\text{acid}]}:\quad
5.45=4.75+\log R\Rightarrow\log R=0.70\Rightarrow R=5$$

```math
# buffer arithmetic with the printed logs
pH = 5.45
pKa = 4.75
logR = pH - pKa =>
R = 10^logR =>
# cross-check with log 5 = 0.70
alt_check = 10^0.70 =>
```

---

### Q45. $E^{\circ}$ for $\text{Co(en)}_3^{3+}+e^{-}\to\text{Co(en)}_3^{2+}$

**Answer: 0.31 – 0.32 (magnitude 0.318 V)**

Build the half-reaction from three steps and add their Gibbs energies:

$$
\begin{aligned}
(1)&\quad \text{Co}^{3+}+e^{-}\to\text{Co}^{2+}, & \Delta G_1&=-F(1.80)\\
(2)&\quad \text{Co}^{2+}+3\text{en}\to[\text{Co(en)}_3]^{2+}, & \Delta G_2&=-RT\ln(10^{12})\\
(3)&\quad [\text{Co(en)}_3]^{3+}\to\text{Co}^{3+}+3\text{en}, & \Delta G_3&=+RT\ln(2\times10^{47})
\end{aligned}
$$

$$\Delta G=-F(1.80)+RT\ln\frac{2\times10^{47}}{10^{12}}
=-F(1.80)+RT\ln(2\times10^{35})$$

```math
# E from the formation-constant cycle
E_Co = 1.80 V
K2 = 1.0e12
K3 = 2.0e47
ratio = K3/K2 =>
logratio = log(10, ratio) =>
E_complex = E_Co - 0.06*logratio =>
magnitude = -E_complex =>
# with the printed logs
log_2e35 = 35 + 0.3 =>
E_alt = 1.80 - 0.06*log_2e35 =>
```

$$E^{\circ}=1.80-0.06\times35.3=-0.318\ \text{V}\ \Rightarrow\ \mathbf{|E^{\circ}|=0.318}$$

---

### Q46. Butane fuel cell: $E=\dfrac{x}{F}$ volts, find $x$

**Answer: 108.92**

$$\text{C}_4\text{H}_{10}+\tfrac{13}{2}\text{O}_2\to4\text{CO}_2+5\text{H}_2\text{O},\qquad n=26$$

$$\Delta_rG^{\circ}=4(-400)+5(-250)-(-18)=-2832\ \text{kJ mol}^{-1}$$

```math
# ΔG → E → x
dG_CO2 = -400 kJ/mol
dG_H2O = -250 kJ/mol
dG_butane = -18 kJ/mol
dG = 4*dG_CO2 + 5*dG_H2O - dG_butane =>
n = 26
F = 96500 C/mol
E = -dG/(n*F) =>
x = E*F =>
E_volts = -dG*1000 J/mol/(n*F) =>
x_value = -dG*1000/(n) =>
```

$$E=\frac{2832\times10^{3}}{26\times96500}=1.1287\ \text{V}
\Rightarrow x=E\cdot F=\mathbf{108.92}$$

---

### Q47. Solubility of barium iodate in the mixed solution

**Answer: 4.00 (so $x=4$)**

```math
# moles before precipitation
V_Ba = 200 mL
c_Ba = 0.010 M
n_Ba = c_Ba*V_Ba =>
V_IO3 = 100 mL
c_IO3 = 0.10 M
n_IO3 = c_IO3*V_IO3 =>
# Ba2+ is the limiting reagent: 2 IO3- per Ba2+
n_IO3_left = n_IO3 - 2*n_Ba =>
V_total = V_Ba + V_IO3 =>
conc_IO3 = n_IO3_left/V_total =>
Ksp = 1.6e-9
s = Ksp/conc_IO3^2 =>
x_value = s*1e6 =>
```

$\text{Ba}^{2+}$ is consumed completely, leaving $0.006$ mol $\text{IO}_3^{-}$ in $0.300$ L
$\Rightarrow[\text{IO}_3^{-}]=0.020$ M. Then

$$K_{sp}=s(0.020)^{2}=1.6\times10^{-9}\Rightarrow s=4\times10^{-6}\ \text{M}
\Rightarrow \mathbf{x=4.00}$$

---

### Q48. Dichloroacetic acid: moles of $\text{NH}_3$ neutralised

**Answer: 0.20**

$$\text{CHCl}_2\text{COOH}\xrightarrow{\text{oxidation}}2\text{CO}_2+\text{H}_2\text{O}+\text{Cl}_2$$

Every carbon goes $+3\to+4$ (2 electrons) and both chlorines go $-1\to0$ (2 electrons):
$n$-factor $=2+4=6$.

```math
# n-factor, equivalents, and the acid–base step
n_factor = 6
equivalents = 1.2 eq
n_acid = equivalents/n_factor =>
# the ammonium salt forms 1:1
x = n_acid =>
```

$1.2=6n\Rightarrow n=0.20$ mol of acid, and the acid–base step is 1:1, so
$\mathbf{x=0.20}$.

---

## 📚 COMPLETE THEORY REFERENCE

### Limits with radicals — the max rule

$$\big(A^{n}+B^{n}\big)^{1/n}\xrightarrow[n\to\infty]{}\max(A,B)$$

### Inverse-trig and floor/fractional identities

$$\lfloor m+\theta\rfloor=m,\quad \{\theta\}=\theta\in[0,1),
\qquad \sec^{-1}(\sec x)=x-2k\pi,\ x\in(2k\pi,(2k+1)\pi)$$

### Logs of trig functions near $0$

$$\ln\cos u\approx-\frac{u^{2}}{2},\qquad 1-\cos u\approx\frac{u^{2}}{2},
\qquad \ln(1+u)\approx u$$

### Wave energy in a standing wave

$$y=A\sin(kx)\cos\omega t:\quad u_{\text{pot}}\propto\cos^{2}(kx),\quad
u_{\text{kin}}\propto\sin^{2}(kx)$$

### Two-media string junction

$$r=\frac{Z_1-Z_2}{Z_1+Z_2},\qquad t=\frac{2Z_1}{Z_1+Z_2},\qquad Z=\sqrt{T\mu},
\qquad P_{\text{reflected}}/P_{\text{incident}}=r^{2}$$

### Radiation force

$$F_\perp=\frac{P\cos\theta}{c}\big[(1+R)-T\big]\ \text{(normal component)}, \qquad
\text{absorbed fraction stops in place}$$

### Solubility

$$K_{sp}\ \text{is temperature-only;} \quad
\text{common ion} \to \text{less dissolves, same } K_{sp}; \quad
\text{complexation} \to \text{more dissolves}$$

### Ostwald's dilution law

$$K_a=\frac{C\alpha^{2}}{1-\alpha}\approx C\alpha^{2}
\ \Longrightarrow\ \text{plot } \alpha^{2}\text{ vs } \frac1C:\ \text{slope }K_a$$

### $K_p$ vs $K_c$

$$K_p=K_c(RT)^{\Delta n_g};\qquad
\text{inert gas at constant }V:\ \text{no shift};\quad
\text{inert gas at constant }P:\ \text{shift toward more moles}$$
