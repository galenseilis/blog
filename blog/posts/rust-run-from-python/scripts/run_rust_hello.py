"""Build and run the ``hello`` Rust project and print its output."""

import os

import run_rust

here = os.path.dirname(os.path.abspath(__file__))

print(run_rust.compile_and_run_rust(os.path.join(here, "..", "hello") + os.sep))
