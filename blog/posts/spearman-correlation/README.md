# spearman-correlation

Small illustrations of [Spearman's rank correlation](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient):
the permutation table of the ranks of four observations, and a grid figure
showing every possible pairing of ranks.

This package is the code from the blog post
[Spearman Correlation Quantifies Comonotonicity](https://galenseilis.github.io/blog/posts/spearman-correlation/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/spearman-correlation"
```

Requires Python 3.11 or newer. Dependencies: `matplotlib`, `numpy`, `pandas`,
`scipy`, and `tabulate` (used by `pandas.DataFrame.to_markdown`).

## Usage

Print the table of the `4! = 24` rank permutations:

```bash
spearman-correlation-table
```

Write the checkerboard figure of the same permutations:

```bash
spearman-correlation-grid
```

Or from Python:

```python
from spearman_correlation.permutations import rank_permutations
from spearman_correlation.perm_grid import permutation_grid, spearman_correlation

len(rank_permutations(4))  # 24
spearman_correlation([1, 2, 3, 4], [4, 3, 2, 1])  # -1.0
permutation_grid()  # writes figures/perm_grid.png
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
