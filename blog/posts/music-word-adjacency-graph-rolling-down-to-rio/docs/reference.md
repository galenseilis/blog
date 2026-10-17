# API reference

## Data

### `music_word_adjacency_rolling_down_to_rio.lyrics`

A `list[str]` of the words of *Rolling Down to Rio*, lower-cased and stripped of
punctuation.

## Graph construction

### `music_word_adjacency_rolling_down_to_rio.plot.create_graph(strings)`

Return a `networkx.DiGraph` whose nodes are the distinct strings and whose edges
connect each string to the next one in `strings`.

## Plotting

### `music_word_adjacency_rolling_down_to_rio.plot.plot_graph(G)`

Draw `G` with Matplotlib. Node size is proportional to the label length. Uses
Graphviz layout when `pygraphviz` is available and a seeded spring layout
otherwise.

### `music_word_adjacency_rolling_down_to_rio.plot.main()`

Build the graph from the bundled lyrics, draw it, and write
`figures/word-adjacency.png` at 300 dpi. This is the console-script entry point.

## Console script

| Command | Writes |
| --- | --- |
| `music-word-adjacency-graph-rolling-down-to-rio` | `figures/word-adjacency.png` |
