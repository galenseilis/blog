"""The asyncio "Hello, World" greeting.

``asyncio.run`` refuses to start when an event loop is already running, which is
exactly the situation inside a Jupyter kernel or a Quarto Python chunk. The
coroutine itself is unaffected; only the call that schedules it has to happen
somewhere else (see :mod:`asyncio_hello_world.runner`).
"""

from __future__ import annotations

import asyncio


async def main() -> None:
    """Print the greeting, pausing between the two lines."""
    print("Hello,")
    await asyncio.sleep(0.2018)
    print("World!")


def run() -> None:
    """Run the greeting as a program, driving its own event loop."""
    asyncio.run(main())


if __name__ == "__main__":
    run()
