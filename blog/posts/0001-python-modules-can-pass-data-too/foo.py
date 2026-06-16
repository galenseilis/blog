"""Load the foo data."""

import json

# Open the file safely using a context manager
FILE_PATH = "data.json"
MODE = "r"
ENCODING = "utf-8"

with open(FILE_PATH, MODE, encoding=ENCODING) as file:
    data = json.load(file)

# NOTE: We can put data validation right after loading for fail-fast data validation.
EXPECTED_FIELD = "datasetName"
if not data.get(EXPECTED_FIELD):
    msg = f"dataset must have {EXPECTED_FIELD}?"
    raise KeyError(msg)
