# music-word-adjacency-graph-silent-noon

Word adjacency graph of Rossetti's *Silent Noon*.

This package is the code from the blog post
[Word Adjacency Graph of Rossetti's *Silent Noon*](https://galenseilis.github.io/blog/posts/music-word-adjacency-graph-silent-noon/).
It turns the post's two snippets into importable code:

- `lyrics` is the lyrics of *Silent Noon* with punctuation and capitalization
  ignored, as a list of words.
- `create_graph` builds a directed word adjacency graph from a list of words.
- `plot_word_adjacency` draws that graph and saves it as a PNG.

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/music-word-adjacency-graph-silent-noon"
```

Requires Python 3.11 or newer, and depends on `matplotlib` and `networkx`.

## Quick start

```python
from music_word_adjacency_graph_silent_noon import create_graph, lyrics

graph = create_graph(lyrics)
print(graph.number_of_nodes(), graph.number_of_edges())
```

Render the figure from the post:

```python
from music_word_adjacency_graph_silent_noon import plot_word_adjacency

plot_word_adjacency("figures/word-adjacency.png")
```

or from the console:

```bash
music-word-adjacency-graph-silent-noon
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
