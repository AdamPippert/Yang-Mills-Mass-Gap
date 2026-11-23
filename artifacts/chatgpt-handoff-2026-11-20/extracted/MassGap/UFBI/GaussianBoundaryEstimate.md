# Gaussian UFBI: explicit boundary-to-interior estimates

**Date:** 2026-11-20. **Status:** analytic derivation in ordinary mathematics, with numerical implementation checks; not a Lean kernel-checked theorem. This note derives new sufficient constants. It does not change or rehabilitate the rejected pilot \(K=4,\gamma=1\).

## 1. Fixed model and units

Let
\[
\Lambda_L=\{1,\ldots,L\}^4,\quad L=RB,\quad
Q=\{s+1,\ldots,s+B\}^4,\quad s=(R-1)B/2,
\]
where \(B\ge1\) and \(R\ge3\) is odd. Fix the physical central side \(q>0\), mass \(m>0\), and spacing \(a=q/B\). Put
\[
A=-\Delta_{\Lambda_L,D}+(ma)^2I,\qquad \Sigma=A^{-1}.
\]
The unscaled nearest-neighbor Dirichlet Laplacian has diagonal \(8\), and off-diagonal \(-1\) for each interior nearest-neighbor pair. Missing neighbors are exterior ghost sites, not identified periodic neighbors.

Let \(\mathcal J\) be the incidence map from exterior ghost values to the interior source: \((\mathcal J\tau)(x)\) sums the values at exterior neighbors of \(x\). All its entries are nonnegative. Face intersections contribute one term for each distinct exterior link.

Completing the square in
\[
\tfrac12\phi^TA\phi-\phi^T\mathcal J\tau
\]
gives \(\mu^\tau=N(A^{-1}\mathcal J\tau,A^{-1})\). Thus the covariance is independent of the collar. This follows directly from this chosen quadratic action; no limiting theorem is required.

Physical scalar fields have the convention \(\phi=a\Phi\). Assume
\[
\|\tau/a\|_\infty\le M,\quad \|\tau'/a\|_\infty\le M.
\]
Set \(g=(\tau-\tau')/a\), so \(\|g\|_\infty\le2M\), and
\[
h=aP_QA^{-1}\mathcal Jg,\qquad
u=h/a=P_QA^{-1}\mathcal Jg.
\]
The assumptions permit arbitrary oscillation of the collar values within this amplitude bound; they do not impose a collar smoothness bound.

The exact node-to-ghost separation is
\[
D=a(s+1)=\frac{R-1}{2}q+a.
\]
The nominal side \(q=aB\) is retained from the test harness. The ghost-to-ghost side of the small Dirichlet box is \(a(B+1)\); these are distinct finite-mesh conventions.

## 2. Massive harmonic comparison

Define
\[
\kappa_a=2\operatorname{arsinh}(ma/2),\quad
\rho_a=\kappa_a/a.
\]
Then \(2(\cosh\kappa_a-1)=(ma)^2\).

### Lemma G1: positivity and boundary comparison

Writing \(W\) for the interior adjacency matrix,
\[
A=(8+(ma)^2)I-W,\quad
A^{-1}=\frac1{8+(ma)^2}
 \sum_{n=0}^\infty\left(\frac{W}{8+(ma)^2}\right)^n.
\]
The series converges because the row-sum norm of \(W\) is at most \(8\). Hence \(A^{-1}\) is entrywise nonnegative. Equivalently, the discrete maximum principle holds: a function with nonnegative boundary values and nonnegative massive Laplacian cannot have a negative interior minimum. At such a minimum the operator would be strictly negative because \(m>0\).

For \(i=1,\ldots,4\), each function \(e^{-\kappa_a x_i}\) and \(e^{-\kappa_a(L+1-x_i)}\) solves the massive homogeneous difference equation when its ghost values are included. Therefore
\[
w(x)=\sum_{i=1}^4
 \frac{e^{-\kappa_a x_i}+e^{-\kappa_a(L+1-x_i)}}
 {1+e^{-\kappa_a(L+1)}}
\]
is massive harmonic in the interior and satisfies \(w\ge1\) on every ghost face. The constant function \(1\) is also a supersolution. Compare both functions with the harmonic extension of \(g/\|g\|_\infty\) and its negative. This yields
\[
|u(x)|\le\|g\|_\infty\min\{1,w(x)\}.
\]
In particular, on \(Q\),
\[
\boxed{\|u\|_{\infty,Q}
 \le\|g\|_\infty b_a(D),\qquad
 b_a(D)=\min\{1,8e^{-\rho_aD}\}.}
\tag{G1}
\]
This estimate is uniform over every collar in the stated amplitude class.

### A sharper average barrier

Let \(\ell_B(v)=B^{-4}\sum_{x\in Q}v(x)\). The average of the barrier factors geometrically:
\[
|\ell_B(u)|\le\|g\|_\infty\,\bar b_{B,L},
\]
\[
\bar b_{B,L}=
\min\left\{1,\
\frac{8e^{-\rho_aD}}{1+e^{-\kappa_a(L+1)}}
\frac{1-e^{-\kappa_aB}}{B(1-e^{-\kappa_a})}\right\}.
\tag{G1a}
\]
The geometric-average factor is at most one. This improves the numerical bound without changing the uniform theorem.

## 3. Physical block-mean covariance

Define the physical block mean
\[
Y_{\rm mean}=\frac1{aB^4}\sum_{x\in Q}\phi_x.
\]
For \(f=B^{-4}\mathbf1_Q\), extended by zero into \(\Lambda_L\), its variance is
\[
V_B=\operatorname{Var}(Y_{\rm mean})=a^{-2}f^TA^{-1}f.
\]

### Lemma G2: one sine mode gives a uniform lower bound

For every vector \(v\), positivity of \(A\) and Cauchy-Schwarz imply
\[
f^TA^{-1}f\ge\frac{(f^Tv)^2}{v^TAv}.
\tag{1}
\]
Choose \(v\) to be the Euclidean unit first tensor sine mode on \(Q\), zero outside \(Q\). Put
\[
\alpha_B=\frac{\pi}{2(B+1)},\quad
\lambda_B=(ma)^2+16\sin^2\alpha_B,\quad
r_B=\frac{2\cot^2\alpha_B}{B(B+1)}.
\]
The one-dimensional identities
\[
\sum_{j=1}^B\sin\frac{\pi j}{B+1}=\cot\alpha_B,\qquad
\sum_{j=1}^B\sin^2\frac{\pi j}{B+1}=\frac{B+1}{2}
\]
give \(v^TAv=\lambda_B\) and \((f^Tv)^2=B^{-4}r_B^4\). The zero extension includes every edge leaving \(Q\), so its energy is exactly the small-box Dirichlet energy even though the surrounding box is larger. Consequently
\[
\boxed{V_B\ge v_B:=
\frac{r_B^4}{a^2B^4\lambda_B}.}
\tag{G2}
\]

For \(0\le x\le\pi/4\), \(\sin^2x\) is convex, so it lies below the chord joining its endpoint values: \(\sin^2x\le2x/\pi\). Using also \(\sin x\le x\), at \(x=\alpha_B\) we obtain
\[
\cot^2\alpha_B
\ge\frac{1-1/(B+1)}{\alpha_B^2}
=\frac{4B(B+1)}{\pi^2}.
\]
Thus \(r_B\ge8/\pi^2\). Also
\[
B^2\lambda_B\le(mq)^2+4\pi^2.
\]
With \(\eta_0=64/\pi^4\), (G2) implies
\[
\boxed{
V_B\ge v_0:=
\frac{\eta_0^2}{q^2((mq)^2+4\pi^2)}.}
\tag{G2u}
\]
Unlike the lattice mean variance, this lower bound has no vanishing power of \(a\).

## 4. Explicit standardized operator norm and Gaussian distances

Define the boundary-to-mean operator
\[
\mathcal T_{\rm mean}g
=\frac{\ell_B(P_QA^{-1}\mathcal Jg)}{\sqrt{V_B}}.
\]
It maps physical collar differences, with their supremum norm, to a dimensionless standardized mean shift. By (G1a) and (G2),
\[
\boxed{
\|\mathcal T_{\rm mean}\|_{\infty\to\mathbb R}
\le \frac{\bar b_{B,L}}{\sqrt{v_B}}
=\frac{qB\sqrt{\lambda_B}}{r_B^2}\bar b_{B,L}.}
\tag{G3}
\]
The simpler expression uniform in \(B,R\) is
\[
\boxed{
\|\mathcal T_{\rm mean}\|_{\infty\to\mathbb R}
\le\frac{\pi^4}{64}\,
q\sqrt{(mq)^2+4\pi^2}\,
\min\{1,8e^{-\rho_aD}\}.}
\tag{G3u}
\]
For a pair of collars individually bounded by \(M\), their mean-channel Mahalanobis distance satisfies
\[
d_{\rm mean}\le2M\frac{\bar b_{B,L}}{\sqrt{v_B}}
\le\frac{\pi^4}{4}Mq\sqrt{(mq)^2+4\pi^2}e^{-\rho_aD}.
\tag{2}
\]

For any equal-covariance Gaussian channel with Mahalanobis displacement \(d\), whitening and rotating the displacement reduce the optimal likelihood-ratio test to one standard normal coordinate. Hence
\[
2\operatorname{TV}=2\operatorname{erf}\left(\frac d{2\sqrt2}\right)
\le\min\{2,\sqrt{2/\pi}\,d\}.
\tag{3}
\]
Completing the square in the integral of the square roots of the densities gives
\[
H^2=1-e^{-d^2/8},\qquad H\le\min\{1,d/(2\sqrt2)\}.
\tag{4}
\]
Here \(H^2=1-\int\sqrt{pq}\); a different Hellinger normalization changes the factor.

### Corollary G4: a fully uniform block-mean UFBI contract

Restrict the meshes by \(ma\le t_*\), with a fixed \(0<t_*<\infty\), and define
\[
\gamma_*=
m\frac{2\operatorname{arsinh}(t_*/2)}{t_*}.
\]
The function \(2\operatorname{arsinh}(t/2)/t\) decreases for \(t>0\): this follows from \(\operatorname{arsinh}x\ge x/\sqrt{1+x^2}\), whose difference has nonnegative derivative and vanishes at zero. Therefore \(\rho_a\ge\gamma_*>0\).

For all allowed \(B,R,\tau,\tau'\),
\[
\boxed{
2\operatorname{TV}_{\rm mean}
\le \min\{2,K_{\rm mean}M e^{-\gamma_*D}\},\quad
K_{\rm mean}=\sqrt{\frac2\pi}\frac{\pi^4}{4}
q\sqrt{(mq)^2+4\pi^2}.}
\tag{G4}
\]
The constants depend only on the declared physical mass, central side, and mesh cutoff. They do not depend on \(a,R,D\), or the collar values.

For \(ma\le1\), \(\gamma_*=0.9624236501\,m\). For the pilot \(m=2,q=1\), all \(B\ge2\) are included and
\[
K_{\rm mean}=128.1198512355,\qquad
\gamma_*=1.9248473002384.
\]
The constants are sufficient, not optimal. The bound can be vacuous at short distances. No fitted constant or observed numerical pass was used in this proof.

### Corollary G5: the block-mean boundary supremum is exact

All entries of the row \(\ell_B P_Q A^{-1}\mathcal J\) are nonnegative. For a nonnegative row vector \(c\),
\[
\sup_{\|g\|_\infty\le2M}|cg|=2M\,c\mathbf1.
\]
Thus the opposite constant collars \(\tau=+aM,\tau'=-aM\) attain the exact maximum block-mean Mahalanobis distance and TV over this collar class. A constant-collar computation evaluates the entire boundary supremum for this scalar channel, up to numerical error. This conclusion does not automatically hold for a joint signed channel.

## 5. Extension to uniformly controlled smearing spaces

Let \(\psi_1,\ldots,\psi_k\) be linearly independent real functions supported in \(Q\), zero extended outside. Use the physical inner product and operator
\[
\langle f,g\rangle_a=a^4\sum_x f(x)g(x),\qquad
L_a=A/a^2=-\Delta_a+m^2.
\]
The physical smeared observables are
\[
Y_i=a^3\sum_x\psi_i(x)\phi_x.
\]
The factor \(a^3\) equals \(a^4/a\): these are Riemann sums for \(\int\psi_i\Phi\). Their common covariance and mean displacement are
\[
C_{ij}=\langle\psi_i,L_a^{-1}\psi_j\rangle_a,\qquad
\delta_i=\langle\psi_i,u\rangle_a.
\]
In ordinary matrix notation \(C=a^6\Psi A^{-1}\Psi^T\), where \(\Psi\) has rows \(\psi_i\).

### Theorem G6: energy bounded on the entire span

Suppose there is a fixed \(\Lambda_{\rm sm}>0\), independent of mesh and outer volume, such that
\[
\langle f,L_af\rangle_a\le\Lambda_{\rm sm}\langle f,f\rangle_a
\quad\hbox{for every }f\in V_a=\operatorname{span}\{\psi_i\}.
\tag{5}
\]
Let \(G_{ij}=\langle\psi_i,\psi_j\rangle_a\) and \(E_{ij}=\langle\psi_i,L_a\psi_j\rangle_a\). For every coefficient vector \(z\), (1) in the physical inner product gives
\[
(z^TCz)(z^TEz)\ge(z^TGz)^2.
\]
Since \(E\preceq\Lambda_{\rm sm}G\), this implies
\[
C\succeq G/\Lambda_{\rm sm}.
\tag{6}
\]
The formula for the orthogonal projection onto \(V_a\) now gives
\[
\delta^TC^{-1}\delta
\le\Lambda_{\rm sm}\delta^TG^{-1}\delta
=\Lambda_{\rm sm}\|P_{V_a}u\|_a^2
\le\Lambda_{\rm sm}q^4\|u\|_\infty^2.
\]
Combining with (G1),
\[
\boxed{
d_F\le2Mq^2\sqrt{\Lambda_{\rm sm}}\,b_a(D)
\le16Mq^2\sqrt{\Lambda_{\rm sm}}e^{-\rho_aD}.}
\tag{G6}
\]
Equivalently the standardized boundary-to-vector operator has
\[
\|\mathcal T_F\|_{\infty\to2}
\le q^2\sqrt{\Lambda_{\rm sm}}\,b_a(D).
\]
The UFBI constants are
\[
\boxed{K_F=16\sqrt{2/\pi}\,q^2\sqrt{\Lambda_{\rm sm}},
\qquad\gamma=\gamma_*.}
\tag{7}
\]
There is no artificial factor \(\sqrt k\). Redundant observables can be removed; an invertible change of channel coordinates leaves both Mahalanobis distance and TV unchanged. A pseudoinverse version works on the common support.

### An explicit admissible class

For fixed \(J\), take any span of Dirichlet tensor sine modes on \(Q\) with frequencies \(1\le n_i\le J\), and require \(B\ge J\). Their discrete physical eigenvalues are
\[
m^2+\frac4{a^2}\sum_{i=1}^4
\sin^2\left(\frac{\pi n_i}{2(B+1)}\right)
\le m^2+\frac{4\pi^2J^2}{q^2}.
\]
Thus any subfamily or invertible recombination of these at most \(J^4\) modes satisfies (G6) with
\[
\Lambda_{\rm sm}=m^2+4\pi^2J^2/q^2.
\]
For the five modes \((1,1,1,1)\) and the four modes with one frequency \(2\) and the others \(1\), a sharper cutoff is
\[
\Lambda_7=m^2+7\pi^2/q^2.
\]
For \(m=2,q=1\), their joint TV coefficient is \(K_F=109.1392079748\).

### What “bounded family” must mean here

Fixed channel count, fixed pointwise amplitude, or separate energy bounds on the listed functions do not by themselves establish (5). For example, the pair \(f_{\rm low}\), \(f_{\rm low}+n^{-1}g_n\) may have individually bounded energy while its span contains a unit high-frequency function \(g_n\) of energy proportional to \(n^2\). The intrinsic sufficient condition is a bound on the whole span, or the trial-pairing certificate below. Failure of a sufficient certificate does not itself disprove UFBI.

The sharp block indicator has zero-extension energy diverging with refinement. It is therefore not an instance of (5); its separate first-sine-mode argument is essential.

### Bounded functions of the smeared vector

If \(\mathcal O(\phi)=F(Y_1,\ldots,Y_k)\), with \(F\) any bounded Borel function and \(\|F\|_\infty\le1\), then
\[
|\mathbb E_\tau\mathcal O-\mathbb E_{\tau'}\mathcal O|
\le2\operatorname{TV}(\operatorname{Law}_\tau Y,\operatorname{Law}_{\tau'}Y).
\]
This follows from the total variation norm of a signed measure, or from integrating indicator functions by the layer-cake formula after shifting \(F\) to \([0,2]\). The same holds for complex \(F\) with modulus at most one. Thus the joint channel estimate controls an entire bounded measurable observable class, and every measurable postprocessing channel satisfies the corresponding TV bound by inverse images of events. No Lipschitz constant is needed. Unbounded polynomial observables require additional moment control.

## 6. Trial-pairing extension: mean plus the existing dipoles

The following formulation covers hard-edged observable weights. Choose trial functions \(v_1,\ldots,v_k\), supported in \(Q\), and set
\[
P_{ij}=\langle\psi_i,v_j\rangle_a,\qquad
(E_v)_{ij}=\langle v_i,L_av_j\rangle_a.
\]
The variational identity
\[
\langle f,L_a^{-1}f\rangle_a
=\sup_v\{2\langle f,v\rangle_a-\langle v,L_av\rangle_a\}
\]
restricted to the trial span proves
\[
\boxed{C_F\succeq P E_v^{-1}P^T.}
\tag{8}
\]
If \(s_{\min}(P)\ge s_0>0\), \(E_v\preceq eI\), and the observable Gram matrix satisfies \(G_F\preceq bI\), then
\[
\boxed{
d_F\le\frac{2Mq^2\sqrt{eb}}{s_0}b_a(D).}
\tag{G7}
\]

### Explicit five-channel certificate

In local coordinates \(j_i=1,\ldots,B\), \(B\ge2\), choose
\[
\psi_0=q^{-2},\qquad
\psi_i=\sqrt{12}\,q^{-2}\frac{j_i-(B+1)/2}{B},
\quad i=1,\ldots,4.
\]
Their physical Gram matrix is
\[
G_F=\operatorname{diag}(1,1-B^{-2},\ldots,1-B^{-2})\preceq I.
\]
These channels are invertible rescalings of the harness's block mean and four coordinate dipoles, so their joint TV is identical to that of its moments channel.

Take the five physical \(L^2\)-orthonormal sine modes described above as trial functions. Parity makes \(P\) diagonal. Writing \(\alpha=\pi/[2(B+1)]\), direct sums give
\[
P_{00}=\eta_B=\frac{4\cot^4\alpha}{B^2(B+1)^2},
\]
\[
\frac{|P_{ii}|}{P_{00}}=
\frac{\sqrt{12}(B+1)}{4B}(1-\tan^2\alpha).
\]
The earlier sine estimate gives \(\eta_B\ge64/\pi^4\). For \(n=B+1\ge3\), convexity of \(\tan\) on \([0,\pi/6]\) gives \(\tan(\pi/(2n))\le\sqrt3/n\), and hence \(\tan^2\alpha\le1/n\). Therefore
\[
\frac{|P_{ii}|}{P_{00}}\ge\frac{\sqrt3}{2},\qquad
s_{\min}(P)\ge s_0:=\frac{32\sqrt3}{\pi^4}.
\]
The trial energy matrix obeys \(E_v\preceq\Lambda_7 I\). Applying (G7) yields
\[
\boxed{
d_{\rm mean+dipoles}\le
\frac{2Mq^2}{s_0}\sqrt{m^2+\frac{7\pi^2}{q^2}}\,
b_a(D).}
\tag{G8}
\]
Its pure exponential TV contract has
\[
\boxed{
K_{\rm mean+dipoles}=
\frac{16\sqrt{2/\pi}}{s_0}\,
q\sqrt{(mq)^2+7\pi^2},
\qquad\gamma=\gamma_*.}
\tag{9}
\]
For \(m=2,q=1\), \(K_{\rm mean+dipoles}=191.8093099258\).

## 7. Limits and the eventual spectral-gap bridge

1. **Mesh cutoff:** \(\rho_a<m\) at nonzero spacing. The uniform finite-mesh estimate proved here uses \(\gamma_*<m\), not an unsupported exact rate \(m\). For any fixed \(\gamma<m\), sufficiently fine meshes satisfy \(\rho_a\ge\gamma\).
2. **Continuum endpoint:** retaining the exact \(\rho_a\) gives \(\rho_a\to m\). At each fixed physical separation, if the finite Gaussian channel means and covariance matrices converge with a nondegenerate limiting covariance, the exact Gaussian distance formula passes the bound to the continuum with exponent \(m\). This is a conditional limit statement; convergence has not been proved here. The covariance lower bounds above prevent collapse for the specified normalized channels.
3. **Fixed physical collars:** the result is for \(|\tau|\le aM\). Holding lattice values at order one corresponds to \(M\sim a^{-1}\) and loses the uniform constant. Smearing alone does not repair that change of boundary normalization.
4. **Scope:** the proof is for the specified Dirichlet free scalar, not a periodic Wilson lattice. A scalar amplitude scaling cannot be assigned to compact gauge links.
5. **Observable completeness:** a single finite channel does not test every reconstructed state. For a mass-gap proof, one needs uniform-rate clustering on a suitable dense observable algebra, plus the selected-phase and OS spectral identification. Constants may depend on a fixed observable while the positive rate remains common.
6. **Full interior field:** these estimates establish the stated channel contracts. They neither assert nor refute a uniform full-field TV theorem under physically bounded collars.
7. **Typical random collars:** a hard deterministic supremum cutoff is not automatically an almost-sure bound on collars drawn from a Gaussian or interacting field. An application to random collars needs an appropriate tail/conditioning argument; that argument is separate.

## 8. Formalization boundary

No Lean compiler is available in the current workspace. No Lean theorem or axiom audit is claimed for this note, and the previous reflection-positivity scaffold has not been altered.

A faithful formalization should make the following theorem dependencies explicit, using the repository's actual types only after inspecting its applicable declarations:

~~~mermaid
flowchart TD
  A["Positive precision and Gaussian conditioning"] --> B["Nonnegative inverse and comparison"]
  B --> C["Exponential boundary barrier"]
  A --> D["Sine-trial covariance lower bound"]
  C --> E["Block-mean operator norm"]
  D --> E
  C --> F["Joint smeared-channel bound"]
  G["Energy-span or trial-pairing certificate"] --> F
  E --> H["Gaussian TV and Hellinger"]
  F --> H
~~~

The numerical checks validate implementation against the formulas; they do not replace the proofs of these lemmas. No existing analytical sorry has been discharged in Lean.

## 9. Numerical checks and reproducibility

The companion implementation is **gaussian_bounds.py**, with regression tests in **test_gaussian_bounds.py** and full numerical output in **estimate_checks.json**. It imports the existing **ufbi_control.py** unchanged; the rejected pilot and its **results.csv** remain separate.

The checks include an independent sparse Kronecker-sum solve compared to DST covariance, the discrete dispersion relation, sine overlap bounds for \(B=1,\ldots,100\), positivity of every boundary response coefficient on a small box, constant-collar attainment, corner source counting, nondefault physical scales, and the moment-family trial matrix inequality.

The sweep uses \(B=2,3,4,5\), \(R=3,5,7\), \(m=2,q=1\), plus two nondefault physical parameter sets. Four collar patterns give 56 collar cases, and three channels give 168 measurements. All 12 tests (seven new and five existing) passed; the sweep found zero numerical violations. These are ordinary floating-point checks without interval error certificates.

For \(m=2,q=M=1,B=4\) and opposite constant collars:

| \(R\) | Mean \(2\mathrm{TV}\), evaluated | Bound from exact-mesh trial/barrier | Bound from uniform constants, exact erf conversion |
|---:|---:|---:|---:|
| 3 | 1.490197 | 1.945278 | approximately 2 |
| 5 | 0.319472 | 0.479554 | 1.418272 |
| 7 | 0.048755 | 0.067241 | 0.244941 |

Both bound columns apply \(2\operatorname{erf}(d_{\rm bound}/(2\sqrt2))\); they are slightly tighter than truncating the linear TV envelope at 2. The first bound uses (G1a), (G2). The uniform bound uses (2) with \(\rho_a\) replaced by \(\gamma_*\).

The maximum observed ratio of mean Mahalanobis distance to the exact-mesh bound was 0.865144 (rounded up). This is a consistency check, not an optimization or an error certificate. The analytic proof covers all admissible collars and all admissible meshes even though the numerical sweep is finite.

Run from the project root:

~~~sh
OPENBLAS_NUM_THREADS=1 python3 -m unittest discover -s MassGap/UFBI -p 'test_*.py' -v
OPENBLAS_NUM_THREADS=1 python3 MassGap/UFBI/gaussian_bounds.py
~~~

The output records Python, NumPy and SciPy versions and source hashes. The new script evaluates analytic estimates; it does not tune or overwrite the earlier rejected candidate.

## 10. Sources and attribution

The constants and inequalities (G1)–(G8) are derived in this note from the explicitly stated finite-dimensional model. Background references support the Gaussian conventions, not a claim that those sources contain these exact UFBI constants.

- Werner and Powell, *Lecture notes on the Gaussian Free Field*, §§1.1, 1.3, 1.5.1: [arXiv:2004.04720](https://arxiv.org/abs/2004.04720). Their Laplacian normalization must be translated to the diagonal-8 convention used here.
- Devroye, Mehrabian and Reddad, *The total variation distance between high-dimensional Gaussians with the same mean*, §2, equations for the same-covariance case and Hellinger distance: [arXiv:1810.08693](https://arxiv.org/abs/1810.08693). Only those standard Gaussian distance identities are used.
- [SciPy 1.17.0 DST documentation](https://docs.scipy.org/doc/scipy-1.17.0/reference/generated/scipy.fft.dst.html), for the numerical orthonormal DST-I implementation.
