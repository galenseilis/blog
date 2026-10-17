# chatgpt-plot-covering-diagram

ChatGPT's attempt at plotting the covering diagram of a partial order.

This package is the code from the blog post
[Asking ChatGPT to Code a Plotting Function for Covering Diagrams](https://galenseilis.github.io/blog/posts/chatgpt-plot-covering-diagram/).
It packages the function the model wrote, together with the two graphs the
post uses to exercise it: the full worked example and the smaller case that
the author uses to show the code does not actually produce a correct covering
diagram. The package is a faithful record of the attempt, not a corrected
covering-diagram implementation.

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/chatgpt-plot-covering-diagram"
```

Requires Python 3.11 or newer, and depends on `networkx` and `matplotlib`.

## Quick start

```python
import networkx as nx

from chatgpt_plot_covering_diagram import covering_diagram

dg = nx.DiGraph()
dg.add_edges_from([("a", "b"), ("a", "c"), ("b", "d")])
ax = covering_diagram(dg)          # draw on a new figure
ax.figure.savefig("covering.png")  # or save it yourself
```

The two examples from the post are also available:

```python
from chatgpt_plot_covering_diagram.full_example import full_example
from chatgpt_plot_covering_diagram.failing_example import failing_example

full_example("figures/chatgpt_cover_relation_plotter_output.png")
failing_example("figures/chatgpt_cover_relation_plotter_output_test.png")
```

or from the console:

```bash
chatgpt-plot-covering-diagram   # writes figures/chatgpt_cover_relation_plotter_output.png
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
