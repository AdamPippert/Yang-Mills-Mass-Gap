# Mathematician review scope and primary references

Prepared 20 November 2026. These are review proposals and source checks, not a new claim that Yang-Mills satisfies the needed estimates.

## Scope and evidentiary status

The immediate review target is the recovered UFBI specification, Gaussian analytic supplement, existing uncompiled Lean scaffold, and conditional spectral-gap argument. This reviewer read `SPECIFICATION.md`, `GaussianBoundaryEstimate.md`, `FOUNDATION_STATUS.md`, `README.md`, and `ReflectionPositivity.lean` after they were recovered during this packaging task. The abbreviation UFBI is retained as used in those sources; it is not silently equated with another established mixing condition.

The recovered status report identifies the upstream repository `yang-mills-group/OpenAI-YM-20261028`, commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464`, and toolchain `leanprover/lean4:v4.32.0`, and reports earlier source inspection. This reviewer has not freshly checked out or compiled that repository. The local scaffold visibly contains `sorry` and placeholder hypotheses. Historical numerical test claims remain distinct from tests rerun during the handoff task. The package is not a solution of the four-dimensional Yang-Mills existence and mass-gap problem.

## Recovered facts that should shape the review

- The actual Gaussian contract fixes physical block size `q`, uses `a=q/B`, diagonal-8 Dirichlet Laplacian, mass input `m>0`, and collars `||tau/a||_infinity <= M`. It is not an unrestricted all-boundary assertion.
- The original pilot `K=4`, `gamma=1`, at `m=2,q=M=1` was rejected. The supplement derives different sufficient constants and must not erase that failure.
- The supplement's physical rate is `rho_a=2 asinh(ma/2)/a`, bounded below by a common `gamma_*` on `ma<=t_*`. Its Gaussian analytical claim covers all collars in the specified deterministic amplitude class; its applicability to collars drawn from the underlying measure is a separate problem.
- Whole-span energy control and the alternative trial-pairing certificate are distinct sufficient conditions for joint channels. The block mean and hard-edged dipoles use the separate trial method; treating them as smooth energy-bounded weights would be a mistake.
- The supplement proves opposite constant collars maximize the scalar block-mean response using nonnegative coefficients. This supersedes the pilot's earlier absence of a maximization theorem for that scalar channel. It does not establish the same maximization for a joint signed channel.
- The original Lean A1 has `hGeometry : True` and arbitrary supplied reflection and support; A2's statement admits the zero operator and has `hQIsOSQuotient : True`; A3 hides the main analytic obligations in an admitted lemma. These are specification and proof debts, not build-only tasks.

## Questions in priority order

### 1 Audit the recovered boundary hypothesis and its proposed gauge extension

Check the explicit scalar conventions above against every theorem and implementation. The gauge extension still needs a measure, action, gauge group, finite-volume geometry, collar thickness, admissible boundary configurations, boundary metric or norm, class of interior channels, and norm or probability metric in the conclusion. Specify whether gauge boundaries are compared pointwise, almost surely, after quotienting gauge transformations, or after averaging. For exceptional boundary configurations, record the exceptional set and its quantitative probability bound.

Do not silently replace control of one block mean by control of the entire interior sigma algebra. If UFBI is intended to bound a channel law, state exactly which measurable channel is being pushed forward. Ask whether it extends to enough bounded functions or products to generate the physical Hilbert space.

For scalar Gaussian boundaries, unrestricted boundary amplitudes can defeat a uniform total-variation bound below one whenever the channel has nonzero boundary sensitivity. The recovered contract avoids that issue by its deterministic physical-amplitude bound. The remaining question is whether this collar class controls the actual conditioning problem, with a quantitative estimate for any excluded collars. Compact gauge variables remove that particular unbounded-amplitude mechanism but do not establish the desired estimate for the Wilson measure; they must not inherit the scalar `tau=a Phi` normalization.

**Requested decision:** Are the proofs of G1 through G8 valid under their literal quantifiers, and what gauge-compatible hypothesis could replace the scalar amplitude condition? If the proposed extension is obstructed, provide the smallest correction or an explicit counterexample.

### 2 Identify the exact implication from boundary influence to temporal correlations

Specify the conditioning sigma algebra and the local Markov or Gibbs specification that is used. Establish a bound on conditional expectations of interior observables as a function of exterior data. Explain how separation in the chosen geometry gives a bound for the positive Euclidean-time autocorrelations needed by the spectral theorem.

For bounded random variables, a useful elementary template is the identity

\[
\operatorname{Cov}(F,G)=\operatorname{Cov}(\mathbb E[F\mid\mathcal E],G)
\]

when \(G\) is measurable with respect to the exterior sigma algebra \(\mathcal E\). If the conditional expectation differs from a fixed constant by at most \(\epsilon\), then

\[
|\operatorname{Cov}(F,G)|\le 2\epsilon\|G\|_\infty.
\]

This is only a template. The proposed UFBI estimate must supply the stated uniform conditional-expectation bound for the actual observables. If a total-variation convention \(d_{\rm TV}=\sup_A|\mu(A)-\nu(A)|\) is used, the corresponding expectation difference for a bounded observable is at most \(2\|F\|_\infty d_{\rm TV}\); retain that factor consistently. For unbounded renormalized fields, specify truncations or moment bounds and justify their removal.

**Requested decision:** Does the stated hypothesis really imply the required temporal estimate, with an explicit rate and constants, or is a missing mixing lemma being assumed?

### 3 Verify observable coverage and positivity

Fix a positive-time gauge-invariant observable algebra and its OS null-space quotient. Prove that centered observable vectors have dense linear span in the vacuum orthogonal complement. A finite list of observables can miss low-energy sectors. Even a dense generating family does not suffice if every observable is allowed its own positive rate with no common lower bound.

The relevant autocorrelation is the positive semigroup matrix element \(\langle\psi,e^{-tH}\psi\rangle\). For an observable \(A\), use \(\psi=(A-\langle\Omega,A\Omega\rangle I)\Omega\), with the adjoint of \(A\) on the left in the correlation. Bounds on arbitrary signed or complex cross-correlations do not automatically give the needed positive spectral measure.

**Requested decision:** Which concrete algebra yields the required density, and does the Gaussian or proposed gauge bound apply to it?

### 4 Audit uniformity and the order of limits

Record separately the lattice spacing \(a\), lattice side length, physical side length, coupling, blocking factor, block size, collar distance, support size, field normalization, and renormalization scale. State every constant's permitted dependence.

For \(T_a=e^{-aH_a}\), a physical gap lower bound \(m>0\) corresponds to \(T_a\) contracting the nonvacuum subspace by at most \(e^{-am}\) per time step. A lattice rate \(\gamma_a\) is meaningful for this purpose through \(\gamma_a/a\), with correlation times measured consistently. Neither a fixed-lattice estimate alone nor the phrase 'uniform in scale' settles the continuum question.

Specify the limiting objects, topology, subsequence choices, normalization, and the reason the correlation bound passes to the infinite-volume and continuum limits. Prefactors need not be uniform in every abstract method, but a concrete passage to the limit must prevent their divergence from destroying the inference. Strong-coupling lattice results alone do not justify a weak-coupling continuum claim.

**Requested decision:** Which uniform estimate is the main unsolved analytic obligation, and does any proposed bound become vacuous as \(a\to0\)?

### 5 Separate reconstruction from the spectral lemma

The conditional spectral lemma can assume a nonnegative self-adjoint Hamiltonian. Constructing that Hamiltonian from the actual limiting Euclidean theory is a separate obligation. Cite a reconstruction theorem with its complete regularity or growth assumptions, covariance, symmetry, positivity, and other required hypotheses.

OS II explicitly extends and corrects OS I. Merely citing reflection positivity or the original 1973 abstract does not establish the full reconstruction theorem. At finite lattice spacing, identify the actual positive transfer-matrix construction and action; if the action is changed under a proposed approximation or improvement, recheck the applicable positivity argument.

The full target also requires a nontrivial quantum Yang-Mills theory, the correct observable interpretation, and the required axiomatic properties. A one-dimensional vacuum-only Hilbert space would satisfy a vacuous lower-bound statement but is not an acceptable solution.

The recovered status report also identifies a selected-phase interface. If spectral measures disintegrate positively as `nu = integral nu_chi d eta`, zero mixed subgap mass implies zero subgap mass for almost every phase. Establish one common admissible phase for a countable determining or dense family, and prove that the phase's PVM is the required public PVM. An arbitrary upper bound on a mixed signed correlator does not automatically transfer to every phase. Full support alone does not upgrade such an upper bound to a pointwise phase bound.

**Requested decision:** Which reconstruction theorem is being invoked, which hypotheses are already established, and which remain research tasks?

### 6 Review the Lean claim after fixing the mathematics

Use the recovered repository and commit as the historical starting point, verify their availability and exact dependency lockfile, and obtain actual build logs and the assumption/axiom report. Repair A1 and A2 statements before attempting to discharge them. For the first conditional theorem, prefer the existing positive scalar-measure and PVM interfaces described in `FOUNDATION_STATUS.md`; only introduce an unbounded Hamiltonian endpoint after proving the generator identification. Check that every theorem refers to the intended observable algebra and phase. Distinguish an abstract theorem proved from assumed clustering from a theorem establishing clustering for the Wilson measure.

**Requested decision:** Does a clean build establish precisely the intended conditional claim without placeholder proofs, hidden gap assumptions, or model-definition drift?

## Minimum useful review outcome

An initial reviewer can return: (1) a corrected conditional theorem and proof assessment; (2) one accepted, fully quantified UFBI candidate or a counterexample to it; (3) a list of missing hypotheses organized by dependency; and (4) the smallest next analytic problem that would materially advance the program. This is a suggested review scope, not an assertion about time or cost.

The strongest subject match is a researcher in constructive quantum field theory or rigorous lattice gauge theory, especially renormalization and correlation inequalities. Functional analysis expertise is sufficient for the spectral lemma; a Lean specialist is a separate useful collaborator for implementation fidelity.

## Primary bibliography with supported use

1. Arthur Jaffe and Edward Witten, *Quantum Yang-Mills Theory*, official Clay problem description. https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf . Section 4 (printed page 6) states the nontrivial four-dimensional theory and positive mass-gap target, defines the Hamiltonian gap, and specifies the relevant local gauge-invariant field interpretation. Use this to audit the final target rather than to justify the proposed proof. Retrieved 20 November 2026; full PDF text available.

2. Clay Mathematics Institute, *Yang-Mills and the Mass Gap*. https://www.claymath.org/millennium/yang-mills-the-maths-gap/ . Current official page identifies the problem as unsolved. This establishes institutional status, not a theorem about the impossibility of any candidate proof. Retrieved 20 November 2026.

3. Konrad Osterwalder and Robert Schrader, *Axioms for Euclidean Green's Functions II*, Communications in Mathematical Physics 42 (1975), 281-305. https://doi.org/10.1007/BF01608978 ; publisher page https://link.springer.com/article/10.1007/BF01608978 ; primary archive PDF https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf . The publisher abstract explicitly says the results extend and correct the preceding paper. The indexed primary PDF names a reconstruction theorem and a linear growth condition. The archive's direct full-text retrieval was blocked by a service notice in this session, so exact technical hypotheses should be checked in the full paper before claiming compliance. Retrieved 20 November 2026.

4. Martin Lüscher, *Construction of a Selfadjoint, Strictly Positive Transfer Matrix for Euclidean Lattice Gauge Theories*, Communications in Mathematical Physics 54 (1977), 283-292. https://doi.org/10.1007/BF01614090 ; primary DESY preprint https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf . The 1976 report, published in 1977, constructs the physical state space and transfer matrix for Wilson lattice gauge theories. Its introduction distinguishes lattice positivity and the extra transfer-matrix argument from the continuum question. Use it for the regulated positivity and reconstruction interface, not for a continuum mass-gap claim. Full primary PDF retrieved 20 November 2026.

5. Konrad Osterwalder and Erhard Seiler, *Gauge Field Theories on a Lattice*, Annals of Physics 110 (1978), 440-471. https://doi.org/10.1016/0003-4916(78)90039-8 ; publisher page https://www.sciencedirect.com/science/article/pii/0003491678900398 . The publisher abstract describes physical positivity and a positive self-adjoint transfer matrix, and identifies its infinite-volume analyticity and confinement results as strong-coupling lattice results. This is a useful scope comparator; it does not license a continuum conclusion. Publisher abstract retrieved through search on 20 November 2026; full article not read here.

## Retrieval references for the assembling agent

These are internal lookup aids and should be replaced by ordinary bibliography entries in the final packet. Parent must open sources itself before using source citations in chat: Clay PDF `turn113460309view1`; Clay status `turn150717220view2`; OS II publisher `turn150717220view0`; OS II indexed primary PDF `turn907845434search7`; Lüscher primary PDF `turn150717220view1`; Osterwalder-Seiler publisher abstract `turn907845434search2`.
