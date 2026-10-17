"""Mixed-type tuples fail: tuples must be mutually orderable.

Ciw sorts its class names, so a ``str``-first tuple such as ``("Baby", 0)``
cannot coexist with an ``int``-first tuple such as ``(1,)``. Python's
lexicographic comparison hits the first differing element, finds ``"Baby"``
against ``1``, and raises ``TypeError: '<' not supported between instances of
'int' and 'str'``. This module builds exactly that broken network so the
failure can be demonstrated and tested.
"""

from __future__ import annotations

import ciw


def build_network() -> ciw.network.Network:
    """Build the network whose mixed-type class names make Ciw raise.

    Returns
    -------
    ciw.network.Network
        This function never returns: sorting the class names raises
        ``TypeError`` before a network can be constructed.
    """
    return ciw.create_network(
        arrival_distributions={
            ("Baby", 0): [
                ciw.dists.Exponential(rate=1.0),
                None,
                None,
            ],
            (1,): [
                ciw.dists.Exponential(rate=2.0),
                None,
                None,
            ],
        },
        service_distributions={
            ("Baby", 0): [
                ciw.dists.Exponential(rate=4.0),
                ciw.dists.Exponential(rate=1.0),
                ciw.dists.Deterministic(value=0.0),
            ],
            (1,): [
                ciw.dists.Exponential(rate=6.0),
                ciw.dists.Deterministic(value=0.0),
                ciw.dists.Exponential(rate=1.0),
            ],
        },
        routing={
            ("Baby", 0): [
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
            (1,): [
                [0.0, 0.0, 1.0],
                [0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0],
            ],
        },
        number_of_servers=[1, 2, 3],
    )


def main() -> None:
    """Attempt the broken build and report the resulting ``TypeError``."""
    try:
        build_network()
    except TypeError as exc:
        print(f"TypeError: {exc}")


if __name__ == "__main__":
    main()
