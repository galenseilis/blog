"""Sort the link table before drawing.

Sorting by destination, then node, then flow is a cosmetic step: as far as the
author knows it does not change anything of substance in the diagram, but it
makes the resulting link order deterministic and easier to read.
"""

from __future__ import annotations

import pandas as pd


def sort_flows(recs: pd.DataFrame) -> pd.DataFrame:
    """Return the link table sorted by destination, node, and flow."""
    return recs.sort_values(by=["destination", "node", "flow"])
