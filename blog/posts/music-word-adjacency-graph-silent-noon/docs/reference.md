# API reference

## `music_word_adjacency_graph_silent_noon.lyrics.lyrics`

The lyrics of *Silent Noon* as a `list[str]` of lowercase words. It is built by
splitting the poem on spaces after removing punctuation and capitalization.

## `music_word_adjacency_graph_silent_noon.plot_word_adjacency.create_graph(strings)`

Build a `networkx.DiGraph` from a list of words. Every word becomes a node and
every consecutive pair becomes a directed edge. Returns the graph.

## `music_word_adjacency_graph_silent_noon.plot_word_adjacency.plot_graph(G)`

Draw `G` onto a new Matplotlib figure: positions from Graphviz when available,
otherwise `nx.spring_layout(seed=2018)`, node sizes scaled by word length, and
the title "Word Adjacency in Silent Noon". It does not save the figure.

## `music_word_adjacency_graph_silent_noon.plot_word_adjacency.plot_word_adjacency(output="figures/word-adjacency.png")`

Build the graph from `lyrics`, draw it, and save it to `output` (a `str` or
`pathlib.Path`); parent directories are created. Returns the written
`pathlib.Path`.

## `music_word_adjacency_graph_silent_noon.plot_word_adjacency.main()`

Console-script entry point. Calls `plot_word_adjacency()`.

## Console scripts

| Command | Writes |
| --- | --- |
| `music-word-adjacency-graph-silent-noon` | `figures/word-adjacency.png` |
