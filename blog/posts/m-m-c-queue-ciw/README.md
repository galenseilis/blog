# m-m-c-queue-ciw

Ciw implementation of an M/M/c queue.

This package contains the code from the blog post
[Implementing a M/M/c Queue in Ciw](https://galenseilis.github.io/blog/posts/m-m-c-queue-ciw/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/m-m-c-queue-ciw"
```

Requires Python 3.11 or newer, and depends on `ciw`.

## Quick start

```python
from m_m_c_queue_ciw.queue import run_simulation

records = run_simulation(seed=2018, horizon=365)
print(records)
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)
