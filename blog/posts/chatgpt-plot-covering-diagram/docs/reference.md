# API reference

## `chatgpt_plot_covering_diagram.covering.covering_diagram(dg, ax=None)`

Plot the directed graph according to the rules of a covering diagram.

- `dg` (`networkx.DiGraph`): the partial order to draw. Nodes are positioned
  one per level along `networkx.topological_sort`, and the edges the function
  treats as covering relations are drawn in red.
- `ax` (`matplotlib.axes.Axes`, optional): the axes to draw on; a new figure
  is created when omitted.

Returns the `matplotlib.axes.Axes` the graph was drawn on.

```python
from chatgpt_plot_covering_diagram import covering_diagram
```

## `chatgpt_plot_covering_diagram.full_example.full_example(output="figures/chatgpt_cover_relation_plotter_output.png")`

Draw the full worked example partial order from the post and save it.

- `output` (`str` or `pathlib.Path`): destination of the rendered PNG. Parent
  directories are created.

Returns the `pathlib.Path` that was written.

## `chatgpt_plot_covering_diagram.full_example.main()`

Console-script entry point. Calls `full_example()` with the default output.

## `chatgpt_plot_covering_diagram.failing_example.failing_example(output="figures/chatgpt_cover_relation_plotter_output_test.png")`

Draw the smaller partial order the post uses as a failing test case and save
it. Returns the `pathlib.Path` that was written.

## Console scripts

| Command | Writes |
| --- | --- |
| `chatgpt-plot-covering-diagram` | `figures/chatgpt_cover_relation_plotter_output.png` |
