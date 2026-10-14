"""Build and run the ``des`` Rust project and print its output."""

import os

from run_rust import compile_and_run_rust

here = os.path.dirname(os.path.abspath(__file__))

print(compile_and_run_rust(os.path.join(here, "..", "des") + os.sep))
