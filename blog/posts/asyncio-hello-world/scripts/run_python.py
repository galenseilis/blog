"""Run a Python file in a subprocess and capture its standard output."""

import subprocess
import sys


def run_python_file(file_path, interpreter=sys.executable):
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
