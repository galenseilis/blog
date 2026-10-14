import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import rankdata, zipf

# Config
np.random.seed(2018)

# Generate data
M = 10000
x = np.random.normal(size=M)
y = np.random.binomial(n=10, p=0.5, size=M)
z = zipf.rvs(2, size=M)

# Create plots
fig, axes = plt.subplots(2,3)

axes[0][0].hist(x,  label='Normal')
axes[0][0].legend()
axes[0][1].bar(*np.unique(y, return_counts=True), label='Binomial')
axes[0][1].legend()
axes[0][2].bar(*np.unique(z, return_counts=True), label='Zipf')
axes[0][2].legend()

axes[1][0].bar(*np.unique(rankdata(x, method='dense'), return_counts=True),  label='Rank(Normal)')
axes[1][0].legend()
axes[1][1].bar(*np.unique(rankdata(y, method='dense'), return_counts=True),  label='Rank(Binomial)')
axes[1][1].legend()
axes[1][2].bar(*np.unique(rankdata(z, method='dense'), return_counts=True),  label='Rank(Zipf)')
axes[1][2].set_yscale('log')
axes[1][2].legend()

plt.tight_layout()
plt.savefig('dist_noninvariant_to_ranking.png', dpi=300, transparent=True)
plt.close()
