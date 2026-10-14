"""Print a summary of the posterior distribution sampling trace."""

import os
import sys

import arviz as az

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sample_model import trace

print(az.summary(trace, round_to=2).to_markdown())
