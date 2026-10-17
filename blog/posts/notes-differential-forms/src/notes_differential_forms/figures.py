"""Render every figure used by the *Notes on Differential Forms* post."""

from __future__ import annotations

from pathlib import Path

from notes_differential_forms.tangent_space_axes import plot_tangent_space_axes
from notes_differential_forms.tangent_space_cubic import plot_tangent_space_cubic
from notes_differential_forms.tangent_space_quadratic import (
    plot_tangent_space_quadratic,
)


def render_all(output_dir: str | Path = "figures") -> list[Path]:
    """Render all three tangent-space figures into ``output_dir``.

    Returns the list of paths that were written, in the order they appear in
    the post.
    """
    output_dir = Path(output_dir)
    return [
        plot_tangent_space_cubic(output_dir / "tangent_space_cubic.png"),
        plot_tangent_space_quadratic(output_dir / "tangent_space_quadratic.png"),
        plot_tangent_space_axes(output_dir / "tangent_space_axes.png"),
    ]


def main() -> None:
    """Console-script entry point: render every figure."""
    for path in render_all():
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
