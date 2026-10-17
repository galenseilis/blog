"""Demonstrate the three tuple-class-name cases from the post.

The console script runs the two working networks and then shows the
``TypeError`` raised by the mixed-type network.
"""

from __future__ import annotations

from ciw_tuple_class_names import empty_string, mixed_types, tuple_keys


def main() -> None:
    """Run both working networks, then demonstrate the mixed-type failure."""
    tuple_keys.run_simulation()
    empty_string.run_simulation()
    print("Tuple class names work for consistently-shaped tuples.")

    try:
        mixed_types.build_network()
    except TypeError as exc:
        print(f"Mixed-type tuples raise TypeError: {exc}")


if __name__ == "__main__":
    main()
