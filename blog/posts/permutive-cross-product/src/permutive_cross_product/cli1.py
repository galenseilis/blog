"""CLI for script 1."""

from __future__ import annotations

import sys

import sympy as sp

from permutive_cross_product.permutive import find_permutive_cross_products


def main() -> int:
    for cross in find_permutive_cross_products(dim=3):
        print(sp.latex(cross))
    return 0


if __name__ == "__main__":
    sys.exit(main())
