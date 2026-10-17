# How-to guides

## Print the diagram as HTML

```bash
ciw-plotly-sankey
```

Or from Python:

```python
from ciw_plotly_sankey import render

print(render.to_html(render.build_diagram()))
```

## Reuse the pipeline on another Ciw model

The transforms only need a records table with `id_number`, `node`,
`destination`, and `arrival_date` columns. Replace the network, keep the rest:

```python
from ciw_plotly_sankey import network
from ciw_plotly_sankey.render import prepare_links
from ciw_plotly_sankey.figure import build_figure

simulation = network.run_simulation()
recs = network.get_records(simulation)
fig = build_figure(prepare_links(recs))
```

Be aware that the node labels in `figure.node_labels` and the exit index in
`edge_flows.exit_index` are specific to the cafe example.

## Change the node labels

`figure.build_figure` uses `figure.node_labels`. Set it to match your model's
node indices before building the figure:

```python
from ciw_plotly_sankey import figure

figure.node_labels = ["Arrival", "Cut", "Cook", "Plate", "Exit"]
```

## Change the exit index

`edge_flows.edge_flows` remaps Ciw's `-1` to `exit_index` (default `4`). Pass a
different value if the exit node has another index in your diagram:

```python
from ciw_plotly_sankey.edge_flows import edge_flows

edges = edge_flows(recs, exit_node=5)
```

## Change the seed or run length

```python
from ciw_plotly_sankey import network

simulation = network.run_simulation(simulation_time=500, random_seed=42)
```

## Draw the arrival node explicitly

The arrival node is the synthetic index `0`, contributed by
`first_nodes.first_nodes`. If you do not want it, skip that step and combine
only the edge flows.
