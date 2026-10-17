# music-word-adjacency-graph-silent-noon documentation

This package contains the word adjacency graph from the blog post about
Rossetti's *Silent Noon*. It has three jobs:

- Hold the poem's lyrics as a list of words, with punctuation and
  capitalization ignored.
- Build a directed graph whose nodes are the words and whose edges join each
  word to the word that follows it.
- Draw that graph as a tall figure, sizing each node by its word length.

The project follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): build the graph and render the figure.
- [How-to guides](how-to-guides.md): use your own text, change the layout, and
  customise the drawing.
- [Reference](reference.md): the public API and the console script.
- [Explanation](explanation.md): what word adjacency graphs show and why this
  one is drawn the way it is.
