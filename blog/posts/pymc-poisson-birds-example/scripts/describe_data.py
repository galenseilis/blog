"""Summarize the flower-visits data grouped by category and species."""

import os

import pandas as pd

POST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv(os.path.join(POST_DIR, 'flower_visits.csv'))

print(df.groupby(by=['Category_ID', 'Species']).describe())
