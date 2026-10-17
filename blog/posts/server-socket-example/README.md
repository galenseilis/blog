# server-socket-example

A minimal client-server example: the client serializes a Python data structure
with [`pickle`](https://docs.python.org/3/library/pickle.html) and sends it over
a TCP socket; the server deserializes it, processes it, serializes the result and
sends it back.

The client and server are the two scripts from the blog post
[Basic Example of Using Sockets to Communicate and Process Data in Python](https://galenseilis.github.io/blog/posts/server-socket-example/),
turned into importable modules. The pure data-processing step lives in
`server_socket_example.protocol`, which is all the test suite exercises -- no
port is ever bound during tests.

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/server-socket-example"
```

The package has no third-party dependencies and requires Python 3.11 or newer.

## Usage

Start the server in one terminal:

```bash
server-socket-example-server
```

Then run the client in another:

```bash
server-socket-example-client
```

```text
Processed data received from script2.py: {'key': 'processed', 'numbers': [2, 3, 4]}
```

Or call the modules directly:

```python
from server_socket_example.client import request
from server_socket_example.protocol import process_data

# Pure logic, safe to use anywhere:
process_data({"key": "value", "numbers": [1, 2, 3]})
# {'key': 'processed', 'numbers': [2, 3, 4]}
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
