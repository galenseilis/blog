# ciw-dirichlet-sampling-router-matrix

Dirichlet resampling for stochastic Ciw routing matrices.

This package is the code from the blog post
[Ciw Hack to Get Resampling Routing Matrices](https://galenseilis.github.io/blog/posts/ciw-dirichlet-sampling-router-matrix/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/ciw-dirichlet-sampling-router-matrix"
```

Requires Python 3.11 or newer.

## Quick start

```python
import ciw
import numpy as np
from ciw_dirichlet_sampling_router_matrix import RandomDirichletList

np.random.seed(2018)
sm = [
    RandomDirichletList([1, 2, 3]),
    RandomDirichletList([3, 4, 5]),
    RandomDirichletList([6, 7, 8]),
]
# ... use as routing matrix in ciw.create_network(...)
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
