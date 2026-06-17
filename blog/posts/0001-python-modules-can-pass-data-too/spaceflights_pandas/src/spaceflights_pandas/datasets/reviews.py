"""Reviews dataset."""

# INFO: Load dependencies
import pandas as pd

# INFO: Setup configuration
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
    "reviews.csv"
)

# INFO: Load data
data = pd.read_csv(URL)

# INFO: Validate data
if not isinstance(data, pd.DataFrame):
    msg = f"{data=} was expected to be of type {pd.DataFrame}"
    raise TypeError(msg)
