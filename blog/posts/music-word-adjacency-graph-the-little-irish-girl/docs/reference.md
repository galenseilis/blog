# API reference

## Data

### `music_word_adjacency_the_little_irish_girl.lyrics`

A `list[str]` of the words of *The Little Irish Girl*, lower-cased and stripped
of punctuation.

## Graph construction

### `music_word_adjacency_the_little_irish_girl.plot.create_graph(strings)`

Return a `networkx.DiGraph` whose nodes are the distinct strings and whose edges
connect each string to the next one in `strings`.

## Plotting

### `music_word_adjacency_the_little_irish_girl.plot.plot_graph(G)`

Draw `G` with Matplotlib. Node size is proportional to the label length. Uses
Graphviz layout when `pygraphviz` is available and a seeded spring layout
otherwise.

### `music_word_adjacency_the_little_irish_girl.plot.main()`

Build the graph from the bundled lyrics, draw it, and write
`figures/word-adjacency.png` at 300 dpi. This is the console-script entry point.

## Console script

| Command | Writes |
| --- | --- |
| `music-word-adjacency-graph-the-little-irish-girl` | `figures/word-adjacency.png` |
