"""Print the simulated autoregressive data for the example."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from simulate import ar_data

print(ar_data)
