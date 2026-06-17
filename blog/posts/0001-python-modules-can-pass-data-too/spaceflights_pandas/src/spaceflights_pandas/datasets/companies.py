"""Companies dataset.

It loads only once, and there is no caching in this example.
These can be added as-needed.
"""

import pandas as pd

# NOTE: If we wanted to, we could declare a `load` function.
URL = (
    "https://"
    "raw.githubusercontent.com/"
    "kedro-org/"
    "kedro-starters/"
    "refs/"
    "heads/"
    "main/"
    "spaceflights-pandas/"
    "%7B%7B%20cookiecutter.repo_name%20%7D%7D/"
    "data/"
    "01_raw/"
    "companies.csv"
)

EXPECTED_COLUMNS = (
    "iata_approved",
    "company_rating",
)

data = pd.read_csv(URL)

# INFO: Input validation
# - we could go on to validate various properties of the data here.
# WARN: Assertions can be turned off by running Python in optimized mode.
if not isinstance(data, pd.DataFrame):
    msg = f"{data=} must be of type {pd.DataFrame}"
    raise TypeError(msg)

for expected_column in EXPECTED_COLUMNS:
    if expected_column not in data.columns:
        msg = f"Expected column '{expected_column}' to be in columns of {data.columns=}"
        raise ValueError(msg)

# TODO: Check expected types of expected columns.
