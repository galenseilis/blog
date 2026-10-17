# permutive-cross-product

Permutive cross product constructions in 3D.

This package is extracted from the blog post
[Permutive Cross Product](https://galenseilis.github.io/blog/posts/permutive-cross-product/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/permutive-cross-product"
```

Requires Python 3.11 or newer.

## Quick start

```python
from permutive_cross_product.permutive import find_permutive_cross_products, find_4perm_cross_products

print(find_permutive_cross_products(dim=3))
print(find_4perm_cross_products(dim=3, max_results=5))
```
