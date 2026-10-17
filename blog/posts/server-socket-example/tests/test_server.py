from server_socket_example.protocol import deserialize, serialize
from server_socket_example.server import handle


class FakeConnection:
    """An in-memory stand-in for a socket connection (no port is bound)."""

    def __init__(self, incoming: bytes) -> None:
        self.incoming = incoming
        self.sent = b""

    def recv(self, size: int) -> bytes:
        return self.incoming

    def sendall(self, data: bytes) -> None:
        self.sent += data


def test_handle_processes_and_replies():
    request = {"key": "value", "numbers": [1, 2, 3]}
    conn = FakeConnection(serialize(request))

    result = handle(conn)

    assert result == {"key": "processed", "numbers": [2, 3, 4]}
    assert deserialize(conn.sent) == {"key": "processed", "numbers": [2, 3, 4]}
