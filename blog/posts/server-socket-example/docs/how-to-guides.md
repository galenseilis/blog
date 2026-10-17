# How-to guides

## Use a different host or port

Both `client.request` and `server.serve` accept `host` and `port`:

```python
from server_socket_example import client, server

# server.py
server.serve(host="127.0.0.1", port=50000)

# client.py
client.request({"key": "value", "numbers": [1, 2, 3]}, host="127.0.0.1", port=50000)
```

The defaults are `DEFAULT_HOST = "localhost"` and `DEFAULT_PORT = 12345` from
`server_socket_example.protocol`.

## Change the processing step

Edit `process_data` in `server_socket_example/protocol.py`. It receives the
deserialized object and returns whatever should be pickled back to the client.

## Send a different payload

Any picklable object works. `client.request` accepts any object as its first
argument; the only requirement is that the server's `process_data` understands
it.

## Test without binding a port

Use `server.handle` with a fake connection object:

```python
from server_socket_example.protocol import serialize
from server_socket_example.server import handle


class FakeConnection:
    def __init__(self, incoming):
        self.incoming = incoming
        self.sent = b""

    def recv(self, size):
        return self.incoming

    def sendall(self, data):
        self.sent += data


conn = FakeConnection(serialize({"key": "value", "numbers": [1, 2, 3]}))
handle(conn)
```

## Handle the "address already in use" error

The default port may still be held by a previous run. Either wait, or pass a
different `port` to `serve`. In a more complete server you would also set
`SO_REUSEADDR` before binding.
