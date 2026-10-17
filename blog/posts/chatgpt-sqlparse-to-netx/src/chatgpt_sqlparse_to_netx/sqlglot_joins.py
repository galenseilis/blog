"""Find ``JOIN`` expressions in SQL with ``sqlglot``.

This is the author's preferred first approximation from the blog post
*ChatGPTs Attempt at Producing a Network Model From SQL Queries*. The model's
``sqlparse`` version in :mod:`chatgpt_sqlparse_to_netx.sqlparse_graph` works
for the simple join queries but fails on nested subqueries and common table
expressions; ``sqlglot`` parses the whole statement into an expression tree,
so a single ``find_all`` call recovers every join regardless of nesting.

The blog post's snippet called ``find_all`` on the list returned by
``sqlglot.parse``. That list has no ``find_all`` method, so the package walks
each parsed statement and collects the joins across all of them.
"""

from __future__ import annotations

from importlib.resources import files

import sqlglot
from sqlglot import expressions


def find_joins(query_str: str) -> list[expressions.Join]:
    """Return every ``JOIN`` expression found anywhere in ``query_str``.

    ``query_str`` may contain several semicolon-separated statements; joins
    from all of them are returned in document order.
    """
    joins: list[expressions.Join] = []
    for expression in sqlglot.parse(query_str):
        joins.extend(expression.find_all(expressions.Join))
    return joins


def load_query(name: str = "nested_queries.sql") -> str:
    """Read one of the SQL files bundled with the package."""
    return files("chatgpt_sqlparse_to_netx").joinpath("sql", name).read_text(encoding="utf-8")


def run(query: str | None = None) -> list[expressions.Join]:
    """Find and print the joins in ``query``, defaulting to the bundled SQL."""
    if query is None:
        query = load_query()

    joins = find_joins(query)
    print(f"Found {len(joins)} JOIN expression(s):")
    for join in joins:
        print(join.this.sql())
    return joins


def main() -> None:
    """Console-script entry point: extract joins from the bundled SQL."""
    run()


if __name__ == "__main__":
    main()
