"""CLI for script 2."""

from __future__ import annotations

import sys

from permutive_cross_product.permutive import find_4perm_cross_products


def main() -> int:
    df = find_4perm_cross_products(dim=3, max_results=10)
    print(df.to_markdown(index=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
