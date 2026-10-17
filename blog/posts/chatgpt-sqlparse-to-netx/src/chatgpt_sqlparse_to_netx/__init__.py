"""Extract a network model on database tables from SQL queries.

The package accompanies the blog post *ChatGPTs Attempt at Producing a
Network Model From SQL Queries*. It contains two extraction strategies:

* :mod:`chatgpt_sqlparse_to_netx.sqlparse_graph` is the implementation
  ChatGPT produced with :mod:`sqlparse`.
* :mod:`chatgpt_sqlparse_to_netx.sqlglot_joins` is the author's preferred
  first approximation using :mod:`sqlglot`.
"""

from __future__ import annotations

from chatgpt_sqlparse_to_netx.sqlglot_joins import find_joins
from chatgpt_sqlparse_to_netx.sqlparse_graph import build_graph

__all__ = ["build_graph", "find_joins"]

__version__ = "0.1.0"
