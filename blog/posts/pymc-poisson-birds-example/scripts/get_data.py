"""Fetch the Stack Exchange question page that contains the flower-visits data."""

import requests

# URL of the Stack Exchange question
url = "https://stats.stackexchange.com/q/651343/69508"

# Send a request to the URL
response = requests.get(url)
response.raise_for_status()
