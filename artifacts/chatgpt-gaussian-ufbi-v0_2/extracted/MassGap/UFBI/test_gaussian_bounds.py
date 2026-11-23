"""Numerical regressions for the Gaussian estimates, not formal verification."""
import math
import unittest

import numpy as np
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import splu

from ufbi_control import GaussianBox, Geometry
from gaussian_bounds import (bounds, channel_covariance, decay_parameters,
                             geometry_checks, mean_boundary_coefficients,
                             mean_variance_bounds, sine_channel, moment_channel,
                             moment_covariance_trial)


class TestGaussianBounds(unittest.TestCase):
    def test_dispersion_and_uniform_rate(self):
        for B in (2, 3, 10, 100):
            g = Geometry(B, 3, 2.0)
            kappa, rho, gamma = decay_parameters(g)
            self.assertAlmostEqual(2 * (math.cosh(kappa) - 1), g.m0**2, places=13)
            self.assertGreaterEqual(rho + 1e-14, gamma)
            self.assertLess(rho, g.mass)
        with self.assertRaises(ValueError):
            decay_parameters(Geometry(1, 3, 2.0))

    def test_sine_overlap_and_variance_constants(self):
        for B in range(1, 101):
            alpha = math.pi / (2 * (B + 1))
            r = 2 / (math.tan(alpha)**2 * B * (B + 1))
            self.assertGreaterEqual(r + 1e-13, 8 / math.pi**2)
            finite, uniform = mean_variance_bounds(Geometry(B, 3, 2))
            self.assertGreaterEqual(finite + 1e-13, uniform)

    def test_sine_normalization_and_independent_covariance(self):
        g = Geometry(2, 3, 2.0)
        box = GaussianBox(g)
        F = sine_channel(g)
        np.testing.assert_allclose((F @ F.T) / g.a**2, np.eye(5), atol=2e-15)
        n = g.L
        d = diags([-np.ones(n - 1), 2 * np.ones(n), -np.ones(n - 1)], [-1, 0, 1])
        a = g.m0**2 * eye(n**4, format="csc")
        for ax in range(4):
            blocks = [d if i == ax else eye(n) for i in range(4)]
            term = blocks[0]
            for block in blocks[1:]:
                term = kron(term, block, format="csc")
            a = a + term
        embedded = np.stack([box.embed(row).ravel() for row in F])
        direct = embedded @ splu(a.tocsc()).solve(embedded.T)
        np.testing.assert_allclose(channel_covariance(box, F), direct, atol=1e-12, rtol=1e-12)
        eigmin = float(np.linalg.eigvalsh(direct)[0])
        self.assertGreaterEqual(eigmin, 1 / bounds(g)["family_lambda"])

    def test_mean_worst_case_and_boundary_corners(self):
        g = Geometry(2, 3, 2.0)
        box = GaussianBox(g)
        coeff = mean_boundary_coefficients(box)
        self.assertTrue(np.all(coeff >= -1e-14))
        self.assertEqual(coeff.size, 8 * g.L**3)
        source = box.source("constant", 1)
        self.assertAlmostEqual(source[0, 0, 0, 0], 8 * g.a)
        h = box.mean_shift(source)
        self.assertAlmostEqual(float(h.mean() / g.a), 2 * float(coeff.sum()), places=13)
        for seed in range(3):
            shifted = box.mean_shift(box.source("random", 1, seed))
            self.assertLessEqual(abs(float(shifted.mean() / g.a)), 2 * float(coeff.sum()) + 1e-13)

    def test_moment_pairing_and_covariance_lower_matrix(self):
        for B in (2, 3, 5):
            g = Geometry(B, 3, 2)
            F, S = moment_channel(g), sine_channel(g)
            np.testing.assert_allclose(F @ F.T / g.a**2,
                                       np.diag([1] + [1 - B**-2] * 4), atol=3e-15)
            pairing = F @ S.T / g.a**2
            self.assertGreaterEqual(float(np.linalg.svd(pairing, compute_uv=False)[-1]),
                                    32 * math.sqrt(3) / math.pi**4)
            cov = channel_covariance(GaussianBox(g), F)
            self.assertGreaterEqual(float(np.linalg.eigvalsh(cov - moment_covariance_trial(g))[0]),
                                    -1e-12)

    def test_analytic_bounds_on_nondefault_physical_scales(self):
        for g in (Geometry(3, 3, 1, 1.5), Geometry(3, 5, 3, 0.5)):
            self.assertEqual(geometry_checks(g)["failures"], [])

    def test_zero_amplitude_and_linear_scaling(self):
        g = Geometry(3, 3, 2)
        b1 = bounds(g, amplitude=1)
        b2 = bounds(g, amplitude=2)
        for key in ("mean_d_finite", "mean_d_uniform", "family_d_finite", "family_d_uniform",
                    "moments_d_finite", "moments_d_uniform"):
            self.assertEqual(b2[key], 2 * b1[key])
        zero = geometry_checks(g, amplitude=0)
        self.assertEqual(zero["failures"], [])
        self.assertTrue(all(row["mean_d"] == row["family_d"] == 0 for row in zero["collars"]))


if __name__ == "__main__":
    unittest.main()
