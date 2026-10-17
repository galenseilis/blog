# API reference

## `spearman_correlation.permutations`

### `rank_permutations(n=4) -> list[tuple[int, ...]]`

Return every permutation of `(1, ..., n)`.

### `rank_columns(n=4) -> list[str]`

Return the LaTeX column labels ``rank(X_1) ... rank(X_n)``.

### `permutation_table(n=4) -> str`

Return the permutations as a Markdown table via `pandas.DataFrame.to_markdown`.

### `main()`

Console entry point for `spearman-correlation-table`. Prints the table.

## `spearman_correlation.perm_grid`

### `spearman_correlation(x, y) -> float`

Return the Pearson correlation of the two samples; on ranks this is Spearman's
coefficient.

### `permutation_grid(output="figures/perm_grid.png", n=4) -> Path`

Render every permutation of ``n`` ranks as a checkboard grid, save the figure,
and return the written path.

### `main()`

Console entry point for `spearman-correlation-grid`.

## Console scripts

- `spearman-correlation-table` — prints the permutation table.
- `spearman-correlation-grid` — writes `figures/perm_grid.png`.
