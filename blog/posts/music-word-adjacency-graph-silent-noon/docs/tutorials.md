# Tutorial

This tutorial builds the word adjacency graph for *Silent Noon* and renders the
figure from the post. It should take a couple of minutes.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/music-word-adjacency-graph-silent-noon"
```

## 2. Look at the lyrics

The lyrics are stored as a list of lowercase words with punctuation removed:

```python
from music_word_adjacency_graph_silent_noon import lyrics

print(len(lyrics), lyrics[:5])
```

The list starts with `your hands lie open` and ends with `the song of love`.

## 3. Build the graph

`create_graph` adds one node per distinct word and one directed edge from each
word to the word that follows it:

```python
from music_word_adjacency_graph_silent_noon import create_graph, lyrics

graph = create_graph(lyrics)
print(graph.number_of_nodes(), graph.number_of_edges())
```

Repeated words become a single node, so the graph is smaller than the word
count and the edges form a path through the poem.

## 4. Render the figure

```python
from music_word_adjacency_graph_silent_noon import plot_word_adjacency

plot_word_adjacency("figures/word-adjacency.png")
```

The figure is tall and narrow because the adjacency path runs the length of
the poem. Node sizes scale with word length, so longer words are easier to
spot. You now have the figure the post embeds. Read the
[how-to guides](how-to-guides.md) to use your own text.
