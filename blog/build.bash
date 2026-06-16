#!/usr/bin/env bash
set -euo pipefail

# INFO: All Posts
uvx ruff format posts
uvx ruff check --select ALL --fix --unsafe-fixes

# INFO: $0001
echo "Building files for post 0001"
uvx pydeps \
  ./posts/0001-python-modules-can-pass-data-too/bar.py \
  --no-output \
  --show-dot |
  dot -Tpng -Gdpi=300 -o ./posts/0001-python-modules-can-pass-data-too/dependency_graph.png
