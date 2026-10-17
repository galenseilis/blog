"""The client side of the pickle-over-sockets example.

It serializes a data structure, sends it to the server, waits for the processed
result, and deserializes it.
"""

from __future__ import annotations

import socket

from server_socket_example.protocol import (
    BUFFER_SIZE,
    DEFAULT_HOST,
    DEFAULT_PORT,
    deserialize,
    serialize,
)

EXAMPLE_DATA: dict[str, object] = {"key": "value", "numbers": [1, 2, 3]}
"""The sample data structure used by :func:`main`."""


def request(
    data_structure: dict[str, object],
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
) -> dict[str, object]:
    """Send ``data_structure`` to the server and return the processed reply."""
    serialized_data = serialize(data_structure)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(serialized_data)

        received_data = s.recv(BUFFER_SIZE)

    return deserialize(received_data)


def main() -> None:
    """Console-script entry point: send the example and print the reply."""
    processed_data = request({"key": "value", "numbers": [1, 2, 3]})
    print("Processed data received from script2.py:", processed_data)


if __name__ == "__main__":
    main()
