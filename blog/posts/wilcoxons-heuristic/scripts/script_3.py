import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import mannwhitneyu, ttest_ind

U = lambda x,y: mannwhitneyu(x,y)[0]
T = lambda x,y: ttest_ind(x,y)[0]

# Generate data
np.random.seed(2018)

us = []
ts = []
for i in range(10000):
    x = np.random.normal(size=1000)
    y = np.random.normal(size=1000) + 4
    us.append(U(x,y))
    ts.append(T(x,y))

# Plot scatter
plt.scatter(ts, us, s=1)
plt.xlabel('t-Score')
plt.ylabel('U-Score')
plt.savefig('randomize_u_vs_t.png', dpi=300, transparent=True)
plt.tight_layout()
plt.close()
