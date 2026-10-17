"""Serialization and the data-processing step shared by client and server."""

from __future__ import annotations

import pickle
from typing import Any

DEFAULT_HOST = "localhost"
"""Address both scripts assume the server is listening on."""

DEFAULT_PORT = 12345
"""Port both scripts assume the server is listening on."""

BUFFER_SIZE = 4096
"""Maximum number of bytes read from the socket at once."""


def serialize(data: Any) -> bytes:
    """Turn an arbitrary object into bytes suitable for the socket."""
    return pickle.dumps(data)


def deserialize(serialized_data: bytes) -> Any:
    """Reconstruct an object from bytes received over the socket."""
    return pickle.loads(serialized_data)


def process_data(received_data: dict[str, Any]) -> dict[str, Any]:
    """Apply the server's transformation to the received data structure.

    The example transformation increments every number in the ``numbers`` list
    and relabels the ``key`` field.
    """
    return {
        "key": "processed",
        "numbers": [x + 1 for x in received_data["numbers"]],
    }
