"""A minimal pickle-over-sockets client and server example.

The package mirrors the two scripts from the blog post:

* :mod:`server_socket_example.protocol` -- serialization plus the pure data
  processing step, shared by both sides.
* :mod:`server_socket_example.client` -- the client that sends a data structure
  and reads back the processed result.
* :mod:`server_socket_example.server` -- the one-shot server that receives,
  processes, and replies.

Only :mod:`server_socket_example.protocol` is exercised by the test suite; the
client and server touch real sockets and are kept behind their ``main()``
functions so that importing the package never binds a port.
"""

from __future__ import annotations

__all__ = ["__version__"]

__version__ = "0.1.0"
