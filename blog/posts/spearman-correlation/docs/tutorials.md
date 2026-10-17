# Tutorial

## 1. Print the permutation table

```python
from spearman_correlation.permutations import permutation_table

print(permutation_table(4))
```

With four continuous observations the ranks are a permutation of
`(1, 2, 3, 4)`, so the table has one row per possible sample.

## 2. Draw the permutation grid

```python
from spearman_correlation.perm_grid import permutation_grid

permutation_grid()  # writes figures/perm_grid.png
```

Each row of the grid is one possible sample; yellow cells mark ranks that are
paired.

## 3. Compute a rank correlation

```python
from spearman_correlation.perm_grid import spearman_correlation

spearman_correlation([1, 2, 3, 4], [10, 20, 30, 40])  # 1.0, perfect monotone
spearman_correlation([1, 2, 3, 4], [4, 3, 2, 1])  # -1.0, perfect antimonotone
```

## 4. Where to go next

- [How-to guides](how-to-guides.md)
- [Reference](reference.md)
