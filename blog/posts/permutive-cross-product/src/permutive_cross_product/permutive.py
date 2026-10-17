"""Permutive cross product computations."""

from __future__ import annotations

import itertools

import pandas as pd
import sympy as sp
from sympy import latex


def find_permutive_cross_products(dim: int = 3) -> list[sp.Matrix]:
    """Find nonzero cross-like vectors orthogonal to a,b using single permutation.

    Returns list of SymPy matrices (column vectors).
    """
    a = sp.Matrix([sp.Symbol(f"a{i + 1}") for i in range(dim)])
    b = sp.Matrix([sp.Symbol(f"b{i + 1}") for i in range(dim)])
    zero_vec = sp.Matrix([[0]] * dim)

    results: list[sp.Matrix] = []
    for perm in itertools.permutations(range(dim)):
        P = sp.eye(dim)[perm, :]
        cross = (P * a).multiply_elementwise(P.T * b) - (
            P.T * a
        ).multiply_elementwise(P * b)
        if (
            cross.dot(a).simplify() == 0
            and cross.dot(b).simplify() == 0
            and cross != zero_vec
        ):
            results.append(cross)
    return results


def find_4perm_cross_products(dim: int = 3, max_results: int | None = None) -> pd.DataFrame:
    """Find orthogonal vectors using four permutations."""
    a = sp.Matrix([sp.Symbol(f"a{i + 1}") for i in range(dim)])
    b = sp.Matrix([sp.Symbol(f"b{i + 1}") for i in range(dim)])
    zero_vec = sp.Matrix([[0]] * dim)

    results: list[list[str]] = []
    count = 0
    perms = list(itertools.permutations(range(dim)))
    for perm1 in perms:
        for perm2 in perms:
            for perm3 in perms:
                for perm4 in perms:
                    P1 = sp.eye(dim)[perm1, :]
                    P2 = sp.eye(dim)[perm2, :]
                    P3 = sp.eye(dim)[perm3, :]
                    P4 = sp.eye(dim)[perm4, :]
                    cross = (P1 * a).multiply_elementwise(P2 * b) - (
                        P3 * a
                    ).multiply_elementwise(P4 * b)
                    if (
                        cross.dot(a).simplify() == 0
                        and cross.dot(b).simplify() == 0
                        and cross != zero_vec
                    ):
                        results.append(
                            [
                                f"${latex(P1)}$",
                                f"${latex(P2)}$",
                                f"${latex(P3)}$",
                                f"${latex(P4)}$",
                                f"${latex(cross)}$",
                                f"${latex(cross.dot(a).simplify())}$",
                                f"${latex(cross.dot(b).simplify())}$",
                            ]
                        )
                        count += 1
                        if max_results is not None and count >= max_results:
                            df = pd.DataFrame(
                                results,
                                columns=[
                                    "P1",
                                    "P2",
                                    "P3",
                                    "P4",
                                    "cross",
                                    "cross_dot_a",
                                    "cross_dot_b",
                                ],
                            )
                            return df
    df = pd.DataFrame(
        results,
        columns=[
            "P1",
            "P2",
            "P3",
            "P4",
            "cross",
            "cross_dot_a",
            "cross_dot_b",
        ],
    )
    return df
