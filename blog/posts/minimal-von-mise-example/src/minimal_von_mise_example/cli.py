"""CLI entry point."""

from __future__ import annotations

import sys

import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc as pm

from minimal_von_mise_example.model import build_model


def main() -> int:
    """Run sampling and plot trace."""
    observed = np.array([-2] * 10 + [2] * 10)
    model = build_model(observed=observed)

    with model:
        data = pm.sample(chains=2, tune=10, draws=10, progressbar=False)
        az.plot_trace(data)
        plt.tight_layout()
        plt.show()
    return 0


if __name__ == "__main__":
    sys.exit(main())
