#!/usr/bin/env bash
set -euo pipefail

# INFO: All Posts
uvx ruff format posts

uvx ruff check \
  --select ALL \
  --fix \
  --unsafe-fixes \
  --ignore INP001,D203,D213

uvx typos posts

# INFO: $0001
echo "$(date): 0001: Building dependency graph of simple module imports..."
uvx pydeps \
  ./posts/0001-python-modules-can-pass-data-too/simple_example/bar.py \
  --no-output \
  --show-dot |
  dot -Tpng -Gdpi=300 -o ./posts/0001-python-modules-can-pass-data-too/analysis_simple_example/dependency_graph.png
echo "done"

echo "$(date): 0001: Creating tree diagram of paths in simple import module example..."
tree ./posts/0001-python-modules-can-pass-data-too/simple_example/ > ./posts/0001-python-modules-can-pass-data-too/analysis_simple_example/tree.txt
echo "done"

echo "$(date): 0001: Creating tree diagram of paths in spaceflights pandas example..."
tree ./posts/0001-python-modules-can-pass-data-too/spaceflights_pandas/ > ./posts/0001-python-modules-can-pass-data-too/analysis_spaceflights_pandas/tree.txt
echo "done"
