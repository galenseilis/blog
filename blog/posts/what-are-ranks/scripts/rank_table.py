"""Print a table of rank transforms for a sample of a binomial variable."""

import numpy as np
import pandas as pd
from scipy.stats import rankdata


np.random.seed(2018)

methods = (
  'average',
  'min',
  'max',
  'dense',
  'ordinal'
  )

d = {}
d['x'] = np.random.binomial(10, 0.5, size=10)
for method in methods:
  d[f'{method} method'] = rankdata(d['x'], method=method)

df = pd.DataFrame(d)
df = df.sort_values(by='x')
print(df.to_string(index=False))
