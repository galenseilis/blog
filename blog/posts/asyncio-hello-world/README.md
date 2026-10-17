# asyncio-hello-world

A minimal [asyncio](https://docs.python.org/3/library/asyncio.html) "Hello,
World" example that can be driven from a notebook.

`asyncio.run()` refuses to start when an event loop is already running, which is
what happens inside a Jupyter kernel or a Quarto Python chunk. The trick used
here is to put the greeting in its own file and run it in a subprocess, capturing
its standard output so the result still shows up in the interactive session.

This package is the code from the blog post
[Hello World, in Asyncio](https://galenseilis.github.io/blog/posts/asyncio-hello-world/).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/asyncio-hello-world"
```

The package has no third-party dependencies and requires Python 3.11 or newer.

## Usage

```bash
asyncio-hello-world
```

```text
Hello,
World!
```

Or from Python:

```python
from asyncio_hello_world import hello, runner

# The coroutine can be awaited from an already-running loop.
# Run a file in a subprocess and capture its stdout:
print(runner.run_python_file("path/to/script.py"), end="")
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
