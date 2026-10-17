"""Generate the functional table shown in the blog post."""

from __future__ import annotations

from itertools import product
from typing import Callable

import pandas as pd
import sympy as sp


def generate_functional_table() -> pd.DataFrame:
    """Return a DataFrame with (f, g, Functional) as markdown-formatted latex.

    The operations are over F(x), F(a), F(b) as in the original post.
    """
    x = sp.Symbol("x")
    b = sp.Symbol("b")
    a = sp.Symbol("a")
    F = sp.Function("F")
    F_x = F(x)
    F_b = F(b)
    F_a = F(a)

    ops: dict[str, Callable[[sp.Expr, sp.Expr], sp.Expr]] = {
        "add": lambda x_, y_: x_ + y_,
        "subtract": lambda x_, y_: x_ - y_,
        "mult": lambda x_, y_: x_ * y_,
        "divide": lambda x_, y_: x_ / y_,
        "exp": lambda x_, y_: x_**y_,
        "log": lambda x_, y_: sp.log(y_, x_),
    }

    results = []
    for f, g in product(ops, ops):
        result = ops[g](ops[f](F_x, F_a), ops[f](F_b, F_a))
        result = result.simplify()
        results.append([f, g, f"${sp.latex(result)}$"])

    df = pd.DataFrame(results, columns=["f", "g", "Functional"])
    return df
