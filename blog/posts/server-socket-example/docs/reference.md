# API reference

## `server_socket_example.protocol`

Shared constants, serialization, and the pure processing step.

### Constants

- `DEFAULT_HOST = "localhost"` — the address both sides assume.
- `DEFAULT_PORT = 12345` — the port both sides assume.
- `BUFFER_SIZE = 4096` — maximum bytes read from a socket at once.

### `serialize(data)`

Return `pickle.dumps(data)`.

### `deserialize(serialized_data)`

Return `pickle.loads(serialized_data)`.

### `process_data(received_data)`

Return the transformed mapping
`{"key": "processed", "numbers": [x + 1 for x in received_data["numbers"]]}`.
The input is not modified.

## `server_socket_example.client`

### `request(data_structure, host=DEFAULT_HOST, port=DEFAULT_PORT)`

Serialize `data_structure`, connect to the server, send the bytes, read the
reply, and return the deserialized result.

### `main()`

Console entry point for `server-socket-example-client`. Sends the example
payload and prints the reply.

## `server_socket_example.server`

### `handle(conn)`

Read one request from a connection-like object, deserialize it, process it,
send the serialized reply, and return the processed object. `conn` only needs
`recv(size)` and `sendall(data)`.

### `serve(host=DEFAULT_HOST, port=DEFAULT_PORT)`

Bind, listen, accept one connection, print the peer address, and call
`handle`. This binds a real port and should not be called from tests.

### `main()`

Console-script entry point that calls `serve()`.

## Console scripts

- `server-socket-example-server` — runs `server.main`.
- `server-socket-example-client` — runs `client.main`.
