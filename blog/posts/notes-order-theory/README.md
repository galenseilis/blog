# notes-order-theory

Figures and helpers from notes on order theory.

This package is the code from the blog post
[Notes on Order Theory](https://galenseilis.github.io/blog/posts/notes-order-theory/).
It turns the post's three snippets into importable functions:

- `plot_example_partial_order` draws the digraph of the example partial order
  on `{a, b, c, d, e}`.
- `plot_cover_diagram` draws the cover diagram of the example strict partial
  order.
- `latex_pairs` formats every ordered pair of a finite set for use in LaTeX.

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/notes-order-theory"
```

Requires Python 3.11 or newer, and depends on `matplotlib` and `networkx`.

## Quick start

```python
from notes_order_theory import plot_cover_diagram

plot_cover_diagram("figures/cover_diagram.png")
```

Format the ordered pairs of a set:

```python
from notes_order_theory import latex_pairs

print(latex_pairs(("a", "b", "c", "d", "e")))
```

Render every figure from the post:

```bash
notes-order-theory   # writes both figures into figures/
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
