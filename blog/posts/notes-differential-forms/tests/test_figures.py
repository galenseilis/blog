import matplotlib

matplotlib.use("Agg")

from notes_differential_forms import (
    plot_tangent_space_axes,
    plot_tangent_space_cubic,
    plot_tangent_space_quadratic,
)
from notes_differential_forms.figures import render_all


def test_plot_tangent_space_cubic_writes_a_png(tmp_path):
    output = tmp_path / "cubic.png"
    written = plot_tangent_space_cubic(output)
    assert written == output
    assert output.exists()
    assert output.stat().st_size > 0


def test_plot_tangent_space_quadratic_writes_a_png(tmp_path):
    output = tmp_path / "quadratic.png"
    written = plot_tangent_space_quadratic(output)
    assert written == output
    assert output.exists()
    assert output.stat().st_size > 0


def test_plot_tangent_space_axes_writes_a_png(tmp_path):
    output = tmp_path / "axes.png"
    written = plot_tangent_space_axes(output)
    assert written == output
    assert output.exists()
    assert output.stat().st_size > 0


def test_render_all_writes_every_post_figure(tmp_path):
    paths = render_all(tmp_path)
    assert [path.name for path in paths] == [
        "tangent_space_cubic.png",
        "tangent_space_quadratic.png",
        "tangent_space_axes.png",
    ]
    assert all(path.exists() for path in paths)


def test_plot_functions_create_parent_directories(tmp_path):
    output = tmp_path / "nested" / "deeper" / "cubic.png"
    plot_tangent_space_cubic(output)
    assert output.exists()
