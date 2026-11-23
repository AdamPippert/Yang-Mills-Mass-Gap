# Mass-gap foundations: status and next work packets

**Audit date:** 20 November 2026  
**Scope:** Gaussian UFBI control, repository interfaces, and the next conditional spectral theorem.  
**Proof status:** No new kernel-checked Yang–Mills mass-gap lemma has been produced in this work. This report records source inspection and mathematical reasoning, not a successful Lean build or an independent human review.

## Decision

The next completed milestone should be a **compiled conditional theorem showing that common-rate exponential decay on dense centered OS states eliminates subgap spectral weight**, followed by an adapter to the public reconstruction interface.

Develop that theorem in parallel with a constructive-QFT review of the Wilson clustering hypothesis. Further numerical Gaussian sweeps are lower priority unless a reviewer identifies a specific unresolved question.

## 1. Present evidence

| Component | Current status | Remaining obligation |
|---|---|---|
| Gaussian boundary estimate | Ordinary proof for a fixed block mean and controlled smeared families | Independent review and Lean formalization |
| Gaussian implementation | Recorded run: 12 passing tests, 14 geometries, 56 collars, 168 channel measurements, no recorded violations | Floating-point checks are not proof certificates |
| Upstream OS and spectral machinery | Inspected pinned source | Compile our imports and adapter |
| Original reflection-positivity scaffold | Unvalidated and inadequately specified | Repair statements before relying on them |
| Conditional clustering-to-gap theorem | Mathematical proof identified | Lean implementation and axiom audit |
| Uniform interacting Wilson clustering | Not established by this work | Nonperturbative estimate with correct cutoff, observable and phase quantifiers |

The recorded tests were inspected, not rerun, in this audit. Their source hashes match the inspected implementation.

The Gaussian precision is
\[
A=-\Delta_D+(ma)^2I,\qquad m>0.
\]
It tests consequences of an input mass. It does not derive Yang–Mills mass generation.

Control materials:

- [GaussianBoundaryEstimate.md](https://chatgpt.com/library?file_id=libfile_fde3_f-0b77088e29e48191a98d6eafdf7d2fa9_85d3e1f1788881918d6cc0938b07dac8&account_id=personal)
- [SPECIFICATION.md](https://chatgpt.com/library?file_id=libfile_fde3_f-31b2914501608191a3faacf16bfdf2ad_85d3e1f1788881918d6cc0938b07dac8&account_id=personal)
- [estimate_checks.json](https://chatgpt.com/library?file_id=libfile_fde3_f-7107326bd9a4819188f7d1d8abec7cab_85d3e1f1788881918d6cc0938b07dac8&account_id=personal)

## 2. Corrections to the original Lean scaffold

The earlier ReflectionPositivity.lean is not an implementation-ready proof foundation.

- **A1:** The assumption <code>hGeometry : True</code> constrains neither the arbitrary reflection nor the positive-time support. Replace it with actual geometry and measure compatibility. This is a specification defect.
- **A2:** Existence of a positive self-adjoint operator alone permits the zero operator. Require identification with descended time translation or a specified transfer kernel, and the quotient, normalization and vacuum relationships.
- **A3:** One large <code>sorry</code> hides density, spectral representation, centering, phase selection and uniform limit passage. Expose these as hypotheses or separately proved adapters.

Compilation with admitted proofs would not repair these specifications.

## 3. Existing upstream attachment points

Repository: yang-mills-group/OpenAI-YM-20261028  
Inspected commit: <code>3456e5e75cf8d4cd558955a5c7638fba2d68f464</code>  
Toolchain: <code>leanprover/lean4:v4.32.0</code>

| Source | Reusable interface |
|---|---|
| [YM/Hilbert/Kolmogorov.lean][kolmogorov] | Kernel.Gram, separated Hilbert completion and bounded-map extension |
| [YM/OS/Dynamics.lean][dynamics] | Chamber realization; translated words agree with flow.E |
| [YM/OS/Flow.lean][flow] | Strongly continuous self-adjoint contraction semigroup |
| [YM/Heat/Lift.lean][heat] | Semigroup.ℚmeasure, nonnegative energy support, diagonal heat/PVM integral |
| [PublicView.lean][publicview] | Public reconstruction uses A.momentum.region and its diagonal measures |
| [YM/Phase/Unique.lean][phase] | Positive phase disintegration and countable dense-family proof pattern |

These are source-level findings. Our adapter has not been compiled. Existing continuum OS machinery does not itself verify our earlier finite periodic Wilson A1/A2 statements.

Use the existing PVM for the first theorem. A formulation using an unbounded Hamiltonian's spectrum additionally needs identification of that generator and its spectral measure.

## 4. Exact next mathematical theorem

Let \(\mathcal H\) be a complex Hilbert space, \(H\ge0\) self-adjoint, \(\Omega\) a unit vector with \(H\Omega=0\), and \(P\) the energy spectral measure.

Let \(\mathcal D\subset\Omega^\perp\) have closed linear span \(\Omega^\perp\). Suppose one common \(\mu>0\) satisfies
\[
\forall v\in\mathcal D\;\exists C_v\ge0\;\forall t\ge0:
\quad
0\le\langle v,e^{-tH}v\rangle\le C_v e^{-\mu t},
\]
with every \(C_v\) finite. Then
\[
P([0,\mu))=P_\Omega,\qquad
\ker H=\mathbb C\Omega,\qquad
\sigma(H)\subseteq\{0\}\cup[\mu,\infty).
\]

### Scalar measure proof

For \(\nu_v(B)=\|P(B)v\|^2\) and \(0\le r<\mu\),
\[
e^{-rt}\nu_v([0,r])
\le\int e^{-tE}\,d\nu_v(E)
\le C_v e^{-\mu t}.
\]
Consequently \(\nu_v([0,r])\le C_v e^{-(\mu-r)t}\to0\). Countably many \(r\uparrow\mu\) eliminate the whole subgap interval. Bounded projections extend the conclusion from the spanning family to \(\Omega^\perp\); the vacuum gives the remaining rank-one projection.

Implement the positive scalar-measure lemma first, followed by the PVM and density step. Prefactors may depend on the fixed state. The rate must be common.

The source-native endpoint has the form
\[
S.\mathbb Q\mathrm{measure}.\mathrm{region}
\{p:0<p(\mathrm{timeAxis})<\mu\}=0.
\]
This displayed formula is not a claim of elaborated Lean code.

### Negative controls

- A massive observed sector can coexist with an unobserved gapless sector: finite channels do not establish density.
- Eigenvalues \(1/n\) allow individual finite-support vectors positive decay rates without any common gap.
- \(\|e^{-tH}v\|^2=\langle v,e^{-2tH}v\rangle\). A squared-norm decay rate \(\mu\) in \(t\) yields only threshold \(\mu/2\).
- The Euclidean input must be the correctly centered, reflected/adjointed diagonal OS pairing.

## 5. Analytical obligations

**Boundary admissibility.** The Gaussian restriction \(|\tau|\le aM\) is deterministic. It does not show that sampled collars satisfy it, or provide a gauge-compatible Wilson condition. Cover all relevant collars or bound the contribution from excluded ones.

For bounded interior \(F\) and exterior-measurable \(G\),
\[
\operatorname{Cov}(F,G)
=\operatorname{Cov}(\mathbb E[F\mid\text{exterior}],G).
\]
A uniform oscillation estimate on the conditional expectation can yield clustering. A bound on an uncontrolled subset of collars cannot.

**Observable density.** Obtain an algebra whose centered OS vectors span the vacuum orthogonal complement. Constants may depend on a fixed observable but must remain finite and cutoff-independent in the relevant limit.

**UV and volume.** The inspected specification requires positive logarithmic growth of \(\beta\) as the mesh shrinks and an ordered continuum/infinite-volume passage. A fixed small-\(\beta\) estimate alone does not cover that trajectory. Subsequence extraction does not supply missing uniformity. [ChallengeSpec.lean][challenge]

**Rates.** Record the boundary-insensitivity rate, temporal clustering rate and spectral threshold separately; geometry and time conventions can change their relationship.

**Phases.** If the relevant positive measures disintegrate as \(\nu=\int\nu_\chi\,d\eta\), zero mixed subgap mass implies zero subgap mass in almost every phase. A common countable dense family and compatible phase selection remain necessary. Full support upgrades zero integral of a continuous nonnegative function to pointwise zero, not an arbitrary averaged upper bound to a pointwise upper bound.

UFBI is optional: direct Wilson clustering can feed the same spectral theorem.

## 6. Work packets

### A. Compiled spectral bridge

**Owner:** Lean analyst with measure theory and functional analysis experience.

Proposed modules, not implemented files:

| Module | Responsibility |
|---|---|
| MassGap/LaplaceSupport.lean | Positive Laplace decay eliminates low-energy measure |
| MassGap/OSGap.lean | Existing OS PVM and dense centered states |
| MassGap/PublicBridge.lean | Chosen OS witness to public energy–momentum projection |
| MassGap/ReflectionPositivity.lean | Separately repair finite-lattice statements using existing types |

Acceptance: pinned build succeeds; no replacement physical base types; no <code>sorryAx</code> in the conditional bridge; <code>#print axioms</code> reports only accepted standard Lean foundations; the Euclidean-time and public-PVM identifications are proved.

The current workspace has no available <code>lean</code>, <code>lake</code>, or <code>elan</code>. A pinned build environment is an operational prerequisite.

### B. Wilson hypothesis review

**Owner:** constructive-QFT / lattice gauge mathematician.

Determine whether a plausible, sufficient uniform estimate can hold along the actual scaling trajectory. Deliver a gauge-compatible boundary class, observable algebra, conditioning identity, exceptional-collar treatment, cutoff quantifiers and explicit rate losses. Mark every conclusion proved, conjectured or obstructed.

This is the highest-value human review. The Gaussian calculation does not resolve it.

### C. OS, density and phase review

**Owner:** OS reconstruction / operator-theory specialist; may be combined with B.

Verify adjoints, centering, physical time, density and phase choice. Trace existing PVM identifications and assess extension of the upstream almost-everywhere phase argument to a common gap.

### D. Additional model work

Use models for bounded declaration audits, small Lean lemmas, counterexamples and code/specification comparisons. Require a proof, compiling term or reproducible counterexample. Model agreement is not a verification criterion.

Three separate agent audits informed this report. They are not independent human peer review.

## 7. Completion and reversal criteria

Proceed with A once the build environment is available; review B in parallel. Keep Gaussian controls for normalization and conditional-expectation checks.

Reconsider UFBI if its collar restriction cannot control the actual conditional measure, or if enlarging the observable family destroys the common positive rate. The generic spectral theorem remains useful if the analytic route changes.

The next completed foundation must include a compiled conditional theorem and its axiom report. A new scaffold or a larger numerical sweep is different evidence.

[kolmogorov]: https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Hilbert/Kolmogorov.lean
[dynamics]: https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/OS/Dynamics.lean
[flow]: https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/OS/Flow.lean
[heat]: https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Heat/Lift.lean
[publicview]: https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicView.lean
[phase]: https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Phase/Unique.lean
[challenge]: https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/ChallengeSpec.lean

