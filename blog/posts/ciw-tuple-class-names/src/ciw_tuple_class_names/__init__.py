"""Using tuples as customer-class names in Ciw.

The public modules are:

* :mod:`ciw_tuple_class_names.tuple_keys` -- the working two-class network
  whose class names are ``("Baby", 0)`` and ``("Child", 1)``.
* :mod:`ciw_tuple_class_names.mixed_types` -- a network whose class names mix
  ``str``- and ``int``-first tuples and therefore raise ``TypeError``.
* :mod:`ciw_tuple_class_names.empty_string` -- the fix: pad the names so every
  tuple has the same length and position-wise types.
"""

from __future__ import annotations

from ciw_tuple_class_names import empty_string, mixed_types, tuple_keys

__all__ = ["empty_string", "mixed_types", "tuple_keys"]

__version__ = "0.1.0"
