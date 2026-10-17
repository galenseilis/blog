# Tutorial

This tutorial runs the full round trip in about five minutes.

## 1. Start the server

Open a terminal and run:

```bash
server-socket-example-server
```

The server binds `localhost:12345`, waits for a single connection, prints the
client address, and replies. It then exits; this example handles exactly one
request.

## 2. Run the client

In a second terminal:

```bash
server-socket-example-client
```

```text
Processed data received from script2.py: {'key': 'processed', 'numbers': [2, 3, 4]}
```

## 3. Follow the data

1. The client builds `{"key": "value", "numbers": [1, 2, 3]}`.
2. `serialize` turns it into bytes with `pickle.dumps`.
3. The client connects and sends the bytes.
4. The server deserializes them, calls `process_data`, which increments every
   number.
5. The server serializes the result and sends it back.
6. The client deserializes the reply and prints it.

## 4. Use only the pure logic

The processing step needs no sockets at all:

```python
from server_socket_example.protocol import process_data

process_data({"key": "value", "numbers": [1, 2, 3]})
```

This is what the package's tests cover, so you can run them without a network.

## 5. Where to go next

- [How-to guides](how-to-guides.md) for changing the example.
- [Reference](reference.md) for the full API.
