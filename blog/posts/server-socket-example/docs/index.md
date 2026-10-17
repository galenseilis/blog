# server-socket-example documentation

`server-socket-example` shows the smallest complete client-server exchange in
Python: serialize an object, send it over a socket, process it on the other side,
and send the result back. It is a teaching package, so the code favours
clarity over robustness.

The package follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): run the client and server and follow the bytes.
- [How-to guides](how-to-guides.md): change the port, the payload, and the
  processing step.
- [Reference](reference.md): the public API and the two console scripts.
- [Explanation](explanation.md): why pickling over a socket is convenient and
  what makes it risky.
