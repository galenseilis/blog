# pandigital-factorial

Largest pandigital factorial number exploration.

This package contains the code from the blog post
[Largest Pandigital Factorial Number](https://galenseilis.github.io/blog/posts/pandigital-factorial/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/pandigital-factorial"
```

Requires Python 3.11 or newer, and depends on `pandas`.

## Quick start

```python
from pandigital_factorial.pandigital import is_pandigital, search_pandigital_factorials_up_to

# Check if a number is pandigital
is_pandigital(1023456789)

# Search up to n=1001
results = search_pandigital_factorials_up_to(k=20, m=10)
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)
