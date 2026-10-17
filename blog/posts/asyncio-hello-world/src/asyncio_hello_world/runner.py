"""Run a Python file in a subprocess and capture its standard output."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run_python_file(
    file_path: str | Path,
    interpreter: str = sys.executable,
) -> str:
    """Run ``file_path`` with ``interpreter`` and return its standard output.

    If the child exits with a non-zero status, the error message printed to
    standard error is returned instead of raising.
    """
    try:
        result = subprocess.run(
            [interpreter, file_path],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred while running the file: {e.stderr}"
