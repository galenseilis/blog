# How-to guides

Practical recipes for common tasks.

## Reproduce the post's report and figure

Run the console script from the post directory:

```bash
chatgpt-sqlparse-to-netx
```

It prints the `Nodes:`/`Edges:` report quoted in the post and writes
`chatgpt_create_multigraph_from_sql.png`.

## Use your own SQL text

`build_graph` and `find_joins` both take a string, so read the SQL from
wherever you keep it:

```python
from pathlib import Path

from chatgpt_sqlparse_to_netx.sqlparse_graph import build_graph, format_report

sql = Path("my_queries.sql").read_text()
print(format_report(build_graph(sql)))
```

## Plot the table graph to a custom path

```python
from chatgpt_sqlparse_to_netx.sqlparse_graph import build_graph, load_queries, plot_graph

plot_graph(build_graph(load_queries()), "out/tables.png")
```

`plot_graph` creates parent directories, draws a spring layout with the node
labels, and saves a transparent PNG.

## Compare the two strategies

Build the graph with `sqlparse` and then check whether its edges agree with
the joins `sqlglot` finds:

```python
from chatgpt_sqlparse_to_netx.sqlglot_joins import find_joins, load_query
from chatgpt_sqlparse_to_netx.sqlparse_graph import build_graph, load_queries

sqlparse_edges = set(build_graph(load_queries("nested_queries.sql")).edges())
sqlglot_joins = [join.this.sql() for join in find_joins(load_query())]
print(len(sqlparse_edges), len(sqlglot_joins))
```

## Inspect a single join

`find_joins` returns `sqlglot` expression objects, so you can call any
`sqlglot` method on them:

```python
from chatgpt_sqlparse_to_netx.sqlglot_joins import find_joins

for join in find_joins("SELECT * FROM a JOIN b ON a.id = b.id"):
    print(type(join).__name__, join.this.sql())
```
