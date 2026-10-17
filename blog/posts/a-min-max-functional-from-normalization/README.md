# a-min-max-functional-from-normalization

Explore min/max functionals under normalization transformations.

This package is extracted from the blog post
[A Min/Max Functional from Normalization](https://galenseilis.github.io/blog/posts/a-min-max-functional-from-normalization/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/a-min-max-functional-from-normalization"
```

Requires Python 3.11 or newer.

## Quick start

```python
from a_min_max_functional_from_normalization.functional import generate_functional_table

print(generate_functional_table().to_markdown(index=False))
```

## CLI

```bash
a-min-max-functional-from-normalization
```
