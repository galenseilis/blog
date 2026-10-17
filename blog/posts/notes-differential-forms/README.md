# notes-differential-forms

Tangent-space figures for notes on differential forms.

This package is the code from the blog post
[Notes on Differential Forms](https://galenseilis.github.io/blog/posts/notes-differential-forms/).
It turns the post's three plotting scripts into importable functions:

- `plot_tangent_space_cubic` draws the tangent space to the cubic
  `y = x**3 - 10x` at `(2, -12)`.
- `plot_tangent_space_quadratic` draws the tangent space to the parabola
  `y = x**2` at `(1, 1)`.
- `plot_tangent_space_axes` draws a tangent vector against the differential
  axes `dx` and `dy`.

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/notes-differential-forms"
```

Requires Python 3.11 or newer, and depends on `matplotlib` and `numpy`.

## Quick start

```python
from notes_differential_forms import plot_tangent_space_cubic

plot_tangent_space_cubic("figures/tangent_space_cubic.png")
```

Render every figure from the post in one call:

```python
from notes_differential_forms.figures import render_all

render_all("figures")
```

or from the console:

```bash
notes-differential-forms   # writes all three figures into figures/
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
