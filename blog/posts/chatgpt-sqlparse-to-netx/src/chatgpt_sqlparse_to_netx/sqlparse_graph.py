"""Build a NetworkX multigraph of table joins with ``sqlparse``.

This is the implementation ChatGPT provided for the blog post *ChatGPTs
Attempt at Producing a Network Model From SQL Queries*, kept faithful to the
model's answer. The post goes on to show that the approach fails once the
queries contain nested subqueries or common table expressions; the
:mod:`chatgpt_sqlparse_to_netx.sqlglot_joins` module is the author's
preferred alternative.

The only behavioural change from the model's answer is that the tables are
tracked in first-seen order rather than in a ``set``. A set made the printed
report nondeterministic under hash randomisation; first-seen order is
deterministic and reproduces the output quoted in the post.
"""

from __future__ import annotations

from importlib.resources import files
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import sqlparse


def extract_tables_columns(
    sql_query: str,
) -> tuple[list[str], list[tuple[str, str]]]:
    """Extract table names and consecutive-table join conditions.

    Parameters
    ----------
    sql_query : str
        A single SQL statement.

    Returns
    -------
    tables : list of str
        The table names discovered after ``FROM``, in first-seen order.
    join_conditions : list of tuple of str
        Pairs of consecutive table names, which stand in for the joins.
    """
    parsed = sqlparse.parse(sql_query)
    tables: list[str] = []
    join_conditions: list[tuple[str, str]] = []

    for stmt in parsed:
        from_seen = False
        last_table = None

        for token in stmt.tokens:
            if token.value.upper() == "FROM":
                from_seen = True
            elif from_seen and isinstance(token, sqlparse.sql.Identifier):
                table_name = token.get_real_name()
                if table_name not in tables:
                    tables.append(table_name)
                if last_table:
                    join_conditions.append((last_table, table_name))
                last_table = table_name

    return tables, join_conditions


def build_graph(sql_text: str) -> nx.MultiGraph:
    """Build a multigraph whose nodes are tables and edges are joins.

    ``sql_text`` may contain several statements separated by semicolons, as
    in the SQL files bundled with the package.
    """
    graph = nx.MultiGraph()

    for sql_query in sql_text.split(";"):
        tables, join_conditions = extract_tables_columns(sql_query)
        for table in tables:
            graph.add_node(table)
        for left, right in join_conditions:
            graph.add_edge(left, right)

    return graph


def format_report(graph: nx.MultiGraph) -> str:
    """Return the ``Nodes:``/``Edges:`` report quoted in the blog post."""
    return f"Nodes:\n{graph.nodes()}\nEdges:\n{graph.edges()}"


def load_queries(name: str = "queries.sql") -> str:
    """Read one of the SQL files bundled with the package.

    Parameters
    ----------
    name : str
        File name inside the package's ``sql`` directory, such as
        ``queries.sql`` (the simple queries from the post) or
        ``nested_queries.sql`` (the nested queries that break the method).
    """
    return files("chatgpt_sqlparse_to_netx").joinpath("sql", name).read_text(encoding="utf-8")


def plot_graph(
    graph: nx.MultiGraph,
    output: str | Path = "chatgpt_create_multigraph_from_sql.png",
) -> Path:
    """Draw the table graph and save it to ``output``; return the path."""
    fig, ax = plt.subplots(figsize=(10, 10))

    pos = nx.spring_layout(graph, seed=42)
    node_labels = {node: node for node in graph.nodes()}
    nx.draw_networkx_labels(
        graph, pos, labels=node_labels, font_size=10, font_color="black", ax=ax
    )
    nx.draw(
        graph,
        pos,
        with_labels=False,
        node_size=300,
        node_color="skyblue",
        alpha=0.7,
        linewidths=0.5,
        font_size=10,
        ax=ax,
    )
    ax.axis("off")

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300, transparent=True)
    plt.close(fig)
    return output_path


def run(
    sql_text: str | None = None,
    output: str | Path = "chatgpt_create_multigraph_from_sql.png",
) -> nx.MultiGraph:
    """Build, print, and plot the table graph for ``sql_text``.

    ``sql_text`` defaults to the simple queries bundled with the package, so
    the printed report matches the one quoted in the blog post.
    """
    if sql_text is None:
        sql_text = load_queries()

    graph = build_graph(sql_text)
    print(format_report(graph))
    plot_graph(graph, output)
    return graph


def main() -> None:
    """Console-script entry point: run the sqlparse extraction."""
    run()


if __name__ == "__main__":
    main()
