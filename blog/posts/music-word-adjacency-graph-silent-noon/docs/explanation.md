# Explanation

## What a word adjacency graph shows

A word adjacency graph treats a text as a walk through a vocabulary. Each
distinct word is a node, and each time a word is followed by another it adds a
directed edge. The result summarizes local structure: words that follow many
others have high out-degree, and words that are followed by many others have
high in-degree. For a poem sung as a line, the edges chain the words together
in reading order.

## Normalisation and its consequences

The post ignores punctuation and capitalization, so `The` and `the` collapse to
the same node and sentence boundaries disappear. This makes the graph easier to
read and focuses attention on adjacency, at the cost of losing the information
that a period marks a stop. The repeated article `the` and the repeated word
`song` therefore appear once each, with multiple incoming and outgoing edges.

## Why node size tracks word length

Encoding word length as node size adds a second dimension of structure to the
drawing. Long words stand out visually and cluster where the poem uses unusual
vocabulary, while short function words recede. It is a simple visual channel,
but it lets a reader scan the graph for lexical texture without reading every
label.

## Why the figure is so tall

The adjacency edges follow the poem from beginning to end, so the graph is
essentially a long chain. A square figure would crowd the labels, so the post
uses a `(8, 30)` figure and lays the nodes out top to bottom. The layout
prefers Graphviz, which arranges such chains legibly, and falls back to a
seeded spring layout when Graphviz is not installed, so the figure is
reproducible either way.
