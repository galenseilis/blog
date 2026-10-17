# Explanation

## Why pickle

`pickle` converts almost any Python object graph into a byte string and back.
That makes it the shortest path from "I have a data structure" to "I have bytes I
can put on a socket", which is exactly what a teaching example wants. The same
idea appears in every serialization format; pickle just happens to need no schema
and no extra dependency.

## The client-server shape

A TCP connection is bidirectional, but this example uses it as a simple
request/response channel:

1. The client connects.
2. The client sends one message (`sendall`).
3. The server reads it (`recv(BUFFER_SIZE)`), processes it, and sends one message
   back.
4. Both sides close.

Because a single `recv(4096)` is treated as the whole message, the example
assumes the payload fits in one buffer. Real protocols prefix each message with
its length (or use a delimiter) so that messages larger than the buffer are
reassembled correctly.

## Trade-offs

- **Pickle is not secure.** Unpickling data from an untrusted source can execute
  arbitrary code. Never unpickle bytes you did not produce or authenticate.
- **Pickle is Python-only and version-sensitive.** Other languages cannot read
  it, and objects can fail to unpickle across versions.
- **The server is deliberately minimal.** It handles exactly one connection and
  has no error handling, timeouts, or concurrency. Those omissions are the point
  of the exercise; each one is a natural next topic.

## Design choice in this package

The socket calls live inside `client.request`, `server.serve`, and `server.main`
so that importing the package has no side effects. The genuinely interesting
logic -- `serialize`, `deserialize`, and `process_data` -- is isolated in
`protocol`, which lets the test suite verify behaviour without opening a socket.
