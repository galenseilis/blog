"""Numerical solvers for general Fokker-Planck models of animal movement.

The public modules are:

* :mod:`moose_fp.general_fp_2d`: the full general equation on a two-dimensional
  landscape with a habitat potential, a river barrier, a diffusion field, and
  an optional nonlocal interaction term.
* :mod:`moose_fp.beyond_gaussian_fp`: three one-dimensional repairs of the
  Ornstein-Uhlenbeck model, namely fractional diffusion, nonlocal attraction,
  and behavioural states.
* :mod:`moose_fp.numerics`: small shared finite-volume helpers.

The code accompanies the blog post
`A General Fokker-Planck Model of Moose Movement
<https://galenseilis.github.io/blog/posts/general-fokker-planck-moose-movement/>`_.
"""

from __future__ import annotations

from moose_fp.numerics import total_variation

__all__ = ["total_variation"]

__version__ = "0.1.0"
