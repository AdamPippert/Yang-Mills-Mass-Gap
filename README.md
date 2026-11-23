# Yang–Mills mass gap: research record

This repository records AI-assisted work toward a proof of the Yang–Mills mass gap. It collects the relevant conversations and generated artifacts from Claude, ChatGPT and Gemini. It states what the work shows and what remains open.

**The mass gap is not proved here.** No result in this repository has been reviewed by an independent mathematician or checked by a Lean compiler. Read [STATUS.md](STATUS.md) before you cite anything.

This document uses no requirement keywords.

## Contents

| Path | Content |
|---|---|
| [STATUS.md](STATUS.md) | Verdict, claim register with evidence levels, obstructions, remaining tasks, source disagreements. |
| [SOURCES.md](SOURCES.md) | Index of every source, capture method, checksums, search coverage and gaps. |
| `sources/claude/` | Full text of the claude.ai conversation C1. |
| `sources/gemini/` | Text of the Gemini conversation G1, with one marked gap, and its Gaussian-check script. |
| `sources/chatgpt/` | Text of ChatGPT chats O1 and O2. Note on chat O3, judged out of scope. |
| `sources/upstream/` | Snapshot of the README of the upstream Lean repository and its metadata. |
| `artifacts/chatgpt-handoff-2026-11-20/` | The ChatGPT review packet: zip and extracted files. Includes the review PDF, derivations, Python controls, the Lean scaffold and test logs. |
| `artifacts/chatgpt-gaussian-ufbi-v0_2/` | The original v0.2 Gaussian package: derivations, specification, harness, tests and results. Eight files match the handoff's recorded hashes. |
| `artifacts/chatgpt-uor-rg-contract/` | The ChatGPT UOR/RG proof-state contract prototype (JSON-LD, JSON Schema, SHACL, Rust stub). Not mathematical evidence. |
| `artifacts/independent-rerun-2026-11-23/` | A rerun of the Gaussian boundary-influence script, with its output and environment. |

## Summary of the work

The work started from a Lean 4 repository, `yang-mills-group/OpenAI-YM-20261028`. Its README claims an existence construction of four-dimensional pure Yang–Mills theory and excludes the mass gap.

The conversations then tried to find a route from that construction to a mass gap. They produced four things:

1. A conditional theorem. Common-rate exponential decay on a dense family of states implies a spectral gap. An AI model wrote an informal proof.
2. A finite-size mixing criterion, named UFBI. It would give the decay hypothesis if a boundary-influence inequality holds uniformly as the lattice spacing goes to zero. Nobody has proved the inequality.
3. Explicit estimates for a free massive scalar, and a numerical check of boundary influence on it. The scalar is a control model with an input mass.
4. A list of obstructions and falsification checks. One check (the Gaussian one) has run. Two have not.

[STATUS.md](STATUS.md) gives the evidence level for each item.

## How to read this repository

1. Read the verdict and claim register in [STATUS.md](STATUS.md).
2. Open the review PDF at `artifacts/chatgpt-handoff-2026-11-20/extracted/Mathematician_Review.pdf` for the mathematics.
3. Read [C1](sources/claude/C1_yang-mills-clustering-bound-audit.md) for the comparison of the two proof strategies and the Bridge Lemma.
4. Read [G1](sources/gemini/G1_yang-mills-proof-status-update.md) for how the three assistants were used together.
5. Check [SOURCES.md](SOURCES.md) for what was not captured.

## Reproduce the integrity checks

Precondition: a shell in the repository root.

1. Run `cd artifacts/chatgpt-handoff-2026-11-20/extracted && shasum -a 256 -c SHA256SUMS`.
2. Confirm that every line ends in `OK`.
3. Run `shasum -a 256 ../Yang_Mills_Mathematician_Handoff_2026-11-20.zip`.
4. Confirm the digest equals the value in [SOURCES.md](SOURCES.md).

The numerical checks inside the packet need Python with NumPy and SciPy. The packet's own README lists the commands. This repository did not rerun them. This repository reran only the Gaussian script. See `artifacts/independent-rerun-2026-11-23/`.

## Known limits of this record

- ChatGPT chat O3 is not captured. It is judged out of scope. See [sources/chatgpt](sources/chatgpt/README.md).
- Two long turns in chat O1 are summarized. The same text is in the packet in `artifacts/`.
- The Gemini chat shows no output from its Gaussian script. ChatGPT chat O1 and a rerun in this repository supply the numbers.
- Files in `sources/` are verbatim copies of the conversations except where a file marks a gap or a reformatting.
- Files in `artifacts/` are unmodified AI output. This repository does not correct them.
- Search covered one query per service on ChatGPT and Gemini. Related chats can exist outside the matches.

## License and rights

This repository is under the [Apache License 2.0](LICENSE).

The license covers what the repository owner can license: the documents `README.md`, `STATUS.md` and `SOURCES.md`, the repository owner's prompts in the transcripts, and the independent-rerun files in `artifacts/independent-rerun-2026-11-23/`.

Three kinds of material carry limits the license cannot remove:

- Text and files that AI models generated (Claude, ChatGPT, Gemini). Unknown: how copyright applies to them. The repository owner publishes them as records, under the same license.
- The snapshot of the upstream README in `sources/upstream/`. It is Apache-2.0 (observed in the upstream repository metadata) and keeps its own attribution.
- Third-party works that the transcripts quote or cite. They keep their own terms.

Observed: the review packet names the repository owner in `REVIEW_REQUEST.md` and in the title block of `Mathematician_Review.md`.
