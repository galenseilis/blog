# Explanation

## What a rank is

A rank is a number that encodes an element's order relative to the other
elements of a set. Give ten runners finishing a marathon and their ranks are
their finishing order. The idea generalises far beyond numbers: any set with a
partial order can be ranked.

## Why ties are the interesting case

For continuous variables, ties have probability zero and every ranking method
agrees. Ranks of a continuous sample are (almost surely) a permutation of
`1...n`, which is why the `ordinal` and `average` methods coincide there. Ties
are where the methods diverge:

- `average` splits the tied ranks evenly, preserving the sum of the ranks.
- `min` and `max` assign the smallest/largest rank in the tie group, leaving
  gaps that reflect how many observations were tied.
- `dense` gives the next distinct value the next consecutive rank, ignoring the
  size of the tie group.
- `ordinal` ignores ties and numbers the observations in input order.

The post's binomial sample makes this visible precisely because its integer
values repeat.

## Rankings versus ratings

The post draws a distinction that the package inherits: a *ranking* is a
function that provably respects an order, while a *rating* is a human or system
preference that may be intransitive. Ratings need not satisfy the order axioms,
so they are not ranks in the mathematical sense used here.

## Trade-offs

- There is no single "rank transform"; pick the tie-handling rule that matches
  the question. Average ranks preserve totals; dense ranks preserve the number
  of distinct levels.
- Rank methods throw away the spacing of the original values, which is what makes
  them robust but also what makes them blind to the magnitude of differences.

## Where to go next

- [Tutorial](tutorials.md)
- [How-to guides](how-to-guides.md)
