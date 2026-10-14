"""Print the flower-visits data as a markdown table."""

import os

import pandas as pd

POST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv(os.path.join(POST_DIR, 'flower_visits.csv'))

print(df.to_markdown(index=False))
