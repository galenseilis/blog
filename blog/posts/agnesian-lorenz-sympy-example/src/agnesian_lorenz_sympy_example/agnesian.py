"""Compute Agnesian order 1 for the Lorenz system with SymPy."""

from __future__ import annotations

from sympy import Function, Symbol, latex, prod


def agnesian_lorenz_order1() -> str:
    """Return the LaTeX string for A_t^1 for the Lorenz system.

    Returns
    -------
    str
        LaTeX representation of the Agnesian of order one.
    """
    sigma = Symbol("\\sigma", real=True)
    rho = Symbol("\\rho", real=True)
    beta = Symbol("\\beta", real=True)
    t = Symbol("t", real=True)

    x = Function("x")(t)
    y = Function("y")(t)
    z = Function("z")(t)

    v = [sigma * (y - x), x * (rho - z - y), x * y - beta * z]
    dvdt = [i.diff(t) for i in v]
    return latex(prod(dvdt))
