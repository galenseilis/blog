"""Render every figure used by the *Notes on Order Theory* post."""

from __future__ import annotations

from pathlib import Path

from notes_order_theory.cover_diagram import plot_cover_diagram
from notes_order_theory.partial_order import plot_example_partial_order


def render_all(output_dir: str | Path = "figures") -> list[Path]:
    """Render both post figures into ``output_dir``.

    Returns the list of paths that were written, in the order the post
    presents them.
    """
    output_dir = Path(output_dir)
    return [
        plot_example_partial_order(output_dir / "example_partial_order.png"),
        plot_cover_diagram(output_dir / "cover_diagram.png"),
    ]


def main() -> None:
    """Console-script entry point: render every figure."""
    for path in render_all():
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
