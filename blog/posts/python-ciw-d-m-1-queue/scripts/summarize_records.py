"""Summarize the D/M/1 queue records with a Markdown table."""

import pandas as pd

from simulate_queue import records

records = pd.DataFrame(records)
print(
    records
    [['waiting_time', 'service_time', 'queue_size_at_arrival', 'queue_size_at_departure']]
    .describe()
    .to_markdown()
    )
