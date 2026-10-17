# How-to guides

## Print the table for a different sample size

```python
from spearman_correlation.permutations import permutation_table

permutation_table(6)  # 6! = 720 rows
```

## Write the figure somewhere else

```python
from spearman_correlation.perm_grid import permutation_grid

permutation_grid(output="figures/ranks.png")
```

## Compute Spearman's coefficient directly

```python
from spearman_correlation.perm_grid import spearman_correlation

spearman_correlation(x, y)  # Pearson correlation of the samples
```

On the ranks, the Pearson product-moment correlation is Spearman's coefficient.

## Add a new rank column

`rank_permutations(n)` generates all permutations of `(1, ..., n)`, which is
exactly the set of order-preserving rank assignments for `n` IID samples.
