import networkx as nx

from chatgpt_sqlparse_to_netx.sqlparse_graph import (
    build_graph,
    extract_tables_columns,
    format_report,
    load_queries,
    run,
)

POST_REPORT = (
    "Nodes:\n"
    "['employees', 'orders', 'customers', 'order_items', 'products']\n"
    "Edges:\n"
    "[('orders', 'customers'), ('orders', 'customers'), "
    "('customers', 'order_items'), ('order_items', 'products')]"
)


def test_extract_tables_from_a_single_query():
    tables, joins = extract_tables_columns("SELECT a FROM orders o JOIN customers c ON 1 = 1")
    assert tables == ["orders", "customers"]
    assert joins == [("orders", "customers")]


def test_extract_tables_of_a_query_without_joins():
    tables, joins = extract_tables_columns("SELECT first_name FROM employees")
    assert tables == ["employees"]
    assert joins == []


def test_build_graph_has_the_expected_nodes():
    graph = build_graph(load_queries())
    assert list(graph.nodes()) == [
        "employees",
        "orders",
        "customers",
        "order_items",
        "products",
    ]


def test_build_graph_has_the_expected_edges():
    graph = build_graph(load_queries())
    assert list(graph.edges()) == [
        ("orders", "customers"),
        ("orders", "customers"),
        ("customers", "order_items"),
        ("order_items", "products"),
    ]


def test_build_graph_is_a_multigraph():
    graph = build_graph(load_queries())
    assert graph.is_multigraph()


def test_format_report_matches_the_blog_post():
    graph = build_graph(load_queries())
    assert format_report(graph) == POST_REPORT


def test_run_prints_the_report_and_writes_a_figure(tmp_path, capsys):
    output = tmp_path / "graph.png"
    graph = run(output=output)
    captured = capsys.readouterr()
    assert captured.out.strip() == POST_REPORT
    assert output.exists()
    assert isinstance(graph, nx.MultiGraph)
