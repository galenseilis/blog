from script_1 import recs
first_nodes = (
    recs.sort_values(by="arrival_date")
    .groupby("id_number")["node"]
    .apply(lambda x: x.iloc[0])
    .value_counts()
    .reset_index(name="flow")
    .rename(columns={"index": "destination"})
    .assign(node=0)
)
