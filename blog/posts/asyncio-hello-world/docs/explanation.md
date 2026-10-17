# Explanation

## Why `asyncio.run` and notebooks disagree

`asyncio.run(coro)` is a convenience function that creates a new event loop,
runs the coroutine to completion, and then closes the loop. It asserts that it is
in charge of the process: if a loop is already running on the current thread, it
raises

```text
RuntimeError: asyncio.run() cannot be called from a running event loop
```

Jupyter kernels (and therefore Quarto Python chunks, which execute through a
kernel) already run an event loop to service cells. So `asyncio.run` is not
available there, even though the coroutine itself is perfectly valid.

## Why a subprocess

The post's solution is deliberately small: move the greeting into its own file
and execute that file in a *new* process. The new process has no event loop, so
`asyncio.run` is free to take over. The parent captures the child's standard
output and can display it in the notebook, which is what lets a Quarto document
render the result of an async program.

## Trade-offs

- **Pro:** works everywhere, isolates the child's event loop, and keeps the
  example tiny.
- **Con:** output is captured in one lump at the end rather than streamed, and
  state cannot easily be shared with the parent process.

For richer asynchronous work inside a notebook you would instead call
`await main()` directly (Jupyter supports top-level `await`), or use
`nest_asyncio`. The subprocess approach here is deliberately the simplest thing
that demonstrates the point.
