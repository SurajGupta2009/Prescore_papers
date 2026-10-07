# Open items — where the solutions still need work

Everything below is a *known* loose end. It is listed here so nothing is silently wrong:
figures are section-by-section verified against the source PDFs, but a handful of written
derivations still stop short of the answer key.

`make prose` (or `python3 tools/check_prose.py`) lists the paragraphs that still read like a
scratch pad; run it after editing a solution.

## Derivations that do not yet reach the key

| Where | What is missing | Key's answer |
|---|---|---|
| `1-paper2` — Q18, three plates with a switch and a battery | the surface-charge bookkeeping is started twice and never closed; the text ends by trusting the key | (C) |
| `1-paper2` — Q10–Q11, normals to the image of a circle under $z \mapsto 1/z$ | the draft lands on $m^2 = 9/8$ (product $-9/8$) while the key gives $-3$; one of the two set-ups must be re-read from the paper's figure | $-3.00$ |
| `1-paper2` — ring of three batteries with three capacitors | the node analysis is restarted three times and ends on "trust the answer" | $14\ \mu$C |
| `1-paper2` — Q6, $\zeta$ a 38th root of unity | the closed form is quoted from the key ($\alpha=4$, $\beta=-2$, $\gamma=-38$) without deriving it | (A, B) |
| `2-paper1` — Q9/Q10, match-the-column optics and circuits | only the key's letters are recorded; the matching argument is not written out | (C) / (A) |
| `4-paper1` — Q18, $f(x) = x^x(x+1)^{-(x+1)}$ on $(0,\infty)$ | the reconstructed statement does not produce the key's value (the formula in the paper is an image, so the transcription itself is suspect) | 1 |
| `4-paper2` — Q38, flux through a cylindrical annulus | the check is written as "the key gives 100" instead of integrating $\rho r^2$ term by term | 100 |

## Style debt

- `tools/check_prose.py` still reports the items above; the rest of the vault is clean.
- The theory sections at the end of each paper are unchanged from the first pass and have
  not been re-read against the syllabus.

## What *is* verified

- Every figure block renders inside Obsidian through the four mobile-capable plugins; the
  vault check (`make check`) validates 85 blocks in 8 notes.
- Figures that encode numbers were re-derived from the source PDFs and corrected where the
  first pass was wrong: cube-of-charges (Q21/4-1), satellite impulse (Q22/4-1), bead
  oscillation (Q36/4-2), Brewster geometry and the circular capacitor (Q18, Q19/3-2),
  energy density in the fifth harmonic (Q20/3-2), $r=a$ points of an ellipse (Q23/4-2),
  the four-plate stack (Q24/4-2), the octahedron network (**5R/12**, Q21/1-2) and the
  convex-mirror image motion (Q19/2-1).
