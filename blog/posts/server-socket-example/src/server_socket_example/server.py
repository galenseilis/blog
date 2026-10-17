"""A one-shot socket server that processes pickled data."""

from __future__ import annotations

import socket
from typing import Any, Protocol

from server_socket_example.protocol import (
    BUFFER_SIZE,
    DEFAULT_HOST,
    DEFAULT_PORT,
    deserialize,
    process_data,
    serialize,
)


class Connection(Protocol):
    """The subset of a socket connection the handler needs."""

    def recv(self, size: int) -> bytes: ...

    def sendall(self, data: bytes) -> None: ...


def handle(conn: Connection) -> Any:
    """Read one request from ``conn``, process it, and send the reply."""
    serialized_data = conn.recv(BUFFER_SIZE)
    received_data = deserialize(serialized_data)
    processed_data = process_data(received_data)
    conn.sendall(serialize(processed_data))
    return processed_data


def serve(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> None:
    """Listen for one connection, process its request, and reply."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            handle(conn)


def main() -> None:
    """Console-script entry point: run the one-shot server."""
    serve()


if __name__ == "__main__":
    main()
