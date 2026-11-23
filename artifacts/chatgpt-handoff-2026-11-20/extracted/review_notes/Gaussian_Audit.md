# Audit of the recovered Gaussian UFBI derivation

**Date:** 20 November 2026. **Scope:** review of the recovered `GaussianBoundaryEstimate.md`, `SPECIFICATION.md`, and `gaussian_bounds.py`. This audit is new; it is not a substitute for the recovered sources. The original sources were left unchanged. This is an ordinary mathematical review, not an independent mathematician's endorsement, a Lean verification, or a certified numerical proof.

## Finding

I found no algebraic defect in the displayed Gaussian estimates G1 through G8 under their stated model, physical normalization, bounded collar class, and channel admissibility hypotheses. The explicit coefficients were independently recomputed and agree with the document. The major outstanding issue for the mass-gap program is using this deterministic bounded-collar estimate to establish temporal connected-correlation decay for a sufficiently complete observable class. No such implication is supplied by the Gaussian note.

The source defines the field convention \(\phi=a\Phi\), fixes the physical central side \(q=aB\), and restricts collars by \(\|\tau/a\|_\infty,\|\tau'/a\|_\infty\le M\). These are essential hypotheses. In particular, this is not an estimate uniform over all real-valued collars.

## 1. Model and normalization checked

The Dirichlet precision has diagonal \(8+(ma)^2\) and off-diagonal \(-1\) for an interior nearest-neighbor pair. Exterior neighbors contribute through the incidence map \(\mathcal J\). With this convention, completing the square gives covariance \(A^{-1}\) and mean \(A^{-1}\mathcal J\tau\).

For \(g=(\tau-\tau')/a\), the difference of conditional means of the physical field is \(u=P_QA^{-1}\mathcal Jg\). The physical block mean is \(Y=(aB^4)^{-1}\sum_Q\phi_x\), so its mean displacement is \(\ell_B(u)\) and its variance is \(a^{-2}f^TA^{-1}f\), where \(f=B^{-4}\mathbf 1_Q\). These powers of \(a\) are consistent.

For smeared observables \(Y_i=a^3\sum_x\psi_i(x)\phi_x\), the covariance \(C=a^6\Psi A^{-1}\Psi^T\) agrees with the physical-inner-product formula \(C_{ij}=\langle\psi_i,L_a^{-1}\psi_j\rangle_a\), where \(L_a=A/a^2\) and \(\langle f,g\rangle_a=a^4\sum_xf(x)g(x)\). The mean displacement is \(\delta_i=\langle\psi_i,u\rangle_a\).

The ghost-node clearance \(D=a(s+1)\) is used consistently. Replacing it silently by \(as\), or using a spacing that fixes the outer box while varying \(R\), would change the experiment and its constants.

## 2. Barrier and covariance argument checked

The discrete dispersion relation

\[
\kappa_a=2\operatorname{arsinh}(ma/2),\qquad
2(\cosh\kappa_a-1)=(ma)^2
\]

makes each coordinate exponential massive harmonic. On an exterior face the corresponding normalized pair of exponentials equals one. Summing over four coordinates therefore gives the required comparison supersolution. Positivity of \(A^{-1}\), or the discrete maximum principle, yields

\[
\|u\|_{\infty,Q}\le\|g\|_\infty b_a(D),\qquad
b_a(D)=\min\{1,8e^{-\rho_aD}\},\quad \rho_a=\kappa_a/a.
\]

The average barrier in G1a correctly includes the geometric sum and the denominator \(1+e^{-\kappa_a(L+1)}\).

For the covariance lower bound, the zero-extended first sine mode has the small-box Dirichlet energy, including all edges leaving \(Q\). Its overlap with the block indicator gives

\[
V_B\ge\frac{r_B^4}{a^2B^4\lambda_B},\qquad
r_B=\frac{2\cot^2(\pi/[2(B+1)])}{B(B+1)},\qquad
\lambda_B=(ma)^2+16\sin^2\frac{\pi}{2(B+1)}.
\]

The inequalities \(r_B\ge8/\pi^2\) and \(B^2\lambda_B\le(mq)^2+4\pi^2\) are valid for \(B\ge1\). They give the displayed physical variance lower bound

\[
V_B\ge\frac{(64/\pi^4)^2}{q^2((mq)^2+4\pi^2)}.
\]

This sharp scaling is material: a generic lower bound from the largest precision eigenvalue would leave spurious vanishing powers of \(a\) and would not establish the same uniform contract.

## 3. Factor and distance audit

The joint smearing estimate in G6 is

\[
\boxed{
 d_F\le2Mq^2\sqrt{\Lambda_{\rm sm}}\,b_a(D)
 \le16Mq^2\sqrt{\Lambda_{\rm sm}}e^{-\rho_aD}.
}
\]

The second coefficient is **16**, arising from the collar difference bound \(2M\) multiplied by the eight-face barrier coefficient. A statement with coefficient 2 directly multiplying \(e^{-\rho_aD}\) would not follow from this proof. The recovered note and `gaussian_bounds.py` retain the factor correctly.

With the specification's convention \(2\operatorname{TV}=2\sup_E|P(E)-Q(E)|\), the same-covariance Gaussian identity and its linear upper bound are

\[
2\operatorname{TV}=2\operatorname{erf}\left(\frac d{2\sqrt2}\right)
\le\min\{2,\sqrt{2/\pi}\,d\}.
\]

The Hellinger formula \(H^2=1-e^{-d^2/8}\) is consistent with the stated convention \(H^2=1-\int\sqrt{pq}\).

The bound on \(\rho_a\) is also correct: for \(ma\le t_*\),

\[
\rho_a\ge\gamma_*=m\frac{2\operatorname{arsinh}(t_*/2)}{t_*}>0.
\]

The exact finite-mesh rate is less than \(m\). The note does not incorrectly assert the continuum rate \(m\) for every finite mesh.

For \(m=2,q=1,t_*=1\), independent scalar arithmetic gives:

| Quantity | Recomputed value |
|---|---:|
| \(K_{\rm mean}\) | 128.11985123551892 |
| \(K_{\rm sine\,5}\) | 109.13920797481637 |
| \(K_{\rm mean+dipoles}\) | 191.80930992578305 |
| \(\gamma_*\) | 1.9248473002384139 |
| Trial-pairing lower bound \(s_0\) | 0.5689984913508406 |

These are evaluations of derived sufficient constants, not fitted constants or estimates of optimality.

## 4. Joint smearing and trial-pairing checks

The bound \(C\succeq G/\Lambda_{\rm sm}\) follows from Cauchy–Schwarz in the \(L_a\) and \(L_a^{-1}\) quadratic forms, provided the energy bound holds on **every vector in the smearing span**. Separate bounds on the displayed basis vectors do not suffice. The note explicitly imposes the stronger span condition and explains the cancellation failure of individual bounds.

For the five hard-edged moment channels, the trial restriction of the variational formula gives \(C_F\succeq P E_v^{-1}P^T\). The parity reduction, the formula for \(P_{00}\), and the ratio for \(|P_{ii}|/P_{00}\) are consistent. The inequality \(s_{\min}(P)\ge32\sqrt3/\pi^4\) follows from the supplied trigonometric bounds for \(B\ge2\). The resulting G8 coefficient is consistent with G7 and with the code.

Redundant finite channels can be removed or treated using the pseudoinverse on the common support. Because the restricted field covariance is positive definite, a fixed linear channel has mean displacement in the range of its covariance. Rank deficiency therefore creates no disjoint-support exception in this setting.

For a bounded complex function of the channel with modulus at most one, the expectation difference is bounded by the total variation norm of the signed difference measure, namely \(2\operatorname{TV}\). The extension from the joint Gaussian law to this bounded measurable class is valid. It does not provide a moment estimate for unbounded polynomials.

## 5. Bounded collars are an essential restriction

The bounded-collar theorem is compatible with the following obstruction. For any finite-lattice Gaussian observable channel with a nonzero boundary-response map, multiplying a boundary difference by an unbounded scalar makes its Mahalanobis displacement unbounded. Consequently

\[
\sup_{\tau,\tau'\in\mathbb R^{\Gamma}}
\operatorname{TV}(\mathcal L_\tau F,\mathcal L_{\tau'}F)=1.
\]

The block-mean channel has nonzero positive response. The note avoids this obstruction by fixing the physical amplitude class. Its proof that opposite constant collars maximize the scalar block-mean response on that class is correct. It does not imply a maximization theorem for a joint signed channel.

The v0.1 specification's older statement that a maximization theorem had not been established must be read together with the explicit v0.2 correction. The latter establishes this result for the scalar block mean. Preserving both sections is a valid history; a current synopsis should use the v0.2 result and retain the joint-channel qualification.

## 6. New observation about typical microscopic Gaussian collars

The note already says that its hard deterministic cutoff is not automatically typical. The obstruction can be made quantitative for a natural random-collar model.

Suppose a collar value \(\tau_y\) is an ordinary, unaveraged Gaussian lattice field value from a larger finite Dirichlet box with the same diagonal-8 precision convention. Its covariance satisfies

\[
\operatorname{Var}(\tau_y)\ge\frac1{16+(ma)^2},
\]

because the entire precision matrix is at most \((16+(ma)^2)I\). A Gaussian density is at most \(1/(\sqrt{2\pi}\sigma)\), so, regardless of its mean,

\[
\Pr\{|\tau_y|\le aM\}
\le\sqrt{\frac2\pi}\,aM\sqrt{16+(ma)^2}
\longrightarrow0
\quad(a\downarrow0, M,m\text{ fixed}).
\]

The event that **every** collar site satisfies the fixed physical supremum cutoff is contained in this one-site event and also has probability tending to zero in this model. This conclusion does not concern a coarse-grained collar, a different field normalization, or compact Wilson links; those require separate definitions.

Thus removing the cutoff by a straightforward fixed-\(M\) high-probability tail argument is not available for unaveraged microscopic Gaussian collars. A useful next step could be an averaged influence estimate, a suitably smeared or distributional boundary norm, or a multiscale boundary condition with explicit tail control. Choosing such a replacement changes the hypothesis and requires a new proof; it must not be presented as already covered by G1–G8.

## 7. Consequences for the research handoff

The recovered Gaussian note supplies a meaningful, physically normalized deterministic control theorem for the declared channels. It does not establish:

1. a Wilson-measure analogue of the collar condition or estimate;
2. a theorem converting the restricted deterministic influence estimate into temporal connected-correlation decay;
3. a dense observable-created subspace of the physical Hilbert space;
4. existence, nontriviality, or the necessary axioms for an interacting continuum Yang–Mills theory;
5. a passage of the required rate through the relevant infinite-volume and continuum limits; or
6. a Lean kernel-checked theorem.

For the later spectral theorem, the correlation prefactor may depend on the fixed observable. The positive decay rate must remain common. One need not demand one finite prefactor simultaneously for an arbitrarily rich dense family if a theorem uses the weaker, sufficient per-observable formulation. This distinction should guide the next specification.

**Recommended mathematical review order:** verify the bounded-collar Gaussian proof; decide which random or coarse boundary condition can support a clustering argument; formulate and prove that implication; then audit the dense-family spectral bridge and the limits separately. A finite numerical pass supports implementation consistency and does not discharge these analytic obligations.
