"""Model for minimal von Mises example."""

from __future__ import annotations

import numpy as np
import pymc as pm


def build_model(observed: np.ndarray | None = None) -> pm.Model:
    """Build the von Mises model."""
    if observed is None:
        observed = np.array([-2] * 10 + [2] * 10)

    model = pm.Model()
    with model:
        kappa = pm.Exponential("kappa", lam=1)
        mu = pm.Uniform("mu", lower=-np.pi, upper=np.pi)
        pm.VonMises("theta", mu=mu, kappa=kappa, observed=observed)
    return model
