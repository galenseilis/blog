# Tutorial

This tutorial runs the cafe example and draws it as a Sankey diagram.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ciw-plotly-sankey"
```

## 2. Run the model

```python
from ciw_plotly_sankey import network

simulation = network.run_simulation()
recs = network.get_records(simulation)
recs[["id_number", "node", "destination"]].head()
```

## 3. Build the link table

Three transforms turn the records into flows: count arrivals, count edge flows,
then stack and sort them.

```python
from ciw_plotly_sankey import render

links = render.prepare_links(recs)
links
```

`links` has columns `node`, `destination`, and `flow`. The arrival-node flows
have `node == 0`; a destination of `4` means the exit node.

## 4. Draw and render

```python
from ciw_plotly_sankey.figure import build_figure
from ciw_plotly_sankey.render import style_figure, to_html

fig = style_figure(build_figure(links))
fig.show()
```

To get an embeddable fragment instead:

```python
html = to_html(fig)
```

The console script does the whole pipeline and prints the HTML:

```bash
ciw-plotly-sankey
```

You now know the whole workflow. Next, read the
[how-to guides](how-to-guides.md) to apply it to your own model.
