"""Parse the flower-visits table out of the question page and save it as a CSV."""

import os
import sys
from io import StringIO

import pandas as pd
from bs4 import BeautifulSoup

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from get_data import response

POST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the code block containing the example data
code_blocks = soup.find_all('code')

# Search for the specific code block containing "visits_df"
example_data = ""
for block in code_blocks:
    if "visits_df" in block.text:
        example_data = block.text
        break

# Clean the extracted example data
# Remove the non-tabular lines and headers
lines = example_data.split("\n")
data_lines = lines[2:]  # Skip the first two lines of metadata

# Join the data lines into a single string
cleaned_data = "\n".join(data_lines)

# Convert the cleaned data into a pandas DataFrame
data = StringIO(cleaned_data)

# Try reading the data with a custom delimiter
df = pd.read_fwf(data, widths=[12, 24, 12], header=None, skiprows=1, names=['Category_ID', 'Species', 'Total_visits'])
df = df.drop(index=0)
df['Category_ID'] = df['Category_ID'].apply(lambda s: s.split(' ')[1])
df['Total_visits'] = df['Total_visits'].astype(int)

df.to_csv(os.path.join(POST_DIR, 'flower_visits.csv'), index=False)
