# How-to guides

Practical recipes for common tasks.

## Build a graph from your own text

Split your text into words and pass the list to `create_graph`:

```python
from music_word_adjacency_graph_silent_noon import create_graph

words = "the quick brown fox jumps over the lazy dog".split()
graph = create_graph(words)
```

Remember to lowercase and strip punctuation first if you want the same
normalisation as the post.

## Render a graph you built yourself

`plot_graph` draws onto the current Matplotlib figure; save it yourself:

```python
import matplotlib.pyplot as plt
import networkx as nx

from music_word_adjacency_graph_silent_noon import create_graph, plot_graph

graph = create_graph("one two three one two".split())
plot_graph(graph)
plt.savefig("out/custom.png", dpi=300, bbox_inches="tight")
plt.close()
```

## Force the spring layout

`plot_graph` prefers Graphviz via `nx.nx_agraph.graphviz_layout` and falls back
to `nx.spring_layout(seed=2018)`. To always use the spring layout, call
`networkx` directly:

```python
import matplotlib.pyplot as plt
import networkx as nx

from music_word_adjacency_graph_silent_noon import create_graph, lyrics

graph = create_graph(lyrics)
pos = nx.spring_layout(graph, seed=2018)
nx.draw(graph, pos, with_labels=True)
plt.savefig("out/spring.png", dpi=300, bbox_inches="tight")
plt.close()
```

## Write the figure to a custom path

`plot_word_adjacency` takes an output path and creates its parent directory:

```python
from music_word_adjacency_graph_silent_noon import plot_word_adjacency

plot_word_adjacency("out/word-adjacency.png")
```
