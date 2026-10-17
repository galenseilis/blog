# what-are-ranks

Compare the rank transforms implemented by
[`scipy.stats.rankdata`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rankdata.html)
on a small sample from a binomial random variable. The binomial is chosen
deliberately: its integer samples tie, and the methods disagree about how to
rank ties.

This package is the code from the blog post
[What are Ranks?](https://galenseilis.github.io/blog/posts/what-are-ranks/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/what-are-ranks"
```

Requires Python 3.11 or newer. Dependencies: `numpy`, `pandas`, and `scipy`.

## Usage

```bash
what-are-ranks
```

```text
 x  average method  min method  max method  dense method  ordinal method
 3             1.5         1.0         2.0           1.0             1.0
 ...
```

Or from Python:

```python
from what_are_ranks import rank_table, sample_binomial

table = rank_table(sample_binomial())
table["average method"]  # ranks under the default tie-handling rule
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
