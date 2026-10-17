"""Print a table of rank transforms for a sample of a binomial variable.

The binomial is a convenient illustration because integer samples produce ties,
and the various methods in :func:`scipy.stats.rankdata` disagree on how to rank
them. Continuous samples are almost surely tie-free, so every method would
agree there.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence

import numpy as np
import pandas as pd
from scipy.stats import rankdata

METHODS: tuple[str, ...] = ("average", "min", "max", "dense", "ordinal")
"""The :func:`scipy.stats.rankdata` methods compared in the post."""

DEFAULT_SEED = 2018
"""Seed used so the table in the post is reproducible."""


def rank_table(
    sample: Sequence[float],
    methods: Iterable[str] = METHODS,
) -> pd.DataFrame:
    """Return the sample and its ranks under each method, sorted by the sample."""
    data: dict[str, object] = {"x": np.asarray(sample)}
    for method in methods:
        data[f"{method} method"] = rankdata(data["x"], method=method)
    frame = pd.DataFrame(data)
    return frame.sort_values(by="x")


def sample_binomial(
    seed: int | None = DEFAULT_SEED,
    size: int = 10,
    trials: int = 10,
    p: float = 0.5,
) -> np.ndarray:
    """Return a reproducible sample from a binomial random variable."""
    np.random.seed(seed)
    return np.random.binomial(trials, p, size=size)


def main() -> None:
    """Console-script entry point: print the rank comparison table."""
    print(rank_table(sample_binomial()).to_string(index=False))


if __name__ == "__main__":
    main()
