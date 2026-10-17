# Tutorial

This tutorial builds the table-join graph from the SQL samples in the post and
then recovers the joins that the `sqlparse` strategy misses. It should take a
few minutes.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/chatgpt-sqlparse-to-netx"
```

## 2. Build the graph with sqlparse

The package bundles the post's simple queries as `queries.sql`. Load them,
build the multigraph, and print the report:

```python
from chatgpt_sqlparse_to_netx.sqlparse_graph import build_graph, format_report, load_queries

graph = build_graph(load_queries())
print(format_report(graph))
```

The output is the report quoted in the post: five tables and four join edges.
Note that `orders` and `customers` appear twice as an edge because the join
shows up in two separate statements and the graph is a `MultiGraph`.

## 3. Try your own SQL

`build_graph` accepts any text with semicolon-separated statements:

```python
sql = """
SELECT * FROM authors a JOIN books b ON a.id = b.author_id;
SELECT * FROM books b JOIN publishers p ON b.publisher_id = p.id;
"""
print(format_report(build_graph(sql)))
```

## 4. See where sqlparse falls short

Run the same idea over the post's nested queries:

```python
from chatgpt_sqlparse_to_netx.sqlparse_graph import build_graph, format_report, load_queries

print(format_report(build_graph(load_queries("nested_queries.sql"))))
```

The tables inside the subqueries and the CTE do not appear, because the
algorithm only looks at the outermost tokens of each statement.

## 5. Recover every join with sqlglot

The `sqlglot` strategy parses the whole statement and finds joins at any
depth:

```python
from chatgpt_sqlparse_to_netx.sqlglot_joins import find_joins, load_query

joins = find_joins(load_query())
print(len(joins))                 # 7
print(joins[0].this.sql())        # the first joined table
```

You now have both halves of the package. Next, read the
[how-to guides](how-to-guides.md) for plotting and comparison recipes.
