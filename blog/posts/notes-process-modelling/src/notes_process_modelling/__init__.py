"""Labelled transition systems and their synchronous product.

The public helpers live in :mod:`notes_process_modelling.lts` and
:mod:`notes_process_modelling.example`:

* :class:`notes_process_modelling.lts.LTS` is a labelled transition system with
  an overloaded ``*`` operator that computes the synchronous product.
* :func:`notes_process_modelling.example.synchronous_product_demo` builds the
  two-machine worked example used in the blog post.
"""

from __future__ import annotations

from notes_process_modelling.example import (
    build_lts1,
    build_lts2,
    synchronous_product_demo,
)
from notes_process_modelling.lts import LTS

__all__ = [
    "LTS",
    "build_lts1",
    "build_lts2",
    "synchronous_product_demo",
]

__version__ = "0.1.0"
