# parity-decomposition-in-python

Parity decomposition plots of scalar functions in Python.

This package contains the code from the blog post
[Parity Decomposition Plots of Scalar Functions in Python](https://galenseilis.github.io/blog/posts/parity-decomposition-in-python/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/parity-decomposition-in-python"
```

Requires Python 3.11 or newer, and depends on `numpy` and `matplotlib`.

## Quick start

```python
import numpy as np
from parity_decomposition_in_python.parity import parity_decomposition_vector, plot_parity_decomposition

f = lambda t: np.exp(np.cos(t) + np.sin(t))
t = np.linspace(-2*np.pi, 2*np.pi, 1000)
e, o = parity_decomposition_vector(f, t)
plot_parity_decomposition(f, t, output="example.png")
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)
