#!/usr/bin/env python3
"""Evaluate analytic Gaussian UFBI bounds; floating-point checks are not proofs.

The model and FFT operator are imported unchanged from ufbi_control.py.
The report tests the block mean, five Dirichlet sine modes, and mean/dipoles.
All sources use physically bounded collars: |tau|, |tau'| <= a*M.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict
import itertools
import hashlib
import json
import math
from pathlib import Path
import platform
import time

import numpy as np
import scipy
from scipy.special import erf

from ufbi_control import GaussianBox, Geometry


def decay_parameters(g: Geometry, t_star: float = 1.0) -> tuple[float, float, float]:
    """Return kappa, exact physical rate, and a proved uniform lower rate."""
    if not math.isfinite(t_star) or t_star <= 0 or g.m0 > t_star * (1 + 1e-14):
        raise ValueError("Require 0 < m*a <= t_star < infinity")
    kappa = 2 * math.asinh(g.m0 / 2)
    return kappa, kappa / g.a, g.mass * 2 * math.asinh(t_star / 2) / t_star


def mean_variance_bounds(g: Geometry) -> tuple[float, float]:
    """Lower bounds on Var[(a*B^4)^(-1) sum_Q phi], exact-mesh and uniform."""
    alpha = math.pi / (2 * (g.B + 1))
    r = 2 / (math.tan(alpha) ** 2 * g.B * (g.B + 1))
    lam = g.m0**2 + 16 * math.sin(alpha) ** 2
    finite = r**4 / (g.a**2 * g.B**4 * lam)
    eta0 = 64 / math.pi**4
    uniform = eta0**2 / (g.q**2 * ((g.mass * g.q) ** 2 + 4 * math.pi**2))
    return finite, uniform


def bounds(g: Geometry, amplitude: float = 1.0, t_star: float = 1.0) -> dict:
    if not math.isfinite(amplitude) or amplitude < 0:
        raise ValueError("amplitude must be finite and nonnegative")
    kappa, rho, gamma = decay_parameters(g, t_star)
    vfinite, vuniform = mean_variance_bounds(g)
    point = min(1.0, 8 * math.exp(-rho * g.distance))
    geometric_average = -math.expm1(-kappa * g.B) / (g.B * -math.expm1(-kappa))
    mean_barrier = min(1.0, 8 * math.exp(-rho * g.distance) * geometric_average
                       / (1 + math.exp(-kappa * (g.L + 1))))
    lam_family = g.mass**2 + 7 * math.pi**2 / g.q**2
    mean_finite = 2 * amplitude * mean_barrier / math.sqrt(vfinite)
    mean_uniform = (math.pi**4 / 4 * amplitude * g.q
                    * math.sqrt((g.mass * g.q) ** 2 + 4 * math.pi**2)
                    * math.exp(-gamma * g.distance))
    family_finite = 2 * amplitude * g.q**2 * math.sqrt(lam_family) * point
    family_uniform = (16 * amplitude * g.q**2 * math.sqrt(lam_family)
                      * math.exp(-gamma * g.distance))
    moment_pairing_min = 32 * math.sqrt(3) / math.pi**4
    return dict(kappa=kappa, rho=rho, gamma=gamma, t_star=t_star,
                mean_variance_finite=vfinite, mean_variance_uniform=vuniform,
                pointwise_physical_shift=2 * amplitude * point,
                mean_physical_shift=2 * amplitude * mean_barrier,
                family_lambda=lam_family, mean_d_finite=mean_finite,
                mean_d_uniform=mean_uniform, family_d_finite=family_finite,
                family_d_uniform=family_uniform,
                moments_pairing_min=moment_pairing_min,
                moments_d_finite=family_finite / moment_pairing_min,
                moments_d_uniform=family_uniform / moment_pairing_min)


def sine_channel(g: Geometry) -> np.ndarray:
    """F=a^3*f for the first sine mode and its four one-axis first excitations.

    The five f rows have Gram matrix a^4*f*f.T=I. The coefficient 7 in
    the energy cutoff is 2^2+1^2+1^2+1^2.
    """
    if g.B < 2:
        raise ValueError("The five-mode channel requires B >= 2")
    j = np.arange(1, g.B + 1)
    frequencies = [(1, 1, 1, 1)]
    frequencies += [tuple(2 if i == ax else 1 for i in range(4)) for ax in range(4)]
    normalizer = (2 / (g.a * (g.B + 1))) ** 2
    rows = []
    for modes in frequencies:
        v = np.ones((g.B,) * 4)
        for ax, n in enumerate(modes):
            shape = [1] * 4
            shape[ax] = g.B
            v *= np.sin(math.pi * n * j / (g.B + 1)).reshape(shape)
        rows.append((g.a**3 * normalizer * v).ravel())
    return np.stack(rows)


def channel_covariance(box: GaussianBox, F: np.ndarray) -> np.ndarray:
    transformed = np.stack([box.sigma_q(row) for row in F])
    result = F @ transformed.T
    return (result + result.T) / 2


def moment_channel(g: Geometry) -> np.ndarray:
    """Physical mean plus four normalized coordinate dipoles (Gram <= I)."""
    if g.B < 2:
        raise ValueError("The five-moment channel requires B >= 2")
    j = np.arange(1, g.B + 1)
    center = (j - (g.B + 1) / 2) / g.B
    f = [np.ones((g.B,) * 4) / g.q**2]
    for ax in range(4):
        shape = [1] * 4
        shape[ax] = g.B
        f.append(np.broadcast_to(math.sqrt(12) * center.reshape(shape) / g.q**2,
                                 (g.B,) * 4))
    return np.stack([(g.a**3 * row).ravel() for row in f])


def moment_covariance_trial(g: Geometry) -> np.ndarray:
    """Variational lower matrix from pairing moments with five sine trials."""
    F, S = moment_channel(g), sine_channel(g)
    pairing = (F @ S.T) / g.a**2
    base = 4 * math.sin(math.pi / (2 * (g.B + 1)))**2
    first = 4 * math.sin(math.pi / (g.B + 1))**2
    eigenvalues = np.array([g.mass**2 + 4 * base / g.a**2]
                          + [g.mass**2 + (3 * base + first) / g.a**2] * 4)
    return (pairing / eigenvalues) @ pairing.T


def mean_boundary_coefficients(box: GaussianBox) -> np.ndarray:
    """Physical collar difference -> physical mean, one coefficient per ghost link.

    Nonnegativity of these coefficients proves constant collars maximize the
    mean shift over an infinity-norm ball. This function evaluates them.
    """
    g = box.g
    row = np.ones(box.n) / (g.a * box.n)
    adjoint = box.inv(box.embed(row))
    pieces = []
    for ax in range(4):
        for side in (0, g.L - 1):
            ix = [slice(None)] * 4
            ix[ax] = side
            pieces.append((g.a * adjoint[tuple(ix)]).ravel())
    return np.concatenate(pieces)


def geometry_checks(g: Geometry, amplitude: float = 1.0, t_star: float = 1.0) -> dict:
    """Reuse covariance for all collars; no restricted-covariance CG is needed."""
    started = time.perf_counter()
    box = GaussianBox(g)
    limits = bounds(g, amplitude, t_star)
    mean_row = np.ones((1, box.n)) / (g.a * box.n)
    F = sine_channel(g)
    Fmom = moment_channel(g)
    mean_var = float(channel_covariance(box, mean_row)[0, 0])
    cov = channel_covariance(box, F)
    covmom = channel_covariance(box, Fmom)
    eig_min = float(np.linalg.eigvalsh(cov)[0])
    eig_min_mom = float(np.linalg.eigvalsh(covmom)[0])
    moment_trial_slack = float(np.linalg.eigvalsh(covmom - moment_covariance_trial(g))[0])
    rows = []
    for pattern in ("constant", "face", "random", "checkerboard"):
        h = box.mean_shift(box.source(pattern, amplitude, seed=0))
        mean_shift = float((mean_row @ h)[0])
        delta = F @ h
        dmean = abs(mean_shift) / math.sqrt(mean_var)
        dfamily = math.sqrt(max(0.0, float(delta @ np.linalg.solve(cov, delta))))
        delta_mom = Fmom @ h
        dmoments = math.sqrt(max(0.0, float(delta_mom @ np.linalg.solve(covmom, delta_mom))))
        record = dict(pattern=pattern, pointwise_physical_shift=float(np.max(np.abs(h)) / g.a),
                      mean_physical_shift=abs(mean_shift), mean_d=dmean, family_d=dfamily,
                      moments_d=dmoments)
        for channel, d in (("mean", dmean), ("family", dfamily), ("moments", dmoments)):
            record[channel + "_two_tv"] = 2 * float(erf(d / (2 * math.sqrt(2))))
            for version in ("finite", "uniform"):
                bound = limits[channel + "_d_" + version]
                record[channel + "_ratio_" + version] = d / bound if bound else 0.0
                record[channel + "_two_tv_bound_" + version] = 2 * float(erf(bound / (2 * math.sqrt(2))))
        rows.append(record)
    tolerance = 2e-10
    failures = []
    if mean_var + tolerance < limits["mean_variance_finite"]:
        failures.append("mean variance finite-grid lower bound")
    if mean_var + tolerance < limits["mean_variance_uniform"]:
        failures.append("mean variance uniform lower bound")
    if eig_min + tolerance < 1 / limits["family_lambda"]:
        failures.append("family covariance spectral lower bound")
    if eig_min_mom + tolerance < limits["moments_pairing_min"]**2 / limits["family_lambda"]:
        failures.append("moment covariance uniform spectral lower bound")
    if moment_trial_slack < -tolerance:
        failures.append("moment covariance exact trial matrix lower bound")
    constant = rows[0]
    for row in rows:
        if row["pointwise_physical_shift"] > limits["pointwise_physical_shift"] + tolerance:
            failures.append(row["pattern"] + ": pointwise barrier")
        if row["mean_physical_shift"] > limits["mean_physical_shift"] + tolerance:
            failures.append(row["pattern"] + ": averaged mean barrier")
        if row["mean_d"] > constant["mean_d"] + tolerance:
            failures.append(row["pattern"] + ": constant-collar dominance")
        for channel, version in itertools.product(("mean", "family", "moments"), ("finite", "uniform")):
            if row[channel + "_ratio_" + version] > 1 + tolerance:
                failures.append(f"{row['pattern']}: {channel} {version} Mahalanobis bound")
    return dict(geometry=asdict(g), L=g.L, a=g.a, separation=g.distance,
                amplitude=amplitude, bounds=limits, measured_mean_variance=mean_var,
                measured_family_covariance_min_eigenvalue=eig_min,
                measured_moments_covariance_min_eigenvalue=eig_min_mom,
                measured_moments_covariance_trial_min_slack=moment_trial_slack,
                collars=rows, failures=failures, seconds=time.perf_counter() - started)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path(__file__).with_name("estimate_checks.json"))
    args = parser.parse_args()
    started = time.perf_counter()
    geometries = [Geometry(B, R, 2.0) for B in (2, 3, 4, 5) for R in (3, 5, 7)]
    geometries += [Geometry(4, 5, 1.0, 1.5), Geometry(4, 5, 3.0, 0.5)]
    checks = [geometry_checks(g) for g in geometries]
    flat = [row for check in checks for row in check["collars"]]
    summary = dict(geometries=len(checks), collar_cases=len(flat),
                   channel_measurements=3 * len(flat),
                   failures=sum(len(check["failures"]) for check in checks),
                   max_mean_finite_ratio=max(row["mean_ratio_finite"] for row in flat),
                   max_mean_uniform_ratio=max(row["mean_ratio_uniform"] for row in flat),
                   max_family_finite_ratio=max(row["family_ratio_finite"] for row in flat),
                   max_family_uniform_ratio=max(row["family_ratio_uniform"] for row in flat),
                   max_moments_finite_ratio=max(row["moments_ratio_finite"] for row in flat),
                   max_moments_uniform_ratio=max(row["moments_ratio_uniform"] for row in flat),
                   seconds=time.perf_counter() - started)
    payload = dict(status="numerical consistency checks, not formal proof or error certification",
                   versions=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__),
                   source_sha256={name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                  for name in ("ufbi_control.py", "gaussian_bounds.py", "test_gaussian_bounds.py")},
                   summary=summary, checks=checks)
    args.out.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    if summary["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
