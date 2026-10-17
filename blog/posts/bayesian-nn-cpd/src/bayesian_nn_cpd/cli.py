"""CLI entry point."""

from __future__ import annotations

import pickle
import sys
from pathlib import Path

import pymc as pm

from bayesian_nn_cpd.model import build_model, simulate_data


def main(output_path: str | Path = "test.pickle", cores: int = 1) -> int:
    """Run a small sample and save inference results."""
    observed, size = simulate_data(size=3)
    model = build_model(size=size, observed=observed)

    with model:
        idata = pm.sample(cores=cores, tune=10, draws=10, progressbar=False)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("wb") as handle:
        pickle.dump(idata, handle)
    return 0


if __name__ == "__main__":
    sys.exit(main())
