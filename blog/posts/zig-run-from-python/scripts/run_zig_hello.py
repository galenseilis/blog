"""Build and run the ``hello`` Zig project and print its output."""

import os

from run_zig import build_and_run_zig

here = os.path.dirname(os.path.abspath(__file__))

print(build_and_run_zig(os.path.join(here, "..", "hello")))
