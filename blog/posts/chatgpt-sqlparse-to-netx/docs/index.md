# chatgpt-sqlparse-to-netx documentation

`chatgpt-sqlparse-to-netx` turns SQL queries into a NetworkX model of the
tables and the joins between them. It contains two strategies: a `sqlparse`
implementation that ChatGPT wrote for the blog post, and a `sqlglot`
first approximation that the author prefers.

The `sqlparse` version scans the top-level tokens of each statement, collects
the table names after `FROM`, and links each table to the one before it. That
is enough for a flat chain of joins and produces the `Nodes:`/`Edges:` report
quoted in the post, but it silently misses joins inside nested subqueries and
common table expressions. The `sqlglot` version parses the statement into an
expression tree and finds every `JOIN`, so it works on the nested cases too.

The project follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): build the table graph and recover the joins from
  nested queries.
- [How-to guides](how-to-guides.md): use your own SQL, plot the graph, and
  compare the two strategies.
- [Reference](reference.md): the public API and the console scripts.
- [Explanation](explanation.md): why the `sqlparse` approach fails on nested
  queries and what `sqlglot` does differently.
