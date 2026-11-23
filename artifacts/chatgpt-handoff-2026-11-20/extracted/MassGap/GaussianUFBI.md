# Gaussian 4D boundary-influence control for MassGap

Date: 2026-11-20. Status: numerical control, NOT a Yang–Mills theorem and NOT a Lean-verified proof.

## Model

Let `D={1,...,L}^4`, `A=-Δ_D + (mℓ/L)^2 I`, `Σ=A⁻¹`, and let `Q` be the middle `B^4` cube with `L=RB` (`R=3` in the experiment). For two fixed external boundary collars, the conditional Gaussian measures on `Q` have common covariance `Σ_QQ` and mean displacement `h_Q = [Σ (b(τ)-b(τ'))]_Q`.

Their squared Mahalanobis displacement is

`d² = h_Qᵀ Σ_QQ⁻¹ h_Q`.

For equal-covariance Gaussians,

`TV = 2 Φ(d/2) - 1 = erf(d/(2√2))`,

`H² = 1 - exp(-d²/8)` under the convention `H² = 1 - ∫√(dP dQ)`.

`2TV` has maximum 2. This experiment tests the fixed pair of constant collars `τ=+1`, `τ'=-1`, not a supremum over arbitrary collars. The test is not a quantitative reflection-positivity result.

## Discretization audit

The source at each boundary-adjacent lattice site counts all external nearest-neighbor links. The DST-I eigenvalues `2(1-cos(π k/(L+1)))` summed over four axes are the correct Dirichlet operator eigenvalues on interior nodes. The inverse action is `DST-I * diag(1/λ) * DST-I`; CG inverts the restricted covariance, not the full field precision matrix.

For a 4D scalar of engineering dimension one, setting a physical boundary field `Φ=±1` corresponds in this normalization to lattice field `φ=aΦ`, with `a=ℓ/L` (and `ℓ=1` in the code). Hence the physical-collar distance equals `a d_lattice`, since means scale linearly and covariance remains unchanged. This interpretation requires the specified Gaussian lattice-field normalization; it cannot be directly transferred to compact gauge links.

Physical side length of `Q` is `ℓ/R`, and its distance to the external boundary tends to `(R-1)ℓ/(2R)` (`ℓ/3` for `R=3`), up to mesh offsets. The mass exponent is controlled by this separation, but a statement `2TV ~ C exp(-m ℓ/3)` is NOT an established asymptotic: finite-volume geometry, the whole field sigma algebra, the covariance precision and the source amplitudes also enter.

## Numerical outputs

Using SciPy 4D DST-I and CG with `rtol=1e-9` and `maxiter=2000`; all reported CG solves returned `info=0`.

| mℓ | B | L | d_lattice | 2TV_lattice | d_physical | 2TV_physical |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 1 | 3 | 1.226966 | 0.920886 | 0.408989 | 0.324065 |
| 6 | 3 | 9 | 6.497153 | 1.997680 | 0.721906 | 0.563731 |
| 6 | 5 | 15 | 13.205239 | ~2 | 0.880349 | 0.680379 |
| 6 | 6 | 18 | 16.762448 | ~2 | 0.931247 | 0.717030 |
| 6 | 8 | 24 | 24.076327 | ~2 | 1.003180 | 0.768088 |
| 6 | 10 | 30 | 31.544090 | ~2 | 1.051470 | 0.801855 |
| 12 | 1 | 3 | 0.231720 | 0.184473 | 0.077240 | 0.061613 |
| 12 | 3 | 9 | 0.839784 | 0.650871 | 0.093309 | 0.074423 |
| 12 | 5 | 15 | 1.744369 | 1.233784 | 0.116291 | 0.092735 |
| 12 | 6 | 18 | 2.260190 | 1.483128 | 0.125566 | 0.100121 |
| 12 | 8 | 24 | 3.366093 | 1.815268 | 0.140254 | 0.111815 |
| 12 | 10 | 30 | 4.534627 | 1.953258 | 0.151154 | 0.120489 |

The growth of `d_lattice` and saturation of `2TV_lattice` is consistent with a nonuniform lattice-amplitude notion of UFBI in this particular collar family. The `a`-rescaled results have not converged by B=10 and cannot yet establish a continuum bound.

## Concrete next analytical theorem (independent of Yang–Mills)

Given a family of regions Q_{a,L}, an admissible family of collar differences δτ, and a uniform physical-energy normalization, seek an **explicit** inequality

`sup_{a,L,δτ} || Σ_QQ^(-1/2) P_Q A^(-1) b(δτ) || ≤ K exp(-m * dist_phys(Q,∂Λ))`,

with specified restrictions on the collar norm, geometric parameters, constants K and m. Uniformity is not justified by the numerical test; establish it using off-diagonal Green-function bounds and an energy/trace estimate. For an arbitrary constant scaled source, only a family-specific estimate is required.

For a chosen coarse/smeared observables map `F`, the pushforward TV satisfies

`TV(F_*P, F_*Q) ≤ TV(P,Q)`.

However full-region TV saturation does NOT prove that blocking is mathematically required: a stronger metric can fail while a weaker observable norm succeeds. Nor does Gaussian UFBI alone imply spectral isolation or a nonabelian gauge-theory estimate.

## Dependency placement

Gaussian covariance / DST and Mahalanobis identity -> boundary-to-central field estimate -> precise test of proposed UFBI hypothesis -> **candidate** supporting estimate for lattice clustering / tightness. Independently require Wilson reflection positivity, phase-wise selected limit, OS-to-semigroup identification, and a dense generating observable algebra before A3.

Do not import this numerical control as an axiom into `ReflectionPositivity.lean` or replace its `sorry` lemmas with assertions about free scalars.

## Run

`python MassGap/GaussianUFBI.py`

Requires `numpy` and `scipy`. Code does not use a dense full covariance matrix. Its floating-point results are numerical approximations to exact finite-dimensional Gaussian quantities, not formally verified exact values.
