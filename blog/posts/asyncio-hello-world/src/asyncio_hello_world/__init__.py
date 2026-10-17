"""A tiny asyncio "Hello, World" example.

The package splits the post's three scripts into importable modules:

* :mod:`asyncio_hello_world.hello` — the coroutine that does the greeting.
* :mod:`asyncio_hello_world.runner` -- run a Python file in a subprocess and
  capture its standard output.
* :mod:`asyncio_hello_world.cli` -- run the greeting in a subprocess so that it
  works even when a notebook is already running an event loop.
"""

from __future__ import annotations

__all__ = ["__version__"]

__version__ = "0.1.0"
