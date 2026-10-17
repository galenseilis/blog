# API reference

## `chatgpt_sqlparse_to_netx.sqlparse_graph`

### `extract_tables_columns(sql_query) -> (tables, join_conditions)`

Scan one SQL statement and return the list of table names after `FROM` (in
first-seen order) and the list of consecutive-table pairs that stand in for
the joins.

### `build_graph(sql_text) -> networkx.MultiGraph`

Build a multigraph whose nodes are tables and whose edges are joins. The text
may contain several semicolon-separated statements.

### `format_report(graph) -> str`

Return the `Nodes:`/`Edges:` report quoted in the blog post.

### `load_queries(name="queries.sql") -> str`

Read a bundled SQL file. Use `"nested_queries.sql"` for the nested queries
from the post.

### `plot_graph(graph, output="chatgpt_create_multigraph_from_sql.png") -> pathlib.Path`

Draw the graph with a spring layout and save it as a transparent PNG. Returns
the written path.

### `run(sql_text=None, output="chatgpt_create_multigraph_from_sql.png") -> networkx.MultiGraph`

Build the graph, print the report, plot it, and return the graph. Defaults to
the bundled simple queries.

### `main()`

Console-script entry point. Calls `run()`.

## `chatgpt_sqlparse_to_netx.sqlglot_joins`

### `find_joins(query_str) -> list[sqlglot.expressions.Join]`

Return every `JOIN` expression in the (possibly multi-statement) query, in
document order.

### `load_query(name="nested_queries.sql") -> str`

Read a bundled SQL file.

### `run(query=None) -> list[sqlglot.expressions.Join]`

Find and print the joins, defaulting to the bundled nested queries.

### `main()`

Console-script entry point. Calls `run()`.

## Console scripts

| Command | Does |
| --- | --- |
| `chatgpt-sqlparse-to-netx` | Prints the table report and writes `chatgpt_create_multigraph_from_sql.png` |
| `chatgpt-sqlglot-joins` | Prints every join found in the bundled nested queries |
