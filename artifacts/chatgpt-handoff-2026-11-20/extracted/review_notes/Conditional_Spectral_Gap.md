# Conditional spectral-gap theorem: proof and audit notes

Date: 2026-11-20. Scope: an abstract spectral consequence of exponential temporal autocorrelation decay, intended as one component of a constructive quantum-field-theory proof.

**Status:** The theorem and proof below are an analytic derivation using the spectral theorem for a positive self-adjoint operator. They have not been checked in Lean. They do not establish the hypotheses for four-dimensional interacting Yang–Mills theory, construct a continuum theory, or prove the Yang–Mills mass gap.

## 1. Exact theorem

Let \(\mathscr H\) be a complex Hilbert space. Let \(H\) be a densely defined, positive self-adjoint operator on \(\mathscr H\), and let \(\Omega\in\operatorname{Dom}(H)\) satisfy

\[
\|\Omega\|=1,\qquad H\Omega=0.
\]

Write \(K=\Omega^\perp\), and let \(S\subset K\) have dense linear span in \(K\). Suppose there is **one common number** \(m>0\) such that, for each \(\psi\in S\), there are finite constants \(C_\psi\ge0\) and \(t_\psi\ge0\) for which

\[
\langle\psi,e^{-tH}\psi\rangle
\le C_\psi e^{-mt}
\qquad(t\ge t_\psi).
\tag{1}
\]

The quantity on the left is real and nonnegative because \(H\ge0\). The constants and the onset time may depend on \(\psi\). No uniform bound on \(C_\psi/\|\psi\|^2\) is assumed.

Then \(K\) reduces \(H\), and

\[
H|_K\ge mI_K,
\qquad
\operatorname{spec}(H)\subset\{0\}\cup[m,\infty),
\qquad
\ker H=\mathbb C\Omega.
\tag{2}
\]

Equivalently, if \(E\) is the projection-valued spectral measure of \(H\) and \(P_\Omega\) is the orthogonal projection onto \(\mathbb C\Omega\),

\[
E([0,m))=P_\Omega.
\tag{3}
\]

The lower bound in (2) is a quadratic-form assertion on \(\operatorname{Dom}(H^{1/2})\cap K\). In particular,

\[
\|H^{1/2}\eta\|^2\ge m\|\eta\|^2
\quad\text{for }\eta\in\operatorname{Dom}(H^{1/2})\cap K.
\]

The conclusion gives a gap **at least** \(m\); it does not show that \(m\) is an eigenvalue or the exact bottom of the excited spectrum. If \(K=\{0\}\), the spectral assertion is vacuous beyond vacuum uniqueness. A nontrivial theory requires a separate nontriviality condition.

## 2. Proof by spectral projections

For \(\psi\in\mathscr H\), define the finite positive measure

\[
\mu_\psi(B)=\langle\psi,E(B)\psi\rangle
=\|E(B)\psi\|^2.
\]

Fix \(0\le r<m\). Functional calculus and positivity give

\[
\begin{aligned}
\langle\psi,e^{-tH}\psi\rangle
&=\int_{[0,\infty)}e^{-t\lambda}\,d\mu_\psi(\lambda)\\
&\ge e^{-tr}\mu_\psi([0,r]).
\end{aligned}
\]

For \(\psi\in S\) and \(t\ge t_\psi\), (1) therefore implies

\[
0\le\|E([0,r])\psi\|^2
\le C_\psi e^{-(m-r)t}.
\]

Since \(m-r>0\), letting \(t\to\infty\) proves \(E([0,r])\psi=0\). Linearity extends this identity to \(\operatorname{span}S\); boundedness of the projection and density extend it to all of \(K\).

Because \(H\Omega=0\), \(E([0,r])\Omega=\Omega\). The orthogonal decomposition \(\mathscr H=\mathbb C\Omega\oplus K\) now gives

\[
E([0,r])=P_\Omega\qquad(0\le r<m).
\]

Choose \(r_n\uparrow m\) with \(r_n<m\). Strong continuity of spectral projections for increasing Borel sets yields

\[
E([0,m))=\operatorname{s\!\!\!-lim}_{n\to\infty}E([0,r_n])=P_\Omega.
\]

Self-adjointness and \(H\Omega=0\) make \(\mathbb C\Omega\), and hence \(K\), reducing subspaces. The restricted spectral measure on \(K\) is supported in \([m,\infty)\). This proves the form inequality and the spectral inclusion. Finally,

\[
E(\{0\})=P_\Omega,
\]

so \(\ker H=\mathbb C\Omega\). Vacuum uniqueness is a consequence, not an additional hypothesis. ∎

One also obtains the stronger normalized estimate, now for every \(\eta\in K\),

\[
0\le\langle\eta,e^{-tH}\eta\rangle
\le e^{-mt}\|\eta\|^2\qquad(t\ge0).
\tag{4}
\]

## 3. Observable formulation and the required density

Use the convention that the inner product is linear in its second argument. For a bounded operator \(A\), set

\[
\omega(A)=\langle\Omega,A\Omega\rangle,
\qquad
\psi_A=(A-\omega(A)I)\Omega.
\]

Then \(\psi_A\in K\), and

\[
\langle\psi_A,e^{-tH}\psi_A\rangle
=\langle\Omega,A^*e^{-tH}A\Omega\rangle-|\omega(A)|^2.
\tag{5}
\]

Thus the needed correlation is a **connected temporal autocorrelation** represented by a positive spectral measure. Bounds for a few arbitrary cross-correlations are not an adequate substitute.

It is sufficient to have a class \(\mathcal A\) for which the vacuum vectors \(\{A\Omega:A\in\mathcal A\}\) have dense linear span in \(\mathscr H\), with (1) holding for their centered vectors. The bounded projection \(I-P_\Omega\) then proves the required density in \(K\). A cyclic vacuum for the specified observable algebra is one way to obtain this condition.

For unbounded fields, (5) must be reformulated using an explicitly controlled common domain or directly using well-defined reconstructed vectors. No unbounded-operator products or domain identities are supplied by the abstract theorem.

A bounded family of smearings may be sufficient if its corresponding vectors span densely; boundedness alone proves no such fact. A finite set of field generators can generate an infinite observable algebra, but estimates on the generators alone do not automatically extend to products or to the generated algebra.

The gap conclusion concerns the Hilbert space specified in the theorem, typically the reconstructed vacuum sector. It does not automatically cover other representations or superselection sectors.

## 4. What this theorem does not reconstruct

This result starts **after** a positive self-adjoint Hamiltonian and its vacuum representation exist. It is not an Osterwalder–Schrader reconstruction theorem.

A separate reconstruction component must state its exact axiom set and establish the Hilbert space, the vacuum, the strongly continuous positive-time translation semigroup, its positive self-adjoint generator, and the correspondence between admissible Euclidean expressions and the autocorrelations in (5). Reflection positivity alone should not be described as supplying every one of those conclusions without the remaining hypotheses.

Continuum existence, Euclidean or relativistic covariance, regularity, the physical observable algebra and nontriviality remain separate obligations. Some reconstruction formulations assume a clustering axiom to obtain vacuum uniqueness. In the abstract contract above, uniqueness instead follows from the common-rate estimate and density.

A Gaussian boundary-to-interior sensitivity estimate is also a distinct assertion. To use it here, one must prove a chain from that estimate to the temporal autocorrelation bounds on a dense class, with all norms, constants, conditioning assumptions and limits specified. No such implication is proved in these notes for interacting Yang–Mills theory.

## 5. Transfer matrix and physical units

Let \(a_t>0\) be the Euclidean time spacing and suppose a normalized transfer matrix satisfies

\[
T=e^{-a_tH},\qquad T\Omega=\Omega.
\]

Here normalization means that the vacuum energy has been subtracted, so the vacuum eigenvalue is one. The representation assumes the conditions needed to define \(H\); positivity of an arbitrary bounded transfer operator alone does not remove possible logarithm/domain issues.

If a dense centered family obeys

\[
\langle\psi,T^n\psi\rangle\le C_\psi e^{-\kappa n}
\]

for all sufficiently large integers \(n\), with a common dimensionless \(\kappa>0\), the same spectral-projection proof along \(t=na_t\) gives

\[
H|_K\ge \frac{\kappa}{a_t}I_K,
\qquad
\operatorname{spec}(T|_K)\subset[0,e^{-\kappa}].
\]

In units \(\hbar=c=1\), \(\kappa/a_t\) is the physical energy lower bound. Across regulators and volumes, the desired condition is a strictly positive common physical lower bound, for example

\[
\frac{\kappa_{a,V}}{a_t}\ge m_*>0
\]

through the limit being taken. A positive gap at each fixed regulator does not establish this condition. Conversely, a dimensionless transfer-matrix gap may approach zero as \(a_t\to0\) while a physical gap survives.

To pass a correlation estimate to a continuum/infinite-volume limit, one sufficient route is convergence of matched, properly normalized observable correlations together with regulator-independent constants \(C_A\) and a common physical rate \(m_*\). This is sufficient, not universally necessary. Another route is to first prove a uniform physical operator gap at every regulator, use the normalized bound (4), and then prove convergence of the matched correlations and finite variances. Either route still needs a dense class in the limiting Hilbert space and a consistent vacuum subtraction.

## 6. Exact audit cases

### A. A finite family can miss arbitrarily low energies

Take \(\mathscr H=\ell^2(\mathbb N_0)\), \(\Omega=e_0\), and fix \(k\ge1\). Define the bounded positive self-adjoint operator

\[
He_0=0,\qquad He_j=e_j\ (1\le j\le k),\qquad
He_{k+j}=\frac1j e_{k+j}\ (j\ge1).
\]

Every \(\psi\in\operatorname{span}\{e_1,\ldots,e_k\}\) has

\[
\langle\psi,e^{-tH}\psi\rangle=e^{-t}\|\psi\|^2.
\]

Nevertheless \(1/j\to0\) through excited eigenvalues. The vacuum is unique and the full theory has no positive gap. The tested family fails the density requirement.

### B. A dense family with observable-dependent positive rates is insufficient

On the same Hilbert space, define

\[
He_0=0,\qquad He_n=\frac1n e_n\quad(n\ge1).
\]

Let \(S\) consist of the finitely supported vectors in \(K\). This set is dense. For a nonzero \(\psi=\sum_{n=1}^N c_ne_n\),

\[
\langle\psi,e^{-tH}\psi\rangle
=\sum_{n=1}^N|c_n|^2e^{-t/n}
\le\|\psi\|^2e^{-t/N}.
\]

Each vector therefore has a strictly positive decay rate. There is no common positive rate on the dense family, and the operator has no positive gap. This demonstrates why the order of quantifiers must be

\[
\exists m>0\;\forall\psi\in S\;\exists C_\psi,t_\psi\;\forall t\ge t_\psi,
\]

rather than allowing \(m\) to be selected separately for each \(\psi\).

### C. A finite time window cannot establish the conclusion

For any positive self-adjoint \(H\), any \(m>0\), any vector \(\psi\), and any finite \(T\), contraction of the semigroup gives

\[
\langle\psi,e^{-tH}\psi\rangle
\le\|\psi\|^2
\le e^{mT}\|\psi\|^2e^{-mt}\quad(0\le t\le T).
\]

Thus arbitrarily fast apparent exponential upper bounds can be obtained on a finite interval by increasing the prefactor. An asymptotic statement for arbitrarily large time is essential.

### D. Cross-correlations can vanish while a low mode remains

If \(u\) and \(v\) are orthogonal eigenvectors of \(H\), then \(\langle u,e^{-tH}v\rangle=0\) for all \(t\), regardless of how small the energy of \(u\) is. Cancellation or orthogonality in selected cross-correlations must not be mistaken for a spectral exclusion. The positive autocorrelations in (1) avoid that error.

### E. Squared semigroup norms introduce a factor of two

Self-adjointness and the semigroup law give

\[
\|e^{-tH}\psi\|^2=\langle\psi,e^{-2tH}\psi\rangle.
\]

A hypothesis \(\|e^{-tH}\psi\|^2\le C_\psi e^{-\mu t}\) therefore yields the spectral threshold \(\mu/2\), not \(\mu\). The transfer from a mixing estimate must record whether its rate applies to an autocorrelation, a norm or a squared norm.

## 7. Concrete Lean formalization contract

**Compilation status: no Lean check performed.** No Lean version, dependency revision, declaration name or existing library coverage is asserted here. The items below are mathematical acceptance contracts; they are not executable code or invented library APIs.

### Inputs that must be explicit

1. A complete complex inner-product space and the chosen inner-product convention.
2. A normalized vacuum vector, its orthogonal complement and the corresponding bounded orthogonal projection.
3. A positive self-adjoint operator with its domain; alternatively, an explicitly specified spectral-measure/functional-calculus interface from which that operator is recovered.
4. The spectral measure, its bounded projections, positivity, support in \([0,\infty)\), functional-calculus identity for \(e^{-tH}\), and increasing-set continuity of projections.
5. The vacuum spectral identity at zero.
6. A set of centered vectors with a proof that its linear span is dense in the vacuum orthogonal complement.
7. The exact quantified common-rate hypothesis, including finite prefactors, allowed onset times and the time domain.

If any of these are introduced as assumptions instead of proved from a reconstruction library, the resulting theorem must be labelled conditional on that interface. Abstracting a missing component does not verify that component.

### Proof obligations, in dependency order

| Obligation | Required mathematical conclusion |
|---|---|
| Scalar exponential squeeze | If \(x\ge0\), \(m>r\), and \(x\le Ce^{-(m-r)t}\) for all sufficiently large \(t\), then \(x=0\). |
| Spectral localization estimate | \(e^{-rt}\|E([0,r])\psi\|^2\le\langle\psi,e^{-tH}\psi\rangle\) for \(r,t\ge0\). |
| Dense annihilation | A bounded linear operator vanishing on a set vanishes on the closure of its linear span. |
| Low-energy projection identity | \(E([0,r])=P_\Omega\) whenever \(0\le r<m\). |
| Open-endpoint limit | \(E([0,m))=P_\Omega\) from increasing closed intervals with endpoints below \(m\). |
| Spectral and form consequences | Vacuum uniqueness, the restricted form lower bound, the spectral inclusion and normalized semigroup bound (4). |
| Observable centering | Identity (5) and density of centered vacuum vectors under the stated cyclicity condition. |
| Discrete-time variant | The same conclusion from integer transfer-matrix powers, with physical rate \(\kappa/a_t\). |

### Validation gates

- Pin the actual Lean/toolchain and dependency revisions before implementation; inspect available declarations rather than guessing names.
- Compile every theorem used in the claimed result. Report any remaining placeholders, admitted axioms or unproved interface assumptions, and inspect the final theorem's axiom dependencies.
- Keep the Gaussian estimate, the correlation-transfer step, reconstruction, density, spectral bridge and continuum-limit step as separate declarations/contracts. A theorem in one component must not silently replace a missing theorem in another.
- Audit the quantifiers against Cases A and B, the time range against Case C, positivity/correlation orientation against Case D, and time/rate normalization against Case E.
- Record whether the checked result establishes only the abstract spectral bridge, a particular Gaussian model, a regulated gauge theory, or a continuum interacting theory. These are different completion states.

## 8. Mathematician review questions

1. Which reconstructed observable vectors will form the dense centered class, and does the proposed UFBI observable channel control that class?
2. What exact theorem transfers boundary sensitivity to the positive temporal autocorrelation in (5), with a rate common to that class?
3. Which quantities are uniform in box size, lattice spacing, renormalization scale and admissible boundary condition, and in what physical units?
4. What reconstruction and limit results are already proved, what are explicit assumptions, and what remain conjectural for the interacting non-Abelian theory?
5. Does the proposed continuum limit remain nontrivial, with the required field content and axioms, rather than only retaining an abstract energy lower bound?

The spectral argument is the short, controlled component. Establishing its hypotheses for the intended interacting continuum theory is the substantive open obligation in this project.

## 9. Integration with the recovered project materials

This section records direct inspection of the recovered `FOUNDATION_STATUS.md`, `SPECIFICATION.md` and `ReflectionPositivity.lean` on 2026-11-20. It does not constitute a new compilation or a fresh inspection of the upstream repository.

### Original scaffold

The recovered `ReflectionPositivity.lean` explicitly labels itself a research scaffold that is not kernel checked. It contains three `sorry` proof bodies, one beneath each of A1, A2 and A3.

- **A1:** The reflection map and positive-time function class are supplied as arbitrary arguments; the geometric assumption is literally `hGeometry : True` and the private proof similarly takes `hReflectionGeometry : True`. Actual reflection geometry, support conditions, measure compatibility and integrability are not encoded by those assumptions. The current statement is not a proved finite-lattice Wilson reflection-positivity result. Its definition bounds the real part of the reflected diagonal integral; a reconstruction must also establish the needed Hermitian/reality properties of the OS form from appropriate geometry and measure invariance.
- **A2:** The OS identification is likewise represented by `hQIsOSQuotient : True`. Its conclusion only asks for existence of a positive self-adjoint bounded operator. The zero operator satisfies that type of conclusion, so even a proof of the displayed statement would not identify physical time translation, a normalized vacuum, an OS quotient or a meaningful transfer matrix. These must be specified explicitly.
- **A3:** The entire passage from `UniformLatticeClustering` and `R.Reconstructed` to the energy–momentum PVM conclusion is admitted. The displayed clustering definition tests two-token finite moments with a common constant; it does not itself state the dense centered OS-vector hypothesis used in Section 1. Reflection/adjoint conventions, continuum passage, phase selection, density and the PVM identification must be exposed as separate hypotheses or proved adapters.
- **Endpoint distinction:** The scaffold's `HasPVMGap` excludes only the region with energy strictly between zero and \(m\). By itself, that assertion allows additional zero-energy vectors. The stronger rank-one identity (3), or a separately established vacuum-uniqueness result, is needed to identify the zero-energy projection with the chosen vacuum.

Compiling the scaffold while retaining admitted proofs would not discharge these specification defects or analytical obligations. The listed `#print axioms` commands are intended checks; their presence in a source file is not evidence that the checks were run.

### Source-native implementation route

`FOUNDATION_STATUS.md` records a prior source audit of `yang-mills-group/OpenAI-YM-20261028` at commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464`, with toolchain `leanprover/lean4:v4.32.0`. It reports upstream OS semigroup, positive spectral-measure and energy–momentum PVM interfaces, but explicitly says that the proposed adapter was not compiled.

Accordingly, the least speculative implementation order is:

1. Prove the positive scalar-measure/Laplace-support lemma independently of an unbounded-Hamiltonian API.
2. Attach it to the actual upstream diagonal measures and PVM, after inspecting the pinned declarations and compiling their imports.
3. Prove the dense-centered-family projection argument and the Euclidean-to-public-PVM identification.
4. Add the unbounded Hamiltonian formulation only after its generator and spectral measure are explicitly identified.

The upstream attachment points listed in the recovered status report are evidence of a previous source inspection, not evidence that A1 or A2 of the local finite-lattice scaffold has been proved. The abstract proof in Sections 1–2 remains valid as a mathematical contract regardless of the eventual Lean interface choice.

### Relationship to the Gaussian result

The recovered specification treats the massive Gaussian model as a control with precision \(-\Delta_D+(ma)^2I\), where \(m>0\) is an input. Its analytic supplement supplies boundary estimates for the block mean and specified joint-smearing classes, with explicit amplitude restrictions and constants. Those results neither generate the input mass nor establish dense all-state temporal clustering for Wilson gauge fields.

The specification preserves the rejection of its original trial constants and distinguishes subsequent analytic bounds from finite-grid numerical evidence. Those distinctions should remain in the handoff. In particular, finite channel dimension, passing numerical sweeps and a theorem for deterministically bounded collars do not discharge the density, unrestricted-conditioner or interacting-continuum obligations above.
