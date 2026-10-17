"""Agnesian (order 1) computation for the Lorenz system via SymPy.

This package extracts the small script from the blog post into an importable
library and a small CLI. The core computation is pure SymPy, and the
CLI just prints the LaTeX string so that stdout matches what the post
quotes.
"""

from __future__ import annotations

__all__ = [
    "agnesian_lorenz_order1",
    "main",
]

__version__ = "0.1.0"
