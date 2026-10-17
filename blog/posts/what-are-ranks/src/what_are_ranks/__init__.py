"""Rank transforms of a sample.

The public helper is :func:`what_are_ranks.rank_table.rank_table`, which returns
a :class:`pandas.DataFrame` with one column per ``scipy.stats.rankdata`` method.
"""

from __future__ import annotations

from what_are_ranks.rank_table import METHODS, rank_table, sample_binomial

__all__ = ["METHODS", "__version__", "rank_table", "sample_binomial"]

__version__ = "0.1.0"
