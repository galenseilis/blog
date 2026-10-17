# Explanation

## What a word adjacency graph shows

A word adjacency graph treats a text as a walk through a state space: the state
at each step is the current word, and the next word is the transition. Drawing
the directed graph makes two things visible at once.

First, the **structure of repetition**. *Rolling Down to Rio* repeats "roll down
to rio" and "some day before i am old" as refrains, and the graph shows the
corresponding cycles and the high-degree hub words that the refrain keeps
revisiting.

Second, the **local grammar of the song**. Edges such as `never -> sailed` or
`white -> and` encode the local ordering that a bag-of-words analysis throws
away, while still being cheap to compute.

## Choices and their consequences

The graph is built after lower-casing and removing punctuation. That is exactly
why the edges look clean, but it also merges distinct senses: "will" the noun
and `will` the auxiliary collapse into one node, and sentence boundaries vanish,
so the last word of one line is linked directly to the first word of the next.

The graph is **unweighted and a simple digraph**. Repeating an adjacent pair does
not add a second edge, so frequency information is lost. When counts matter, use
a `MultiDiGraph` or attach weights.

## Reading the picture

- **Hubs** (large nodes with many neighbours) are the common words that stitch
  the song together.
- **Cycles** correspond to repeated phrases.
- **Long chains** correspond to passages that never repeat a local transition.

A layout algorithm places the nodes, so the arrangement of the figure is not
itself meaningful; only the edges are.

## Limitations

Adjacency is a shallow model of language. It ignores syntax, metre, and
semantics, and it treats the song as a linear token stream rather than as
sections with repeats. It is best used as a compact, legible summary of the
local order in a short text.
