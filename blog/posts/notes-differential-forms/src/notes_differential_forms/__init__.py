"""Tangent-space figures for the *Notes on Differential Forms* post.

The package turns the post's three plotting scripts into importable
functions that draw a tangent space at a point on a curve, or a tangent vector
drawn against the differential axes:

* :func:`notes_differential_forms.tangent_space_cubic.plot_tangent_space_cubic`
* :func:`notes_differential_forms.tangent_space_quadratic.plot_tangent_space_quadratic`
* :func:`notes_differential_forms.tangent_space_axes.plot_tangent_space_axes`
"""

from __future__ import annotations

from notes_differential_forms.tangent_space_axes import plot_tangent_space_axes
from notes_differential_forms.tangent_space_cubic import plot_tangent_space_cubic
from notes_differential_forms.tangent_space_quadratic import (
    plot_tangent_space_quadratic,
)

__all__ = [
    "plot_tangent_space_axes",
    "plot_tangent_space_cubic",
    "plot_tangent_space_quadratic",
]

__version__ = "0.1.0"
