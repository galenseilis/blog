# Explanation

## The goal: a network model of a schema

A collection of SQL queries is an implicit description of a schema. Every
`JOIN` names two tables that share a key, so the queries induce a multigraph
whose nodes are tables and whose edges are join relationships. Recovering that
graph is useful for ranking central tables, spotting unused ones, or
documenting how a warehouse is stitched together.

## What token scanning can and cannot see

The `sqlparse` implementation works at the top level of a statement. It walks
the statement's tokens, notices the `FROM` keyword, and treats each following
identifier as a table, linking it to the one before. For a flat chain of joins
that is exactly right: `FROM a JOIN b JOIN c JOIN d` yields `a—b—c—d`.

The approach breaks as soon as the query nests. A subquery is a single
`Parenthesis` token at the top level, so the tables inside it are invisible;
the same is true of the CTE body in a `WITH` clause. The model's code also
ignores the actual `ON` conditions, so it records adjacency rather than the
key relationships the joins express, and it treats every identifier as a
table even when it is a subquery alias.

## Why a real parser helps

`sqlglot` does not scan text; it parses the statement into an expression tree
in which `SELECT`, `FROM`, and `JOIN` are distinct node types, and a subquery
is simply a `SELECT` node nested inside another. Searching that tree for join
nodes therefore reaches joins at any depth. That is why the author reports it
as "an easy first approximation".

The `sqlglot` snippet in the post was a first sketch, and it called
`find_all` on the list returned by `sqlglot.parse`. A list has no `find_all`,
so the package walks each parsed statement and gathers the joins across all of
them instead.

## What is still left to do

Even with `sqlglot`, the schema graph is only a first approximation. The
joined table on each side of an `ON` is available, but extracting the key
columns, normalising aliases, resolving CTE references back to their sources,
and deciding how to represent self-joins or non-equi joins all remain as
ordinary string and tree processing on top of the parsed expressions. The
package stops at the pleasant point where the parser has done the hard
structural work and the remaining decisions are application-specific.
