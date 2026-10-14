from script_1 import recs
recs = (
        recs
        .groupby(by=["node", "destination"])
        .size()
        .reset_index(name="flow")
        .replace({-1:4})
        )
