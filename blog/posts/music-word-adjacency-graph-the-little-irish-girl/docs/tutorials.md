# Tutorial

This tutorial builds the word adjacency graph for *The Little Irish Girl*. It
should take a couple of minutes.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/music-word-adjacency-graph-the-little-irish-girl"
```

## 2. Load the lyrics

The lyrics are already lower-cased and stripped of punctuation, then split on
spaces into a list of words.

```python
from music_word_adjacency_the_little_irish_girl import lyrics

print(len(lyrics))
print(lyrics[:8])
```

## 3. Build the graph

`create_graph` adds one node per distinct word and one directed edge per
adjacent pair.

```python
from music_word_adjacency_the_little_irish_girl import create_graph, lyrics

G = create_graph(lyrics)
print(G.number_of_nodes(), G.number_of_edges())
```

## 4. Look at a word's neighbours

Successors are the words that follow `delight` in the song; predecessors are the
words that come before it.

```python
print(sorted(G.successors("delight")))
print(sorted(G.predecessors("delight")))
```

## 5. Draw the figure

`main` draws the graph and writes `figures/word-adjacency.png` relative to the
post directory.

```bash
music-word-adjacency-graph-the-little-irish-girl
```

You now have the full workflow. Continue with the [how-to
guides](how-to-guides.md) for practical tweaks.
