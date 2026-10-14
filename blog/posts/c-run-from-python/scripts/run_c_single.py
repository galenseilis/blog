"""Compile and run the single-file C example in ``hello/`` and print the output."""

import os

import run_c

here = os.path.dirname(os.path.abspath(__file__))

print(run_c.compile_and_run_c(os.path.join(here, "..", "hello")))
