# music-word-adjacency-graph-the-little-irish-girl

Word adjacency graph for the lyrics of *The Little Irish Girl*.

Each distinct word becomes a node and each adjacent pair of words becomes a
directed edge, turning the song into a digraph that highlights repeated phrases
and the words that connect them.

This package is the code from the blog post
[Word Adjacency Graph of The Little Irish Girl](https://galenseilis.github.io/blog/posts/music-word-adjacency-graph-the-little-irish-girl/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/music-word-adjacency-graph-the-little-irish-girl"
```

Requires Python 3.11 or newer and depends on `networkx` and `matplotlib`.

## Quick start

```python
from music_word_adjacency_the_little_irish_girl import create_graph, lyrics

G = create_graph(lyrics)
print(G.number_of_nodes(), G.number_of_edges())
print(sorted(G.successors("delight")))
```

## Reproduce the figure

```bash
music-word-adjacency-graph-the-little-irish-girl
```

This writes `figures/word-adjacency.png`.

## Docs

Start at [`docs/index.md`](docs/index.md).
