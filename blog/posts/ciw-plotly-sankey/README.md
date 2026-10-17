# ciw-plotly-sankey

Plotting Ciw's cafe example as a Sankey diagram using Plotly.

A Sankey diagram is a good way to show what *actually happened* in a
discrete-event simulation: rather than the routing you think you specified, it
shows how many customers took each path. This package runs Ciw's cafe example,
turns the records table into a table of flows between nodes, and draws those
flows as a Plotly Sankey diagram.

This package is the code from the blog post
[Plotting Ciw's Café Example As A Sankey Diagram Using Plotly](https://galenseilis.github.io/blog/posts/ciw-plotly-sankey/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ciw-plotly-sankey"
```

Requires Python 3.11 or newer, and depends on `ciw`, `pandas`, and `plotly`.

## Quick start

```python
from ciw_plotly_sankey import render

fig = render.build_diagram()
fig.show()
```

Run the console script to print the diagram as an embeddable HTML fragment:

```bash
ciw-plotly-sankey
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
