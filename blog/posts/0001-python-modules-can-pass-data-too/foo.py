import json

# Open the file safely using a context manager
FILE_PATH = 'data.json'
MODE = 'r'
ENCODING = 'utf-8'

with open(FILE_PATH, MODE, encoding=ENCODING) as file:
    data = json.load(file)

# NOTE: We can put data validation right after loading for fail-fast data validation.
EXPECTED_FIELD = "datasetName"
assert data.get(EXPECTED_FIELD), f"dataset must have {EXPECTED_FIELD}?"

