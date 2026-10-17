# API reference

## `asyncio_hello_world.hello`

The greeting itself.

### `async def main() -> None`

Print `Hello,`, await `asyncio.sleep(0.2018)`, then print `World!`.

### `run() -> None`

Run `main()` on a new event loop via `asyncio.run`. This is what the module's
`__main__` guard calls.

## `asyncio_hello_world.runner`

### `run_python_file(file_path, interpreter=sys.executable)`

Run `file_path` in a subprocess and return its standard output as a string. If
the subprocess exits with a non-zero status, return
`"An error occurred while running the file: <stderr>"` rather than raising.

- `file_path` — path to the Python file to run.
- `interpreter` — the executable used to run it; defaults to the current
  interpreter.

## `asyncio_hello_world.cli`

### `main()`

Console-script entry point. Runs the greeting in a subprocess and prints its
output with the trailing newline trimmed.

## Command line

```text
asyncio-hello-world
```

Prints:

```text
Hello,
World!
```
