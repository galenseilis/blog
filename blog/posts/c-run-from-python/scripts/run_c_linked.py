"""Compile and run the linked-files C example in ``hello2/`` and print the output."""

import os

import run_c

here = os.path.dirname(os.path.abspath(__file__))

print(run_c.compile_and_run_c(os.path.join(here, "..", "hello2")))
