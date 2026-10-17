# chatgpt-sqlparse-to-netx

Extract a NetworkX model of table joins from SQL queries.

This package accompanies the blog post
[ChatGPTs Attempt at Producing a Network Model From SQL Queries](https://galenseilis.github.io/blog/posts/chatgpt-sqlparse-to-netx/).
It packages two extraction strategies side by side:

- **`sqlparse_graph`** — the implementation ChatGPT produced with
  [`sqlparse`](https://sqlparse.readthedocs.io/). It scrapes table names after
  `FROM` and between joins into a `networkx.MultiGraph`, and prints the
  `Nodes:`/`Edges:` report quoted in the post.
- **`sqlglot_joins`** — the author's preferred first approximation with
  [`sqlglot`](https://sqlglot.com/). It parses the whole statement into an
  expression tree and recovers every `JOIN`, including joins hidden inside
  nested subqueries and CTEs.

The package bundles the two SQL samples the post uses: `queries.sql` (the
simple case the `sqlparse` version handles) and `nested_queries.sql` (the
expanded cases where it fails).

## Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/chatgpt-sqlparse-to-netx"
```

Requires Python 3.11 or newer, and depends on `networkx`, `matplotlib`,
`sqlparse`, and `sqlglot`.

## Quick start

```python
from chatgpt_sqlparse_to_netx.sqlparse_graph import build_graph, format_report, load_queries

graph = build_graph(load_queries())
print(format_report(graph))
```

```text
Nodes:
['employees', 'orders', 'customers', 'order_items', 'products']
Edges:
[('orders', 'customers'), ('orders', 'customers'), ('customers', 'order_items'), ('order_items', 'products')]
```

The `sqlglot` alternative recovers joins from the nested queries that the
`sqlparse` version misses:

```python
from chatgpt_sqlparse_to_netx.sqlglot_joins import find_joins, load_query

len(find_joins(load_query()))  # 7 joins across all statements
```

Or from the console:

```bash
chatgpt-sqlparse-to-netx   # prints the report and writes chatgpt_create_multigraph_from_sql.png
chatgpt-sqlglot-joins      # prints the joins found in the nested queries
```

## Documentation

- [Documentation index](docs/index.md)
- [Tutorial](docs/tutorials.md)
- [How-to guides](docs/how-to-guides.md)
- [API reference](docs/reference.md)
- [Explanation](docs/explanation.md)

## License

Released for reuse with attribution to the original blog post.
