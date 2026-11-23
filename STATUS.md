# Research status

Snapshot date: 2026-11-22. This document is a reference with an explanation section. It uses no requirement keywords. Source IDs (C1, G1, O1, A1, U1) are defined in [SOURCES.md](SOURCES.md).

## Verdict

**The Yang–Mills mass gap is not proved.** No source in this repository contains a proof. No result here has been reviewed by a human mathematician. No result here has been checked by a Lean compiler.

The work so far isolates the missing step. The missing step is a quantitative estimate that holds uniformly along the continuum and infinite-volume limits of four-dimensional pure Yang–Mills theory. The sources call the estimate "UFBI" or "common-rate temporal clustering". Nobody has proved it.

Four facts summarize the state:

- An informal, AI-written proof exists for a conditional statement: uniform decay on a dense family of states implies a spectral gap (A1).
- An informal, AI-written derivation exists for Gaussian estimates in a free massive scalar model (A1). The model has an input mass and does not generate one.
- A Gaussian check of the boundary-influence idea has run. It shows that fixed lattice-unit collars drive the total-variation distance to its maximum as the mesh is refined. Physically scaled collars do not reach the maximum over the tested range (check X1 below).
- The interacting estimate that would connect the two has no proof. The audits in A1, C1 and G1 found specific obstructions to the strategies tried so far (B1 to B9).
- The upstream Lean repository the work builds on states that the mass gap is outside its scope (U1).

## Evidence levels

Each claim in this document carries one level.

| Level | Meaning | Reached by any claim here? |
|---|---|---|
| E0 | Proposed or conjectured. Stated, not argued. | Yes |
| E1 | Informal argument written by an AI model. No human review. | Yes |
| E2 | E1 plus floating-point numerical checks that agree. The checks are not proofs. | Yes |
| E3 | Checked by an independent human mathematician. | **No** |
| E4 | Machine-checked in Lean with no `sorry` and an axiom report. | **No** |

Status words: **Established** means E1 or higher for the stated scope. **Proposed** means E0. **Open** means no argument exists. **Rejected** means a check refuted a candidate. **Obstructed** means an audit found a specific barrier.

## Claim register

| ID | Claim | Status | Level | Scope and limits | Source | What would falsify it |
|---|---|---|---|---|---|---|
| W1 | If a Hamiltonian H ≥ 0 has a unit vacuum and the centered vectors in a dense family decay as ⟨ψ, e^(−tH) ψ⟩ ≤ C_ψ e^(−Δt) with one common Δ > 0, then H has spectrum in {0} ∪ [Δ, ∞). | Established | E1 | Abstract theorem. It assumes the hypotheses. It does not construct a quantum field theory. Prefactor C_ψ can depend on ψ. The rate must be common. | A1 `Mathematician_Review.md` §"Conditional spectral theorem"; also `review_notes/Conditional_Spectral_Gap.md` §2 (not read in full by this repository) | An error in the scalar-measure argument, or a Lean proof attempt that fails. |
| W2 | Dirichlet boundary-influence estimates G1 to G8 bound the total-variation distance between central-block laws under two collars by min{2, K·M·e^(−γD)}. | Established | E2 | Free massive scalar in four dimensions with mass m > 0 put in by hand. Deterministic collar bound ‖τ/a‖∞ ≤ M. Says nothing about Yang–Mills. | A1 `Mathematician_Review.md` §"Gaussian model and explicit estimates" (condensed from `MassGap/UFBI/GaussianBoundaryEstimate.md`, not read in full by this repository); `validation/validation_summary.json` | An error in a derivation step, or a counterexample geometry. |
| W3 | The first pilot constants K = 4, γ = 1 are wrong. | Rejected | E2 | 9 failures in 108 measurements. All at R = 3, B = 2, 3, 4, opposite constant collars. | A1 `validation/validation_summary.json`, `pilot_results_rerun.csv` | Not applicable. The candidate stays rejected. |
| W4 | A raw Gaussian collar sampled from a larger box eventually violates any fixed amplitude cutoff as the lattice spacing a → 0. | Obstructed | E1 | Added by an AI audit. Applies to raw, unaveraged collars with the stated precision. Does not refute W2. Does not apply automatically to coarse collars or compact Wilson links. | A1 `Mathematician_Review.md` §"Missing implication from boundary influence to clustering" | An error in the density bound Pr{\|τ_y\| ≤ aM} ≤ √(2/π)·aM·√(16 + (ma)²). |
| W5 | UFBI Part I: if boundary influence δ at box side R·B is at most ε₀(R), then connected correlations of block observables decay as K·exp(−c·dist/B), with constants depending only on R. | Proposed | E0 | C1 calls it a hypothesis. It says the Dobrushin–Shlosman and Martinelli–Olivieri versions for compact spin spaces and gauge-invariant σ-algebras were not verified. G1 calls the core theorem "established". The sources disagree. | C1 §2; G1 Turn 2 | A proof that the criterion fails for gauge-invariant σ-algebras, or a proof of the criterion. |
| W6 | UFBI Part II: there is a physical length ℓ > 0 with limsup over N of sup over p of δ(ℓ, R) ≤ ε₀(R). | Open | E0 | C1 estimates Part II as "roughly as hard as a mass gap at finite physical volume". It is the whole unsolved problem in one inequality. | C1 §2 | Any of the checks X1 to X3 below returning a failure. |
| W7 | The Lean scaffold `MassGap/ReflectionPositivity.lean` states the clustering-to-gap bridge. | Proposed | E0 | Not compiled. Contains three `sorry` bodies. Premises `hGeometry : True` and `hQIsOSQuotient : True` are placeholders. The statement for A2 permits the zero operator. A1 says the scaffold needs repair before use. | A1 `Mathematician_Review.md` §"Lean status"; the Lean file | A Lean build, or a corrected statement. |
| W8 | The Bridge Lemma Lean signature in C1 type-checks against the upstream definitions. | Proposed | E0 | C1 states it has not compiled any of the code. | C1 §3 | A Lean build against the pinned upstream commit. |
| W9 | The UOR/RG proof-state contract (JSON-LD, JSON Schema, SHACL, Rust stubs) enforces uniformity declarations. | Proposed | E0 | Structural prototype. Declares constants independent of a and L but cannot verify the mathematics. A1 does not rely on it. The package README says the toy SU(2) example "is not a constructive Yang–Mills RG proof and not evidence of a mass gap". The Rust file was not compiled. | O2; artifact A2 [`artifacts/chatgpt-uor-rg-contract/`](artifacts/chatgpt-uor-rg-contract/); G1 Turn 2, pasted block 2; A1 `Mathematician_Review.md` last paragraph | A malformed example that passes the schema, or a mathematically false constant that passes. |
| W10 | The upstream Lean repository constructs pure Yang–Mills theory with a selected Wightman phase, positive energy, and a unique vacuum. | Third-party claim | Unchecked | Observed: the repository exists and its README makes this claim and excludes the mass gap. Observed in web-search result summaries on 2026-11-23 (pages not opened): several outlets report that a committee chaired by David Gross validated the Lean code, that the validation covers existence and not the mass gap, that the committee says it does not yet fully understand the proof, and that its roughly 1,147-page informal document is private. Reports differ on the release date (Nov 9 plan versus Nov 10 publication). One reports that OpenAI said its public target omitted some lattice-construction links. Not observed: a Lean build, or a reading of the committee document. | U1; W1 in [SOURCES.md](SOURCES.md#web-reports-on-the-upstream-validation); G1 Turn 0a | A failed `lake build` or `VerifyJoint.lean` at the pinned commit. |
| W11 | For the free massive scalar, the full-central-block total-variation distance between opposite constant collars of fixed lattice-unit amplitude (φ_bdy = ±1) reaches the maximum value 2 as the refinement B grows. | Observed | E2 | At mℓ = 6, 2TV is 2.000000 (to six decimals) for B ≥ 5. At mℓ = 12 it is 1.953 at B = 10 and still rising. Extrapolation to a → 0 is inferred. Free field with input mass. Opposite constant collars only. R = 3, mℓ = 6 and 12. Says nothing about Yang–Mills or about other collars. | O1 turn 2 (ChatGPT's run); independent rerun [`artifacts/independent-rerun-2026-11-23/`](artifacts/independent-rerun-2026-11-23/) | A run with different parameters that does not saturate. |
| W12 | For the same model, the full-central-block distance for a physically scaled collar (φ_bdy = ±a) stays below the maximum over B = 1 to 10 and grows more slowly as B increases. | Observed, not established | E2 | 2TV(phys) at mℓ = 6 rises 0.324 → 0.802. At mℓ = 12 it rises 0.062 → 0.120. Both still rise at B = 10. No limit as a → 0 is shown or proved. O1 states the same limit. | O1 turn 2; independent rerun | A proof or run showing the value approaches 2, or a proof that it converges. |

## What is done

1. **The spectral half is formulated.** W1 turns a decay hypothesis into a spectral gap. A1 gives the proof, five exact audit cases that show why weaker hypotheses fail (`Conditional_Spectral_Gap.md` §6, cases A to E), and a formalization plan. The hypotheses are the hard part.
2. **The Gaussian control is worked out.** W2 gives explicit constants for a free field with a given mass. For m = 2, q = 1, t* = 1 the sufficient constants are K = 128.12 (block mean), 109.14 (five sine modes) and 191.81 (mean plus four dipoles), with rate γ* = 1.9248 (A1 §"Exact Gaussian distances and uniform constants").
3. **Two candidate routes are compared.** C1 compares Balaban-style renormalization with Tomboulis vortex decimation. C1 concludes that the renormalization route has one localized gap, the crossover from weak to strong coupling. The vortex route has three open problems and bounds the Wilson-loop area law, not local clustering. These are C1's inferences. No test confirmed them.
4. **The upstream interface is mapped.** O1, A1 and G1 record that the upstream repository exposes an energy–momentum projection-valued measure and not a standalone Hamiltonian. The Lean target is therefore E({0 < p₀ < m}) = 0, which A1 recommends proving first.
5. **Traps are named.** The obstructions in the next section came from this work. They narrow the search.

## Known obstructions

| ID | Obstruction | Effect | Source |
|---|---|---|---|
| B1 | The upstream renormalization stack assumes weak coupling at every step (`1 < hatBeta m`, `threshold m ≤ 1`). | Lowering a parameter cannot carry the construction into the crossover. A new layer of estimates is required. | C1 §0; G1 |
| B2 | The upstream infinite-volume limit comes from compactness and a subsequence. | It gives existence without a uniform bound. Uniqueness of the limit is not claimed. | C1 §0; G1 |
| B3 | The upstream construction splits the limit into "characters" with a full-support phase measure. | Decay of the mixed correlation does not imply decay in each phase. UFBI would force almost every character to give the same correlations. If characters encode distinct physical sectors, UFBI is refuted for this construction. C1 could not determine what `Character` represents. Check X2 found that the public spec leaves it abstract and does not require distinct correlations. The question for the constructed witness stays open. | C1 §0, §4 check 2; G1 |
| B4 | Boundary supremum over all collars includes collars that force a center vortex through the box. | If their influence does not decay, UFBI fails. Restricting to trivial-flux collars breaks the Part I argument, and the vortex free energy returns as a needed quantity. | C1 §4 check 1; G1 |
| B5 | The supremum over the full gauge-invariant σ-algebra of a central block of about (ℓ/(R·a))⁴ links can saturate at the maximum value of 2 as a → 0. | Observed for the free massive scalar with fixed lattice-unit collars (W11). Not observed for physically scaled collars over B ≤ 10 (W12). Order-one lattice collars make the amplitude bound M grow like 1/a, which removes the uniform prefactor. Restricting to blocked or smeared observables should follow from a demonstrated failure of the needed estimate, not from this saturation alone (O1 turn 2). | C1 §4 check 3; O1 turns 2 and 3; independent rerun |
| B6 | Clustering of a single plaquette or Wilson-loop pair does not give a gap. | The decay bound must cover a family whose centered vectors are dense in the vacuum's orthogonal complement, with one common rate. | G1 pasted block 1; A1 §"Conditional spectral theorem" |
| B7 | Rates differ by convention. A squared-norm decay rate Δ gives energy threshold Δ/2. Lattice-step decay converts to physical rate through the time spacing. | A bound stated in lattice steps can describe a different physical scale. | A1; G1 pasted block 1 |
| B8 | Gaussian collars are bounded deterministically. Random collars are not. | W2 does not transfer to random boundary data without an averaged estimate, a different norm or a coarse boundary. | A1 (W4) |
| B9 | The Wilson measure in the upstream repository is defined on periodic tori. | It has no fixed-boundary measure. The finite-box measure with frozen collar that UFBI needs does not exist upstream. | C1 §0 |

## What is left

The list follows the dependency order. Items 1 to 3 are the mathematical core. Every item is open.

| # | Task | Done when | Source of the criterion |
|---|---|---|---|
| 1 | Prove a uniform, gauge-compatible clustering estimate for Wilson Yang–Mills along the actual mesh, coupling and volume trajectory. The estimate must cover a family of observables dense in the vacuum's orthogonal complement, with one common positive rate. | A written proof that a mathematician checks, with every quantifier explicit. | A1 `Mathematician_Review.md` §"Review questions and next work" |
| 2 | Prove that this estimate gives temporal decay (SG) with a common rate. Track every loss between boundary-influence rate, clustering rate and spectral threshold. | A proof of the conditioning identity, the treatment of exceptional collars, the reflected pairing and the rate relation. | A1 §"Missing implication" |
| 3 | Pass the estimate to the continuum limit and to the selected phase. | Convergence of correlations with finite, cutoff-independent prefactors, plus a common selected phase for the dense family. | A1 §"Reconstruction and limit obligations" |
| 4 | Show that the reconstructed theory is nontrivial and satisfies the axioms the problem statement requires. | A check against the official problem statement (R1). | A1 §"Review mandate" |
| 5 | Run the cheap falsification checks X1 to X3 before further formal work. | See table below. | C1 §4; G1 |
| 6 | Obtain independent review of the Wilson hypothesis by a constructive-QFT or lattice-gauge mathematician. | A written assessment that classifies each claim as correct, correct with added hypotheses, incorrect, or unresolved. | A1 `REVIEW_REQUEST.md`; A1 `Mathematician_Review.md` §"Review questions and next work" |
| 7 | Compile the conditional spectral bridge (W1) in Lean against a pinned upstream build. | Build succeeds. No `sorryAx`. `#print axioms` shows only standard axioms. Euclidean-time and PVM identifications are proved. | A1 `FOUNDATION_STATUS.md` §6 packet A |
| 8 | Repair the A1 and A2 statements in the Lean scaffold (reflection positivity, transfer operator). | Real reflected geometry in place of `True`. A2 excludes the zero operator. | A1 `Mathematician_Review.md` §"Lean status" |
| 9 | Formalize the whole chain in Lean with no `sorry`. | Pinned build, axiom report. | A1 |

### Falsification checks

| ID | Check | Cost (per source) | Result so far |
|---|---|---|---|
| X1 | Gaussian UV check. Compute the boundary influence for a free massive scalar as a → 0 at fixed m·ℓ. | "1–2 days" (G1). | **Run, partial answer.** ChatGPT ran G1's script in O1 turn 2 and extended it to B = 10. An independent rerun on 2026-11-23 reproduced the numbers. Fixed lattice-unit collars: 2TV reaches 2.000 for B ≥ 5 at mℓ = 6. Physically scaled collars: 2TV rises slowly (0.32 → 0.80 at mℓ = 6, B = 1 to 10), no limit shown. Free model only. G1's own transcript shows no output, and its Discord draft says "Running now in Python". |
| X2 | Character audit. Find what `Character` means in `ChallengeSpec.lean`. Search the 100,168 reachable declarations for a result that makes correlations differ between characters. | "hours" (G1). "days" (C1). | **Partly run (2026-11-23).** Observed in the pinned source: `Character` is an abstract compact metric space with a full-support probability measure `phaseMeasure`, a distinguished `selected` point, and a correlation indexed by `Option Character` ([`ChallengeSpec.lean`](sources/upstream/pinned-3456e5e/ChallengeSpec.lean) lines 34–41). The `Reconstructed` structure constrains it by continuity in the character, the mixture identity ∫ correlation(some i) = correlation none, and `root` at `selected` (lines 124–143). Nothing in that structure requires two characters to give different correlations. The header of [`YM/Phase/Mixture.lean`](sources/upstream/pinned-3456e5e/Mixture.lean) describes characters of "the actual compression algebra devoted to H₀ of the same table". Inferred: a one-point character space satisfies the stated constraints, so the public statement does not refute the UFBI collapse. Unknown: whether the constructed witness has a nontrivial character space. Not done: the search of all 100,168 declarations. Coverage: `ChallengeSpec.lean` read in full. `PublicTheory.lean` and `Construction.lean` searched for the word `Character` only (no match in either). `PublicWilson.lean` fetched, not searched. `YM/Phase/Unique.lean`, `Mixture.lean`, `Picks.lean` and `Detect.lean`: first 14 to 40 lines and a declaration grep. |
| X3 | Twisted-collar Monte Carlo. SU(2) Wilson at β ≈ 2.3 to 2.7. Compare trivial and maximally twisted collars. Cheaper first runs: 3D SU(2) and 4D Z₂. | Not stated. | **Not run.** |

## Disagreements and corrections among sources

| Topic | Claim A | Claim B | Resolution |
|---|---|---|---|
| UFBI Part I | G1: "the core theorem is established" (Dobrushin–Shlosman, Martinelli–Olivieri). | C1: hypothesis. Applicability to compact spin spaces and gauge-invariant σ-algebras unverified. | Unresolved. This repository sides with C1, the primary source, because C1 states what it did not verify. |
| Gaussian UV check | G1 Discord draft: "Running now in Python". | G1 transcript: script supplied, no output shown. | G1 did not report a result. ChatGPT (O1 turn 2) ran the script and reported numbers, and an independent rerun reproduced them. The result is in W11 and W12. |
| Scaffold quality | G1, pasted block 1: scaffold of the three lemmas. | A1: the scaffold has placeholder premises and admits the zero operator. | A1 supersedes. A1 is later and audits the file. |
| Collar random sampling | A1 earlier Gaussian work treats deterministic bounded collars. | A1 audit (W4): raw random collars violate the cutoff. | Both stand. They answer different questions. |
| Mass-gap formulation | Task prompts ask for `spectrum H ⊆ {0} ∪ [m, ∞)`. | Upstream exposes a projection-valued measure, not H. | The projection form is the first target. The operator form needs a generator identification. |

## Provenance of the models and process

Observed from the sources: the work ran across three assistants. C1 used Claude (page label "Opus 5.5"). G1 used Gemini and mentions assistants "Fable 5.5" and "Astra 6.2" that ran elsewhere. A1 and O1 used ChatGPT. The human user coordinated the runs by pasting outputs between assistants (G1 Turn 2).

Inferred: results that two assistants repeat, such as the weak-coupling obstruction B1, are not independent confirmations. G1 summarizes C1 and O1. A1 builds on earlier ChatGPT work. A1 says so: "Model agreement is not a verification criterion."

## Not covered

- ChatGPT chat O3 ("Kernel construction from UOR", Jul 2025) was opened but not read in full. The viewed parts concern neural kernels and operations tooling. This repository judges it out of scope. Unknown: whether unseen parts mention Yang–Mills. See [SOURCES.md](SOURCES.md#search-coverage).
- The upstream Lean sources were not cloned or built.
- The Python tests in A1 were not rerun. This repository reran only the G1 script (independent rerun, W11 and W12). Observed: `lean`, `lake` and `elan` are not on the path. Observed: all 33 checksums in A1 verify.
- Literature named in C1 from memory was not looked up.
