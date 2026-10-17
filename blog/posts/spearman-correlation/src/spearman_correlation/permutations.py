"""Tabulate the possible rank permutations of a sample.

With four continuous observations there is zero probability of tied ranks, so
every sample realises one of the ``4! = 24`` permutations of ``(1, 2, 3, 4)``.
This module lists them and renders the Markdown table quoted in the post.
"""

from __future__ import annotations

from itertools import permutations

import pandas as pd


def rank_permutations(n: int = 4) -> list[tuple[int, ...]]:
    """Return every permutation of ``(1, ..., n)`` as a tuple."""
    return list(permutations(range(1, n + 1)))


def rank_columns(n: int = 4) -> list[str]:
    """Return the LaTeX column labels used in the post's table."""
    return [f"$\\operatorname{{rank}}(X_{i})$" for i in range(1, n + 1)]


def permutation_table(n: int = 4) -> str:
    """Render the rank permutations of ``n`` observations as Markdown."""
    frame = pd.DataFrame(data=rank_permutations(n), columns=rank_columns(n))
    return frame.to_markdown(index=False)


def main() -> None:
    """Console-script entry point: print the permutation table."""
    print(permutation_table())


if __name__ == "__main__":
    main()
