"""Fokker-Planck and analytic solutions of the Ornstein-Uhlenbeck moose model.

The public helpers live in :mod:`moose_ou_fp.fokker_planck`:

* :func:`moose_ou_fp.fokker_planck.solve_fokker_planck` integrates the 1D
  Fokker-Planck equation on a grid with a finite-volume scheme.
* :func:`moose_ou_fp.fokker_planck.analytic_variance` and
  :func:`moose_ou_fp.fokker_planck.analytic_pdf` give the closed-form OU
  transition density.
* :func:`moose_ou_fp.fokker_planck.run` reproduces the figure in the blog post.
"""

from __future__ import annotations

from moose_ou_fp.fokker_planck import (
    CENTRE,
    KAPPA,
    SIGMA,
    T_END,
    analytic_pdf,
    analytic_variance,
    diagnostics,
    solve_fokker_planck,
    stationary_sd,
)

__all__ = [
    "CENTRE",
    "KAPPA",
    "SIGMA",
    "T_END",
    "analytic_pdf",
    "analytic_variance",
    "diagnostics",
    "solve_fokker_planck",
    "stationary_sd",
]

__version__ = "0.1.0"
