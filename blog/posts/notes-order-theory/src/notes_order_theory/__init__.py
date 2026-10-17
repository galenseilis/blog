"""Order-theory figures and helpers from the *Notes on Order Theory* post.

The package turns the post's three snippets into importable functions:

* :func:`notes_order_theory.partial_order.plot_example_partial_order` draws the
  digraph representation of the example partial order.
* :func:`notes_order_theory.cover_diagram.plot_cover_diagram` draws its cover
  diagram.
* :func:`notes_order_theory.latex_pairs.latex_pairs` formats every ordered pair
  of a finite set for use in LaTeX.
"""

from __future__ import annotations

from notes_order_theory.cover_diagram import (
    COVER_EDGES,
    COVER_POSITIONS,
    build_cover_graph,
    plot_cover_diagram,
)
from notes_order_theory.latex_pairs import latex_pairs
from notes_order_theory.partial_order import (
    EXAMPLE_ORDER,
    build_digraph,
    plot_example_partial_order,
)

__all__ = [
    "COVER_EDGES",
    "COVER_POSITIONS",
    "EXAMPLE_ORDER",
    "build_cover_graph",
    "build_digraph",
    "latex_pairs",
    "plot_cover_diagram",
    "plot_example_partial_order",
]

__version__ = "0.1.0"
