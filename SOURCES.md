# Sources

Every claim in [STATUS.md](STATUS.md) cites a source ID from this file. This file is a reference. It uses no requirement keywords.

## Source index

| ID | Type | Service or origin | Title | File | Captured |
|---|---|---|---|---|---|
| C1 | Chat | claude.ai | Yang–Mills clustering bound audit | [C1](sources/claude/C1_yang-mills-clustering-bound-audit.md) | Full text. Tool steps not shown by the page. |
| G1 | Chat | Gemini | Yang-Mills Proof Status Update | [G1](sources/gemini/G1_yang-mills-proof-status-update.md) | Most of the text. One marked gap. Script stored separately: [G1 script](sources/gemini/G1_gaussian_ufbi_check.py). |
| O1 | Chat | ChatGPT | Lean reflection positivity scaffold | [O1](sources/chatgpt/O1_lean-reflection-positivity-scaffold.md) | All 7 turns. Two long turns summarized with links to the same text in A1. |
| O2 | Chat | ChatGPT | Design UOR RG Schema | [README](sources/chatgpt/README.md) | One turn. Text matches the pasted block in G1. |
| O3 | Chat | ChatGPT | Kernel construction from UOR (Jul 31, 2025) | [README](sources/chatgpt/README.md) | Opened, not read in full, judged out of scope. |
| A1 | Artifact | ChatGPT file | Yang_Mills_Mathematician_Handoff_2026-11-20.zip | [artifacts](artifacts/chatgpt-handoff-2026-11-20/) | Full. 33 files. |
| A2 | Artifact | ChatGPT file | uor_rg_contract.zip | [artifacts](artifacts/chatgpt-uor-rg-contract/) | Full. 9 files. |
| A4 | Artifact | ChatGPT file | GaussianUFBI_v0_2.zip (original v0.2 package, from chat O1 turn 3) | [artifacts](artifacts/chatgpt-gaussian-ufbi-v0_2/) | Full. 8 files. |
| A3 | Artifact | This repository | Independent rerun of the G1 Gaussian script | [artifacts](artifacts/independent-rerun-2026-11-23/) | Output and environment record. |
| U1 | Web | GitHub | yang-mills-group/OpenAI-YM-20261028, README and metadata | [U1](sources/upstream/U1_OpenAI-YM-20261028_README.md) | Full README. Source tree not cloned. |

## Artifact A1

| Field | Value |
|---|---|
| File | `artifacts/chatgpt-handoff-2026-11-20/Yang_Mills_Mathematician_Handoff_2026-11-20.zip` |
| Size | 263,441 bytes |
| SHA-256 | `73e2fae89d9fa49f00c289645cf792cf0daf5c2041ae12f3ce94f520371cd9ec` |
| Origin | Generated in chat O1, downloaded from the ChatGPT library on 2026-11-22. |
| Extracted copy | `artifacts/chatgpt-handoff-2026-11-20/extracted/` |
| Integrity check | Observed: `shasum -a 256 -c SHA256SUMS` in `extracted/` reports OK for all 33 listed files. |
| Author | ChatGPT, prepared for the repository owner. Not independently reviewed by a human. |

## Artifact A2

| Field | Value |
|---|---|
| File | `artifacts/chatgpt-uor-rg-contract/uor_rg_contract.zip` |
| Size | 12,342 bytes |
| SHA-256 | `2497397941b49b7c035f0b5459055cb1c86e77f25a6cea44fbe26166cec9aff9` |
| Origin | Link "Download the UOR–RG contract package" in chat O2. Downloaded 2026-11-23. |
| Contents | `context.jsonld`, `contract.schema.json`, `contract.shacl.ttl`, `example.jsonld`, `example-graph.jsonld`, `mcp-contract.json`, `rg_contract.rs`, `verify_example.py`, `README.md` |
| Handling | Observed: the zip holds no absolute or parent-directory paths. Extracted to its own folder. No file was run or compiled. |
| Status stated by the package | A proposal. The Rust file "is a stub and has not been compiled". The example "is not evidence of a mass gap". |

## Artifact A4

| Field | Value |
|---|---|
| File | `artifacts/chatgpt-gaussian-ufbi-v0_2/GaussianUFBI_v0_2.zip` |
| Size | 45,771 bytes |
| SHA-256 | `52fa0454c9193f710f7623f43cd7c1b3babdfab3ec95db7758cc58e19eebbbea` |
| Origin | File card in chat O1, turn 3 ("GaussianUFBI_v0_2.zip — complete runnable package"). Found by ChatGPT library search "UFBI". Downloaded 2026-11-23. |
| Contents | `MassGap/UFBI/`: `GaussianBoundaryEstimate.md`, `SPECIFICATION.md`, `gaussian_bounds.py`, `test_gaussian_bounds.py`, `ufbi_control.py`, `test_ufbi_control.py`, `estimate_checks.json`, `results.csv` |
| Integrity | Observed: the SHA-256 of each of the 8 files equals the hash recorded for the same path in A1 `provenance/original_sources.json`. The handoff's claim that its original files are unchanged holds for these 8. |
| Not in this zip | The 5 other original files that A1 lists: `ReflectionPositivity.lean`, `GaussianUFBI.py`, `GaussianUFBI.md`, `FOUNDATION_STATUS.md` and the scaffold `README.md`. |
| Handling | Extracted to its own folder. Nothing was run. |

## Artifact A3

| Field | Value |
|---|---|
| Path | `artifacts/independent-rerun-2026-11-23/` |
| What | A rerun of [G1_gaussian_ufbi_check.py](sources/gemini/G1_gaussian_ufbi_check.py) for B = 1, 2, 3, 4, 5, 6, 8, 10 at R = 3 and mℓ = 6 and 12. |
| Environment | Python 3.9.6, NumPy 2.0.2, SciPy 1.13.1, macOS x86_64. See `ENVIRONMENT.txt`. |
| Result | Observed: the numbers equal the values ChatGPT reports in O1 turn 2 to the printed precision (for example mℓ = 6, B = 3: d_M(lat) 6.49715, 2TV(lat) 1.997680, d_M(phys) 0.72191, 2TV(phys) 0.563731). |
| Independence | Limited. The rerun used the same script. It confirms the arithmetic and the report. It does not test the model's meaning. |

Files in A1 that STATUS.md cites:

| Path in `extracted/` | Content |
|---|---|
| `Mathematician_Review.md` and `.pdf` | Main review packet. 13 pages. |
| `review_notes/Conditional_Spectral_Gap.md` | Full spectral-gap proof and counterexamples. |
| `review_notes/Gaussian_Audit.md` | Audit of the Gaussian estimates. |
| `review_notes/Reviewer_Questions.md` | Questions for an outside mathematician. |
| `MassGap/UFBI/GaussianBoundaryEstimate.md` | Derivations G1 to G8. |
| `MassGap/UFBI/SPECIFICATION.md` | UFBI specification v0.1 and v0.2. |
| `MassGap/ReflectionPositivity.lean` | Uncompiled Lean scaffold. |
| `original_notes/FOUNDATION_STATUS.md` | Earlier status audit. |
| `validation/` | Test logs and sweep outputs from the 2026-11-20 rerun. |

The Markdown, Python, Lean and log files in A1 are reproduced as ChatGPT generated them. This repository does not edit them.

## External references cited by A1

The URLs below resolve (HTTP 200 on 2026-11-22). Observed: only the status code. Unknown: whether the cited pages support the claims that A1 attaches to them. This repository did not read them in full.

| Ref | Citation | URL |
|---|---|---|
| R1 | Jaffe and Witten, *Quantum Yang-Mills Theory*, Clay Mathematics Institute problem description | <https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf> |
| R2 | Powell and Werner, *Lecture notes on the Gaussian Free Field*, arXiv:2004.04720v2 | <https://arxiv.org/abs/2004.04720v2> |
| R3 | Devroye, Mehrabian and Reddad, *The total variation distance between high-dimensional Gaussians with the same mean*, arXiv:1810.08693v7 | <https://arxiv.org/abs/1810.08693v7> |
| R4 | Osterwalder and Schrader, *Axioms for Euclidean Green's functions II*, Commun. Math. Phys. 42 (1975) 281–305 | <https://doi.org/10.1007/BF01608978> |
| R5 | Lüscher, *Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories*, Commun. Math. Phys. 54 (1977) 283–292 | <https://doi.org/10.1007/BF01614090> |
| R6 | Tomboulis, reply cited in C1 as arXiv:0712.2620 | <https://arxiv.org/abs/0712.2620> |

Literature that C1 names "from memory" and no source here verifies: Osterwalder–Seiler 1978, Tomboulis–Yaffe 1985, Dobrushin–Shlosman and Martinelli–Olivieri mixing criteria, Magnen–Rivasseau–Sénéor, Davydov's covariance inequality, Balaban's 1987–89 papers, and the Ito–Seiler critique of Tomboulis. C1 states these are unverified.

## Upstream repository U1

| Field | Value |
|---|---|
| Repository | <https://github.com/yang-mills-group/OpenAI-YM-20261028> |
| Observed | `gh api` on 2026-11-22: repository exists, license Apache-2.0, default branch `main`, last push 2026-11-05T23:01:25Z, description "OpenAI construction of pure Yang-Mills obtained 10/28/2026". |
| Observed | `main` points to commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464`, the commit that A1 and C1 pin. The commit message is "Import original October 28 OpenAI Yang-Mills submission". |
| Observed | The README says the volume limit allows refinement and that "A positive mass gap ... are outside its scope." |
| Not done | This repository did not clone or build the Lean sources. It did not check the repository's claims. |
| Snapshot note | The snapshot [U1](sources/upstream/U1_OpenAI-YM-20261028_README.md) is an unmodified copy of the README. Its relative links point to files in the upstream repository and do not resolve in this repository. |

## Web reports on the upstream validation

Observed: a web search on 2026-11-23 returned the pages below. This repository read only the search-result summaries. Unknown: whether each page supports the summary. Gemini's G1 Turn 0a cites two of these outlets by name ("Conyso" and "CASRAI" appear as citation markers; only the CASRAI URL matched).

| ID | Title as listed | URL |
|---|---|---|
| W1a | Gross Panel Sets Release of OpenAI's Yang-Mills Lean Proof | <https://fourweekmba.com/ai-gross-panel-sets-release-of-openais-yang-mills-lean-proof/> |
| W1b | openai yang mills proof confirmed mass gap open | <https://pasqualepillitteri.it/en/news/32547/openai-yang-mills-proof-confirmed-mass-gap-open> |
| W1c | ai rivals physics mathematical challenge 2026 (CASRAI) | <https://casrai.org/news/ai-rivals-physics-mathematical-challenge-2026> |
| W1d | yang mills group publish openai lean code | <https://cryptobriefing.com/yang-mills-group-publish-openai-lean-code/> |
| W1e | Formalization of QFT? (a blog post by Peter Woit) | <https://www.math.columbia.edu/~woit/wordpress?p=15637> |

## Search coverage

| Service | Search performed on 2026-11-22 | Result |
|---|---|---|
| claude.ai, personal organization | Fetched all 186 conversations through the signed-in session. Matched content against: Yang-Mills, mass gap, lattice gauge, Wilson loop, Osterwalder, reflection positivity, confinement, clustering bound, constructive QFT. | One conversation: C1. |
| claude.ai, organization "Western New Media" | Tried to list conversations. | "Permission denied." The user states it has no Yang-Mills conversations. |
| ChatGPT | UI search "Yang-Mills". | Three chats, two files. See above. O1 and O2 captured. O3 judged out of scope. |
| Gemini | UI search "Yang-Mills". | One chat: G1. |

Gaps in coverage:

- ChatGPT and Gemini searches used one query. Chats that discuss the topic without the phrase "Yang-Mills" can exist. Planned: search "mass gap", "Wilson", "UFBI" and "reflection positivity" in both.
- ChatGPT search results mixed exact and semantic matches. The search also returned "Sovereign AI Operations Lessons" and a file `chatgpt-custom-instructions-compressed.zip` for a different query. This repository did not open them. They are unrelated by title.
- ChatGPT projects (for example "Eigentunnel") were not opened. Unknown: whether any holds related chats.
- Claude Code and Codex session logs on this machine mention Yang-Mills only in the session that built this repository.
- The claude.ai conversation C1 shows no artifact card on the rendered page. Observed: none. Unknown: whether the omitted tool steps produced files.
