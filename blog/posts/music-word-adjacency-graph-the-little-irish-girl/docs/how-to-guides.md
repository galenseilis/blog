# How-to guides

Practical recipes for the word adjacency graph.

## Reproduce the figure from the blog post

```bash
music-word-adjacency-graph-the-little-irish-girl
```

This writes `figures/word-adjacency.png` next to the post's `index.qmd`.

## Save the figure somewhere else

Call the plotting code directly rather than the console script.

```python
import matplotlib.pyplot as plt

from music_word_adjacency_the_little_irish_girl import create_graph, lyrics, plot_graph

G = create_graph(lyrics)
plot_graph(G)
plt.savefig("out/word-adjacency.png", dpi=300, bbox_inches="tight")
```

## Change the node sizing

Node size is proportional to the word's character length. Edit the scaling
factor inside `plot_graph` or set sizes yourself after creating the axes.

## Use a different lyric

Replace the `lyrics` list with any tokenised text and pass it to `create_graph`.
The graph code makes no assumption about the poetry.

```python
from music_word_adjacency_the_little_irish_girl import create_graph

tokens = "one fish two fish red fish blue fish".split()
G = create_graph(tokens)
print(sorted(G.successors("fish")))
```

## Export the graph

NetworkX graphs serialise directly.

```python
import networkx as nx

from music_word_adjacency_the_little_irish_girl import create_graph, lyrics

G = create_graph(lyrics)
nx.write_graphml(G, "lyrics.graphml")
```
