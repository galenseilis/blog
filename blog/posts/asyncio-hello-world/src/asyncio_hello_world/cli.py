"""Run the asyncio greeting in a subprocess and print its output.

Running the greeting in a separate interpreter sidesteps the
``RuntimeError: asyncio.run() cannot be called from a running event loop`` that
a notebook raises, while still letting the notebook show the captured output.
"""

from __future__ import annotations

from asyncio_hello_world import hello
from asyncio_hello_world.runner import run_python_file


def main() -> None:
    """Console-script entry point."""
    output = run_python_file(hello.__file__)
    print(output.rstrip("\n"))


if __name__ == "__main__":
    main()
