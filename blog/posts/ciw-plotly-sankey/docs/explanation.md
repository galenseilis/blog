# Explanation

## Showing what happened, not what you planned

The point of a Sankey diagram of a simulation is not to display the model you
wrote. It is to display *what actually happened*. A routing matrix says that
thirty percent of customers go one way and seventy percent another; a Sankey
diagram says that, in this particular run, thirteen customers went this way and
thirty-seven that way. The structure of the model is implicit in the results,
and when the simulation is small or heavily constrained, some paths may not
appear at all — which is often exactly what you want to see.

## From records to flows

Ciw produces one record per service completion, with the node served and the
destination the customer moved to. Two aggregations turn that into a diagram:

1. **Edge flows.** Grouping by `(node, destination)` and counting gives how many
   moves happened along each edge.
2. **Arrival flows.** The arrival node is not part of the records, so it has to
   be reconstructed: find each customer's first node and count how many started
   at each. Those rows are tagged with the synthetic index `0`.

Listing these to a common index scheme — `0` arrival, `1..3` the cafe nodes, `4`
exit — makes the two tables stackable and directly usable as the `source`,
`target`, and `value` arrays of a Plotly Sankey.

## Why the arrival flows lose their destination

`first_nodes` follows the post exactly, including a subtle pandas detail: after
`value_counts().reset_index(name="flow")` the index column is named `node`
because the grouped series is called `node`, so the subsequent
`rename(columns={"index": "destination"})` matches nothing. The result is that
the arrival-node rows carry a `node` of `0` and a `flow`, but no destination —
which is why the two arrival links in the diagram have a null target. This
faithfully reproduces the diagram pasted into the post. A human reviewer may
prefer to fix it by renaming `node` to `destination` explicitly before
assigning `node=0`, which would give the arrival links concrete targets.

## Limits of the layout

The default `snap` arrangement is a prototype, and the author notes that the
arcs leaving cold food are jumbled. Plotly does not expose many layout controls
for Sankey diagrams, so a tidier arrangement may require computing explicit
node coordinates — for example with a `layout` function from Networkx — and
passing them to Plotly, rather than using Plotly's automatic layout.
