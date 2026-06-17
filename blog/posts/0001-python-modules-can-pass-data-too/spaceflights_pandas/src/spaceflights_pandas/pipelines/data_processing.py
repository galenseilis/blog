"""Data processing pipeline.

Note that if you're pulling from a SQL database that you can
get the SQL database to do more of the work instead of Python.
"""

import spaceflights_pandas.datasets.companies
import spaceflights_pandas.datasets.reviews
import spaceflights_pandas.datasets.shuttles

# NOTE: Compared to the Kedro example, we use Python variables
# instead of strings.

# NOTE: at this point we 'could' just reuse the functions they're specified.
# Copy them into another module and then import them.
# However, some of these functions look like they can be replaced
# by a few pandas method chains.
processed_companies = spaceflights_pandas.datasets.companies.data.assign(
    # WARN: Kedro example if overriding a column name.
    iata_approved=lambda df: df["iata_approved"].eq("t"),
    company_rating=lambda df: (
        df["company_rating"].str.removesuffix("%").astype(float).div(100)
    ),
)

processed_shuttles = spaceflights_pandas.datasets.shuttles.data.assign(
    # WARN: Kedro example is overriding a column name.
    d_check_complete=lambda df: df["d_check_complete"].eq("t"),
    # WARN: Kedro example is overriding a column name.
    moon_clearance_complete=lambda df: df["moon_clearance_complete"].eq("t"),
    # WARN: Kedro example is overriding a column name.
    price=lambda df: (
        df["price"]
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .astype(float)
    ),
)

model_input_table = (
    processed_shuttles.merge(
        spaceflights_pandas.datasets.reviews.data,
        left_on="id",
        right_on="shuttle_id",
    )
    .drop(columns="id")
    .merge(processed_companies, left_on="company_id", right_on="id")
    .dropna()
)
