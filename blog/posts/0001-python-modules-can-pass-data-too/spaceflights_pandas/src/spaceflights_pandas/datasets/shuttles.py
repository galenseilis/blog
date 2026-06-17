"""Shuttles dataset."""

# INFO: Load dependencies
import pandas as pd

# INFO: Setup dataset configuration
URL = "https://github.com/kedro-org/kedro-starters/raw/refs/heads/main/spaceflights-pandas/%7B%7B%20cookiecutter.repo_name%20%7D%7D/data/01_raw/shuttles.xlsx"

# INFO: Load data
data = pd.read_excel(URL)

if not isinstance(data, pd.DataFrame):
    msg = f"Expected {data=} to be of type {pd.DataFrame}, but got {type(data)=}"
    raise TypeError(msg)
