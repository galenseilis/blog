"""Load the foo data."""

# INFO: Load dependencies
import json
import pathlib

# INFO: Configuration file IO
FILE_PATH = pathlib.Path("data.json")
MODE = "r"
ENCODING = "utf-8"

# INFO: Configuration data validation.
EXPECTED_FIELD = "datasetName"

# INFO: Open the file safely using a context manager
with FILE_PATH.open(MODE, encoding=ENCODING) as file:
    data = json.load(file)

# NOTE: We can put data validation right after loading for fail-fast data validation.
if not data.get(EXPECTED_FIELD):
    msg = f"dataset must have {EXPECTED_FIELD}?"
    raise KeyError(msg)
