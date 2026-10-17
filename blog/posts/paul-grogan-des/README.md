# paul-grogan-des

A minimal, pedagogical discrete-event simulation of a single-server queue,
transcribed from Paul Grogan's video and compared with a Ciw implementation.

The `Simulation` class is a hand-written **event-advance** simulation of an
M/M/1 queue. Arrivals and services are exponential, the clock jumps to whichever
of the next arrival or the next departure comes first, and the simulation
accumulates the total wait. A second module runs the same system through Ciw.

This package is the code from the blog post
[Paul Grogan's DES Example and Its Implementation in Ciw](https://galenseilis.github.io/blog/posts/paul-grogan-des/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/paul-grogan-des"
```

Requires Python 3.11 or newer and depends on `numpy` and `ciw`.

## Quick start

```python
from paul_grogan_des import Simulation

S = Simulation()
for _ in range(2018):
    S.advance_time()

print(S.num_arrivals, S.num_departs, S.total_wait)
```

## Docs

Start at [`docs/index.md`](docs/index.md).
