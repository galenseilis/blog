# Explanation

## What an adjacency graph shows

A word adjacency graph turns a song into a directed graph: each distinct word is
a node and each adjacent pair of words is a directed edge. The resulting picture
is a compact summary of the local order of the text.

For *The Little Irish Girl* the repeated refrain ("she is my joy and my delight")
shows up as a tightly connected cluster that the verses feed into and out of,
while the verse lines form longer chains that connect the refrain back to
itself.

## What is and is not captured

The graph records only *which* word follows which. Because it is a simple
(unweighted) digraph, a transition that occurs many times is drawn once, so the
picture does not distinguish a phrase that appears twice from one that appears
twenty times. Add edge weights or use a `MultiDiGraph` when frequency matters.

The lyrics are normalised before graph construction: lower-cased and split on
spaces. That deliberately throws away capitalisation and punctuation, which
turns "McDonnell" and "mcdonnell" into the same node and closes the gap between
the end of one line and the start of the next.

## Reading the picture

The layout is chosen by NetworkX and is not itself meaningful. The information
is in the edges: chains are non-repeating passages, cycles are repeated phrases,
and high-degree nodes are the connective words of the song.

## Limitations

Adjacency is a shallow model of language. It ignores grammar, metre, and
meaning, and it treats repeated sections of a song as ordinary linear text. It
is a compact, legible summary rather than a linguistic analysis.
