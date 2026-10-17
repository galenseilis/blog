# Explanation

## Partial orders and their many representations

A partial order is a set together with a reflexive, transitive and
antisymmetric relation. The post's example uses `X = {a, b, c, d, e}` and the
relation

```
{(a, a), (a, c), (a, e), (b, b), (b, c), (b, d), (b, e),
 (c, c), (d, d), (d, e), (e, e)}.
```

The same object can be written as the ordered-pair set above, as an upper
triangular matrix, or as a digraph. The first figure is the digraph; because
the relation is reflexive it draws a self-loop at every node.

## Strict orders and cover relations

Removing the self-pairs from a partial order gives a strict partial order,
whose digraph is a directed acyclic graph (DAG). A *cover relation* `x < y`
holds when there is no `z` between them. In the example, `b < e` holds in the
strict order, but it is not a cover because `b < d < e`; so the cover relation
is `{(a, c), (a, e), (b, c), (b, d), (d, e)}`.

## Why the cover diagram looks the way it does

A cover diagram is a drawing of the cover graph in which each element is placed
below every element that covers it, and each edge is monotone in the vertical
direction. That is why the module fixes the node positions instead of letting
`networkx` choose a spring layout: the fixed `COVER_POSITIONS` guarantee that
`a` and `b` sit at the bottom, `e` at the top, and every edge climbs. A spring
layout would generally violate the upward-edge convention and stop being a
cover diagram.

## The LaTeX helper

The Cartesian product `X x X` has `|X|**2` ordered pairs, 25 for a
five-element set. `latex_pairs` enumerates them with `itertools.product`,
sorts them, and rewrites Python list syntax as LaTeX set syntax, escaping the
curly braces. It is a convenience for typesetting rather than a mathematical
operation, but it saves a lot of error-prone typing.
