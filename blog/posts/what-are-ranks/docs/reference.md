# API reference

## `what_are_ranks.rank_table`

### Constants

- `METHODS = ("average", "min", "max", "dense", "ordinal")` — the
  `scipy.stats.rankdata` tie-handling methods compared in the post.
- `DEFAULT_SEED = 2018` — seed making the post's table reproducible.

### `rank_table(sample, methods=METHODS) -> pandas.DataFrame`

Return a `DataFrame` with a column `x` for the sample and one column per method
(named `"<method> method"`). Rows are sorted by `x`.

### `sample_binomial(seed=DEFAULT_SEED, size=10, trials=10, p=0.5) -> numpy.ndarray`

Return `numpy.random.binomial(trials, p, size=size)` after seeding. Pass
`seed=None` for a non-reproducible draw.

### `main() -> None`

Console-script entry point. Prints `rank_table(sample_binomial()).to_string(index=False)`.

## `what_are_ranks`

`rank_table`, `sample_binomial`, and `METHODS` are re-exported from the package
root.

## Console script

```text
what-are-ranks
```

Prints the table of the post:

```text
 x  average method  min method  max method  dense method  ordinal method
 3             1.5         1.0         2.0           1.0             1.0
 ...
```
