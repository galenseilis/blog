"""Format every ordered pair of a finite set for use in LaTeX.

For a ground set ``X`` the full Cartesian product ``X x X`` has ``|X|**2``
ordered pairs, which is tedious to write out by hand. This module generates
them and renders the set in LaTeX set-builder syntax.
"""

from __future__ import annotations

from collections.abc import Iterable
from itertools import product


def latex_pairs(elements: Iterable[str]) -> str:
    """Return the LaTeX source for every ordered pair of ``elements``.

    The result is a single line such as
    ``\\{(a, a), (a, b), ..., (e, e)\\}`` with the escape sequences needed to
    typeset the curly braces in LaTeX.

    Parameters
    ----------
    elements : iterable of str
        The ground set, e.g. ``("a", "b", "c", "d", "e")``.

    Returns
    -------
    str
        LaTeX set notation for ``X x X``.
    """
    pairs = ["(" + ", ".join(pair) + ")" for pair in product(elements, elements)]
    pairs = sorted(pairs)
    text = str(pairs).replace("'", "")
    text = text.replace("[", "\\\\{")
    text = text.replace("]", "\\\\}")
    return text


def main() -> None:
    """Console-script entry point: print the pairs for ``{a, b, c, d, e}``."""
    print(latex_pairs(("a", "b", "c", "d", "e")))


if __name__ == "__main__":
    main()
