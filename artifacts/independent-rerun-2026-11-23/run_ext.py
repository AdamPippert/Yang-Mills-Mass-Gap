"""Rerun of the Gemini Gaussian UFBI check, extended to B = 10.

Usage, from this directory:  OPENBLAS_NUM_THREADS=1 python run_ext.py
Needs NumPy and SciPy. See ENVIRONMENT.txt for the versions used.
"""
import importlib.util
import pathlib

script = pathlib.Path(__file__).resolve().parents[2] / "sources" / "gemini" / "G1_gaussian_ufbi_check.py"
spec = importlib.util.spec_from_file_location("g", script)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

g.run_sweep(R=3, m_ell=6.0, B_values=(1, 2, 3, 4, 5, 6, 8, 10))
print()
g.run_sweep(R=3, m_ell=12.0, B_values=(1, 2, 3, 4, 5, 6, 8, 10))
