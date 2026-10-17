"""Worked example: the synchronous product of two small labelled transition systems.

Two two-state machines are built, each looping on one private action and one
shared action ``a``. Their synchronous product couples the two machines on the
shared action, so the product only has ``a`` transitions; the private actions
``b`` and ``c`` are dropped because they are not in the intersection of the
action sets.
"""

from __future__ import annotations

from notes_process_modelling.lts import LTS


def build_lts1() -> LTS:
    """The first two-state machine, with actions ``a`` and ``b``."""
    S1 = ["s1", "s2"]
    A1 = ["a", "b"]
    transitions1 = {"s1": {"a": "s2", "b": "s1"}, "s2": {"a": "s1", "b": "s2"}}
    return LTS(S1, A1, transitions1, "s1", ["s2"])


def build_lts2() -> LTS:
    """The second two-state machine, with actions ``a`` and ``c``."""
    S2 = ["s3", "s4"]
    A2 = ["a", "c"]
    transitions2 = {"s3": {"a": "s4", "c": "s3"}, "s4": {"a": "s3", "c": "s4"}}
    return LTS(S2, A2, transitions2, "s3", ["s4"])


def synchronous_product_demo() -> LTS:
    """Return ``build_lts1() * build_lts2()``."""
    return build_lts1() * build_lts2()


def main() -> None:
    """Build the two machines and print the properties of their product."""
    product_lts = synchronous_product_demo()

    print(product_lts.S)
    print(product_lts.A)
    print(product_lts.transitions)
    print(product_lts.initial_state)
    print(product_lts.accepting_states)


if __name__ == "__main__":
    main()
