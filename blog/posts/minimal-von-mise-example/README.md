# minimal-von-mise-example

Minimal von Mises example using PyMC.

This package is extracted from the blog post
[Minimal von Mises Example](https://galenseilis.github.io/blog/posts/minimal-von-mise-example/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/minimal-von-mise-example"
```

Requires Python 3.11 or newer.

## Quick start

```python
from minimal_von_mise_example.model import build_model
import numpy as np

model = build_model(observed=np.array([-2, 2]))
```
