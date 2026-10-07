# Open items — where the vault still needs work

`python3 tools/check_coverage.py` is the source of truth for this page: it compares every
solution note against the printed answer key of its paper and reports

* **missing** — questions with no section at all, and
* **thin** — sections shorter than the threshold (answer letter only, no working).

Re-run it after any editing session; `make coverage` does the same thing.

## Status after the Test-3 overhaul

| Note | Questions | Missing | Thin (answer-only) |
|---|---|---|---|
| 1-paper1 | 51 | 0 | 29 |
| 1-paper2 | 51 | 0 | 17 |
| 2-paper1 | 54 | **8** (Q47–Q54) | 28 |
| 2-paper2 | 54 | **24** (Q11–18, Q29–36, Q47–54) | 12 |
| 3-paper1 | 48 | 0 | 1 |
| 3-paper2 | 48 | **32** (all of maths Q9–16, physics Q21–32, chem Q37–48) | 6 |
| 4-paper1 | 57 | 0 | 40 |
| 4-paper2 | 57 | 0 | 34 |

**Totals: 64 questions not written at all, 167 written as answer-only.**

## Order of work

1. **3-paper2** — 32 missing questions. The booklet prints worked solutions for mathematics
   Q1–Q8 only; everything else (maths Q9–16, all 12 physics numericals and MCQ sections, all
   of chemistry from Q37) has to be worked from scratch.
2. **2-paper2** — 24 missing (maths numericals Q11–18, physics numericals Q29–36, chemistry
   numericals Q47–54). The printed booklet has solutions for these, so the answers can be
   cross-checked easily.
3. **2-paper1** — 8 missing (Q47–Q54, numericals).
4. **Thin sections** — 167 answer-only entries in papers 1, 4-1, 4-2, 2-1. These are the
   legacy multi-question blocks ("Q7–Q10. Various …" followed by bullets). Each needs to be
   split into per-question sections with working.

## Known content defects (not coverage)

| Where | What is wrong |
|---|---|
| `1-paper2` Q10–Q11 | draft lands on $m^2=9/8$ while the key gives $-3$; the set-up needs re-reading from the paper |
| `1-paper2` ring of 3 batteries + 3 capacitors | node analysis restarted three times, ends on "take the key's value" |
| `1-paper2` Q18 (three plates + switch) | surface-charge bookkeeping started twice, never closed |
| `4-paper1` Q18 | the reconstructed statement $f=x^{x}(x+1)^{-(x+1)}$ does not give the key's value (the formula is an image in the paper, so the transcription is suspect) |
| `4-paper2` Q38 | flux written as "the key gives 100" instead of integrating $\rho r^{2}$ |

`python3 tools/check_prose.py` (`make prose`) lists the paragraphs that still read like a
scratch pad — currently one line, and the table above is the honest remainder.

## What *is* verified

- Figures render inside Obsidian through mobile-capable plugins only; `make check` validates
  every block (139 at the time of writing, 0 errors / 0 warnings).
- Figures that encode numbers were re-derived from the source PDFs and corrected where the
  first pass was wrong (cube of charges, satellite impulse, bead oscillation, Brewster
  geometry, circular capacitor, fifth-harmonic energy density, $r=a$ points of an ellipse,
  four-plate stack, octahedron resistance $5R/12$, convex-mirror image motion).
- **3-paper1 is fully worked**: all 48 questions, every numeric answer reproduced
  independently of the key (see the note itself for each derivation).
