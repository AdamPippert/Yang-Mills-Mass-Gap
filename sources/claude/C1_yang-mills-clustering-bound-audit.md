# C1 — Claude: "Yang–Mills clustering bound audit"

## Provenance

| Field | Value |
|---|---|
| Source ID | C1 |
| Service | claude.ai |
| Conversation title | Yang–Mills clustering bound audit |
| Conversation URL | <https://claude.ai/chat/b4c2d53d-0ed0-48f3-8b6d-2b3e15938697> |
| Last updated | 2026-11-20 (API field `updated_at` 2026-11-20T20:34:07Z) |
| Model shown in page | Opus 5.5 |
| Messages | 2 (one human prompt, one assistant response) |
| Captured | 2026-11-22, text copied from the rendered page with Claude in Chrome |
| Fidelity | Observed: text below is the rendered page text. The page flattened the comparison table, so the table is re-rendered in Markdown with the cell text unchanged. The headings, bullet markers and the Lean code fence are also added Markdown; the words are unchanged. The page's Lean code lost its indentation, and the file keeps it as captured. |
| Not captured | The assistant response contains about 25 tool steps (web search, page fetches, shell commands) between the thinking blocks. The rendered page does not show their inputs or outputs. Unknown: the exact commands and outputs. |

The prompt text is identical to "Prompt 2" in [G1](../gemini/G1_yang-mills-proof-status-update.md). The user ran the prompt from G1 in this conversation.

## Human prompt

You are a mathematical physicist specializing in constructive quantum field theory and automated theorem proving.

CONTEXT:
The OpenAI-YM-20261028 Lean 4 proof constructs 4D pure Yang–Mills theory using Balaban-style ultraviolet machinery and a subsequence-based infinite-volume limit, explicitly stopping short of clustering and a mass gap. We want to evaluate two candidate engines for proving a uniform exponential clustering bound |⟨O(x) O(y)⟩_c| ≤ C * exp(-m * |x - y|) across the weak-to-strong coupling crossover (g → 0, a → 0):
- Engine 1: Multi-Scale Renormalization Group (Balaban-style block-spin RG flow from UV to confinement scale Λ_YM⁻¹, handing off to an Osterwalder–Seiler strong-coupling cluster expansion).
- Engine 2: Center-Vortex / Magnetic Flux Decimation (Tomboulis-style decimation bounding the Z_N vortex free energy from below across scales to enforce an area law / mass gap).

INSTRUCTIONS:
1. Build a side-by-side technical audit of Engine 1 vs. Engine 2 specifically optimized for Lean 4 automated theorem proving:
- Bookkeeping overhead (number of scale-dependent polymer/field-splitting estimates).
- Compatibility with the existing UV/IR interface in OpenAI-YM-20261028.
- Exact point of failure where known literature stops (e.g., large-field/small-field stability at intermediate coupling for Balaban RG; proving reflection positivity / exact decimation bounds survive the continuum limit for Tomboulis).
2. Propose a concrete, falsifiable intermediate conjecture (the "Bridge Lemma") for the stronger engine that, if proved, closes the weak-to-strong gap.
3. Translate that Bridge Lemma into:
- A precise mathematical statement (all quantifiers, norms, and uniformity conditions explicit).
- A candidate Lean 4 theorem signature.
- Three concrete failure modes or counterexample checks we should test computationally/formally before burning prover cycles on it.

## Assistant response

Searched the web, read 2 pages, and 10 more steps

I recommend Engine 1 (Balaban-style RG), with one change: replace the Osterwalder–Seiler handoff with a finite-size mixing criterion. The Bridge Lemma below would close the weak-to-strong gap if proved, but it does not make the core problem easier. It turns the missing infrared physics into one inequality, uniform in the lattice spacing, about finite-volume measures the archive already builds. That inequality can be tested numerically, and if it holds you also get uniqueness of the infinite-volume limit with no subsequence.

### 0. What the archive actually provides (checked in the source)

I cloned yang-mills-group/OpenAI-YM-20261028 and read the public spec and the RG interface. These points drive the audit:

- Periodic boxes only. The lattice is a periodic torus, Site l := Axis → ZMod l.val. wilsonLaw uses product Haar measure and the plaquette energy 1 − Re tr/(n+1). Nothing in the public interface defines a measure with fixed boundary links.
- The RG is tied to weak coupling at every stage. YM/RG/History.lean, Calendar.Fits, requires delayed m : 1 < hatBeta m and smallField m : threshold m ≤ 1 for all m. Here hatBeta m = bar + slopeConstant * scale m, and threshold = ĝ · exp((log log β̂)²), which is a Balaban-type large-field cutoff p(g). Lowering bar cannot carry the stack into the crossover; every step's estimates assume β̂ > 1.
- The infrared is reached by compactness, not by estimates. The README says that for each strictly increasing volume sequence there is a subsequence and a hierarchy, and that "The volume limit allows refinement." Uniqueness of the infinite-volume limit is not claimed, and the mass gap is explicitly out of scope.
- The state is decomposed into phases. ChallengeSpec.Hierarchy carries a compact Character space with a full-support phaseMeasure. Integrating the phase correlations over it gives the unselected limit (∫ correlation (some i) dμ = correlation none). I could not determine what Character represents physically; this matters for failure mode 2.
- There is a blocking-kernel penalty. YangMills.constructed fixes a penalty b > 0 before choosing the family (C.path.levels.clock.kernel.penalty = b).
- Large-field machinery exists. YM/SectorNext/LARGE_FIELD_REMAINDERS/ is present. No identifier mentions Balaban, vortices as an engine, cluster expansions or reflection positivity, so the "Balaban-style" label is your description, which the structure supports.

The Gross committee's validation covers existence of pure Yang–Mills, not the mass gap (secondary reporting; I did not open the committee document). The original jointExistence target omitted some lattice-construction links. The committee relied on the stronger combined_acceptance, in the review repository yang-mills-group/YM, which I did not inspect.

### 1. Side-by-side audit

| Row | Engine 1: Balaban RG plus strong-coupling handoff | Engine 2: Tomboulis decimation and vortex free energy |
|---|---|---|
| Estimate families per RG step (my structural count, not a measured figure) | About 9: block kernel and gauge fixing; background-field minimizer and its analyticity; covariant Green's-function decay; small/large-field partition; polymer expansion of the fluctuation integral; extraction of the relevant terms (coupling renormalization); large-field suppression; inductive polymer norms; control of the coupling flow. Plus about 2 for the handoff. | About 4–5: character-coefficient positivity and monotonicity; upper and lower decimation bounds on Z and on the twisted Z; existence and monotonicity of the interpolation parameter; ratio bound on the vortex free energy; the Tomboulis–Yaffe inequality from vortex free energy to Wilson loops. |
| Lean cost driver | Each family is proved once, with the scale as a parameter; the number of steps k* ~ g₀⁻²/(b₀ log L) does not multiply the proof size. The cost is the size and coupling of the inductive hypothesis. Most of this already exists in the archive. | Fewer families, but almost none exist. New infrastructure: twisted boundary conditions, character expansions of the Wilson action, chessboard and reflection-positivity inequalities. |
| Compatibility with the archive | High in the UV. It uses the same Calendar, Levels, kernel penalty and large-field remainders, and the same convergence at fixed physical volume. Gap: every Fits field assumes weak coupling, so the IR needs a new layer, not a parameter change. | Low. It needs twisted tori, which Site/wilsonLaw do not support. Its statements are about a fixed β; the continuum limit needs the string tension to scale with the lattice spacing, which only RG-type control provides. So Engine 2 depends on Engine 1 for uniformity anyway. |
| Quantity it controls | Correlations of local gauge-invariant observables, which is your target. | Vortex free energy, hence the Wilson-loop area law. No theorem turns an area law into exponential clustering of local observables. |
| Where the literature stops | Balaban proved ultraviolet stability at weak coupling for finite volume (1987–89 CMP series, including Large Field Renormalization I–II). Small-field estimates need g_k ≪ 1, and large-field suppression ~exp(−c·p(g_k)²) needs the same. Osterwalder–Seiler needs bare β below a small threshold. In between there is no small parameter, and no known estimate covers it. | Ito and Seiler identified gaps in Tomboulis's 2007 confinement claim for 4D SU(2), and discussed what would be needed to fill them. Tomboulis replied (arXiv:0712.2620); to my knowledge the gaps remain open. Even if they were closed, you would still need uniformity in the continuum limit and the step from area law to clustering. |
| Number of open problems | One: the crossover regime. | Three: the disputed decimation step, uniform scaling of the string tension, and area law to clustering. |

Inference: Engine 1 is stronger for this target. Its single gap is localized, and both the UV machinery and the finite-volume continuum limit already exist. Engine 2's gaps are disputed or unknown, and it bounds the wrong quantity.

Why I changed the handoff (a departure from your Engine 1). A handoff to Osterwalder–Seiler would need a local effective action with small strong-coupling polymer activities at some scale. Proving that the effective action is quasi-local at strong coupling is itself an infrared statement, so that version of the bridge is circular. A finite-size mixing criterion needs no effective action. It is a statement about expectations in finite physical boxes, which the archive already controls uniformly in the lattice spacing.

### 2. Bridge Lemma: uniform finite-size boundary insensitivity (UFBI)

The lemma has two parts. Part I is a pure statement about Gibbs measures, with no physics input. Part II is the physical conjecture.

Setup. G is a compact group with simple Lie algebra, and C is a WilsonFamily satisfying WilsonRegularity: β_N/log(1/a_N) → s > 0, uniformly in the volume.

Let R ≥ 3 be odd and ℓ > 0 a physical length.
Set B_N = ⌈ℓ/(R·a_N)⌉ and let Λ_N be the cube of side R·B_N lattice units. Its central sub-cube Q_N has side B_N, i.e. physical side ℓ/R.
A collar condition τ fixes every link outside Λ_N that shares a plaquette with Λ_N. 𝒯_N is the set of all collar conditions.
μ_{N,p,τ} is the Wilson measure on the links of Λ_N at β = β_{N,p}, with Haar prior and collar τ frozen.
𝔉(Q_N) is the set of measurable F with |F| ≤ 1 that depend only on links inside Q_N and are invariant under gauge transformations at interior sites.

Define the boundary influence

δ_{N,p}(ℓ, R) := sup_{τ,τ'∈𝒯_N} sup_{F∈𝔉(Q_N)} |μ_{N,p,τ}(F) − μ_{N,p,τ'}(F)|.

Part I (finite-size criterion; provable without physics input). For each odd R ≥ 3 there are ε₀(R), c(R), K(R) > 0, depending only on R and the dimension 4, with the following property. For every compact G, β, B ≥ 1 and periodic torus l: if the influence at box side R·B is at most ε₀(R), then for all F, H with |F|, |H| ≤ 1, gauge invariant and supported in cubes of side B around sites x and y,

|Cov_{wilsonLaw(l, β)}(F, H)| ≤ K · exp(−c·dist_l(x, y)/B).

Treating each block of side B as one "super-spin" makes the specification nearest-neighbour at block level, so the constants cannot depend on G, β, B or l.
Status: hypothesis. Dobrushin–Shlosman and Martinelli–Olivieri criteria are known for finite-range spin systems. I have not verified that the versions for general compact spin spaces cover the gauge-invariant σ-algebras here, and the size of ε₀(R) is unknown.

Part II (the conjecture). There exists ℓ > 0 such that

limsup_{N→∞} sup_p δ_{N,p}(ℓ, R) ≤ ε₀(R).

Consequences if Parts I and II hold:

- Exponential clustering uniform in N, with m = c(R)·R/ℓ, for bounded block observables.
- The same for the continuum smeared two-point functions, with rate m·δ/(2+δ) (via Davydov's covariance inequality), provided smeared insertions have L^{2+δ} moments uniform in N. This extra input is not in the public spec; the archive's OPE bounds may or may not supply it.
- The infinite-volume limit is unique along the full sequence, so no subsequence is needed, and for each correlation, μ-almost every character gives the same value as the unselected state.

Inference: Part II is roughly as hard as a mass gap at finite physical volume, because in the one-phase regime strong mixing and exponential decay are equivalent. The lemma's value is that it isolates the gap: one inequality, on objects that already exist, that can be checked numerically.

### 3. Lean 4 signature

These definitions are proposed only. None exist in the repository, and I have not compiled any of this; it targets Lean 4.32.0 and the public namespaces.

```lean
import ChallengeSpec
set_option autoImplicit false
noncomputable section
namespace YangMills.Bridge
open MeasureTheory Filter Topology

/-- PROPOSED. Links of the cube of side `L` in ℤ⁴, and the collar links outside it
that share a plaquette with it. -/
opaque BoxLink (L : ℕ) : Type
opaque CollarLink (L : ℕ) : Type
abbrev BoxConfig (g : GaugeGroup) (L : ℕ) := BoxLink L → g.image
abbrev Collar (g : GaugeGroup) (L : ℕ) := CollarLink L → g.image

/-- PROPOSED. Wilson law on the box, Haar prior, collar links frozen at `τ`. -/
opaque boxLaw (g : GaugeGroup) (L : ℕ) (β : ℝ) (haar : Measure g.image)
(τ : Collar g L) : Measure (BoxConfig g L)

/-- PROPOSED. Bounded, interior-gauge-invariant observables of the central side-`B` sub-cube. -/
opaque CentralObs (g : GaugeGroup) (L B : ℕ) : Set (BoxConfig g L → ℝ)

def influence (g : GaugeGroup) (L B : ℕ) (β : ℝ) (haar : Measure g.image)
(𝒯 : Set (Collar g L)) : ℝ :=
⨆ (τ : 𝒯) (τ' : 𝒯) (F : CentralObs g L B),
|∫ U, F.1 U ∂boxLaw g L β haar τ - ∫ U, F.1 U ∂boxLaw g L β haar τ'|

/-- PROPOSED. Bounded and gauge invariant, depending only on links in the side-`B` cube at `x`. -/
opaque LocalObs {g : GaugeGroup} {l : ℕ+} (x : Site l) (B : ℕ) : Set (Configuration g l → ℝ)
opaque torusDist {l : ℕ+} (x y : Site l) : ℕ

/-- Part I. Constants depend only on `R`. -/
theorem finiteSize_criterion (R : ℕ) (hR : 3 ≤ R) (hodd : Odd R) :
∃ ε₀ c K : ℝ, 0 < ε₀ ∧ 0 < c ∧ 0 < K ∧
∀ (g : GaugeGroup) (haar : Measure g.image) [IsProbabilityMeasure haar]
(β : ℝ) (B : ℕ), 1 ≤ B →
influence g (R * B) B β haar Set.univ ≤ ε₀ →
∀ (l : ℕ+) (x y : Site l) (F H : Configuration g l → ℝ),
F ∈ LocalObs x B → H ∈ LocalObs y B →
|∫ U, F U * H U ∂wilsonLaw g l β haar
- (∫ U, F U ∂wilsonLaw g l β haar) * (∫ U, H U ∂wilsonLaw g l β haar)|
≤ K * Real.exp (-c * (torusDist x y : ℝ) / B) := by
sorry

/-- Part II, as a predicate on a Wilson family. -/
def UFBI {g : GaugeGroup} (C : WilsonFamily g) (R : ℕ) (ε₀ : ℝ) : Prop :=
∃ ℓ : ℝ, 0 < ℓ ∧ ∀ᶠ N in atTop, ∀ p : ℕ,
let B := ⌈ℓ / (R * C.mesh N)⌉₊
influence g (R * B) B (C.beta N p) C.haar Set.univ ≤ ε₀

/-- PROPOSED interface: L^{2+δ} bounds on smeared insertions, uniform in N and p. -/
opaque UniformMoments {g : GaugeGroup} (C : WilsonFamily g) (δ : ℝ) : Prop
/-- PROPOSED: connected smeared two-point function of the hierarchy, second test translated by `e`. -/
opaque connected₂ {g : GaugeGroup} {C : WilsonFamily g} (T : Hierarchy C)
(a b : C.Token) (f h : WilsonFamily.SeparatedTest 1) (e : Spacetime) : ℂ

/-- Bridge: Part I + Part II ⇒ clustering and collapse of the phase decomposition. -/
theorem clustering_of_UFBI {g : GaugeGroup} (hg : g.IsSimple)
(C : WilsonFamily g) (hC : WilsonRegularity C)
(R : ℕ) (hR : 3 ≤ R) (hodd : Odd R) (ε₀ c K : ℝ)
(hcrit : 0 < ε₀ ∧ 0 < c ∧ 0 < K ∧ True /- the Part I conclusion for (ε₀, c, K) -/)
(hU : UFBI C R ε₀) (δ : ℝ) (hδ : 0 < δ) (hmom : UniformMoments C δ)
(order : ℕ → ℕ) (hord : StrictMono order) (T : Hierarchy C)
(hT : C.Converges order (fun v x => T.correlation none (T.project ∘ v) x)) :
(∃ m : ℝ, 0 < m ∧ ∀ (a b : C.Token) (f h : WilsonFamily.SeparatedTest 1),
∃ K' : ℝ, ∀ e : Spacetime, ‖connected₂ T a b f h e‖ ≤ K' * Real.exp (-m * ‖e‖)) ∧
(∀ (n : ℕ) (a : Fin n → T.Tag) (x : Points n), x ∈ WilsonFamily.separated n →
∀ᵐ i ∂T.phaseMeasure, T.correlation (some i) a x = T.correlation none a x) := by
sorry
```

Implementation notes:

- Replace the True placeholder in hcrit with a named definition, criterionThreshold R, extracted from Part I.
- UFBI quantifies over all p because WilsonRegularity.running is uniform in p; check that C.beta N p actually depends on p in the constructed family.
- connected₂ needs the one-point functions, which come from the 1-arity correlation.

### 4. Three checks before spending prover time

1. Boundary conditions carrying center flux (could make Part II false as stated).

Frozen collars include configurations that force a Z_N vortex surface through the box. If the influence of such a collar on central observables stops decreasing, or only decays polynomially in ℓ, then the supremum over all collars kills Part II.

- Test: Monte Carlo on SU(2) Wilson at β ≈ 2.3–2.7 with ℓ fixed in units of r₀. Compare a trivial collar against a maximally twisted collar, measuring small Wilson loops and plaquettes in the central sub-cube as functions of ℓ. Cheaper runs first: 3D SU(2), and 4D Z₂ in its confined phase.
- Pass: the influence decays exponentially, with a rate that converges as β grows.
- Fail: the supremum must be restricted to trivial-flux collars. That breaks the standard Dobrushin–Shlosman argument, whose collars are samples that carry flux, so Part I has to be re-proved with the vortex free energy as an explicit term. This is the one place where Engine 2's quantity becomes necessary, and it would argue for a hybrid of the two engines.

2. Conflict with the phase decomposition (formal, cheap). UFBI implies that μ-almost every character has the same correlations as the unselected state.

- Test: first find what Character represents. Then search the archive's 100,168 reachable declarations for any result implying that correlations differ between characters (correlation (some i) ≠ correlation (some j)), including one-point functions.
- Fail: any such result refutes the Bridge for this construction immediately.
- Pass: proving the implication UFBI ⇒ character independence is a short Lean lemma, and it is the cheapest end-to-end test that the signature type-checks against Hierarchy.

3. Whether the influence norm stays small as the lattice spacing shrinks, and how large ε₀ is. The supremum over the full gauge-invariant σ-algebra of a central block, which has ~(ℓ/(R·a))⁴ links, may fail to stay small as a → 0 even in a massive theory.

- Test (a): exact Gaussian computation for a 4D massive free scalar and for Villain U(1): total-variation or Hellinger distance between central-block marginals under two collars as a → 0, at fixed m·ℓ. Pass if it is bounded by C·e^{−mℓ/2} uniformly in a.
- Test (b): compute ε₀(R) explicitly from Part I's proof. If it is extremely small, Part II can only be checked by extrapolating decay rates, not by direct measurement.
- Fail: redefine the influence on blocked links at scale ℓ/R built with the archive's own kernel (penalty b). Those are UV-regular by construction, so the RG machinery feeds the criterion directly. Note that this changes Part I's spin space.

Recommended first step: run check 2 in Lean and check 3(a) numerically, since both take days, not months. Then run the SU(2) twisted-collar Monte Carlo before formalizing Part I. Switch to Engine 2, or a hybrid, only if check 1 fails and the trivial-flux restriction cannot be absorbed into Part I.

Unverified items:

- The literature details not covered by the search results are from memory: Osterwalder–Seiler 1978, Tomboulis–Yaffe 1985, the Dobrushin–Shlosman and Martinelli–Olivieri criteria, Magnen–Rivasseau–Sénéor, and Davydov's inequality.
- The estimate-family counts in the table are my own structural estimates.
- The Lean code above has not been compiled.

Sources:

- OpenAI-YM-20261028 source archive (README, PublicWilson.lean, ChallengeSpec.lean, Construction.lean, YM/RG/History.lean, YM/Source/Construction.lean)
