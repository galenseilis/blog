# API reference

## `ciw_plotly_sankey.network`

| Name | Description |
| --- | --- |
| `seed` | Default random seed, `2018`. |
| `max_time` | Default simulation end time, `200`. |
| `build_network()` | Return the three-node cafe network. |
| `run_simulation(simulation_time=200, random_seed=2018)` | Seed Ciw, build the network, simulate, and return the `ciw.Simulation`. |
| `get_records(simulation)` | Return the records table as a `pandas.DataFrame`. |

## `ciw_plotly_sankey.first_nodes`

| Name | Description |
| --- | --- |
| `first_nodes(recs)` | Return a frame with columns `node` (always `0`) and `flow`: the number of customers whose first node was each node. |

## `ciw_plotly_sankey.edge_flows`

| Name | Description |
| --- | --- |
| `exit_index` | The index used for the exit node, `4`. |
| `edge_flows(recs, exit_node=4)` | Return a frame with columns `node`, `destination`, and `flow`. |

## `ciw_plotly_sankey.combine`

| Name | Description |
| --- | --- |
| `combine_flows(arrival_flows, edge_flows)` | Stack the arrival and edge flow frames. |

## `ciw_plotly_sankey.sort`

| Name | Description |
| --- | --- |
| `sort_flows(recs)` | Return the link table sorted by `destination`, `node`, and `flow`. |

## `ciw_plotly_sankey.figure`

| Name | Description |
| --- | --- |
| `node_labels` | Node labels: `["ArrivalNode", "ColdFood", "HotFood", "Till", "Exit"]`. |
| `build_figure(recs)` | Return a Plotly Sankey `Figure` for the link table. |

## `ciw_plotly_sankey.render`

| Name | Description |
| --- | --- |
| `transparent_grey` | The background colour `"rgba(0.5,0.5,0.5,0.5)"`. |
| `prepare_links(recs)` | Compose the transforms into the sorted link table. |
| `style_figure(fig)` | Set the paper and plot backgrounds. |
| `to_html(fig)` | Return the figure as an HTML fragment using the Plotly CDN. |
| `build_diagram()` | Run the example and return the styled figure. |
| `main()` | Build the diagram and print its HTML. |

## Console script

| Command | Effect |
| --- | --- |
| `ciw-plotly-sankey` | Runs the cafe example and prints the Sankey diagram as HTML |
