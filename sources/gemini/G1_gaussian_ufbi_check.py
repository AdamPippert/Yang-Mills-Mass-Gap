#!/usr/bin/env python3
"""
Exact 4D Massive Free Scalar sanity check for UFBI (Uniform Finite-Size Boundary Insensitivity).

Tests whether the boundary influence (2 * TV distance and Hellinger distance) on the
full central sub-cube Q_N of side B stays bounded as lattice spacing a = ell / (R * B) -> 0
at fixed physical length m * ell.

Requires: numpy, scipy
"""

# PROVENANCE (added by this repository; not part of the original script)
# Origin: Gemini conversation G1 (turn 3). The user pasted the same script into
# ChatGPT conversation O1 (turn 2), which is where this text was captured on 2026-11-23.
# Fidelity: the page text lost all indentation. This repository restored the indentation
# from Python syntax. The code lines are otherwise unchanged.
# Check: `python3 -I -m py_compile G1_gaussian_ufbi_check.py` succeeds (syntax only).
# Not run by this repository: NumPy and SciPy are not installed on the capture machine.
# ChatGPT reports running it and gives numbers in O1; see STATUS.md, check X1.

import time
import numpy as np
from scipy.fft import dstn
from scipy.sparse.linalg import LinearOperator, cg
from scipy.special import erf


def build_inv_eigenvalues(L: int, m0: float) -> np.ndarray:
    """Inverse eigenvalues of (-Delta_Dirichlet + m0^2 I) on an L^4 grid."""
    k = np.arange(1, L + 1, dtype=np.float64)
    lam_1d = 2.0 * (1.0 - np.cos(np.pi * k / (L + 1)))
    # Broadcast sum across 4 dimensions
    lam_4d = (
        lam_1d[:, None, None, None]
        + lam_1d[None, :, None, None]
        + lam_1d[None, None, :, None]
        + lam_1d[None, None, None, :]
        + m0**2
    )
    return 1.0 / lam_4d


def apply_A_inv(v: np.ndarray, inv_eigs: np.ndarray) -> np.ndarray:
    """Apply (-Delta + m0^2)^(-1) using orthonormal 4D DST-I (self-inverse)."""
    v_hat = dstn(v, type=1, norm="ortho")
    return dstn(v_hat * inv_eigs, type=1, norm="ortho")


def boundary_source_constant_collar(L: int, val: float = 1.0) -> np.ndarray:
    """
    Boundary source b(tau) for a constant collar tau == val on all faces of the 4D cube.
    Each face site gets +val for each face it touches (corners touch up to 4 faces).
    """
    b = np.zeros((L, L, L, L), dtype=np.float64)
    for axis in range(4):
        idx_low = [slice(None)] * 4
        idx_high = [slice(None)] * 4
        idx_low[axis] = 0
        idx_high[axis] = L - 1
        b[tuple(idx_low)] += val
        b[tuple(idx_high)] += val
    return b


def compute_mahalanobis_distance(R: int, B: int, m_ell: float, cg_tol: float = 1e-10):
    """
    Computes exact Mahalanobis distance d_M between collars tau = +1 and tau' = -1
    (lattice-unit amplitude) on the central B^4 sub-cube Q inside an (R*B)^4 box.
    """
    L = R * B
    a = 1.0 / L  # Set ell = 1 without loss of generality; m0 = m * a = m_ell / L
    m0 = m_ell * a

    inv_eigs = build_inv_eigenvalues(L, m0)

    # Difference of boundary sources: b(+1) - b(-1) = 2 * b(+1)
    delta_b = boundary_source_constant_collar(L, val=2.0)

    # Mean shift across full box, then restrict to central sub-cube Q
    delta_mu_full = apply_A_inv(delta_b, inv_eigs)
    start = ((R - 1) // 2) * B
    q_slice = (slice(start, start + B),) * 4
    delta_m_Q = delta_mu_full[q_slice].ravel()

    # Define linear operator for Sigma_QQ = P_Q A^(-1) P_Q^T
    n_Q = B**4

    def matvec(x_flat: np.ndarray) -> np.ndarray:
        buf = np.zeros((L, L, L, L), dtype=np.float64)
        buf[q_slice] = x_flat.reshape((B, B, B, B))
        res = apply_A_inv(buf, inv_eigs)
        return res[q_slice].ravel()

    sigma_QQ_op = LinearOperator((n_Q, n_Q), matvec=matvec, dtype=np.float64)

    # Solve Sigma_QQ * x = delta_m_Q
    x, info = cg(sigma_QQ_op, delta_m_Q, rtol=cg_tol, maxiter=2000)
    if info != 0:
        raise RuntimeError(f"CG did not converge (info={info}) for L={L}, B={B}")

    d_M_sq = float(np.dot(delta_m_Q, x))
    d_M = np.sqrt(max(d_M_sq, 0.0))
    return d_M, a


def run_sweep(R: int = 3, m_ell: float = 6.0, B_values=(1, 2, 3, 4, 5)):
    print(f"4D Massive Free Scalar UFBI Check | R={R}, m*ell={m_ell}")
    print("-" * 92)
    print(
        f"{'B':>3} | {'L':>3} | {'a=1/L':>7} | "
        f"{'d_M (lat)':>10} | {'2*TV (lat)':>10} | "
        f"{'d_M (phys)':>10} | {'2*TV (phys)':>11} | {'Time(s)':>7}"
    )
    print("-" * 92)

    for B in B_values:
        t0 = time.perf_counter()
        d_M_lat, a = compute_mahalanobis_distance(R=R, B=B, m_ell=m_ell)
        dt = time.perf_counter() - t0

        # Lattice-unit collar: phi_bdy = +/- 1 (analogous to O(1) gauge links U_e in G)
        two_tv_lat = 2.0 * erf(d_M_lat / (2.0 * np.sqrt(2.0)))

        # Physical-unit collar: Phi_bdy = +/- 1 => phi_bdy = +/- a
        d_M_phys = d_M_lat * a
        two_tv_phys = 2.0 * erf(d_M_phys / (2.0 * np.sqrt(2.0)))

        print(
            f"{B:>3} | {R*B:>3} | {a:>7.4f} | "
            f"{d_M_lat:>10.5f} | {two_tv_lat:>10.6f} | "
            f"{d_M_phys:>10.5f} | {two_tv_phys:>11.6f} | {dt:>7.2f}"
        )


if __name__ == "__main__":
    # Sweep B=1..5 (L=3..15). B=6 (L=18, 105k sites) also runs in a few seconds on a laptop.
    run_sweep(R=3, m_ell=6.0, B_values=(1, 2, 3, 4, 5))
    print()
    run_sweep(R=3, m_ell=12.0, B_values=(1, 2, 3, 4, 5))
