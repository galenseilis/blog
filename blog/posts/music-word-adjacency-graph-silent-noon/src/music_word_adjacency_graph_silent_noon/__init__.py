"""Word adjacency graph of Rossetti's *Silent Noon*.

This package turns the post's two snippets into an importable module:

* :data:`music_word_adjacency_graph_silent_noon.lyrics.lyrics` is the lyrics of
  *Silent Noon* as a list of lowercase words.
* :func:`music_word_adjacency_graph_silent_noon.plot_word_adjacency.plot_word_adjacency`
  builds the word adjacency graph and draws it.
"""

from __future__ import annotations

from music_word_adjacency_graph_silent_noon.lyrics import lyrics
from music_word_adjacency_graph_silent_noon.plot_word_adjacency import (
    create_graph,
    plot_graph,
    plot_word_adjacency,
)

__all__ = [
    "create_graph",
    "lyrics",
    "plot_graph",
    "plot_word_adjacency",
]

__version__ = "0.1.0"
