# Explanation

## Why the permutation table

For a sample of four continuous random variables the probability of tied ranks
is zero, so the ranks always realise a permutation of `(1, 2, 3, 4)`. The table in
the post enumerates those 24 permutations, which is the sample space of
"comonotonic" relationships.

## Why the checkerboard grid

Each permutation pairs two or more variables together. The `n x n` grid marks
which rank is assigned to which variable; a yellow cell means a pair was matched
by the permutation. Since Spearman's coefficient is a function of such a pairing
(through the Pearson correlation on the ranks), the grid makes the combinatorics
of the coefficient visible.

## Spearman's coefficient

Spearman's correlation is the Pearson product-moment correlation computed on
the ranks rather than on the raw values. Because ranking is order-preserving, a
perfect monotone relationship survives the transform, and perfect linearity on
the ranks means perfect monotonicity before ranking. Perfect
antimonotonicity is rewarded with `-1`.

## Trade-offs

- The permutation table scales factorially; beyond four or five variables the
  table is only feasible for small samples.
- The grid assumes distinct ranks; tied ranks need a ranking method such as the
  `average` method from `scipy.stats.rankdata`, which the
  [What are ranks?](../what-are-ranks/index.qmd) post covers.

## Where to go next

- [Tutorial](tutorials.md)
- [How-to guides](how-to-guides.md)
