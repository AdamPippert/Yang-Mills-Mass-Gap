# UFBI v0.1 — operational specification and Gaussian control

**Date:** 2026-11-20  
**Status:** preregisterable mathematical contract and executable *finite-grid falsification test*. Not a Yang–Mills theorem, a proof of uniformity, or a Lean kernel-checked result.

## Purpose and non-goals

The ultimate use of UFBI is as an auxiliary strong spatial-mixing estimate while proving **uniform Euclidean clustering** for gauge-invariant local observables, and then a reconstructed Hamiltonian mass gap. It is not interchangeable with reflection positivity, exponential time clustering, a selected-phase limit, or density of the observable-created states. The Gaussian free-field experiment is a *control*, not a proof for Wilson gauge fields.

## 1. General probabilistic contract (Track 2)

Let `a>0` be lattice spacing and `Λ_{a,L}` a finite four-dimensional region. Let `Q⊂Λ` be a central block with fixed physical side `q>0`. Let `D=dist_phys(Q, exterior collar)` be the minimum physical separation. For each admissible exterior collar `τ∈C_{a,L}(M)`, let `μ_{a,L}^τ` be a **probability** law of the interior configuration given that collar. An admissible *observable channel* `F_{a,Q}: Configuration(Q)→ℝ^k` must be measurable and specified *before* testing. Its dimension `k` must remain bounded under refinement; a fixed collection of smeared Wilson loops/blocked plaquettes is a candidate in gauge theory. Write `ν_{a,L,F}^τ= (F_{a,Q})_* μ_{a,L}^τ`.

**UFBI-F(K, γ, M, q, F):** there exist fixed `K<∞` and `γ>0` such that for **every** admissible `a,L,Q,τ,τ'` with central side `q` and collar amplitude bounded by `M`,

`2 TV(ν^τ, ν^τ') ≤ min(2, K · M · exp(-γ D))`.

`2TV(ν,ν') := 2 sup_{A measurable} |ν(A)-ν'(A)|`, so `0≤2TV≤2`. `K` has units inverse to those of `M`; if collars are normalized dimensionlessly, `K` is dimensionless. Quantifiers matter: **K and γ cannot depend on a, L, D, the collars, or the particular discretization of a fixed channel F**. They *may* depend on the declared central physical size `q`, class of observable channels, fixed mass/coupling, and declared amplitude class. If varying `q`, declare the allowed interval and use common constants.

For nonlinear or gauge-valued collars, `M` denotes a separately specified admissible-class size, **not** the unbounded supremum of a real field. Near `M=0`, the linear factor `M` is appropriate for the Gaussian test but must not be assumed for Wilson measures absent an established continuity theorem.

### Non-vacuous test criterion

An observed inequality with the right side equal to 2 is tautological. A useful acceptance test must include separations with `K M exp(-γD)<2` and measure the worst ratio over sampled collars. A finite grid can *falsify* specified `K,γ`, but cannot establish a quantified UFBI theorem. To avoid fitting away a counterexample, choose the constants and observable family on a calibration set and test them unchanged on held-out refinements, separations, and collars.

## 2. Free-scalar instantiation (Track 1)

Take `D_L={1,…,L}⁴`, `L=R B`, odd `R≥3`, center `Q` of `B⁴` sites, **fixed physical central side** `q=1`, and spacing `a=q/B`. Thus the whole box has physical side `R q`. This deliberately differs from the earlier `a=1/(RB)`, which fixed the *outer box* and changed the *central size* when varying `R`. With the new choice, changing `R` increases the physical collar separation while leaving `Q` fixed.

The discrete precision is `A=-Δ_D+(ma)² I` and covariance is `Σ=A⁻¹`. For fixed ghost-node Dirichlet collar `τ`, `μ^τ=N((A⁻¹ b(τ))|_Q, Σ_QQ)`. A continuum scalar of canonical engineering dimension one is encoded as `φ=a Φ`; hence the sampled opposite collars are `τ=+a M s`, `τ'=-a M s` for a face pattern `s∈{-1,0,+1}`. On face intersections, **each exterior nearest-neighbor link contributes independently**.

The measured lattice-to-ghost separation is `D=a ([(R-1)/2]B+1)`; the offset `+a` is explicitly retained. It approaches `[(R-1)/2]q` as `B→∞`.

For `h=P_Q A⁻¹ (b(τ)-b(τ'))` and `Σ_QQ=P_Q A⁻¹ P_Qᵀ`, the **full region** Mahalanobis statistic is

`d_full² = hᵀ Σ_QQ⁻¹ h`.

For a linear observable channel `F: ℝ^{B⁴}→ℝᵏ` with nonsingular `F Σ_QQ Fᵀ`, the reduced statistic is

`d_F² = (F h)ᵀ (F Σ_QQ Fᵀ)⁻¹ (F h)`.

The exact distributional identities are `2TV(F_*μ^τ,F_*μ^τ')=2erf(d_F/(2√2))` and `H²=1−exp(−d_F²/8)` with Hellinger convention `H²=1−∫√(dP dQ)`. Data processing requires `d_mean≤d_moments≤d_full` (for nested linear channels). These equalities are exact mathematical statements; the floating-point evaluations are approximate.

### Predeclared channels

- `mean`: one block-constant linear statistic (the average field);
- `moments`: block constant plus four coordinate dipole moments (five dimensions for B>1);
- `full`: identity channel on all B⁴ sites, used only as a stress test, **not** assumed continuum-stable.

Channel normalization does not affect `TV` for a nondegenerate linear transformation. The current code uses no explicit smooth convolution kernel; the block constant and dipoles are elementary test smearings and should not be confused with a complete Wilson observable family.

### Sampled collars

`constant` (opposite uniform values on all faces), `face` (one nonzero face), `checkerboard` (alternating face signs), and `random` (reproducible independent face signs with seed 0). This is **not** a supremum over all collars. A counterexample from any one pattern refutes the proposed bound; passing all four does not prove it. Constant collars can be worst among some classes, but no maximization theorem has been established here.

## 3. Registered pilot test

- Model: 4D massive free scalar, physical mass `m=2`, central side `q=1`, amplitude `M=1`;
- Candidate: `K=4`, `γ=m/2=1` (hypothesis to test, **not** mathematically justified);
- Refinements: `B=2,3,4`; relative box sizes: `R=3,5,7`;
- Four face patterns and three observation channels;
- Measured response: exact Gaussian `2TV` to numerical tolerance, plus `H`, `d_F`, candidate bound and pass/fail;
- Test status: **rejected** by `constant` collars at `R=3` for all `B` tested, including the `mean` observable channel. Passing other cases does not rescue the universal statement.

Examples (constant collars):

| B | R | D | full 2TV | candidate bound | result |
|---:|---:|---:|---:|---:|---|
| 2 | 3 | 1.5 | 1.2517 | 0.8925 | FAIL |
| 3 | 3 | 1.3333 | 1.4423 | 1.0544 | FAIL |
| 4 | 3 | 1.25 | 1.5551 | 1.1460 | FAIL |
| 4 | 5 | 2.25 | 0.3423 | 0.4216 | PASS |
| 4 | 7 | 3.25 | 0.0523 | 0.1551 | PASS |

The failure is specific to the *proposed constants*: it does **not** show a uniform bound with larger K or smaller γ is impossible. Indeed, the finite-grid test does not determine the optimal constants. It suggests testing larger B at fixed q, and larger R at fixed q, with **held-out** samples.

## 4. Numerical validation and limits

`test_ufbi_control.py` independently constructs a small Dirichlet Laplacian as a dense Kronecker sum, checks DST inversion, checks `τ=τ'` yields zero distance, linearity of boundary source and the nested-channel data processing inequality. Full covariance inversion uses CG on the implicit restricted inverse, while low-dimensional channel covariance is computed via matrix-vector applications of the DST inverse. The result CSV records `solver_diagnostic` (CG relative residual for `full`, covariance condition number for the others).

Residual convergence is not a certified floating-point bound. A proof needs a finite-grid linear-algebra theorem, quantitative numerical error control if test outputs are to be formally certified, and an analytic estimate uniform across grids. Hellinger/TV are exact only up to numerical error in the reported run.

## 5. What would be necessary for Yang–Mills

The gauge-theory version requires (i) a precise gauge-invariant collar condition or boundary state, (ii) conditional Wilson measures that are normalizable and gauge-compatible, (iii) a fixed, controlled family of blocked/transported gauge-invariant observables, (iv) an actual estimate uniform in UV spacing and volume, and (v) transfer to a selected continuum phase. Compact group elements should **not** be rescaled by the scalar-field factor a.

UFBI for a fixed finite-dimensional observable family cannot itself supply the required all-state spectral completeness. Before inserting UFBI into `ReflectionPositivity.lean`, prove/assume separately the argument that a suitable uniform strong-mixing condition yields connected temporal clustering for a dense family, with the **same physically normalized positive rate**. This argument must handle operator insertions, normalization, and possible contact terms.

## 6. Run and acceptance

```bash
python -m pip install numpy scipy
python -m unittest discover -s MassGap/UFBI -p 'test_*.py' -v
python MassGap/UFBI/ufbi_control.py --strict --mass 2 --B 2 3 4 --R 3 5 7 \
  --patterns constant random checkerboard face --K 4 --gamma-fraction 0.5 \
  --out MassGap/UFBI/results.csv
```

The `--strict` command is **expected to exit with status 1** for the preregistered rejected candidate. Omit `--strict` to generate the diagnostic CSV without failure. A subsequent hypothesis must change an explicitly versioned parameter, not silently weaken this rejection.

## 7. Next proof obligations, ranked

1. **Hardest:** uniform, physically normalized upper bound on `d_F` for *all* admissible collars and lattice refinements, depending on an explicitly chosen bounded channel class. Derive through Green-function decay, trace/operator estimates and conditional covariance stability.
2. **High:** identify physically meaningful admissible collar norm in the Wilson model (not scalar-field amplitude), and show quantitative bounds for conditioned gauge-invariant observables.
3. **High:** prove UFBI-to-clustering for a dense observable class, then preserve the rate under UV/volume subsequences and phase selection.
4. **Moderate:** exact Gaussian equal-covariance TV/Hellinger formulas and data-processing inequality as independent Lean/mathlib lemmas.
5. **Moderate:** certified finite-lattice DST eigenvalue computation and residual-to-Mahalanobis error certificates.

## 8. Analytic supplement v0.2 — 2026-11-20

The original v0.1 pilot and its rejection above remain unchanged. The new **GaussianBoundaryEstimate.md** derives sufficient UFBI constants analytically for the specified Dirichlet free scalar, then checks their implementation in **gaussian_bounds.py**. This supplement is an ordinary mathematical derivation, not a Lean-verified proof.

For all physical collars \(|\tau|,|\tau'|\le aM\), all odd \(R\ge3\), and all \(B\ge1\) with \(ma\le t_*\), the **block mean** satisfies
\[
2\operatorname{TV}_{\mathrm{mean}}
\le\min\{2,K_{\mathrm{mean}}M e^{-\gamma_*D}\},
\]
\[
K_{\mathrm{mean}}=
\sqrt{2/\pi}\frac{\pi^4}{4}q\sqrt{(mq)^2+4\pi^2},
\qquad
\gamma_*=
m\frac{2\operatorname{arsinh}(t_*/2)}{t_*}.
\]
This comes from a massive harmonic comparison barrier and a first-sine-mode lower bound on physical block-mean variance. Opposite constant collars are proved to attain the exact block-mean supremum over the amplitude class; the earlier “no maximization theorem” observation remains applicable to general joint channels, but no longer to the scalar block mean.

For a joint smearing channel, a sufficient intrinsic admissibility certificate is
\[
\langle f,(-\Delta_a+m^2)f\rangle_a\le
\Lambda_{\mathrm{sm}}\langle f,f\rangle_a
\quad\text{for all }f\text{ in the smearing span}.
\]
It gives \(K_F=16\sqrt{2/\pi}\,q^2\sqrt{\Lambda_{\mathrm{sm}}}\), with the same \(\gamma_*\). Fixed channel count or individual bounded norms alone do not establish this certificate. A separate explicit trial-pairing certificate covers the existing mean-plus-four-dipoles channel despite its sharp support boundary.

For \(m=2,q=1,t_*=1\), the new sufficient coefficients are:

| Channel | \(K\) | Uniform \(\gamma_*\) |
|---|---:|---:|
| Block mean | 128.1198512355 | 1.9248473002 |
| First sine mode plus four first coordinate excitations | 109.1392079748 | 1.9248473002 |
| Existing mean plus four dipoles | 191.8093099258 | 1.9248473002 |

These conservative constants are derived, not fitted, and include \(B\ge2\) for the five-component channels. Each controls all bounded measurable functions of the chosen channel with supremum norm at most one. They do not establish an estimate for compact gauge links, arbitrary unbounded observables, typical unrestricted random collars, or a reconstructed all-state spectral gap.

**Validation:** twelve numerical regression tests pass; 14 geometries, 56 collars, and 168 channel measurements produce no violations of the new bounds. The complete numerical results, source hashes and version information are in **estimate_checks.json**. Numerical checks are not the proof of uniformity and are not formal error certificates.

**Decision gate:** do not promote a sampled test to a theorem. Record `PASS_SAMPLE`, `REJECTED_BY_COUNTEREXAMPLE`, or `INCONCLUSIVE`; only a mathematical proof discharges the universal UFBI obligation.
