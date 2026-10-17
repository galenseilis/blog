from sqlglot import expressions

from chatgpt_sqlparse_to_netx.sqlglot_joins import find_joins, load_query, run


def test_find_joins_in_a_single_join_query():
    joins = find_joins("SELECT a FROM orders o JOIN customers c ON 1 = 1")
    assert len(joins) == 1
    assert isinstance(joins[0], expressions.Join)


def test_find_joins_in_a_query_without_joins():
    assert find_joins("SELECT first_name FROM employees") == []


def test_find_joins_across_all_bundled_statements():
    assert len(find_joins(load_query())) == 7


def test_find_joins_recovers_the_nested_join():
    joins = find_joins(load_query())
    sources = [join.this.sql() for join in joins]
    assert any(source.startswith("(SELECT order_id") for source in sources)


def test_run_returns_the_joins_it_prints(capsys):
    joins = run()
    captured = capsys.readouterr()
    assert captured.out.startswith("Found 7 JOIN expression(s):")
    assert len(joins) == 7
