"""Represent a compound distribution in SymPy.

A compound distribution has random parameters: the mean and the scale of ``N``
are themselves random variables.
"""

from __future__ import annotations

from sympy.stats import Exponential, Normal
from sympy.stats.compound_rv import CompoundDistribution
from sympy.stats.crv_types import NormalDistribution


def compound_distribution() -> CompoundDistribution:
    """Build the compound distribution used in the post.

    Returns the ``CompoundDistribution`` for

    .. math::

        X \\sim \\mathrm{Normal}(2, 4), \\quad
        L \\sim \\mathrm{Exponential}(100), \\quad
        N \\sim \\mathrm{Normal}(X, L).
    """
    X = Normal("X", 2, 4)
    L = Exponential("L", 100)
    N = NormalDistribution(X, L)
    return CompoundDistribution(N)


def main() -> None:
    """Console-script entry point: build the compound distribution."""
    print(compound_distribution())


if __name__ == "__main__":
    main()
