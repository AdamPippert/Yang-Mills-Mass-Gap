# Yang Mills mathematician handoff

Version 1.0 - 20 November 2026

Start with **Mathematician_Review.pdf**. It gives the review mandate, the exact Gaussian setup and bounds, the conditional spectral theorem and proof, the missing analytic implications, the Lean status, and the requested next decisions. **REVIEW_REQUEST.md** is a short note that can accompany the package. No message has been sent to a reviewer.

## What this package establishes

The recovered Gaussian manuscript supplies ordinary mathematical derivations for deterministic physically bounded collars and specified observable channels. The conditional spectral theorem supplies a separate analytic implication from common-rate temporal decay on a dense centered family to a gap. No interacting Yang-Mills estimate, continuum construction, independent human endorsement, or Lean-verified result is claimed.

The new Gaussian audit also isolates a difficulty with using the deterministic collar condition: for raw microscopic Gaussian collars from a larger box under the same normalization, the fixed physical supremum cutoff becomes atypical as the spacing tends to zero. This is an added analytic observation for review, not a change to the original theorem.

## Reading order

1. `Mathematician_Review.pdf` or its editable Markdown source.
2. `MassGap/UFBI/GaussianBoundaryEstimate.md` for the complete original G1-G8 derivations.
3. `review_notes/Conditional_Spectral_Gap.md` for the full spectral proof, counterexamples and formalization contract.
4. `review_notes/Gaussian_Audit.md` and `review_notes/Reviewer_Questions.md` for source-specific review findings and next questions.
5. `MassGap/UFBI/SPECIFICATION.md`, `MassGap/ReflectionPositivity.lean`, and `original_notes/FOUNDATION_STATUS.md` for historical specification and implementation boundaries.

## File map

| Location | Contents |
|---|---|
| `Mathematician_Review.pdf` | Main typeset packet |
| `Mathematician_Review.md` | Editable source of the main packet |
| `Mathematician_Review.tex` | Generated LaTeX source for the same packet |
| `REVIEW_REQUEST.md` | Short reviewer request to copy or adapt |
| `review_notes/` | New analytical and review notes prepared for this handoff |
| `MassGap/UFBI/` | Original specification, analytic note, executable controls, tests and original results |
| `MassGap/GaussianUFBI.py` and `.md` | Earlier exploratory control with the outer-box-fixed convention |
| `MassGap/ReflectionPositivity.lean` | Original uncompiled scaffold with three admitted proof bodies |
| `original_notes/` | Original status report and scaffold README |
| `validation/` | Fresh unit-test, sweep and rejected-pilot logs and outputs |
| `provenance/original_sources.json` | Source versions, original byte sizes and SHA-256 hashes for 13 recovered files |
| `SHA256SUMS` | Checksums for all packaged files except the checksum list itself |
| `requirements.txt` | Exact numerical dependency versions used in this rerun |
| `document_style.tex` and `code_wrap.lua` | Typesetting configuration used to build the packet |

The 13 recovered files are unchanged. Their directory arrangement was restored to make the numerical controls runnable; this is not an original Git checkout. Earlier files contain historical claims and superseded statements: the v0.2 supplement establishes scalar constant-collar maximization, and the new packet contains the current qualification. The original rejected candidate remains rejected.

## Verified numerical rerun

Python 3.12.14; NumPy 2.3.5; SciPy 1.17.0. The supplied 12 tests passed. The analytic-bound sweep evaluated 14 geometries, 56 collars and 168 channel measurements with zero recorded violations. The rejected pilot produced 9 failures in 108 measurements and returned strict exit status 1, as expected. The original recorded implementation hashes agree with the recovered and rerun files.

These are floating-point consistency checks. They do not prove quantified uniformity or supply interval certificates. No Lean command was run; `lean` and `lake` were unavailable. The earliest exploratory sweep was not rerun.

## Reproduce the numerical checks

Prerequisites: Python with the NumPy and SciPy versions in `requirements.txt`. From the extracted package root, a separate virtual environment can be used:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 .venv/bin/python -m unittest discover \
  -s MassGap/UFBI -p 'test_*.py' -v
OPENBLAS_NUM_THREADS=1 .venv/bin/python MassGap/UFBI/gaussian_bounds.py \
  --out validation/estimate_checks_local.json
```

Expected success: 12 passing tests and a JSON summary with zero analytic-bound violations. New output names keep the original and supplied rerun results intact.

Replay the historical rejected pilot separately:

```sh
OPENBLAS_NUM_THREADS=1 .venv/bin/python MassGap/UFBI/ufbi_control.py \
  --strict --mass 2 --B 2 3 4 --R 3 5 7 \
  --patterns constant random checkerboard face \
  --K 4 --gamma-fraction 0.5 \
  --out validation/pilot_results_local.csv
```

Expected outcome: exit status **1**, 108 rows, 9 failures. All failures are constant collars at R=3, B=2,3,4, for the mean, moments and full channels. Changing the constants would test a different candidate; do not erase this rejection.

If dependencies differ or a check fails, preserve the error and environment details before changing anything. Keep an unchanged copy of this package and compare hashes before editing.

## Lean handoff

The original status report records upstream `yang-mills-group/OpenAI-YM-20261028`, commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464`, with reported toolchain `leanprover/lean4:v4.32.0`. The upstream project and dependencies are not vendored here. The scaffold is neither implementation-ready nor a formal proof. Its A1 geometry assumption and A2 quotient assumption are placeholders; A2 permits a zero operator; A3 needs separate density, reconstruction, phase and limit arguments.

First repair the statements. Then build a scalar Laplace-support lemma, a dense-family PVM theorem, and an adapter to the actual upstream interfaces. Record build logs and axiom dependencies. A successful build with `sorryAx` is not acceptance.

## Rebuild the main PDF

Prerequisites: Pandoc and a TeX installation with XeLaTeX, Latin Modern fonts, and the packages referenced in `document_style.tex`.

```sh
pandoc Mathematician_Review.md --from=markdown+tex_math_dollars \
  --standalone --toc --toc-depth=2 --number-sections \
  --pdf-engine=xelatex --include-in-header=document_style.tex \
  --lua-filter=code_wrap.lua \
  -V documentclass=article -V fontsize=11pt \
  -V geometry:margin=0.8in -V papersize=letter \
  -V mainfont='Latin Modern Roman' -V monofont='Latin Modern Mono' \
  -o Mathematician_Review.pdf
```

The Markdown source and PDF contain the same main review text. The generated TeX is included for mathematicians who prefer editing equations directly. Render and inspect the PDF after edits, especially long equations and tables.

## Intended review outcome

Return an assessment of the conditional theorem, a corrected or rejected boundary/clustering hypothesis, a list of missing dependencies, and one concrete next analytic lemma plus one formalization task. The package is intended to make those judgments possible without treating empirical agreement or model agreement as proof.
