# Tutorial

This tutorial walks through the greeting from first principles. It should take
about five minutes.

## 1. The coroutine

The unit of work is an ordinary coroutine:

```python
import asyncio

async def main() -> None:
    print("Hello,")
    await asyncio.sleep(0.2018)
    print("World!")
```

Calling `main()` creates a coroutine but runs nothing. It has to be scheduled on
an event loop, usually with `asyncio.run(main())`.

## 2. Run it as a program

```bash
python -m asyncio_hello_world.hello
```

```text
Hello,
World!
```

`python -m` imports the module and hits the `if __name__ == "__main__":` guard,
which calls `run()` -> `asyncio.run(main())`.

## 3. Run it from an interactive session

If you try `asyncio.run(main())` inside a notebook you will see

```text
RuntimeError: asyncio.run() cannot be called from a running event loop
```

Instead, hand the work to a fresh interpreter and read back its stdout:

```python
from asyncio_hello_world import runner

print(runner.run_python_file("greet.py"), end="")
```

The packaged command does this for the greeting itself:

```bash
asyncio-hello-world
```

## 4. Where to go next

- [How-to guides](how-to-guides.md) for recipes.
- [Reference](reference.md) for the full API.
