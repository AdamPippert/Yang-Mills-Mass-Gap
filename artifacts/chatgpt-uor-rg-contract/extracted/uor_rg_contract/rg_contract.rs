//! Proposed QFT extension. Does not implement sealed UOR pipeline internals.
//! Dependency versions must be pinned against the inspected UOR 0.5.2 checkout.
use serde::{Deserialize, Serialize};
use std::collections::{BTreeMap, BTreeSet};
use num_bigint::BigInt;
use num_rational::BigRational;
use num_traits::Zero;
use std::str::FromStr;
use sha2::{Digest, Sha256};

// Verified namespace and exact supertrait bounds from foundation/src/user/state.rs:
use uor_foundation::{HostTypes, user::state::{Context as UorContext, Transition as UorTransition}};

/// Only an interface bridge. Concrete implementations must supply every
/// Context/Binding/ComputationTrace/TopologicalDelta-associated requirement.
#[allow(dead_code)]
fn accept_native_uor_transition<H, T>(_transition: &T)
where H: HostTypes, T: UorTransition<H>, T::Context: UorContext<H> {}

#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Interval { pub lo: String, pub hi: String }
#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Constant {
    pub name: String, pub value: Interval, pub scope: String,
    pub derivation: String, #[serde(default, rename = "freeVariables")]
    pub free_variables: Vec<String>,
}
#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Scale {
    pub k: u64, pub a: String,
    #[serde(rename = "boxLength")] pub box_length: u64,
    #[serde(rename = "volumeSites")] pub volume_sites: u64,
    pub dimension: u8,
}
#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct TransitionCandidate {
    pub source: String, pub target: String,
    #[serde(rename = "blockFactor")] pub block_factor: u64,
    #[serde(rename = "constantEnvelope")] pub constants: Vec<Constant>,
}

fn fraction(input: &str) -> Result<BigRational, String> {
    let (numer, denom) = input.split_once('/').unwrap_or((input, "1"));
    let n = BigInt::from_str(numer).map_err(|_| "bad numerator")?;
    let d = BigInt::from_str(denom).map_err(|_| "bad denominator")?;
    if d <= BigInt::zero() { return Err("denominator must be positive".into()); }
    Ok(BigRational::new(n,d))
}

pub fn canonical_digest(value: &serde_json::Value) -> Result<String, String> {
    // This is a prototype application-side digest, not a native UOR fingerprint.
    // Production code MUST use a versioned canonicalization format and the
    // supported UOR Grounding -> Validated -> pipeline path for UOR identity.
    fn sort(v: &serde_json::Value) -> serde_json::Value {
        match v {
            serde_json::Value::Object(m) => serde_json::Value::Object(
                m.iter().map(|(k,v)| (k.clone(), sort(v))).collect()),
            serde_json::Value::Array(a) => serde_json::Value::Array(a.iter().map(sort).collect()),
            _ => v.clone(),
        }
    }
    let bytes = serde_json::to_vec(&sort(value)).map_err(|e| e.to_string())?;
    Ok(format!("sha256:{:x}", Sha256::digest(bytes)))
}

/// Checks only *declared* free variables and exact scalar relations.
/// A semantic prover MUST independently reconstruct transitive dependencies.
pub fn check_candidate(
    t: &TransitionCandidate, source: &Scale, target: &Scale,
) -> Result<(), String> {
    if source.dimension != 4 || target.dimension != 4 { return Err("dimension drift".into()); }
    if target.k != source.k.checked_add(1).ok_or("scale overflow")? {
        return Err("nonconsecutive scales".into());
    }
    let bf = BigRational::from_integer(BigInt::from(t.block_factor));
    if t.block_factor < 2 || fraction(&target.a)? != fraction(&source.a)? * bf {
        return Err("incorrect lattice spacing".into());
    }
    if source.box_length != target.box_length.checked_mul(t.block_factor).ok_or("box overflow")? {
        return Err("incorrect box length".into());
    }
    for s in [source,target] {
        if s.volume_sites != s.box_length.checked_pow(4).ok_or("volume overflow")? {
            return Err("incorrect four-dimensional volume".into());
        }
    }
    let mut names = BTreeSet::new();
    for c in &t.constants {
        if !names.insert(c.name.as_str()) { return Err("duplicate constant".into()); }
        if c.scope != "uniform_all_a_L" { return Err("missing uniform scope".into()); }
        if c.free_variables.iter().any(|v| ["a","L","a_k","volume","box_length"].contains(&v.as_str())) {
            return Err("forbidden declared variable".into());
        }
        if fraction(&c.value.lo)? > fraction(&c.value.hi)? { return Err("inverted interval".into()); }
    }
    if !["C","m","g_bound"].iter().all(|n| names.contains(n)) {
        return Err("missing required constant".into());
    }
    Ok(())
}

/// Production MCP boundary, to be implemented with object storage, Lean
/// subprocess attestation and exact interval-expression DAG evaluation.
pub trait RgMcpStore {
    fn put_candidate(&mut self, payload: &[u8]) -> Result<String, String>;
    fn get_verified_bytes(&self, digest: &str) -> Result<Vec<u8>, String>;
    fn check_structural(&self, transition_digest: &str) -> Result<(), String>;
    fn check_semantic(&self, transition_digest: &str) -> Result<(), String>;
    fn check_lean_kernel(&self, transition_digest: &str) -> Result<(), String>;
    fn certify(&mut self, transition_digest: &str) -> Result<String, String>;
}
