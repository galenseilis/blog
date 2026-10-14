import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind as ttest, mannwhitneyu

# Skip p-values
tscore = lambda a,b: ttest(a, b)[0]
uscore = lambda a,b: mannwhitneyu(a, b)[0]

# Grid sweep global translation
np.random.seed(2018)
m = 1000
x = np.random.normal(size=m)
y = np.random.normal(size=m)
A = np.linspace(-10, 10, num=1000)

# Compute translated scores
tscores = []
uscores = []
for alpha in A:
    dx = x + alpha
    tscores.append(tscore(dx, y))
    uscores.append(uscore(dx, y))

# Pairwise plots
plt.scatter(tscores, uscores, s=1)
plt.xlabel('t score')
plt.ylabel('U score')
plt.savefig('U_vs_t.png', dpi=300, transparent=True)
plt.close()


plt.step(A, uscores)
plt.xlabel('$\\alpha$')
plt.ylabel('U score')
plt.savefig('U_vs_alpha.png', dpi=300, transparent=True)
plt.close()

plt.step(A, tscores)
plt.xlabel('$\\alpha$')
plt.ylabel('t score')
plt.savefig('t_vs_alpha.png', dpi=300, transparent=True)
plt.close()
