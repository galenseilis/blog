# asyncio-hello-world documentation

`asyncio-hello-world` is a small teaching package: it shows how to write an
asyncio "Hello, World" and then how to run it from an environment (a notebook, a
Quarto chunk) that already owns an event loop.

The package follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): run the greeting and capture the output from a
  notebook-style session.
- [How-to guides](how-to-guides.md): run arbitrary files in a subprocess, embed
  output, and debug the "running event loop" error.
- [Reference](reference.md): the public API and the command line entry point.
- [Explanation](explanation.md): why `asyncio.run` and notebooks conflict.
