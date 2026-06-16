"""Companies dataset.

It loads only once, and there is no caching in this example. These can be added as-needed.
"""

import pandas as pd

# NOTE: If we wanted to, we could declare a `load` function. However in such a simple example that's not needed to illustrate modules in DS pipelines.
URL = "https://raw.githubusercontent.com/kedro-org/kedro-starters/refs/heads/main/spaceflights-pandas/%7B%7B%20cookiecutter.repo_name%20%7D%7D/data/01_raw/companies.csv"
data = pd.read_csv(URL)
