"""CLI entry points."""

from __future__ import annotations

import sys

from agnesian_lorenz_sympy_example.agnesian import agnesian_lorenz_order1


def main() -> int:
    """Print the LaTeX string to stdout.

    Returns
    -------
    int
        Exit code (always 0).
    """
    print(agnesian_lorenz_order1())
    return 0


if __name__ == "__main__":
    sys.exit(main())
