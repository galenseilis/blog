"""SymPy compound distributions.

The public entry point is :func:`sympy_compound_distributions.compound.compound_distribution`,
which builds the ``N ~ Normal(X, L)`` model from the blog post, where the mean
``X`` and the scale ``L`` are themselves random variables.
"""

from __future__ import annotations

from sympy_compound_distributions.compound import compound_distribution

__all__ = ["__version__", "compound_distribution"]

__version__ = "0.1.0"
