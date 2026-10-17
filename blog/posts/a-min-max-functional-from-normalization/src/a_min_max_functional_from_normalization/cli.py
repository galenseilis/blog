"""CLI entry point."""

from __future__ import annotations

import sys

from a_min_max_functional_from_normalization.functional import generate_functional_table


def main() -> int:
    """Print the markdown table to stdout."""
    df = generate_functional_table()
    print(df.to_markdown(index=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
