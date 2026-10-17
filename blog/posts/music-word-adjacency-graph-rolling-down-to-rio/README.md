# music-word-adjacency-graph-rolling-down-to-rio

Word adjacency graph for the lyrics of *Rolling Down to Rio*.

Each distinct word becomes a node and each adjacent pair of words becomes a
directed edge, turning the song into a digraph that highlights repeated phrases
and the words that connect them.

This package is the code from the blog post
[Word Adjacency Graph of Rolling Down to Rio](https://galenseilis.github.io/blog/posts/music-word-adjacency-graph-rolling-down-to-rio/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/music-word-adjacency-graph-rolling-down-to-rio"
```

Requires Python 3.11 or newer and depends on `networkx` and `matplotlib`.

## Quick start

```python
from music_word_adjacency_rolling_down_to_rio import create_graph, lyrics

G = create_graph(lyrics)
print(G.number_of_nodes(), G.number_of_edges())
print(sorted(G.successors("roll")))
```

## Reproduce the figure

```bash
music-word-adjacency-graph-rolling-down-to-rio
```

This writes `figures/word-adjacency.png`.

## Docs

Start at [`docs/index.md`](docs/index.md).
