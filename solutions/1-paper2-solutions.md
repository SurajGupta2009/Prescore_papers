---
test: 1
paper: 2
subjects: [Mathematics, Physics, Chemistry]
total_questions: 51
status: complete
tags: [solutions, jee-advanced, test-1]
---
# 1-PAPER 2 — COMPLETE SOLUTIONS (JEE Advanced Level)

> **Target:** Top 100 Rank Improvement<br>
> **Approach:** Concept-first, fully worked solutions; independent checks; plugin-rendered diagrams where they add value; and a compact theory vault at the end.<br>
> **Source check:** The paper and its printed answer key (PDF pp. 1–18) were checked against the worked mathematics notes (pp. 19–25). The remaining physics and chemistry workings below are derived from the stated data and diagrams.

---

## MASTER ANSWER KEY

| Subject | Question | Answer |
|---|---:|---|
| Mathematics | 1–4 | D (96), C (5), A (850), D (9) |
| Mathematics | 5–7 | B,C,D · A,B · A,B,C,D |
| Mathematics | 8–11 | 1.00 · 0.00 · 5.00 · −3.00 |
| Mathematics | 12–17 | 9 · 1 · 22 · 3 · 2498 · 482 |
| Physics | 18–21 | C · C (220 °C) · A · A (5R/12) |
| Physics | 22–24 | B,C · A,B,C · A,B,C,D |
| Physics | 25–28 | 0.19 s · 1.60 A · 7.87 kV · 0.48 N m⁻¹ |
| Physics | 29–34 | 14 · 203 · 8 · 6 · 892 · 3 |
| Chemistry | 35–38 | A · A · B · D |
| Chemistry | 39–41 | A,C,D · A,B · A,C,D |
| Chemistry | 42–45 | 5 · 12 · 331 · 135 |
| Chemistry | 46–51 | 2 · 146 · 167 · 5 · 8 · 0 |

---

# PART 1: MATHEMATICS

## SECTION I (i) — Single Correct

### Q1. Three couples sit for a photograph in two rows of three. No couple may sit adjacent in the same row or directly one behind the other in the same column. Find the number of arrangements.

(A) 48 (B) 56 (C) 72 (D) 96

**Answer: (D) 96**

#### Approach 1 — Count by the number of husbands in the first row

Call the couples \(H_i,W_i\), for \(i=1,2,3\). Classify the first row by its gender composition.

- **Three husbands:** arrange them in \(3!\) ways. The wives in the second row must be a derangement of their column positions, so there are \(D_3=2\) possibilities. Count: \(3!D_3=12\).
- **Three wives:** by symmetry, another \(12\).
- **Two husbands and one wife:** if the wife is paired with one of the two husbands in row 1, that couple must occupy the two end seats; the remaining husband sits in the middle. The corresponding husband–wife pair in row 2 must also occupy the ends, forcing the other wife into the middle directly behind her husband, so these cases have no valid completion. Thus the row-1 wife must be the wife of the omitted husband: choose the two husbands in \(\binom32=3\) ways, arrange the three people in \(3!\) ways, and derange their three spouses in \(D_3=2\) ways. Count: \(3\cdot3!\cdot2=36\).
- **Two wives and one husband:** symmetrically, \(36\).

Thus \(12+12+36+36=96\).

#### Approach 2 — Derangement check

In each mixed-gender case that can be completed, row 1 contains one person from each couple and row 2 contains exactly their three spouses. They must avoid the three partner-columns; inclusion–exclusion gives \(3!-{3\choose1}2!+{3\choose2}1!-{3\choose3}=2\). If row 1 contains a married pair, the end-seat/middle-seat constraint described above leaves no valid row 2.

> [!tip] Exam Shortcut
> First classify the first row by its gender composition; the column restriction is a three-object derangement in every case.

> [!warning] Common Pitfall
> The wording does not directly ban a same-row couple; in this 2×3 arrangement, however, a separated pair in the first row forces a vertical partner match in the second. Exclude those cases by showing the conflict, not by assuming same-row couples are forbidden.

> [!success] Key Takeaway
> For a 2×3 arrangement, separating partners by column is a derangement condition; the four row-composition cases give the total.

---

### Q2. Real sequences satisfy \(U_{n+1}=U_n-V_n\), \(V_{n+1}=U_n+V_n\), with \(U_{2024}=2^{1012}\), \(V_{2024}=2^{1013}\). Find \(U_1+2V_1\).

(A) 1 (B) 3 (C) 5 (D) 0

**Answer: (C) 5**

#### Approach 1 — Complex recurrence

Set \(W_n=U_n+iV_n\). Then

\[W_{n+1}=(U_n-V_n)+i(U_n+V_n)=(1+i)W_n.\]

Hence \(W_{2024}=(1+i)^{2023}W_1\). Since \((1+i)^{2023}=2^{1011}(1-i)\),

\[W_1=\frac{2^{1012}(1+2i)}{2^{1011}(1-i)}=\frac{2(1+2i)}{1-i}=-1+3i.\]

Therefore \(U_1=-1\), \(V_1=3\), and \(U_1+2V_1=5\).

#### Approach 2 — Matrix interpretation

The vector \( (U_n,V_n)^T\) is multiplied by \(A=\begin{pmatrix}1&-1\\1&1\end{pmatrix}\) at each step. The complex method diagonalizes this real rotation-dilation at once: \(A\) represents multiplication by \(1+i\), with scale \(\sqrt2\) and rotation \(\pi/4\).

> [!tip] Exam Shortcut
> A coupled recurrence with the pattern \(U-V, U+V\) almost always suggests \(U+iV\).

> [!warning] Common Pitfall
> There are 2023 transitions from index 1 to 2024, not 2024.

> [!success] Key Takeaway
> Complex encoding turns a two-component linear recurrence into a geometric progression.

---

### Q3. The ten roots of \(z^{10}+(13z-1)^{10}=0\) are \(z_1,\bar z_1,\ldots,z_5,\bar z_5\). Evaluate \(\displaystyle\sum_{j=1}^{5}\frac1{|z_j|^2}\).

(A) 850 (B) 1700 (C) 900 (D) 1800

**Answer: (A) 850**

#### Approach 1 — Map the roots to the unit circle

Put \(\omega=z/(13z-1)\). Then \(\omega^{10}=-1\), so the ten \(\omega\)'s are the unit-modulus roots \(e^{i(2k+1)\pi/10}\). Solving for \(z\),

\[z=\frac{\omega}{13\omega-1}=\frac1{13-\omega^{-1}},\qquad \frac1{|z|^2}=|13-\omega^{-1}|^2=170-26\operatorname{Re}(\omega).\]

The ten \(\omega\)'s occur in five conjugate pairs. The sum of their real parts is zero, so the five pair-representative real parts also sum to zero. Thus

\[\sum_{j=1}^5\frac1{|z_j|^2}=5(170)-26(0)=850.\]

#### Approach 2 — Symmetry check

The transformation \(z=1/(13-\omega^{-1})\) maps conjugate \(\omega\)-pairs to conjugate \(z\)-pairs. Summing one reciprocal squared modulus from each pair is half the sum over all ten roots, again giving \(850\).

> [!tip] Exam Shortcut
> Once \( |\omega|=1\), expand \( |13-\omega|^2=170-26\cos\theta\); the cosine sum vanishes by root symmetry.

> [!warning] Common Pitfall
> The requested sum uses five roots—one from each conjugate pair. Do not double the final total.

> [!success] Key Takeaway
> A rational substitution can convert a sum of complicated root moduli into a simple trigonometric sum over equally spaced angles.

---

### Q4. Let \(N\) be the number of five-digit integers that contain the consecutive block “15” and are divisible by 15. Find the last digit of \(N\).

(A) 3 (B) 5 (C) 7 (D) 9

**Answer: (D) 9**

#### Approach 1 — Enumerate placements and use inclusion–exclusion

Divisibility by 15 requires the last digit to be 0 or 5 and the digit sum to be divisible by 3. Count numbers by a specified occurrence of the block:

| Pattern | Count after the digit-sum test |
|---|---:|
| \(abc15\) | 300 |
| \(ab150\) | 30 |
| \(ab155\) | 30 |
| \(a15b0\) | 30 |
| \(a15b5\) | 30 |
| \(15ab0\) | 34 |
| \(15ab5\) | 33 |

The raw total is \(487\). Subtract the duplicate valid numbers: \(31515,61515,91515\) (3); \(15150\) (1); and \(15015,15315,15615,15915\) (4). The overlap \(15155\) is not divisible by 3, so it was never counted. Therefore \(N=487-8=479\), whose last digit is 9.

For example, in \(a15b0\), divisibility by 3 requires \(a+b+6\equiv0\pmod3\); there are 30 valid \(a,b\) pairs with \(a\ne0\). The other rows use the same residue-counting rule.

#### Approach 2 — Split by the last digit

If the number ends in 0, the possible patterns are \(ab150,a15b0,15ab0\): the raw count is \(30+30+34=94\). Their only valid overlap is \(15150\), leaving 93. If it ends in 5, the patterns are \(abc15,ab155,a15b5,15ab5\): the raw count is \(300+30+30+33=393\). The valid overlaps are the 3 numbers \(31515,61515,91515\) and the 4 numbers \(15015,15315,15615,15915\); \(15155\) is not divisible by 3. This leaves 386. Hence \(N=93+386=479\), whose last digit is 9.

> [!tip] Exam Shortcut
> Fix the final digit first (0 or 5), then impose the mod-3 condition on the remaining free digits.

> [!warning] Common Pitfall
> A number can contain “15” more than once (for example, \(31515\)); simply adding the four possible block positions overcounts.

> [!success] Key Takeaway
> For a short block-counting problem, list each possible block position, count residue classes, and explicitly subtract intersections.

---

## SECTION I (ii) — Multiple Correct

### Q5. Let \(Z=e^{2\pi i/19}\) and \(S=1+5Z+9Z^2+\cdots+73Z^{18}\). Define real \(\alpha,\beta,\gamma\) by

\[S=\frac{19\alpha}{Z-1},\quad 1+5\cos\frac{2\pi}{19}+\cdots+73\cos\frac{36\pi}{19}=19\beta,\]
\[5\sin\frac{2\pi}{19}+\cdots+73\sin\frac{36\pi}{19}=\gamma\cot\frac{\pi}{19}.\]

Which statements are correct?

(A) \( |\beta|+|\gamma|\) is divisible by 19. (B) \( |\alpha|+|\beta|+|\gamma|=44\).<br>
(C) \(10\alpha+\beta+\gamma\) is divisible by 19. (D) The digit sum of \( |\alpha|-|\beta|+|\gamma|\) is 4.

**Answer: (B), (C), (D)**

#### Approach 1 — Shift the weighted geometric sum

Multiply by \(1-Z\). Consecutive coefficients differ by 4, and \(Z^{19}=1\):

\[S(1-Z)=1+4(Z+Z^2+\cdots+Z^{18})-73.\]

Since \(1+Z+\cdots+Z^{18}=0\), the parenthesized sum is \(-1\), giving \(S(1-Z)=-76\), or \(S=76/(Z-1)\). Therefore \(\alpha=4\).

For \(Z=e^{i\theta}\), \(1/(Z-1)=-\tfrac12-\tfrac i2\cot(\theta/2)\). With \(\theta=2\pi/19\),

\[\operatorname{Re}S=-38=19\beta\Rightarrow\beta=-2,\qquad
\operatorname{Im}S=-38\cot(\pi/19)=\gamma\cot(\pi/19)\Rightarrow\gamma=-38.\]

Check the choices: (A) \(2+38=40\not\equiv0\pmod{19}\); (B) \(4+2+38=44\); (C) \(40-2-38=0\); (D) \(4-2+38=40\), digit sum 4.

#### Approach 2 — Differentiate the geometric sum

Write \(S=\sum_{k=0}^{18}(1+4k)Z^k\). Since \(\sum Z^k=0\), differentiate \(1+x+\cdots+x^{18}=(1-x^{19})/(1-x)\) and evaluate at \(x=Z\):

\[\sum_{k=0}^{18}kZ^k=Z\frac{d}{dZ}\sum_{k=0}^{18}Z^k=\frac{19}{Z-1}.\]

Therefore \(S=76/(Z-1)\), recovering \(\alpha=4,\beta=-2,\gamma=-38\) and the same choices.

> [!tip] Exam Shortcut
> For \(Z^{19}=1\), use \(1+Z+\cdots+Z^{18}=0\) before expanding anything else.

> [!warning] Common Pitfall
> The definition uses \(Z-1\), not \(1-Z\); this changes the sign of both the real and imaginary parts.

> [!success] Key Takeaway
> Multiplying an arithmetic–geometric sum by \(1-Z\) turns it into a short telescoping expression.

---

### Q6. Which statements are correct?

(A) The number of integers between \(10^2\) and \(10^4\) with digit sum 14 is 535.<br>
(B) For distinct primes \(p,q,r\), if \(\operatorname{lcm}(\alpha,\beta,\gamma)=p^3q^2r\) and \(\gcd(\alpha,\beta,\gamma)=pqr\), there are 72 ordered triples.<br>
(C) The sum of all five-digit numbers made from 2,4,6,7,9 without repetition is \(\frac{(10^6-1)(4!)(28)}9\).<br>
(D) Assigning six distinct hats and their six matching-colour shirts to five men, with no man receiving a matching hat and shirt, gives \(310\cdot6!\) ways.

**Answer: (A), (B)**

#### Approach 1 — Test each statement

**(A)** Count four-digit strings (leading zero allowed) with digit sum 14. The coefficient of \(x^{14}\) in \((1+x+\cdots+x^9)^4\) is

\[\binom{17}{3}-4\binom73=680-140=540.\]

Remove the five values below 100 with digit sum 14: 59, 68, 77, 86, 95. Thus \(540-5=535\), true.

**(B)** For the exponents of \(p\), each of the three exponents is 1, 2, or 3, with at least one 1 and one 3: \(3^3-2(2^3)+1=12\). For \(q\), the exponents are 1 or 2, with both extremes present: \(2^3-2=6\). For \(r\), all exponents are 1: one way. Product: \(12\cdot6=72\), true.

**(C)** Each digit occurs \(4!\) times in every place, so the actual sum is

\[4!(2+4+6+7+9)(11111)=24\cdot28\cdot11111=7{,}466{,}592.\]

The displayed expression has \(10^6-1\), not \(10^5-1\), and is ten times too large. False.

**(D)** Fix the hats. Inclusion–exclusion gives the number of injective shirt assignments avoiding the five forbidden matches:

\[{}^6P_5-5({}^5P_4)+10({}^4P_3)-10({}^3P_2)+5({}^2P_1)-1=309.\]

There are \(6P_5=6!\) hat assignments, so the total is \(309\cdot6!\), not \(310\cdot6!\). False.

#### Approach 2 — Derangement cross-check for (D)

After fixing the hats, add a dummy sixth position for the unused shirt. Among the \(6!\) shirt permutations, either the dummy is also a derangement point (\(D_6=265\) possibilities) or it is fixed and the five men form a derangement (\(D_5=44\)). This gives \(D_6+D_5=309\) shirt assignments per hat assignment, confirming that the printed \(310\) is false.

> [!tip] Exam Shortcut
> In (C), each digit appears 24 times in each place; the repunit multiplier is \(11111=(10^5-1)/9\).

> [!warning] Common Pitfall
> In (D), five men receive items but one colour of each type remains unused. Do not count a full six-person derangement.

> [!success] Key Takeaway
> Generating functions count bounded digit sums; prime-exponent choices and inclusion–exclusion handle the other two claims.

---

### Q7. Define \(a_n=\displaystyle\sum_{r=0}^n\frac1{\binom nr}\). If

\[\sum_{r=0}^n\frac{r^2}{\binom nr}=P(n)a_{n+2}+Q(n)a_{n+1}+a_n+R(n),\]

where \(P,Q,R\) are polynomials, which statements are true?<br>
(A) \(P(5)=42\) (B) \(Q(5)=-18\) (C) \(R(5)=-30\) (D) \(P(5)-Q(5)+R(5)=30\)

**Answer: (A), (B), (C), (D)**

#### Approach 1 — Re-index using binomial ratios

By symmetry under \(r\mapsto n-r\), the left side equals \(\sum (n-r)^2/\binom nr\). Also

\[\frac{(n+1)(n+2)}{\binom{n+2}{r}}-\frac{3(n+1)}{\binom{n+1}{r}}+\frac1{\binom nr}
=\frac{(n-r)^2}{\binom nr}.\]

Summing \(r=0,\ldots,n\) and restoring the omitted end terms in \(a_{n+1},a_{n+2}\) gives

\[P(n)=(n+1)(n+2),\quad Q(n)=-3(n+1),\quad R(n)=-n(n+1).\]

At \(n=5\), these are \(42,-18,-30\); and \(42-(-18)-30=30\). All four statements are true.

#### Approach 2 — Direct check at \(n=5\)

The reciprocal-binomial sums are \(a_5=13/5\), \(a_6=151/60\), and \(a_7=256/105\). The derived coefficients give

\[42a_7-18a_6+a_5-30=\frac{297}{10}=\sum_{r=0}^{5}\frac{r^2}{\binom5r},\]

which checks all four statements numerically.

> [!tip] Exam Shortcut
> Use \(\binom{n+2}{r}\) and \(\binom{n+1}{r}\) ratios to manufacture a quadratic in \(n-r\).

> [!warning] Common Pitfall
> The sums defining \(a_{n+1}\) and \(a_{n+2}\) contain extra endpoint terms; omitting them gives the wrong constant \(R(n)\).

> [!success] Key Takeaway
> Symmetry of \(1/\binom nr\) converts \(r^2\) to \((n-r)^2\), then Pascal-type ratios yield the recurrence.

---

## SECTION II (i) — Numerical (Common Data)

Let \(\alpha=e^{2\pi i/11}\), \(\lambda=\alpha^{2019}\), \(\mu=\alpha^{2020}\), and \(\beta=\alpha^{2015}\).

### Q8. Evaluate

\[\left|i+(i-\beta)(i-\beta^2)\cdots(i-\beta^{10})\right|+2\operatorname{Re}(\lambda+\lambda^2+\cdots+\lambda^5).\]

**Answer: 1.00**

#### Approach 1 — Cyclotomic product

Reduce exponents modulo 11: \(\beta=\alpha^2\), \(\lambda=\alpha^6\). Because 2 is invertible modulo 11, \(\beta,\ldots,\beta^{10}\) are exactly the ten nontrivial 11th roots of unity. Hence

\[\prod_{k=1}^{10}(x-\beta^k)=1+x+\cdots+x^{10},\]

so at \(x=i\), the product is \(1+i+\cdots+i^{10}=i\). The modulus term is therefore \( |i+i|=2\).

The powers \(\lambda,\ldots,\lambda^{10}\) sum to \(-1\). Pairing conjugates gives \(2\operatorname{Re}(\lambda+\cdots+\lambda^5)=-1\). Total: \(2-1=1\).

#### Approach 2 — Evaluate the cyclotomic polynomial directly

The product is \(1+i+\cdots+i^{10}=(i^{11}-1)/(i-1)=i\). For the second term, pair each \(\lambda^k\) with its conjugate \(\lambda^{11-k}\); their sum over all ten nontrivial roots is \(-1\), so the real-part contribution is \(-1\). The result is again 1.

> [!tip] Exam Shortcut
> Reduce large powers of \(\alpha\) mod 11 immediately; never calculate \(\alpha^{2019}\) directly.

> [!warning] Common Pitfall
> The product includes powers 1 through 10, not the root \(1\); it is \(1+x+\cdots+x^{10}\), not \(x^{11}-1\).

> [!success] Key Takeaway
> Products over all non-unit roots are evaluations of the cyclotomic polynomial.

---

### Q9. Evaluate

\[(\alpha-\beta)(\alpha-\beta^2)\cdots(\alpha-\beta^{10})+(\mu-\beta)(\mu-\beta^2)\cdots(\mu-\beta^{10}).\]

**Answer: 0.00**

#### Approach 1 — A root appears in each product

The set \(\{\beta^k:1\le k\le10\}\) is the set of all nontrivial 11th roots. Since \(\alpha\) and \(\mu=\alpha^7\) are both in that set, one factor in each product is zero. Therefore each product is zero and the sum is \(0\).

#### Approach 2 — Use the polynomial of all nontrivial roots

For every nontrivial 11th root \(u\), \(1+u+u^2+\cdots+u^{10}=0\). Since \(\alpha\) and \(\mu\) are both nontrivial 11th roots, this identity makes each of the two products vanish.

> [!tip] Exam Shortcut
> Before expanding a product, check whether its leading value is itself one of the factors.

> [!warning] Common Pitfall
> \(\alpha\) and \(\mu\) are nontrivial 11th roots, not the root 1.

> [!success] Key Takeaway
> Cyclotomic products can collapse instantly when the evaluation point belongs to the factor set.

---

## SECTION II (i) — Numerical (Common Curves)

Given \(C_1:|z-1|=1\) and \(C_2:w=\dfrac{z^2-z-2}{1-z}\).

### Q10. If the eccentricity of \(C_2\) is \(a\sqrt2/b\) in lowest positive-integer terms, find \(a+b\).

**Answer: 5.00**

#### Approach 1 — Parametrize the circle

Put \(z=1+e^{i\theta}\). Since \(1-z=-e^{i\theta}\),

\[w=-1-e^{i\theta}+2e^{-i\theta}=(\cos\theta-1)-3i\sin\theta.\]

Thus, for \(w=x+iy\), \((x+1)^2+y^2/9=1\): an ellipse with semiaxes 3 and 1. Its eccentricity is \(e=\sqrt{1-1/9}=2\sqrt2/3\), so \(a+b=2+3=5\).

```desmos-graph
---
bounds: [-4, 2, -4, 4]
grid: true
---
(x + 1)^2 + y^2/9 = 1
```

#### Approach 2 — Read the semiaxes from the parametrization

The real coordinate has amplitude 1 and the imaginary coordinate amplitude 3. Therefore the major/minor semiaxes are 3 and 1 without needing to eliminate \(\theta\) first.

> [!tip] Exam Shortcut
> An affine image \(x=a+b\cos\theta, y=c+d\sin\theta\) is an axis-aligned ellipse with semiaxes \(|b|,|d|\).

> [!warning] Common Pitfall
> Eccentricity is computed using the **major** semiaxis: \(a_{\rm major}=3\), \(b_{\rm minor}=1\).

> [!success] Key Takeaway
> Parametrizing \(z=1+e^{i\theta}\) converts the complex locus into an elementary ellipse.

---

### Q11. Find the product of the slopes of the normals to \(C_1\) that touch \(C_2\).

**Answer: −3.00**

#### Approach 1 — Tangents from the circle centre

A normal to the circle \((x-1)^2+y^2=1\) passes through its centre \((1,0)\). The ellipse from Q10 is \((x+1)^2+y^2/9=1\). A line through \((1,0)\) with slope \(m\) is \(y=m(x-1)\). Substitution into the ellipse gives

\[(9+m^2)x^2+(18-2m^2)x+m^2=0.\]

Tangency requires zero discriminant:

\[(18-2m^2)^2-4(9+m^2)m^2=0\Rightarrow m^2=3.\]

The two slopes are \(\sqrt3\) and \(-\sqrt3\); their product is \(-3\).

#### Approach 2 — Tangent equation in ellipse-parameter form

Parametrize the ellipse by \(x=-1+\cos t,\ y=3\sin t\). Its tangent at parameter \(t\) is \((x+1)\cos t+(y/3)\sin t=1\). Requiring it to pass through \((1,0)\) gives \(2\cos t=1\), so \(\sin t=\pm\sqrt3/2\). The tangent slopes are \(-3\cot t=\pm\sqrt3\); their product is \(-3\).

> [!tip] Exam Shortcut
> Normals to a circle are its radii. Find the tangent lines from the circle's centre to the ellipse.

> [!warning] Common Pitfall
> The normals are not perpendicular to the ellipse's tangent at an arbitrary point; here they are specifically required to be tangent to \(C_2\).

> [!success] Key Takeaway
> A tangency condition for a line through a fixed point is efficiently imposed by setting the quadratic discriminant to zero.

---

## SECTION II (ii) — Numerical

### Q12. Suppose

\[(1-x^3)^n=\sum_{r=0}^n a_r x^r(1-x)^{3n-2r}.\]

Evaluate \(p+q\) if

\[\sum_{n=1}^k\left(\sum_{r=0}^{n-1}\binom{k}{n}a_r\right)=p^k-q^k,\]

where \(p,q\) are coprime positive integers.

**Answer: 9**

#### Approach 1 — Binomially expand in \(x/(1-x)^2\)

Since \(1-x^3=(1-x)(1+x+x^2)=(1-x)^3+3x(1-x)\),

\[(1-x^3)^n=(1-x)^{3n}\left(1+\frac{3x}{(1-x)^2}\right)^n
=\sum_{r=0}^n3^r\binom nr x^r(1-x)^{3n-2r}.\]

Thus \(a_r=3^r\binom nr\), and

\[\sum_{r=0}^{n-1}a_r=\sum_{r=0}^{n-1}3^r\binom nr=4^n-3^n.\]

The given double sum is

\[\sum_{n=1}^k\binom kn(4^n-3^n)=[5^k-1]-[4^k-1]=5^k-4^k.\]

Therefore \(p=5,q=4\), and \(p+q=9\).

#### Approach 2 — Separate the two binomial transforms

From \(a_r=3^r\binom nr\), the inner partial sum is the full binomial sum \(4^n\) minus its last term \(3^n\). Applying the outer binomial theorem to \(4^n-3^n\) gives \(5^k-4^k\), hence \((p,q)=(5,4)\) and \(p+q=9\).

> [!tip] Exam Shortcut
> Factor \(1-x^3=(1-x)(1+x+x^2)\); the coefficient pattern becomes a binomial theorem in one line.

> [!warning] Common Pitfall
> The inner sum stops at \(n-1\), so its missing final term is \(3^n\); this is why it equals \(4^n-3^n\), not \(4^n\).

> [!success] Key Takeaway
> A deliberately unusual basis \(x^r(1-x)^{3n-2r}\) is chosen so the factorization of \(1-x^3\) reveals the coefficients directly.

---

### Q13. A person climbs \(3k\) steps, using steps of size 1 or \(k\) only (\(k\ge2\)). Let \(A(k)\) count the ways to reach the top and \(\lambda_k=A(k+1)-A(k)\). Find \(\lambda_{k+1}-\lambda_k\).

**Answer: 1**

#### Approach 1 — Count by the number of long steps

If there are \(j\) jumps of length \(k\), then there are \(3k-jk\) unit steps. The number of ordered move sequences is

$$\binom{3k-j(k-1)}{j},\qquad j=0,1,2,3.$$

Therefore

$$A(k)=1+(2k+1)+\binom{k+2}{2}+1=2k+3+\binom{k+2}{2}.$$

Taking consecutive differences gives \(\lambda_k=k+4\), hence \(\lambda_{k+1}-\lambda_k=1\).

#### Approach 2 — Difference of the closed form

Expanding \(\binom{k+2}{2}\), \(A(k)=\tfrac12k^2+\tfrac72k+4\). Thus \(\lambda_k=A(k+1)-A(k)=k+4\), a linear sequence with unit first difference.

> [!tip] Exam Shortcut
> At most three \(k\)-jumps fit into \(3k\) steps; the sum has only four terms, regardless of \(k\).

> [!warning] Common Pitfall
> The number of **moves** is not the number of staircase steps. With \(j\) long jumps, it is \(j+(3k-jk)\).

> [!success] Key Takeaway
> Count arrangements by choosing the positions of the long jumps, then simplify before taking the second difference.

---

### Q14. Find the remainder modulo 49 of

$$\sum_{k=0}^{1012}\frac{\binom{1012}{k}}{\binom{2024}{k}}\sum_{r=k}^{2024}\binom rk\binom{2024}r.$$

**Answer: 22**

#### Approach 1 — Collapse the inner sum

Use \(\binom{2024}{r}\binom rk=\binom{2024}{k}\binom{2024-k}{r-k}\). The inner sum is therefore \(\binom{2024}{k}2^{2024-k}\), and the full expression is

$$\sum_{k=0}^{1012}\binom{1012}{k}2^{2024-k}=2^{1012}3^{1012}=6^{1012}.$$

Since \(6^{1012}=(-1+7)^{1012}\), all terms with \(7^2\) vanish modulo 49:

$$6^{1012}\equiv1-1012\cdot7=1-7084\equiv22\pmod{49}.$$

#### Approach 2 — Modular binomial check

Only the constant and linear terms in \((-1+7)^{1012}\) survive modulo \(7^2\). The sign of the linear term is negative because \(1012-1\) is odd; the residue is \(22\).

> [!tip] Exam Shortcut
> Reduce to \(6^{1012}\) first, then use the binomial theorem modulo \(7^2\); do not compute a huge power.

> [!warning] Common Pitfall
> Modulo 49, keep the term linear in 7. Discarding it would incorrectly give remainder 1.

> [!success] Key Takeaway
> The identity \(\binom Nr\binom rk=\binom Nk\binom{N-k}{r-k}\) is the key to the nested sum.

---

### Q15. Complex numbers \(z_1,z_2,z_3\) have equal magnitude and satisfy

$$z_1+z_2+z_3=-\frac{\sqrt3}{2}-i\sqrt5,\qquad z_1z_2z_3=\sqrt3+i\sqrt5.$$

For \(z_j=x_j+iy_j\), evaluate \(\dfrac{16}{5}(x_1y_1+x_2y_2+x_3y_3)^2\).

**Answer: 3**

#### Approach 1 — Symmetric sums and conjugation

Let \(S=z_1+z_2+z_3\), \(P=z_1z_2z_3\), and \(|z_j|=r\). Then

$$r^3=|P|=2\sqrt2\Rightarrow r=\sqrt2,\qquad \sum_j\frac1{z_j}=\frac{\overline S}{r^2}=\frac{\overline S}{2}.$$

Thus the second elementary symmetric sum is \(e_2=P\overline S/2=-13/4+i\sqrt{15}/4\), while \(S^2=-17/4+i\sqrt{15}\). Therefore

$$\sum_jz_j^2=S^2-2e_2=\frac94+i\frac{\sqrt{15}}2.$$

Since \(\operatorname{Im}(z_j^2)=2x_jy_j\), \(x_1y_1+x_2y_2+x_3y_3=\sqrt{15}/4\). The requested value is \((16/5)(15/16)=3\).

#### Approach 2 — Use the equal-modulus constraint first

The equal-modulus condition is essential: it gives \(1/z_j=\bar z_j/2\), which determines \(e_2=P\sum1/z_j\) from the supplied sum and product. No individual root needs to be found.

> [!tip] Exam Shortcut
> For equal-modulus roots, turn reciprocal sums into conjugate sums using \(1/z=\bar z/r^2\).

> [!warning] Common Pitfall
> \(\operatorname{Im}(z_1^2+z_2^2+z_3^2)\) is **twice** the requested sum of \(x_jy_j\).

> [!success] Key Takeaway
> Elementary symmetric functions can recover a sum of squares without solving for the individual complex numbers.

---

### Q16. With \({}^{n}C_r=\binom nr\), define

$$A=\sum_{r=1}^{50}\frac{\binom{50+r}{r}(2r-1)}{\binom{50}{r}(50+r)},\quad
B=\sum_{r=0}^{50}\binom{50}{r}^{\!2},\quad
C=50\sum_{r=1}^{49}\frac{2r^2-48r+1}{(50-r)\binom{50}{r}}.$$

Find \(A-B+C\).

**Answer: 2498**

#### Approach 1 — Telescope all three sums

For \(A\), let \(V(r)=\binom{50+r}{r}/\binom{50}{r}\). The summand becomes \(V(r)-V(r-1)\), because

$$2r-1=(50+r)-(50-r+1).$$

Hence \(A=V(50)-V(0)=\binom{100}{50}-1\). Vandermonde's identity gives \(B=\binom{100}{50}\), so \(A-B=-1\).

For \(C\), use \(2r^2-48r+1=(r+1)^2-r(50-r)\) and \((50-r)\binom{50}{r}=(r+1)\binom{50}{r+1}\). Then

$$C=50\sum_{r=1}^{49}\left(\frac{r+1}{\binom{50}{r+1}}-\frac r{\binom{50}{r}}\right)
=50\left(\frac{50}{\binom{50}{50}}-\frac1{\binom{50}{1}}\right)=2499.$$

Thus \(A-B+C=-1+2499=2498\).

#### Approach 2 — What to notice

The enormous central binomial terms in \(A\) and \(B\) cancel exactly; the remaining rational-looking sum \(C\) is itself a telescoping difference. Keep the cancellation symbolic instead of evaluating large integers.

> [!tip] Exam Shortcut
> Look for consecutive-binomial ratios and rewrite each summand as \(V(r)-V(r-1)\).

> [!warning] Common Pitfall
> In \(C\), the factor \(\binom{50}{r}\) is in the denominator. The numerator identity must be split before applying the binomial relation.

> [!success] Key Takeaway
> Telescoping can hide inside complicated binomial quotients; simplify ratios before summing.

---

### Q17. The polynomial

$$P(x)=(1+x+x^2+\cdots+x^{17})^2-x^{17}$$

has 34 distinct complex roots \(z_k=r_ke^{2\pi i a_k}\), with \(0<a_1<\cdots<a_{34}<1\). If \(a_1+\cdots+a_5=m/n\) in lowest terms, find \(m+n\).

**Answer: 482**

#### Approach 1 — Show every root lies on the unit circle

Write \(x=e^{2i\phi}\). Then

$$1+x+\cdots+x^{17}=e^{17i\phi}\frac{\sin(18\phi)}{\sin\phi}.$$

The equation \(P(x)=0\) becomes \(\sin(18\phi)=\pm\sin\phi\). With \(a=\phi/\pi\), the solutions in \((0,1)\) are

$$a=\frac{2j}{17}\ (j=1,\ldots,8),\quad a=\frac{1+2j}{17}\ (j=0,\ldots,7),$$
$$a=\frac{2j}{19}\ (j=1,\ldots,9),\quad a=\frac{1+2j}{19}\ (j=0,\ldots,8).$$

These are 34 distinct roots, the degree of \(P\), so they are all the roots. The five smallest are

$$\frac1{19},\quad\frac1{17},\quad\frac2{19},\quad\frac2{17},\quad\frac3{19}.$$

Their sum is \(6/19+3/17=159/323\), so \(m+n=159+323=482\).

#### Approach 2 — Root count sanity check

The four families contain \(8+8+9+9=34\) angles. None overlap in \((0,1)\) (the numerator parity and denominators 17,19 prevent equality), confirming that the unit-circle construction accounts for the full degree.

> [!tip] Exam Shortcut
> For a reciprocal-looking polynomial, divide by the middle power and use the finite geometric-sum identity on \(|x|=1\).

> [!warning] Common Pitfall
> The apparent solution \(a=0\) from the sine equation is extraneous: \(P(1)=18^2-1\ne0\).

> [!success] Key Takeaway
> Trigonometric factorization turns a degree-34 root problem into four simple rational-angle families.

---

# PART 2: PHYSICS

## SECTION I (i) — Single Correct

### Q18. Three identical parallel metal plates have area \(S\) and adjacent spacing \(d\). A battery of emf \(\varepsilon\) is connected between plates 2 and 3 (positive to plate 3); plate 1 is given charge \(q_0\), then a switch connects plates 1 and 3. Find the final charge on plate 3.

(A) \(q_0/2-\varepsilon_0S\varepsilon/d\) (B) \(q_0+\varepsilon_0S\varepsilon/d\)<br>
(C) \(q_0/2+\varepsilon_0S\varepsilon/d\) (D) \(q_0/2+2\varepsilon_0S\varepsilon/d\)

**Answer: (C)**

#### Approach 1 — Common-mode charge plus battery charge

Let \(C=\varepsilon_0S/d\). After closing the switch, \(V_1=V_3\), while the battery fixes \(V_3-V_2=\varepsilon\). Since the gaps are equal, the fields are \(E_{12}=+\varepsilon/d\) and \(E_{23}=-\varepsilon/d\). The total charge on the three-plate system is \(q_0\), so planar symmetry leaves \(q_0/2\) on each exterior face. The plate-3 face toward plate 2 carries an additional \(\varepsilon_0S|E_{23}|=C\varepsilon\). Thus

$$q_3=\frac{q_0}{2}+C\varepsilon=\frac{q_0}{2}+\frac{\varepsilon_0S\varepsilon}{d}.$$

#### Approach 2 — Superposition

Separate the final state into (i) the common excess charge shared by the connected plates 1 and 3, and (ii) the differential charge induced by the ideal battery across one plate gap. The two contributions add on plate 3, giving the same result.

> [!tip] Exam Shortcut
> For a large parallel-plate gap, use \(Q=C\Delta V\) with \(C=\varepsilon_0S/d\).

> [!warning] Common Pitfall
> The battery-controlled charge is the charge on **one facing surface** in gap 2–3, not twice that value.

> [!success] Key Takeaway
> A connected symmetric conductor shares common-mode charge; the battery adds a separate capacitor charge.

---

### Q19. A 10 Ω resistor at 20 °C has temperature coefficient \(5.0\times10^{-3}\,\mathrm K^{-1}\). It is in series with a 10 Ω internal resistance and a 60 V battery. Heat loss is \(0.40(T-20)\) W. With \(x=1+0.005(T-20)\), equilibrium requires \(2x^3+2x^2-11x-2=0\), whose roots are \(2,(-3+\sqrt7)/2,(-3-\sqrt7)/2\). Find the physical equilibrium temperature.

(A) 120 °C (B) 170 °C (C) 220 °C (D) 270 °C

**Answer: (C) 220 °C**

#### Approach 1 — Select the physical root

Because \(R(T)=10x\,\Omega\) and the resistor is above ambient, the physical root must have \(x\ge1\). Of the three roots, only \(x=2\) satisfies this. Thus

$$T=20+\frac{x-1}{0.005}=20+200=220^\circ\mathrm C.$$

#### Approach 2 — Check with the power balance

At \(x=2\), \(R=20\,\Omega\). The current is \(60/(10+20)=2\) A, so resistor heating is \(I^2R=80\) W. The heat loss is \(0.40(220-20)=80\) W, verifying equilibrium.

> [!tip] Exam Shortcut
> The cubic is supplied; reject roots that give negative resistance or a temperature below ambient before doing extra algebra.

> [!warning] Common Pitfall
> Do not interpret every algebraic root as a thermodynamic state. The linear resistance model is physically meaningful here only for the positive-resistance branch.

> [!success] Key Takeaway
> A substituted variable is not automatically physical; always translate it back to temperature and resistance.

---

### Q20. A galvanometer has \(G_0=100\,\Omega\), \(I_g=2.0\) mA, and \(\alpha_g=4.0\times10^{-3}\,\mathrm K^{-1}\). Series resistors \(R_1,R_2\) have coefficients \(\alpha_1=2.0\times10^{-3}\,\mathrm K^{-1}\), \(\alpha_2=-1.0\times10^{-3}\,\mathrm K^{-1}\). The instrument is a 13 V voltmeter at 20 °C and its range is temperature-independent to first order. Find \((R_1,R_2)\).

(A) (2.0, 4.4) kΩ (B) (2.4, 4.0) kΩ (C) (3.2, 3.2) kΩ (D) (4.4, 2.0) kΩ

**Answer: (A) \(R_1=2.0\) kΩ, \(R_2=4.4\) kΩ**

#### Approach 1 — Range and temperature constraints

At 20 °C, the required total resistance is \(13/I_g=6500\,\Omega\). Thus \(R_1+R_2=6400\,\Omega\). First-order temperature independence requires the temperature derivative of the total series resistance to vanish:

$$\alpha_gG_0+\alpha_1R_1+\alpha_2R_2=0,$$
$$0.4+0.002R_1-0.001R_2=0.$$

Together with \(R_1+R_2=6400\), this gives \(R_1=2000\,\Omega\), \(R_2=4400\,\Omega\).

#### Approach 2 — Weighted-coefficient check

The positive temperature drift of the coil and \(R_1\) must be cancelled by the negative drift of \(R_2\). The pair (2.0,4.4) kΩ gives \(0.4+4.0-4.4=0\,\Omega/\mathrm K\), and its sum is 6.4 kΩ.

> [!tip] Exam Shortcut
> A first-order compensation condition is a weighted sum \(\sum \alpha_iR_i=0\), not an unweighted sum of coefficients.

> [!warning] Common Pitfall
> Include the galvanometer coil's own temperature coefficient; the compensating resistors do not act alone.

> [!success] Key Takeaway
> The instrument's full-scale voltage is constant when the total series resistance has zero first derivative with temperature.

---

### Q21. Twelve equal resistors \(R\) form an octahedral network. The ohmmeter terminals are at the bottom pole and a neighbouring equatorial vertex. Find the equivalent resistance.

(A) \(5R/12\) (B) \(12R/5\) (C) \(10R/19\) (D) \(19R/10\)

**Answer: (A) \(5R/12\)**

#### Approach 1 — Symmetry and nodal potentials

Set the terminal potentials to 0 and 1 V. Let the top pole be at \(t\), the two symmetric equatorial vertices at \(u\), and the equatorial vertex opposite the 1 V terminal at \(w\). With every edge resistance set temporarily to 1 Ω, KCL gives

$$4t=1+2u+w,\qquad 4u=1+t+w,\qquad4w=t+2u.$$

Solving gives \(t=0.6\), \(u=0.5\), \(w=0.4\). The current leaving the 1 V terminal is

$$I=(1-0)+(1-t)+2(1-u)=1+0.4+1=2.4\ \mathrm A.$$

So \(R_{\rm eq}=1/2.4=5/12\,\Omega\). Restoring the common edge resistance gives \(5R/12\).

```tikz
\begin{document}
\begin{tikzpicture}[scale=1.0, every node/.style={circle,fill=black,inner sep=2pt}]
  \coordinate (T) at (0,2.8); \coordinate (B) at (0,-2.8);
  \coordinate (L) at (-2.6,0); \coordinate (R) at (2.6,0);
  \coordinate (U) at (0.9,0.65); \coordinate (D) at (-0.9,-0.65);
  \draw (T)--(L) (T)--(U) (T)--(R) (T)--(D);
  \draw (B)--(L) (B)--(U) (B)--(R) (B)--(D);
  \draw (L)--(U)--(R)--(D)--cycle;
  \foreach \p in {T,B,L,R,U,D} \node at (\p) {};
  \draw[thick,blue] (R)--(3.5,0) node[right,black,fill=none] {terminal};
  \draw[thick,blue] (B)--(0,-3.5) node[below,black,fill=none] {terminal};
\end{tikzpicture}
\end{document}
```

#### Approach 2 — Effective-conductance check

The 1 V source supplies 2.4 A when each edge is 1 Ω, so the effective conductance is 2.4 S and the resistance is its reciprocal. This is an adjacent-vertex pair; the opposite-vertex resistance would be different.

> [!tip] Exam Shortcut
> Use symmetry to merge equal-potential nodes, or solve only the three distinct internal potentials.

> [!warning] Common Pitfall
> The terminals are adjacent vertices, not the two opposite poles of the octahedron.

> [!success] Key Takeaway
> A unit-voltage nodal calculation gives the effective conductance directly: \(R_{\rm eq}=V/I\).

---

## SECTION I (ii) — Multiple Correct

### Q22. An isolated capacitor carries fixed charges \(+Q,-Q\). A dielectric of permittivity \(\varepsilon\) is inserted in three configurations: (a) full plate area, thickness \(h\); (b) partial area \(\ell\sqrt S\), full gap; (c) partial area \(\ell\sqrt S\), thickness \(h\). Which statements about the dielectric fields \(E_a,E_b,E_c\) are correct?

(A) In (a) the normal electric field is the same in air and dielectric, hence \(E_a=Q/(\varepsilon S)\).<br>
(B) In (b), \(E_b=Q/[\varepsilon\ell\sqrt S+\varepsilon_0(S-\ell\sqrt S)]\).<br>
(C) In (c), \(E_c=Q/[\varepsilon\ell\sqrt S+(S-\ell\sqrt S)\{\varepsilon(d-h)+\varepsilon_0h\}/d]\).<br>
(D) In (c), increasing \(h\) does not alter the field inside the dielectric.

**Answer: (B), (C)**

#### Approach 1 — Displacement field and equivalent capacitance

**(A) False.** The normal component of electric displacement \(D\), not electric field \(E\), is continuous across an air–dielectric boundary without free surface charge. In (a), \(D=Q/S\), so the dielectric field is indeed \(Q/(\varepsilon S)\), but the stated reason (“the normal electric field remains the same”) is false; therefore the complete statement is false.

**(B) True.** The air and dielectric portions are parallel capacitors. Their common field is

$$E_b=\frac{Q}{\varepsilon A_d+\varepsilon_0(S-A_d)},\qquad A_d=\ell\sqrt S.$$

**(C) True.** In the covered area, air and dielectric layers are in series; the uncovered area is an air capacitor in parallel. Using \(Q=E_c[\varepsilon A_d+(S-A_d)(\varepsilon(d-h)+\varepsilon_0h)/d]\) gives the printed expression.

**(D) False.** The denominator in (C) depends on \(h\) whenever an uncovered air area remains, so \(E_c\) generally changes with thickness.

#### Approach 2 — Boundary-condition check

Compare fields across interfaces: normal \(D\) is continuous, while \(E=D/\varepsilon\) changes with permittivity. This immediately rejects (A); the parallel/series capacitor models then verify (B),(C) and reject (D).

> [!tip] Exam Shortcut
> Separate the geometries: side-by-side regions are parallel; stacked layers are series.

> [!warning] Common Pitfall
> “Same normal field” is not a valid dielectric boundary condition. Do not mark (A) true solely because its final formula happens to be right.

> [!success] Key Takeaway
> Fixed total charge means compute the equivalent capacitance and use the local voltage/displacement to recover the field.

---

### Q23. Five identical 6 V, 0.3 A bulbs are wired as follows: \(L_1\) from A to node X, \(L_2\) from X to Y, \(L_3\) from Y to B, \(L_4\) from A to Y, and \(L_5\) from X to B. A 12 V ideal battery is connected across A–B. An intact bulb has its rated ohmic resistance. Which statements are correct?

(A) With all bulbs, \(L_2\) is dark and \(L_1,L_3,L_4,L_5\) glow normally.<br>
(B) Removing \(L_2\) leaves the other bulbs' currents and brightness unchanged.<br>
(C) Removing \(L_1\) gives \((V_{L_2},V_{L_3},V_{L_4},V_{L_5})=(2.4,4.8,7.2,2.4)\) V.<br>
(D) Removing \(L_4\) makes \(L_1\) exceed 8.5 V and burn out.

**Answer: (A), (B), (C)**

Each bulb's resistance is \(R=6/0.3=20\,\Omega\).

#### Approach 1 — Nodal analysis

With all bulbs intact and A=12 V, B=0 V, KCL at X,Y gives \(3V_X-V_Y=12\) and \(3V_Y-V_X=12\). Thus \(V_X=V_Y=6\) V. So \(L_2\) has zero voltage, while the other four each have 6 V: (A) true. Removing a zero-current branch \(L_2\) changes nothing: (B) true.

If \(L_1\) is removed, \(L_4\) is in series with \([L_3\parallel(L_2+L_5)]\):

$$R_{YB}=20\parallel40=\frac{40}{3}\,\Omega,\quad R_{AB}=20+\frac{40}{3}=\frac{100}{3}\,\Omega,\quad I=0.36\,\mathrm A.$$

Therefore \(V_{L_4}=7.2\) V, node Y is at 4.8 V, and the series pair \(L_2,L_5\) divides that equally: 2.4 V each. \(L_3\) has 4.8 V. This verifies (C).

If \(L_4\) is removed, the symmetric reduction gives \(V_{L_1}=7.2\) V, below 8.5 V. Thus (D) is false.

```tikz
\usepackage{circuitikz}
\begin{document}
\begin{circuitikz}
  \draw (0,0) to[battery1,l=$12\,\mathrm V$] (0,3)
    -- (0.6,3) to[lamp,l=$L_1$] (2.2,3)
    -- (2.6,3) to[lamp,l=$L_2$] (4.2,3)
    -- (4.6,3) to[lamp,l=$L_3$] (6.2,3) -- (7,3) -- (7,0) -- (0,0);
  \draw (0,3) -- (0,4.5) to[lamp,l=$L_4$] (4.6,4.5) -- (4.6,3);
  \draw (2.6,3) -- (2.6,1.5) to[lamp,l=$L_5$] (7,1.5) -- (7,3);
  \node[left] at (0,3) {A}; \node[right] at (7,3) {B};
\end{circuitikz}
\end{document}
```

#### Approach 2 — Symmetry check

The bridge is balanced when all five branches are present: the two equal-voltage divider arms force X and Y both to 6 V, so the bridge bulb carries no current. A broken outer bulb destroys that balance, so recompute the changed network rather than assuming the original voltages persist.

> [!tip] Exam Shortcut
> Rated resistance is \(R=V^2/P=6/0.3=20\,\Omega\). Compare each calculated voltage directly with 6 V and 8.5 V.

> [!warning] Common Pitfall
> A dark bulb in the intact bridge is not an open circuit; it is an intact zero-voltage branch. Removing it happens to leave the remaining topology equivalent, but only because it carried no current.

> [!success] Key Takeaway
> A nonlinear brightness description can be handled with an ohmic network first, then classified by each bulb's voltage.

---

### Q24. Capacitors have \(C_1=3\,\mu\mathrm F\), \(C_2=6\,\mu\mathrm F\), \(C_3=12\,\mu\mathrm F\), \(C_4=6\,\mu\mathrm F\), and a 15 V battery. With switch A closed and B open, then B is closed while A stays closed, decide which statements are true:

(A) Initially \(C_{\rm eq}=30/13\,\mu\mathrm F\) and \(U=3375/13\,\mu\mathrm J\).<br>
(B) Initially \((Q_1,Q_2,Q_3,Q_4)=(450,180,180,270)/13\,\mu\mathrm C\).<br>
(C) Closing B shorts \(C_2\) and increases stored energy by \(2700/91\,\mu\mathrm J\).<br>
(D) The battery supplies an additional \(360/91\,\mu\mathrm C\).

**Answer: (A), (B), (C), (D)**

#### Approach 1 — Reduce the network in each switch state

With B open, \(C_2\) and \(C_3\) are in series, giving 4 μF. This is in parallel with \(C_4=6\) μF, and that 10 μF combination is in series with \(C_1=3\) μF:

$$C_{\rm eq}=\frac{3\cdot10}{3+10}=\frac{30}{13}\,\mu\mathrm F,\quad U=\frac12C_{\rm eq}V^2=\frac{3375}{13}\,\mu\mathrm J.$$

The series charge is \(Q_1=C_{\rm eq}V=450/13\,\mu\mathrm C\). The parallel section has 45/13 V across it, so \(Q_4=6(45/13)=270/13\) μC. The C2–C3 series branch carries \(4(45/13)=180/13\) μC on each capacitor. Hence (A),(B) are true.

Closing B shorts C2. The new network is C1 in series with \(C_3+C_4=18\) μF:

$$C_{\rm new}=\frac{3\cdot18}{3+18}=\frac{18}{7}\,\mu\mathrm F,\quad
U_{\rm new}=\frac{2025}{7}\,\mu\mathrm J.$$

Thus \(\Delta U=2025/7-3375/13=2700/91\,\mu\mathrm J\). The battery remains connected, so its net supplied charge is

$$\Delta Q=15\left(\frac{18}{7}-\frac{30}{13}\right)=\frac{360}{91}\,\mu\mathrm C.$$

All four are true.

#### Approach 2 — Charge and energy consistency

The final equivalent capacitance is larger than the initial value, so with fixed battery voltage both total charge and stored energy increase. Their exact increments above reproduce the stated fractions.

> [!tip] Exam Shortcut
> Track the capacitor network as two separate equivalent circuits: before and after B closes.

> [!warning] Common Pitfall
> The network is **not isolated** during redistribution—the battery stays connected. Charge and energy of the capacitor subsystem need not be conserved.

> [!success] Key Takeaway
> Charge is conserved only on isolated conductor junctions; source-connected terminals exchange charge with the battery.

---

## SECTION II (i) — Numerical (Common Thermal-Hysteresis Data)

At 60 V, the element is at a steady 80 °C while in the 50 Ω state. Its heat capacity is \(C_{\rm th}=3\,\mathrm{J\,K^{-1}}\), ambient temperature 20 °C, and heat loss is \(k(T-20)\). At 80 V it heats from 99 to 100 °C at 50 Ω and cools from 100 to 99 °C at 100 Ω.

### Q25. Find the period of the self-sustained oscillation (two decimal places).

**Answer: 0.19 s** (accepted range 0.18–0.20 s)

#### Approach 1 — Integrate the thermal balance in each state

At 60 V and 50 Ω, steady power is \(60^2/50=72\) W, so \(72=60k\), hence \(k=1.2\,\mathrm{W\,K^{-1}}\). At 80 V, the heating-state power is 128 W and its equilibrium temperature would be \(T_{\infty,h}=20+128/1.2=126.667^\circ\mathrm C\). Therefore

$$t_h=\frac{C_{\rm th}}k\ln\frac{T_{\infty,h}-99}{T_{\infty,h}-100}=2.5\ln\frac{83}{80}.$$

In the 100 Ω cooling state, power is 64 W and \(T_{\infty,c}=20+64/1.2=73.333^\circ\mathrm C\). Thus

$$t_c=2.5\ln\frac{100-T_{\infty,c}}{99-T_{\infty,c}}=2.5\ln\frac{80}{77}.$$

So \(t_h+t_c=2.5\ln(83/77)=0.18759\ldots\) s, which rounds to **0.19 s**.

#### Approach 2 — Use the supplied small-log approximation

Because the swing is only 1 K,

$$t_h\simeq2.5\frac{3}{80}=0.0938\,\mathrm s,\qquad t_c\simeq2.5\frac{3}{77}=0.0974\,\mathrm s,$$

so the period is about 0.191 s, consistent with the exact logarithmic result.

> [!tip] Exam Shortcut
> The thermal time constant is \(C_{\rm th}/k=2.5\) s; for a 1 K excursion, linearize the logarithm as permitted.

> [!warning] Common Pitfall
> Use different Joule powers in the two hysteresis branches: 128 W at 50 Ω and 64 W at 100 Ω.

> [!success] Key Takeaway
> Each constant-resistance branch obeys \(C_{\rm th}\dot T=P-k(T-20)\); the period is the sum of the heating and cooling times.

---

### Q26. Find the maximum current during the oscillation.

**Answer: 1.60 A**

#### Approach 1 — Compare the two resistor states

The voltage is fixed at 80 V. Current is greatest in the lower-resistance, 50 Ω heating branch:

$$I_{\max}=\frac{80}{50}=1.60\,\mathrm A.$$

The cooling-state current is only \(80/100=0.80\) A.

#### Approach 2 — Use the two-state bound

The element switches only between 50 Ω and 100 Ω while the source remains at 80 V. Thus its only steady-branch current values are 1.60 A and 0.80 A; the larger value is necessarily the maximum.

> [!tip] Exam Shortcut
> At fixed voltage, the maximum current occurs at the minimum resistance.

> [!warning] Common Pitfall
> Do not use the 60 V calibration voltage; the oscillation occurs after the source is changed to 80 V.

> [!success] Key Takeaway
> The thermal dynamics determine the switching times, but the instantaneous current is simply \(V/R\) in each state.

---

## SECTION II (i) — Numerical (Common Conducting-Liquid Data)

A glass capacitor of thickness \(h=0.50\) mm and dielectric constant \(\varepsilon_r=7\) is in series with a fixed reference capacitor. A connected conducting drop spreads when the source reaches \(U_1=5.90\) kV. At the slope change, \(U_C=U_1/3\); during spreading the voltage across the glass capacitor remains at its threshold value. Use \(\varepsilon_0=8.85\times10^{-12}\,\mathrm{F\,m^{-1}}\).

### Q27. Find \(U_C\) when the source is raised to \(2U_1\).

**Answer: 7.87 kV**

#### Approach 1 — Pin the glass-capacitor voltage at threshold

At onset,

$$U_{g,\rm th}=U_1-U_C=U_1-\frac{U_1}{3}=\frac{2U_1}{3}.$$

During spreading this glass voltage stays fixed. At \(U=2U_1\), the reference-capacitor voltage is therefore

$$U_C=2U_1-\frac{2U_1}{3}=\frac{4U_1}{3}=7.8667\,\mathrm{kV}\simeq7.87\,\mathrm{kV}.$$

#### Approach 2 — Read the graph in two regimes

Before spreading, the plotted slope is fixed. After the kink, the glass voltage is clamped and each further increment in source voltage appears across the reference capacitor. Apply this to the interval from \(U_1\) to \(2U_1\).

> [!tip] Exam Shortcut
> The kink gives the threshold voltage directly: source voltage minus the measured reference voltage.

> [!warning] Common Pitfall
> The glass voltage is not \(U_1\) at the kink; it is \(U_1-U_C=2U_1/3\).

> [!success] Key Takeaway
> Once the drop spreads, the threshold condition fixes one series-capacitor voltage while the other takes the source's additional voltage.

---

### Q28. Find the liquid surface-tension coefficient \(\sigma\) in N m⁻¹.

**Answer: 0.48 N m⁻¹**

#### Approach 1 — Balance electric free-energy gain and surface-energy cost

The threshold glass voltage is \(U_g=2U_1/3=3.9333\) kV. Increasing the covered area by \(dA\) increases capacitance by \(dC=(\varepsilon_0\varepsilon_r/h)dA\). At fixed voltage, the electrical driving free-energy change per area is \(\tfrac12(\varepsilon_0\varepsilon_r/h)U_g^2\). With the two equal interface-tension contributions, the surface-energy cost is \(2\sigma\) per area. At equilibrium,

$$2\sigma=\frac12\frac{\varepsilon_0\varepsilon_r}{h}U_g^2,
\qquad \sigma=\frac{\varepsilon_0\varepsilon_rU_g^2}{4h}.$$

Substitution gives \(\sigma=0.4796\,\mathrm{N\,m^{-1}}\), or **0.48 N m⁻¹**.

#### Approach 2 — Dimensional and magnitude check

\(\varepsilon_0U_g^2/h\) has units \((\mathrm{F/m})\mathrm V^2/\mathrm m=\mathrm{J/m^2=N/m}\), the correct units for surface tension. The factor \(\varepsilon_r/4\) gives the stated magnitude.

> [!tip] Exam Shortcut
> First find the actual glass voltage at onset; use that voltage—not the full source voltage—in the capacitor energy.

> [!warning] Common Pitfall
> The fixed reference capacitor is not part of the local capacitance-per-area change; it only determines the measured voltage division.

> [!success] Key Takeaway
> Spreading is driven by the decrease in fixed-voltage capacitor free energy and opposed by the increase in interfacial energy.

---

## SECTION II (ii) — Numerical

### Q29. Three batteries of emfs 6, 5, and 3 V and internal resistances 2, 1, and 4 Ω form a clockwise-aiding ring A–B–C–A. Capacitors \(C_1=1\), \(C_2=5\), \(C_3=6\) μF connect A, B, C respectively to a shared isolated inner conductor O. A charge of +48 μC is deposited on O. Find the magnitude of the final charge on \(C_3\).

**Answer: 14 μC**

#### Approach 1 — Ring current, node potentials, and charge conservation

The steady ring current is

$$I=\frac{6+5+3}{2+1+4}=2\,\mathrm A$$

clockwise. The terminal rises are \(V_B-V_A=6-2(2)=2\) V and \(V_C-V_B=5-2(1)=3\) V. Set \(V_A=0\); then \(V_B=2\) V, \(V_C=5\) V.

The net charge on the common inner conductor is

$$48=\sum_i C_i(V_O-V_i)=12V_O-(1\cdot0+5\cdot2+6\cdot5),$$

with μC and μF units understood. Hence \(V_O=88/12=22/3\) V, so

$$|Q_3|=C_3|V_O-V_C|=6\left|\frac{22}{3}-5\right|=14\,\mu\mathrm C.$$

#### Approach 2 — Use only potential differences

The source/internal-resistance loop fixes \(V_C-V_A=5\) V. The weighted mean \(\sum C_iV_i/\sum C_i=40/12\) V and the net O-charge shift \(48/12=4\) V give \(V_O=40/12+4=22/3\) V, leading to the same C3 charge.

> [!tip] Exam Shortcut
> Solve the battery ring first; at DC steady state the capacitors do not carry ring current, but they still determine O's potential through charge balance.

> [!warning] Common Pitfall
> The ideal EMFs add to 14 V, but the internal resistors carry a 2 A loop current. Do not set the node-to-node drops equal to the EMFs alone.

> [!success] Key Takeaway
> A floating common electrode satisfies \(Q_O=\sum_i C_i(V_O-V_i)\); its potential is a capacitance-weighted average plus the net-charge offset.

---

### Q30. Four parallel branches connect A–B: a 6 Ω resistor in series with a 60 V cell, a 4 Ω resistor with a 24 V cell, a 12 Ω resistor alone, and a 3 Ω resistor with a 30 V cell. The cell positives face A. Find the maximum power deliverable to a variable load across A–B (nearest watt).

**Answer: 203 W**

#### Approach 1 — Thevenin equivalent

With the load open, KCL at A gives

$$V_{\rm th}\left(\frac16+\frac14+\frac1{12}+\frac13\right)=\frac{60}{6}+\frac{24}{4}+\frac{30}{3}=26.$$

The total conductance is \(5/6\) S, so \(V_{\rm th}=31.2\) V. Suppressing ideal voltage sources gives

$$R_{\rm th}=6\parallel4\parallel12\parallel3=\frac65=1.2\,\Omega.$$

Maximum power occurs at \(R_L=R_{\rm th}\):

$$P_{\max}=\frac{V_{\rm th}^2}{4R_{\rm th}}=202.8\,\mathrm W\simeq203\,\mathrm W.$$

#### Approach 2 — Norton check

The Norton current is \(I_N=V_{\rm th}/R_{\rm th}=26\) A. A matched load receives \(I_N/2=13\) A at \(V=15.6\) V, so \(P=VI=202.8\) W.

> [!tip] Exam Shortcut
> Once the Thevenin pair is found, use \(P_{\max}=V_{\rm th}^2/(4R_{\rm th})\); do not optimize the load algebraically.

> [!warning] Common Pitfall
> The 12 Ω branch has no cell but still contributes conductance when finding both the open-circuit voltage and Thevenin resistance.

> [!success] Key Takeaway
> Multiple parallel source branches reduce to a conductance-weighted source voltage and the parallel resistance.

---

### Q31. A metal conductor of length 1 m has cross-section \(A(x)=A_0(1+x/L)^2\), \(A_0=1.0\) mm². Its density is \(8.0\times10^3\) kg m⁻³, molar mass 64 g mol⁻¹, valence 1, and it carries 3.84 A at 0.20 V. Find the electron mobility in cm² V⁻¹ s⁻¹ (nearest integer). Use \(N_A=6.0\times10^{23}\), \(e=1.6\times10^{-19}\) C.

**Answer: 8 cm² V⁻¹ s⁻¹**

#### Approach 1 — Integrate the nonuniform resistance

For constant resistivity \(\rho\),

$$R=\int_0^L\frac{\rho\,dx}{A_0(1+x/L)^2}=\frac{\rho L}{2A_0}.$$

Measured resistance is \(0.20/3.84=0.0520833\,\Omega\), so \(\rho=2A_0R/L=1.04167\times10^{-7}\,\Omega\,\mathrm m\), and \(\sigma=1/\rho=9.60\times10^6\) S m⁻¹.

The electron density is

$$n=\frac{8000}{0.064}N_A=7.5\times10^{28}\,\mathrm m^{-3}.$$

Using \(\sigma=ne\mu\), \(\mu=8.0\times10^{-4}\,\mathrm{m^2V^{-1}s^{-1}}=8.0\,\mathrm{cm^2V^{-1}s^{-1}}\).

#### Approach 2 — Unit check

\(\sigma/(ne)\) has units \(\mathrm{(S/m)/(C/m^3)}=\mathrm{m^2/(V\,s)}\); converting m² to cm² multiplies by \(10^4\).

> [!tip] Exam Shortcut
> Integrate \(1/A(x)\), not \(A(x)\); infinitesimal wire slices are in series.

> [!warning] Common Pitfall
> The conductor is monovalent, so each atom contributes exactly one carrier; do not multiply \(n\) by an extra valence factor.

> [!success] Key Takeaway
> Mobility is obtained from the macroscopic conductivity through \(\sigma=ne\mu\), after accounting for the nonuniform geometry.

---

### Q32. A metre-bridge wire has \(A(x)=A_0/(1+\alpha x/L)\), with \(L=100\) cm and unknown positive \(\alpha\). With X left and 10 Ω right, balance is at 50.0 cm. After interchanging the gaps without reversing the wire, balance is at 72.47 cm. Find X.

**Answer: 6 Ω**

#### Approach 1 — Integrate the resistance density

Since \(dR=\rho dx/A(x)\), the resistance from 0 to \(uL\) is proportional to \(u+\alpha u^2/2\); the remaining section is proportional to \((1-u)+\alpha(1-u^2)/2\). At \(u=1/2\),

$$\frac X{10}=\frac{4+\alpha}{4+3\alpha}.$$

After swapping, with \(u=0.7247\),

$$\frac{10}{X}=\frac{u+\alpha u^2/2}{(1-u)+\alpha(1-u^2)/2}.$$

Solving gives \(\alpha\simeq2\) (the printed length is rounded) and \(X/10\simeq0.6\). Hence \(X=6\,\Omega\).

#### Approach 2 — Check the chosen balance length

For \(\alpha=2\), the resistance density is proportional to \(1+2x/L\). The first half has resistance ratio \(3/5\) relative to the second half, so \(X=6\) Ω. After swapping, the balance fraction predicted by the same integral is \(u=(\sqrt6-1)/2=0.724745\ldots\), i.e. 72.47 cm as stated.

> [!tip] Exam Shortcut
> The bridge wire is not uniform in resistance per centimetre. Integrate \(\rho/A(x)\) to get the segment resistance.

> [!warning] Common Pitfall
> Do not use the uniform-wire rule \(X/10=\ell/(100-\ell)\); the cross-section varies with x.

> [!success] Key Takeaway
> A meter bridge still obeys the Wheatstone ratio, but each wire-arm resistance must be computed from its own integral.

---

### Q33. A 99 Ω galvanometer with full-scale current 1 mA is converted to a 100 mA ammeter using a uniform shunt. The shunt is cut into three equal lengths and those three pieces are connected in parallel. Find the new full-scale range in mA.

**Answer: 892 mA**

#### Approach 1 — Find and modify the shunt

The original shunt is

$$R_s=\frac{I_gG}{I-I_g}=\frac{(0.001)(99)}{0.100-0.001}=1\,\Omega.$$

Each third has resistance \(1/3\,\Omega\); three in parallel give \(R_s'=1/9\,\Omega\). Thus

$$I_{\rm new}=I_g\left(1+\frac{G}{R_s'}\right)=0.001(1+891)=0.892\,\mathrm A=892\,\mathrm{mA}.$$

#### Approach 2 — Scaling check

Cutting a wire into three equal lengths divides each resistance by 3; placing all three in parallel divides again by 3. The shunt becomes one ninth its original resistance, so the shunt current capacity rises by a factor of 9.

> [!tip] Exam Shortcut
> A uniform wire cut into n equal pieces and placed in parallel has resistance \(R/n^2\).

> [!warning] Common Pitfall
> Each piece is \(R/3\), not \(3R\); cutting a wire shortens its length.

> [!success] Key Takeaway
> Ammeter range follows from the fixed galvanometer voltage and the modified shunt resistance.

---

### Q34. A capacitor bridge has \(C_{AP}=2\), \(C_{PB}=5\), \(C_{AQ}=3\), \(C_{QB}=3\), and \(C_{PQ}=3\) μF. Find the equivalent capacitance between A and B.

**Answer: 3 μF**

#### Approach 1 — Floating-node charge balance

Set \(V_A=V\), \(V_B=0\), and let the isolated node potentials be \(V_P,V_Q\). Net charge at each floating node is zero:

$$2(V_P-V)+5V_P+3(V_P-V_Q)=0\Rightarrow10V_P-3V_Q=2V,$$
$$3(V_Q-V)+3V_Q+3(V_Q-V_P)=0\Rightarrow-3V_P+9V_Q=3V.$$

Solving gives \(V_P=V/3\), \(V_Q=4V/9\). Charge drawn from A is

$$Q_A=2(V-V_P)+3(V-V_Q)=3V,$$

so \(C_{\rm eq}=Q_A/V=3\,\mu\mathrm F\).

#### Approach 2 — Electrical-network analogy

At DC steady state the capacitor charge-balance equations have exactly the same form as KCL equations in a resistor network with conductances replaced by capacitances. Solving the two internal-node equations gives the same 3 μF input capacitance.

> [!tip] Exam Shortcut
> For each floating conductor, sum the signed plate charges and set the net to its initial value (zero here).

> [!warning] Common Pitfall
> The bridge is not balanced because \(2/5\ne3/3\); the P–Q capacitor cannot be discarded.

> [!success] Key Takeaway
> A capacitor bridge is solved by conservation of charge at its isolated internal nodes.

---

# PART 3: CHEMISTRY

## SECTION I (i) — Single Correct

### Q35. In the reaction sequence

$$\mathrm{C_7H_9N\xrightarrow[(pyridine)]{(CH_3CO)_2O}C_9H_{11}ON\xrightarrow{Fe/Br_2,\ then\ H^+/H_2O}C_7H_8NBr\xrightarrow{HNO_2,\ Cu/HBr}C_7H_6Br_2\xrightarrow{KMnO_4,\ then\ soda\ lime}p\text{-dibromobenzene}},$$

compound A gives a positive carbylamine test. Which statement is correct?

(A) A can be o-toluidine (shown). (B) A can be p-toluidine (shown).<br>
(C) The diazonium conversion uses the Sandmeyer reaction. (D) C is more basic than aniline.

**Answer: (A)**

#### Approach 1 — Identify the amine and follow directing effects

A has formula \(\mathrm{C_7H_9N}\) and gives the carbylamine test, so it must be a primary amine; the toluidine isomers are the relevant candidates. Acetylation protects \(-NH_2\) as \(-NHCOCH_3\). Bromination then occurs mainly at the para position relative to the protected amino group. The later diazotization replaces the amino group by Br; oxidation converts the methyl substituent to \(-COOH\), and soda lime removes that carboxyl carbon. The displayed o-toluidine route is consistent with the final para-dibromobenzene, so (A) is correct.

```smiles
Cc1ccccc1N
```

For comparison, the para isomer has its para site blocked by methyl:

```smiles
Cc1ccc(N)cc1
```

**(C) is false:** Cu powder/HBr is the Gattermann variant; Sandmeyer uses a cuprous salt such as CuBr/CuCl. **(D) is false:** the para-bromo substituent in C is net electron-withdrawing and lowers the availability of the aniline lone pair; the ortho substituent also imposes the usual steric/solvation penalty. C is not more basic than aniline.

#### Approach 2 — Use the end product as a structural constraint

The final product is para-dibromobenzene. Working backwards, one Br is introduced by bromination of the protected amine and the other replaces the diazonium group; the methyl-bearing carbon is then oxidized and removed. This restricts the starting substitution pattern and rules out the p-toluidine drawing, whose para position is already occupied.

> [!tip] Exam Shortcut
> Protect aniline-type \(-NH_2\) before electrophilic bromination; the acetamido group directs strongly to ortho/para, with para usually major.

> [!warning] Common Pitfall
> “Cu/HBr” as written is not the cuprous bromide reagent notation \(\mathrm{CuBr}\) used for Sandmeyer; the stated powder/acid system is Gattermann.

> [!success] Key Takeaway
> In multistep aromatic sequences, track substituent positions as well as formulas; the final ring substitution often identifies the starting isomer.

---

### Q36. Identify the monosaccharide represented in the disaccharide shown in the paper.

(A) Fischer projection with C2–C5 OH pattern right–left–right–left.<br>
(B) Its mirror-image Fischer projection, left–right–left–right.<br>
(C), (D) Ketose projections.

**Answer: (A)**

#### Approach 1 — Read the Haworth stereochemistry

Both residues in the drawing are aldohexopyranose rings. The \(\mathrm{CH_2OH}\) substituent is drawn down, identifying the L-series in the Haworth convention used. Reading the remaining substituents around the ring and translating “down in Haworth = right in Fischer” gives the C2–C5 pattern right–left–right–left: option (A), L-idose.

#### Approach 2 — Eliminate by functional group and configuration

Options (C) and (D) are ketoses, but each unit in the disaccharide is a pyranose aldose. Options (A) and (B) are enantiomeric aldoses; the down-oriented \(\mathrm{CH_2OH}\) group selects the L member, (A).

> [!tip] Exam Shortcut
> First locate the ring oxygen and anomeric carbon; then map each substituent's up/down orientation to the Fischer projection.

> [!warning] Common Pitfall
> Do not infer D/L from the anomeric OH or glycosidic-bond direction. D/L is set by the configuration at the highest-numbered chiral centre (the carbon bearing \(\mathrm{CH_2OH}\)).

> [!success] Key Takeaway
> Haworth–Fischer conversion is a stereochemical mapping, not a visual guess based only on the glycosidic bond.

---

### Q37. A colourless compound P, \(\mathrm{C_6H_7N}\), is sparingly soluble in water; it forms a soluble salt with mineral acid, gives a foul-smelling product with \(\mathrm{CHCl_3/KOH}\), gives an alkali-soluble Hinsberg product with \(\mathrm{PhSO_2Cl}\), and forms a red-orange azo dye after diazotization and coupling with β-naphthol. Which statement about P is correct?

(A) Acetylation gives benzanilide.<br>
(B) P cannot undergo Friedel–Crafts acylation.<br>
(C) P can be made by Gabriel phthalimide synthesis.<br>
(D) P and its diazonium salt give a yellow dye in alkaline medium.

**Answer: (B)**

#### Approach 1 — Identify P as aniline and test each claim

The formula and reactions identify P as aniline, \(\mathrm{C_6H_5NH_2}\).

- **(A) False:** acetic anhydride gives acetanilide, \(\mathrm{C_6H_5NHCOCH_3}\), not benzanilide.
- **(B) True:** aniline coordinates strongly to \(\mathrm{AlCl_3}\), forming a salt/complex that deactivates the ring; ordinary Friedel–Crafts acylation therefore fails.
- **(C) False:** Gabriel synthesis proceeds by \(S_N2\) alkylation and does not prepare aryl amines from aryl halides.
- **(D) False:** aniline coupling with its diazonium salt to form aniline yellow is carried out in mildly acidic conditions. Alkaline medium is used for β-naphthol coupling; excess alkali converts diazonium ions to less-coupling-active diazohydroxide/diazotate species.

#### Approach 2 — Check the reaction-test combination

The carbylamine and Hinsberg results show P is a primary amine; diazotization plus azo coupling establishes that it is aromatic. The formula \(\mathrm{C_6H_7N}\) then identifies aniline. Its Lewis-acid complexation explains the Friedel–Crafts exception (B).

> [!tip] Exam Shortcut
> Primary aromatic amine + \(\mathrm{CHCl_3/KOH}\) is the carbylamine test; diazotization at 0–5 °C is a fingerprint for aniline.

> [!warning] Common Pitfall
> Acetic anhydride gives an **acetyl** group. “Benzanilide” contains a benzoyl group and is not the product here.

> [!success] Key Takeaway
> Aniline's lone pair both activates the ring in electrophilic substitution and binds Lewis-acid catalysts strongly enough to block Friedel–Crafts chemistry.

---

### Q38. Which test can distinguish the pair?

(A) Glucose and fructose by Barfoed's test.<br>
(B) Ribose and mannose by Seliwanoff's test.<br>
(C) Valine and proline by Xanthoproteic test.<br>
(D) Alanine and insulin by Biuret test.

**Answer: (D)**

#### Approach 1 — Identify what each test detects

- **(A) False:** glucose and fructose are both monosaccharides and both reduce Barfoed's reagent.
- **(B) False:** ribose and mannose are aldoses; Seliwanoff distinguishes ketoses from aldoses, not these two aldoses.
- **(C) False:** Xanthoproteic detects aromatic rings (Tyr, Trp, Phe); valine and proline are both non-aromatic.
- **(D) True:** alanine has no peptide bonds and gives a negative Biuret test. Insulin is a polypeptide and gives the violet Biuret complex.

#### Approach 2 — Eliminate by the property each reagent detects

Barfoed's distinguishes monosaccharides from disaccharides, not two monosaccharides; Seliwanoff's distinguishes ketoses from aldoses; Xanthoproteic requires an aromatic residue. Only Biuret separates a free amino acid from a peptide/protein, so (D) is the unique correct choice.

> [!tip] Exam Shortcut
> Match each named test to its functional-group target before comparing the compounds.

> [!warning] Common Pitfall
> Seliwanoff's test is not a general pentose/hexose test; it is a rapid ketose/aldose distinction.

> [!success] Key Takeaway
> Biuret requires multiple peptide bonds, which distinguishes a free amino acid from a protein.

---

## SECTION I (ii) — Multiple Correct

### Q39. Salicin, a willow-bark glycoside, is hydrolysed with dilute HCl to a carbohydrate P and compound Q. Which statements are correct?

(A) P is D-glucose.<br>
(B) Q is itself a non-narcotic analgesic.<br>
(C) Q can be converted to aspirin by side-chain oxidation followed by acetylation.<br>
(D) Hydrolysis proceeds through a carbocation/oxocarbenium intermediate.

**Answer: (A), (C), (D)**

#### Approach 1 — Identify the glycoside products

Salicin is a β-D-glucoside of salicyl alcohol (saligenin). Acid hydrolysis cleaves its anomeric C–O glycosidic bond, giving D-glucose (P) and salicyl alcohol (Q). Oxidizing the benzylic \(-CH_2OH\) side chain of Q gives salicylic acid; acetylating its phenolic OH gives aspirin. Thus (A),(C) are true and (B) is false. Acid-catalysed cleavage is facilitated by an oxocarbenium-ion-like intermediate at the anomeric carbon, so (D) is true.

#### Approach 2 — Functional-group sequence

\(\mathrm{ArCH_2OH\xrightarrow{oxidation}ArCO_2H}\); the phenolic oxygen then undergoes acetylation to form acetylsalicylic acid. Q itself is salicyl alcohol, not the analgesic product aspirin.

> [!tip] Exam Shortcut
> Salicin = glucose + salicyl alcohol; oxidation of the alcohol side chain gives the salicylic-acid skeleton.

> [!warning] Common Pitfall
> Do not call salicyl alcohol “salicylic acid.” The benzylic carbon must be oxidized before aspirin can be formed.

> [!success] Key Takeaway
> Glycoside hydrolysis breaks the anomeric acetal bond, while the aglycone's side chain can be transformed independently.

---

### Q40. Toluene gives ortho- and para-isomers P,Q on treatment with chlorosulfonic acid. Ammonia converts them to sulfonamides R,S. Oxidation of R followed by acid heating gives T. Which statements are correct?

(A) Q can convert an alcohol \(-OH\) into a good leaving group.<br>
(B) S contains a sulfonamide group, the basis of several drugs.<br>
(C) T can be used as a tranquilizer.<br>
(D) The degree of unsaturation of T is 7.

**Answer: (A), (B)**

#### Approach 1 — Track the functional groups

P and Q are o- and p-toluenesulfonyl chlorides (tosyl chlorides). Q converts an alcohol into a tosylate ester, replacing poor-leaving \(-OH\) with the excellent leaving group \(-OTs\): (A) true. Ammonolysis gives p-toluenesulfonamide S, which contains \(-SO_2NH_2\), a sulfonamide group used in drug families: (B) true. Oxidation/cyclization of the ortho sulfonamide gives saccharin T, an artificial sweetener, not a tranquilizer: (C) false. Saccharin has formula \(\mathrm{C_7H_5NO_3S}\), so

$$\mathrm{DBE}=\frac{2(7)+2+1-5}{2}=6,$$

not 7; (D) false.

#### Approach 2 — Recognize the named products

\(p\)-Toluenesulfonyl chloride is tosyl chloride; the ortho analogue oxidizes/cyclizes to saccharin. Knowing those two functional identities settles all four statements.

> [!tip] Exam Shortcut
> A tosyl chloride is a reagent for converting alcohols into tosylates; the leaving group departs from oxygen, not from the carbon skeleton.

> [!warning] Common Pitfall
> Saccharin is a non-nutritive sweetener. Its nitrogen-containing cyclic imide does not make it a tranquilizer.

> [!success] Key Takeaway
> Use formula-based DBE, \((2C+2+N-H-X)/2\), for a quick consistency check on heteroatom-rich structures.

---

### Q41. Which statements about polymers are correct?

(A) Vulcanization increases cross-links and stiffens rubber.<br>
(B) LDPE is produced from ethene using a Ziegler–Natta catalyst at 333–343 K and 6–7 atm.<br>
(C) PHBV is biodegradable.<br>
(D) Novolac is a linear polymer used in paints.

**Answer: (A), (C), (D)**

#### Approach 1 — Classify the polymerization conditions and structures

(A) True: sulfur cross-links restrict chain motion and strengthen/stiffen rubber. (B) False: Ziegler–Natta catalyst at comparatively low pressure produces linear, high-density polyethylene; low-density polyethylene is made by high-pressure free-radical polymerization. (C) True: PHBV (poly-β-hydroxybutyrate-co-β-hydroxyvalerate) is biodegradable. (D) True: novolac is a predominantly linear phenol–formaldehyde resin and is used in paints/varnishes and as a precursor to Bakelite.

#### Approach 2 — Count monomer types

The five single-monomer addition polymers are polythene, neoprene, PVC, Teflon, and polyacrylonitrile. Nylon-6,6, Buna-N, Buna-S, Bakelite, Terylene, Novolac, and Nylon-2-nylon-6 all use two monomer types or two amino-acid-derived units; thus the homopolymer count is five.

> [!tip] Exam Shortcut
> Ziegler–Natta → linear HDPE; high-pressure radical process → branched LDPE.

> [!warning] Common Pitfall
> Do not confuse novolac (linear, acid-catalysed, phenol-rich) with cross-linked Bakelite.

> [!success] Key Takeaway
> Polymer properties follow from chain architecture: cross-linking stiffens elastomers; branching lowers polyethylene density.

---

## SECTION II (i) — Numerical (Common Dettol Data)

### Q42. In Dettol component A's synthesis, an aldehyde on a methyl-substituted cyclohexene ring is oxidized with Tollens reagent, esterified with ethanol, then treated with excess \(\mathrm{CH_3MgBr}\) and work-up. Let x be the number of stereoisomers of A and y the number of carbons in its IUPAC parent chain. Find x+y.

**Answer: 5**

#### Approach 1 — Follow the carbonyl chemistry and count stereogenic centres

Tollens oxidation converts the aldehyde to the carboxylic acid; ethanol/\(\mathrm{H_2SO_4}\) gives the ethyl ester. Excess methylmagnesium bromide adds twice to an ester carbonyl, producing a tertiary alcohol of the form \(\mathrm{ring-C(OH)(CH_3)_2}\).

The alcohol's parent chain is propan-2-ol, so \(y=3\). The alcohol carbon is not stereogenic because it bears two identical methyl groups. The ring carbon bearing the new side chain is stereogenic: its two directions around the unsymmetrical alkene/methyl-substituted ring are different. Thus there is one stereocentre and \(x=2\) stereoisomers. Hence \(x+y=2+3=5\).

The non-stereospecific skeleton is shown below; the attachment carbon on the ring is the one stereogenic centre:

```smiles
CC(O)(C)C1CC=C(C)CC1
```

#### Approach 2 — Avoid overcounting

The methyl-bearing alkene carbon is sp² and cannot be a stereocentre; the tertiary alcohol carbon has two identical methyl groups. Only the ring attachment carbon is chiral, so \(2^1=2\) stereoisomers (no internal symmetry makes a meso form).

> [!tip] Exam Shortcut
> For an ester plus excess Grignard reagent, expect two nucleophilic additions and a tertiary alcohol.

> [!warning] Common Pitfall
> Do not count the alkene carbon or the tertiary alcohol carbon as stereogenic.

> [!success] Key Takeaway
> Stereoisomer count depends on distinct substituent paths, not merely on the number of sp³ atoms.

---

### Q43. In the Dettol scheme, the nitro group on 4-chloro-3,5-dimethylnitrobenzene is reduced, diazotized, then replaced by OH on heating with water. Find the sum of substituent locants in B.

**Answer: 12**

#### Approach 1 — Name the phenol with the OH as the parent

Reduction gives the aniline; diazotization followed by hydrolysis replaces \(-NH_2\) by \(-OH\). The product is 4-chloro-3,5-dimethylphenol. Its substituent locants are 4 (chloro), 3 and 5 (methyl):

$$4+3+5=12.$$

The structure check below has OH at position 1 and methyl groups at 3,5:

```smiles
Oc1cc(C)c(Cl)c(C)c1
```

#### Approach 2 — Check the numbered ring positions

Start with phenol carbon 1. The two methyl-bearing carbons are 3 and 5, and the chlorine-bearing carbon is 4; the requested sum excludes the parent locant 1 and is \(3+4+5=12\).

> [!tip] Exam Shortcut
> Once the diazonium group is hydrolysed, name the ring as a phenol; OH receives position 1.

> [!warning] Common Pitfall
> Do not include the parent suffix locant 1 in the sum; only substituent locants are requested.

> [!success] Key Takeaway
> Diazotization–hydrolysis replaces an aromatic amino group by hydroxyl while retaining the other ring substituents.

---

## SECTION II (i) — Numerical (Common Aspirin-Hydrolysis Data)

Aspirin hydrolysis gives P and Q; P gives a positive FeCl₃ test. Q is converted successively by \(\mathrm{SOCl_2}\), diazomethane/Wolff rearrangement, silver salt/\(\mathrm{Br_2}\), and \(\mathrm{AgCN}\). The later products are labelled R through Y in the paper.

### Q44. Find the molecular mass of the product from P with bromine water.

**Answer: 331 g mol⁻¹**

#### Approach 1 — Identify P and the bromination product

Aspirin (acetylsalicylic acid) hydrolyses to salicylic acid P and acetic acid Q. The phenolic ring of salicylic acid is activated; in bromine water the standard bromodecarboxylative bromination gives 2,4,6-tribromophenol. Its formula is \(\mathrm{C_6H_3Br_3O}\), so

$$M=6(12)+3(1)+3(80)+16=72+3+240+16=331\,\mathrm{g\,mol^{-1}}.$$

```smiles
O=C(O)c1ccccc1O
```

```smiles
Oc1c(Br)cc(Br)cc1Br
```

#### Approach 2 — Stoichiometric check

The net transformation balances as

$$\mathrm{C_7H_6O_3+3Br_2\longrightarrow C_6H_3Br_3O+CO_2+3HBr}.$$

Both sides contain C₇H₆O₃Br₆, confirming loss of the carboxyl carbon as \(\mathrm{CO_2}\) and formation of the tribromophenol product.

> [!tip] Exam Shortcut
> The 331 g mol⁻¹ value is the mass of \(\mathrm{C_6H_3Br_3OH}\); count three Br atoms and one phenolic O.

> [!warning] Common Pitfall
> Do not stop at brominated salicylic acid: the bromine-water reaction represented in this question proceeds to the tribromophenol product after decarboxylation.

> [!success] Key Takeaway
> Check the product identity as well as the formula: the expected bromine-water product is 2,4,6-tribromophenol.

---

### Q45. The chain gives Y, which is oxidized by Jones reagent and heated with ammonia to Z. Treating Z with \(\mathrm{Br_2/NaOH}\), then benzoyl chloride, gives aromatic A. Find the molecular mass of A.

**Answer: 135 g mol⁻¹**

#### Approach 1 — Follow the reaction sequence

From the common chain, acetic acid Q gives acetyl chloride R; diazomethane followed by Wolff rearrangement gives propanoic acid S. Hunsdiecker reaction of silver propionate gives bromoethane T. \(\mathrm{AgCN}\) gives ethyl isocyanide U; acidic hydrolysis yields formic acid and ethylammonium salt W. Basic work-up gives ethylamine X, which with nitrous acid hydrolyses to ethanol Y.

Jones oxidation of ethanol gives acetic acid; heating its ammonium salt gives acetamide Z. Hofmann rearrangement converts acetamide to methylamine, which benzoyl chloride acylates to N-methylbenzamide, \(\mathrm{C_6H_5CONHCH_3}\) (formula \(\mathrm{C_8H_9NO}\)).

$$M=8(12)+9(1)+14+16=135\,\mathrm{g\,mol^{-1}}.$$

#### Approach 2 — Carbon-count check

Hofmann rearrangement removes the carbonyl carbon: two-carbon acetamide gives one-carbon methylamine. Benzoylation adds the seven-carbon benzoyl fragment, yielding an eight-carbon amide, consistent with \(\mathrm{C_8H_9NO}\).

> [!tip] Exam Shortcut
> \(\mathrm{RCONH_2\xrightarrow{Br_2/NaOH}RNH_2}\): the Hofmann product has one fewer carbon than the amide.

> [!warning] Common Pitfall
> Silver cyanide gives an isocyanide (Et–NC) in this context, not the nitrile (Et–CN); the hydrolysis products differ.

> [!success] Key Takeaway
> Trace each named reaction's carbon skeleton before calculating a final molecular mass.

---

## SECTION II (ii) — Numerical

### Q46. Phenol is nitrated with dilute nitric acid below 25 °C. The more volatile isomer P is reduced with Zn/NH₄Cl and then treated with Tollens reagent, giving a silver precipitate R and organic product S. How many oxygen atoms are in one molecule of S?

**Answer: 2**

#### Approach 1 — Mulliken–Barker reduction test

The more volatile isomer is o-nitrophenol. Zn/NH₄Cl reduces its nitro group to a hydroxylamine intermediate; ammoniacal silver hydroxide oxidizes that intermediate to o-nitrosophenol while depositing Ag. Product S has one phenolic oxygen and one nitroso oxygen:

$$\mathrm{HO{-}C_6H_4{-}N{=}O};\qquad N_O=1+1=2.$$

#### Approach 2 — Count oxygen atoms through the redox sequence

The starting o-nitrophenol has three oxygen atoms (two in \(-NO_2\), one phenolic). Conversion of \(-NO_2\) to the nitroso group \(-N=O\) removes one oxygen overall; the phenolic oxygen is retained, leaving two in S.

> [!tip] Exam Shortcut
> The Mulliken–Barker test uses a mild reducing agent to convert an aromatic nitro group to nitroso while silver ions are reduced to metal.

> [!warning] Common Pitfall
> Count oxygen atoms in the organic product S, not the starting nitro compound P or the inorganic silver precipitate R.

> [!success] Key Takeaway
> Reduction of \(-NO_2\) to \(-NO\) removes one oxygen; the phenolic oxygen remains.

---

### Q47. X is the smallest hydrocarbon that forms a precipitate with Tollens reagent. The scheme takes X through Fe/Δ trimerization, Friedel–Crafts acylation/oxidation, nitration, nitro reduction/bromination, and diazotization followed by CuBr/HBr. Starting with 1 mol X, find the mass of Y.

**Answer: 146 g**

#### Approach 1 — Identify the end product and track the mole ratio

The smallest hydrocarbon giving a precipitate with ammoniacal silver reagent is ethyne, \(\mathrm{HC\equiv CH}\), which forms silver acetylide. Three ethyne molecules trimerize over hot Fe to one benzene molecule.

```tikz
\usepackage{chemfig}
\begin{document}
\chemfig{H-C~C-H}\qquad\longrightarrow\qquad\chemfig{*6(-=-=-=)}
\end{document}
```

Benzene is converted to benzoic acid through acetylation followed by side-chain oxidation; nitration gives meta-nitrobenzoic acid. Reduction gives meta-aminobenzoic acid; bromine water introduces three Br atoms at the activated positions, and diazotization/CuBr replaces the amino group by Br. Y is tetrabromobenzoic acid, \(\mathrm{C_7H_2Br_4O_2}\), with

$$M_Y=7(12)+2(1)+4(80)+2(16)=438\,\mathrm{g\,mol^{-1}}.$$

One mole of ethyne makes \(1/3\) mol benzene and hence \(1/3\) mol Y. Therefore

$$m_Y=\frac13(438)=146\,\mathrm g.$$

#### Approach 2 — Stoichiometric shortcut

Every aromatic transformation is one molecule-to-one molecule after benzene forms. The only yield factor is the trimerization \(3\,\mathrm{C_2H_2}\to\mathrm{C_6H_6}\), so the final mass is one third of Y's molar mass.

> [!tip] Exam Shortcut
> Terminal alkyne + Tollens reagent identifies ethyne; hot Fe converts three molecules to benzene.

> [!warning] Common Pitfall
> The final product has four bromines: three enter by bromination and the diazonium group is replaced by the fourth.

> [!success] Key Takeaway
> Keep track of the one non-unit stoichiometric step; the long aromatic sequence does not change the one-to-one molecule count.

---

### Q48. The amide \((\mathrm{CH_3})_2\mathrm{CHCONH_2}\) is dehydrated with \(\mathrm{P_4O_{10}}\), hydrolysed with acid, then treated with \(\mathrm{Br_2/P}\) and a trace of water. Find the molecular mass of final product C.

**Answer: 167 g mol⁻¹**

#### Approach 1 — Dehydration, hydrolysis, then HVZ bromination

The primary amide dehydrates to the nitrile \((\mathrm{CH_3})_2\mathrm{CHCN}\). Acidic hydrolysis gives 2-methylpropanoic acid, \((\mathrm{CH_3})_2\mathrm{CHCOOH}\). \(\mathrm{Br_2/P}\) followed by water performs the Hell–Volhard–Zelinsky reaction, replacing the α-hydrogen by Br:

$$\mathrm{(CH_3)_2CHCOOH\longrightarrow(CH_3)_2C(Br)COOH}.$$

The product formula is \(\mathrm{C_4H_7BrO_2}\), so

$$M=4(12)+7(1)+80+2(16)=167\,\mathrm{g\,mol^{-1}}.$$

#### Approach 2 — Formula change

Start with isobutyric acid, \(\mathrm{C_4H_8O_2}\). HVZ replaces one α-H (mass 1) with Br (mass 80), increasing molecular mass by 79: \(88+79=167\) g mol⁻¹.

> [!tip] Exam Shortcut
> HVZ substitutes the α-hydrogen next to \(-COOH\); it does not add Br across a double bond.

> [!warning] Common Pitfall
> The central carbon in \((\mathrm{CH_3})_2\mathrm{C(Br)COOH}\) has no hydrogen; the bromine is on the α-carbon.

> [!success] Key Takeaway
> Primary amide → nitrile by dehydration; nitrile hydrolysis → acid; HVZ → α-halo acid.

---

### Q49. How many of these are homopolymers? Polythene, Nylon-6,6, Buna-N, Buna-S, neoprene, PVC, Bakelite, Teflon, polyacrylonitrile, Terylene, Novolac, Nylon-2-nylon-6.

**Answer: 5**

#### Approach 1 — Classify each polymer by its monomers

Homopolymers: polythene (ethene), neoprene (chloroprene), PVC (vinyl chloride), Teflon (tetrafluoroethene), and polyacrylonitrile (acrylonitrile): **five**.

The others are copolymers/condensation products: Nylon-6,6 (diamine + diacid), Buna-N (butadiene + acrylonitrile), Buna-S (butadiene + styrene), Bakelite and Novolac (phenol + formaldehyde), Terylene (ethylene glycol + terephthalic acid), and Nylon-2-nylon-6 (two amino-acid-derived monomers).

#### Approach 2 — Group the list by feed monomer

Single-feed chains: ethene → polythene; chloroprene → neoprene; vinyl chloride → PVC; tetrafluoroethene → Teflon; acrylonitrile → polyacrylonitrile. This gives 5. The remaining 7 listed materials require two monomer species (including the two phenol–formaldehyde resins).

> [!tip] Exam Shortcut
> A homopolymer is made from one monomer species; a common name containing two monomer names often signals a copolymer.

> [!warning] Common Pitfall
> Do not classify only by “addition” versus “condensation.” Either kind can be a homo- or copolymer.

> [!success] Key Takeaway
> Count the distinct monomer species, not the number of repeat-unit fragments visible in the polymer name.

---

### Q50. A nucleoside is formed from ribose and uracil. Find the total number of nitrogen and oxygen atoms in one molecule.

**Answer: 8**

#### Approach 1 — Formula and dehydration

Ribose is \(\mathrm{C_5H_{10}O_5}\), uracil is \(\mathrm{C_4H_4N_2O_2}\). Glycosidic condensation removes \(\mathrm{H_2O}\):

$$\mathrm{C_5H_{10}O_5+C_4H_4N_2O_2-H_2O=C_9H_{12}N_2O_6}.$$

The nucleoside is uridine and contains \(2+6=8\) N and O atoms.

#### Approach 2 — Count the components

Uracil contributes two N and two O; ribose contributes five O. Condensation removes the anomeric OH oxygen together with one H from the base, but the water's oxygen comes from the sugar. The net formula has six O and two N, again totaling eight.

> [!tip] Exam Shortcut
> A nucleoside is sugar + base − H₂O; a nucleotide would additionally contain phosphate.

> [!warning] Common Pitfall
> Do not count the sugar and base atoms before subtracting the water molecule formed at glycosidic-bond formation.

> [!success] Key Takeaway
> Uridine's molecular formula is \(\mathrm{C_9H_{12}N_2O_6}\); the requested heteroatom total is 8.

---

### Q51. How many essential amino acids are obtained on complete hydrolysis of the shown tetrapeptide?

**Answer: 0**

#### Approach 1 — Read the side chains

The peptide is Ala–Ser–Asp–Cys: the side chains are \(-CH_3\) (alanine), \(-CH_2OH\) (serine), \(-CH_2COOH\) (aspartic acid), and \(-CH_2SH\) (cysteine). All four are non-essential amino acids in humans (cysteine is conditionally essential in some contexts, but it is classified as non-essential in the standard JEE list). Therefore the number of essential amino acids released is **0**.

#### Approach 2 — Verify against the essential set

The commonly tested essential set includes Val, Leu, Ile, Lys, Met, Thr, Phe, Trp, and often His/Arg depending on age. None of Ala, Ser, Asp, or Cys belongs to that set.

> [!tip] Exam Shortcut
> Identify amino-acid side chains from the α-carbon outward; the peptide backbone itself is not the side chain.

> [!warning] Common Pitfall
> Cysteine's conditional importance does not change the answer under the standard essential/non-essential classification used for this question.

> [!success] Key Takeaway
> Complete hydrolysis cleaves peptide bonds and releases the constituent amino acids unchanged.

---

# COMPLETE THEORY VAULT

## Mathematics — Roots of Unity, Counting, and Symmetry

### Complex roots and root filters

- If \(\omega^n=1\) and \(\omega\ne1\), then \(1+\omega+\cdots+\omega^{n-1}=0\).
- For a primitive n-th root, \(\prod_{k=1}^{n-1}(x-\omega^k)=1+x+\cdots+x^{n-1}\).
- Large powers reduce modulo n: \((e^{2\pi i/n})^m=e^{2\pi i(m\bmod n)/n}\).
- For \(|\omega|=1\), use \(|a-b\omega|^2=a^2+b^2-2ab\operatorname{Re}\omega\).

### Complex loci and conics

- A circle \(|z-z_0|=r\) is parametrized by \(z=z_0+re^{i\theta}\).
- The parametrization \(x=x_0+a\cos\theta,\ y=y_0+b\sin\theta\) gives an ellipse with semiaxes \(|a|,|b|\); \(e=\sqrt{1-b^2/a^2}\) when \(a\ge b\).
- A line through a fixed point is tangent to a conic when substitution gives a repeated quadratic root, i.e. discriminant zero.

### Binomial sums and generating functions

- Bounded digit sums are coefficients of \((1+x+\cdots+x^9)^m\); use inclusion–exclusion on the upper digit bound.
- \(\sum_{r=0}^n\binom nr a^r=(1+a)^n\); missing endpoints must be subtracted explicitly.
- Vandermonde: \(\sum_r\binom nr^2=\binom{2n}{n}\).
- In block-counting problems, impose the divisibility residue after fixing the block and last digit; use inclusion–exclusion for overlapping blocks.

### Symmetric sums and equal moduli

For \(|z_i|=r\), \(1/z_i=\bar z_i/r^2\). With elementary symmetric sums \(e_1=\sum z_i\), \(e_2=\sum_{i<j}z_iz_j\), \(e_3=\prod z_i\),

$$\sum z_i^2=e_1^2-2e_2,\qquad e_2=e_3\sum_i1/z_i.$$

This avoids solving a high-degree polynomial when only a symmetric expression is requested.

## Physics — Circuits, Capacitors, and Transport

### Networks and bridges

- Equivalent resistance is found by applying a test voltage: \(R_{\rm eq}=V/I\). Use graph symmetry to equate node potentials before solving KCL.
- Wheatstone balance: ratio of the two gap resistances equals the ratio of the two wire-arm resistances. For a nonuniform wire, \(R(a,b)=\int_a^b\rho\,dx/A(x)\).
- Maximum power transfer to a resistive load occurs at \(R_L=R_{\rm th}\), giving \(P_{\max}=V_{\rm th}^2/(4R_{\rm th})\).
- Ammeter shunt: \(R_s=I_gG/(I-I_g)\). For a uniform wire cut into n equal pieces and connected in parallel, \(R_s'=R_s/n^2\).

### Capacitors and dielectrics

- \(Q=CV\), \(U=\tfrac12CV^2=Q^2/(2C)\). Choose the energy form that matches the constraint (constant V versus isolated constant Q).
- Side-by-side dielectric regions share voltage and add capacitances (parallel); layers along the field share displacement and combine in series.
- At a dielectric interface without free surface charge, normal \(D\) is continuous; \(E=D/\varepsilon\) changes when permittivity changes.
- Floating conductor/node: its net charge is conserved. A battery-connected terminal can exchange charge with the source.

### Thermal and electrical transport

- Thermal balance: \(C_{\rm th}\,dT/dt=P_{\rm in}-k(T-T_a)\). For constant \(P_{\rm in}\), the solution approaches \(T_\infty=T_a+P_{\rm in}/k\) exponentially with time constant \(C_{\rm th}/k\).
- Drude conductivity: \(\sigma=ne\mu\); for a varying cross-section, integrate the local resistance \(dR=\rho dx/A(x)\).
- A series voltmeter's first-order temperature drift vanishes when \(\sum_i\alpha_iR_i=0\), including the galvanometer coil.

### Plate fields, switching, and thermal hysteresis

- For large parallel plates, a gap capacitance is \(C=\varepsilon A/d\). With fixed charge, \(D_n=Q/A\) is continuous across a dielectric boundary without free surface charge, while \(E=D/\varepsilon\) changes with the material.
- For an isolated capacitor, charge on floating junctions is conserved. If a battery remains connected, its voltage is fixed and it may supply/remove charge; compare the equivalent capacitance before and after switching.
- Constant-voltage spreading: the electrical energy available per increase in capacitance is \(\tfrac12V^2dC\). For a dielectric layer, \(dC/dA=\varepsilon_0\varepsilon_r/h\); balance this against the change in surface energy.
- A constant-power thermal branch obeys \(C_{\rm th}\dot T=P-k(T-T_a)\), with \(T_\infty=T_a+P/k\), \(\tau=C_{\rm th}/k\). Time from \(T_1\) to \(T_2\) is \(t=\tau\ln[(T_\infty-T_1)/(T_\infty-T_2)]\) while heating; use the corresponding cooling ratio when \(T_\infty<T\).
- At a hysteresis threshold, current may jump when resistance switches. For fixed source voltage compare the allowed branch currents \(V/R_i\); calculate the switching period separately from the current extrema.

### Bridge and measurement identities

- For a meter bridge with varying area, define \(F(u)=\int_0^u dt/[A(t)]\). Balance at fraction \(u=\ell/L\) gives the left/right wire ratio \(F(u)/[F(1)-F(u)]\), not simply \(u/(1-u)\).
- A source branch of emf \(E_i\) and series resistance \(R_i\) contributes conductance \(1/R_i\) and Norton current \(E_i/R_i\). Parallel source branches have \(V_{\rm th}=\dfrac{\sum_i E_i/R_i}{\sum_i 1/R_i}\).
- Galvanometer shunt relation: \(I_gG=I_sR_s\); the new range is \(I_g(1+G/R_s)\). For a uniform shunt wire split into \(n\) equal sections and paralleled, \(R_s'=R_s/n^2\).

## Chemistry — Functional Groups, Mechanisms, and Biomolecules

### Aromatic amines and diazonium chemistry

- Carbylamine: only primary amines give isocyanides with \(\mathrm{CHCl_3/KOH}\).
- Aniline + acetic anhydride → acetanilide; aniline complexes with \(\mathrm{AlCl_3}\), suppressing Friedel–Crafts acylation.
- Diazotization is performed cold (about 0–5 °C); hydrolysis gives phenol, while Cu(I) salts effect Sandmeyer substitution and Cu powder/halogen acid is the Gattermann variant.
- Sulfonyl chlorides convert alcohols to sulfonate esters, excellent leaving groups. Aromatic sulfonamides are tested by Hinsberg chemistry.

### Carbonyl and named reactions in this paper

- Ester + excess Grignard reagent → tertiary alcohol (two additions).
- Carboxylic acid → acyl chloride with \(\mathrm{SOCl_2}\); diazomethane/acyl chloride followed by Wolff rearrangement homologates by one carbon.
- Silver carboxylate + \(\mathrm{Br_2}\) (Hunsdiecker) → alkyl bromide with one fewer carbon.
- \(\mathrm{AgCN}\) commonly gives isocyanides; acidic hydrolysis yields formic acid and an amine salt.
- Primary amide dehydration → nitrile; nitrile hydrolysis → acid; \(\mathrm{Br_2/P}\) then water is the HVZ α-bromination.
- \(\mathrm{RCONH_2\xrightarrow{Br_2/NaOH}RNH_2}\) is Hofmann rearrangement, with loss of the carbonyl carbon.

### Carbohydrates, amino acids, and polymers

- Glycosides hydrolyse at the anomeric acetal linkage; the sugar residue and aglycone are distinct products.
- Seliwanoff distinguishes ketoses from aldoses; Biuret detects peptide bonds; Xanthoproteic detects aromatic amino-acid residues.
- A nucleoside is sugar + nitrogenous base; a nucleotide also includes phosphate.
- Homopolymer = one monomer type; copolymer = two or more. Ziegler–Natta ethene polymerization gives linear HDPE; high-pressure radical polymerization gives branched LDPE.

---

### Diagnostic tests and stereochemical reference

- **Carbylamine:** only primary amines give foul-smelling isocyanides with chloroform/strong base. **Hinsberg:** primary amines form sulfonamides soluble in base; the test helps distinguish amine classes.
- **Azo coupling:** aromatic primary amine → diazonium salt at 0–5 °C. Aniline coupling is generally mildly acidic; phenol/β-naphthol coupling is carried out in alkaline medium and gives vivid azo dyes.
- **Barfoed:** rapid reduction indicates a monosaccharide (not a way to distinguish two monosaccharides). **Seliwanoff:** ketose reacts rapidly, aldose more slowly. **Xanthoproteic:** aromatic amino-acid residues give a yellow/orange product. **Biuret:** two or more peptide bonds give a violet complex.
- **Tollens silver acetylide test:** terminal alkynes form insoluble silver acetylides in ammoniacal silver solution. **Mulliken–Barker:** Zn/\(\mathrm{NH_4Cl}\) partially reduces aromatic nitro compounds; the hydroxylamine/nitroso redox sequence reduces ammoniacal silver to Ag.
- In a conventional Haworth drawing with ring O at upper right, Fischer groups on the right map down and groups on the left map up. D/L is set by the highest-numbered stereocentre (the penultimate carbon): \(\mathrm{CH_2OH}\) is up for D and down for L in this orientation. The anomeric OH sets α/β, not D/L.
- For a neutral formula containing C,H,N, halogens X, the degree of unsaturation is \(\mathrm{DBE}=(2C+2+N-H-X)/2\); oxygen and sulfur do not enter the count.

### Reaction-sequence map for this paper

- **Protected aromatic substitution:** acetylate aniline before bromination; \(-NHCOCH_3\) directs ortho/para (para usually major). Remove the protecting group before diazotization. Cu(I) salt = Sandmeyer; Cu powder/halogen acid = Gattermann.
- **Grignard on esters:** two additions of \(\mathrm{CH_3MgBr}\) followed by work-up give a tertiary alcohol; the carbonyl-derived alcohol carbon has two identical methyl groups here and is not stereogenic.
- **Arndt–Eistert/Wolff:** acid chloride → diazoketone → ketene rearrangement/hydrolysis, homologating a carboxylic acid by one carbon. **Hunsdiecker:** silver carboxylate → alkyl bromide with one fewer carbon.
- **AgCN versus KCN:** covalent AgCN favours isocyanide \(\mathrm{R-NC}\); hydrolysis produces formic acid and an amine salt. Primary aliphatic amine + nitrous acid gives the corresponding alcohol with nitrogen released.
- **Hofmann rearrangement:** \(\mathrm{RCONH_2\xrightarrow{Br_2/NaOH}RNH_2}\), one fewer carbon. **HVZ:** \(\mathrm{Br_2/P}\), then water, replaces an α-H of a carboxylic acid by Br.
- **Aspirin route:** salicin aglycone salicyl alcohol → side-chain oxidation to salicylic acid → phenolic acetylation. Salicylic acid in bromine water gives the tribromophenol product represented in Q44.
- **Acetylene route:** ethyne gives silver acetylide with ammoniacal silver and trimerizes over hot Fe: \(3\,\mathrm{C_2H_2}\to\mathrm{C_6H_6}\). Aromatic nitration/reduction/bromination/diazotization steps retain the ring-carbon count except for the explicit trimerization ratio.

## Obsidian Plugin Notes

- **TikZJax / Circuitikz:** vector schematics are included for the octahedron and five-bulb bridge.
- **Desmos:** the complex-plane ellipse in Q10 is an interactive `desmos-graph` block.
- **Chemtrails / Obsidian Chem:** standard one-SMILES-per-block structures are included where they help identify aromatic compounds.
- **LaTeX Suite / MathJax:** all derivations use ordinary inline/display LaTeX, which remains readable without a plugin.
- **Dataview:** the frontmatter below lets the vault dashboard query this note consistently.

```dataview
TABLE paper AS "Paper", status AS "Status", total_questions AS "Questions"
FROM "solutions"
WHERE test = 1
SORT paper ASC
```

> [!success] Completion Check
> All 51 questions in 1-paper2 are answered. The multiple-correct items are evaluated statement by statement, numerical answers include units where applicable, and original figures are translated into Obsidian-compatible diagrams or described directly.

---

*Answer key cross-check: printed key on PDF pp. 17–18. Full derivations above; questions with shared data are solved independently under each question number so the note can be read sequentially.*
