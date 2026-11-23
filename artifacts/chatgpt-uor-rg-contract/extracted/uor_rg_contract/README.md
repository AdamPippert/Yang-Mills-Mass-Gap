# RG/UOR extension contract (proposal)

Source inspected: UOR-Foundation/UOR-Framework, default branch, workspace 0.5.2, `foundation/src/user/state.rs` and `foundation/src/bridge/proof.rs`.

This is a separate QFT vocabulary. Native UOR `state:Context` and `state:Transition` are related conceptually; no claim is made that RGTransition directly implements those Rust traits. `proof:Proof` specifically attests to UOR kernel identities and MUST NOT be asserted for unverified Lean artifacts.

`contract.schema.json`: Draft 2020-12 validation of immutable **payloads**. `context.jsonld`: JSON-LD term mappings. `contract.shacl.ttl`: graph-level illustrative validation of linked expanded RDF data. `example.jsonld`: linked JSON-LD envelope carrying digest + payload (application-side digest uses sorted compact UTF-8 JSON with SHA-256; it is NOT claimed to equal a native UOR content fingerprint). `verify_example.py`: structural example checks.

**Trust boundary:** literal `uniform_all_a_L` scope and absence of `a`/`L` from claimed freeVariables do not prove semantic independence. The verifier must parse the complete expression DAG, check transitive free variables, validate bounds by exact rational arithmetic, verify referenced proofs against kernel output, and reject unknown/unresolved certificate links. The example is a candidate and deliberately has placeholder certificate digests; it MUST NOT be elevated to certified status.

Run `python verify_example.py` after installing `jsonschema`. For SHACL, materialize linked payload nodes into RDF with `rdf:type` and execute a SHACL-SPARQL engine; the `example.jsonld` envelope itself is not an RDF materialization of each payload.

The toy SU(2) blocking is a bookkeeping demonstration, not a constructive Yang–Mills RG proof and not evidence of a mass gap.

`rg_contract.rs`: typed Rust application-side contract and exact rational checks; `mcp-contract.json`: proposed MCP method envelope. The Rust file is a stub and has not been compiled. Suggested Cargo dependencies: serde, serde_json, num-bigint, num-rational, num-traits, sha2, and uor-foundation pinned to the inspected revision.
