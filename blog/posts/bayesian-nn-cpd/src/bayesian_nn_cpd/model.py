"""Model construction for toy Bayesian CPD."""

from __future__ import annotations

import numpy as np
import pymc as pm
from pytensor import tensor as at


def simulate_data(size: int = 3) -> tuple[np.ndarray, int]:
    """Simulate prior-predictive data for the toy example."""
    rng = np.random.default_rng(0)
    u1 = rng.exponential(0.001, size=size)
    u2 = rng.exponential(0.001, size=size)
    u3 = rng.exponential(0.001, size=size)
    x = np.outer(u1, u2)
    x = np.outer(x, u3).reshape((size,) * 3).flatten()
    return x, size


def build_model(size: int = 3, observed: np.ndarray | None = None) -> pm.Model:
    """Build and return the PyMC model."""
    model = pm.Model()
    if observed is None:
        observed, _ = simulate_data(size)

    with model:
        u1 = pm.Exponential("u1", lam=1, size=size)
        u2 = pm.Exponential("u2", lam=1, size=size)
        u3 = pm.Exponential("u3", lam=1, size=size)
        mu = at.outer(at.outer(u1, u2), u3).flatten()

        pm.Exponential("X", mu, shape=observed.size, observed=observed)
    return model
