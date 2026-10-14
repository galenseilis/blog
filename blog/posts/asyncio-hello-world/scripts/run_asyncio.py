"""Run the asyncio "Hello, World" example and print its output.

This is a standalone version of the code that used to live in an executable
Quarto chunk. Run it from anywhere with ``python run_asyncio.py``.
"""

import os

import run_python

here = os.path.dirname(os.path.abspath(__file__))

print(run_python.run_python_file(os.path.join(here, "example.py")))
