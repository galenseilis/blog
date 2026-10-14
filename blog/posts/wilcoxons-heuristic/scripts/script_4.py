'''
Plots the standard one-way ANOVA
F score and the Kruskall-Wallis ANOVA
score surfaces changing with respect to
translations of the groups of points within
the data.
'''
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

from scipy.stats import kruskal, f_oneway as anova

# Make data
np.random.seed(2018)
m = 100
x, y, z = np.random.normal(size=m*3).reshape(m,3).T

# Kruskall
alpha = np.linspace(-10, 10, num=200)
beta = np.linspace(-10, 10, num=200)
K = np.zeros((alpha.size, beta.size))

for i, ai in enumerate(alpha):
    for j, aj in enumerate(beta):
        K[i,j] = kruskal(x + ai, y + aj, z)[0]

alpha, beta = np.meshgrid(alpha, beta)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(alpha, beta, K, vmin=K.min() * 2, cmap=cm.Blues)

ax.set(xlabel='$\\alpha$',
       ylabel='$\\beta$',
       zlabel='$K$-Score')

plt.savefig('kruskall_translation_surface.png', dpi=300, transparent=True)
plt.close()


# Anova
alpha = np.linspace(-10, 10, num=200)
beta = np.linspace(-10, 10, num=200)
K = np.zeros((alpha.size, beta.size))

for i, ai in enumerate(alpha):
    for j, aj in enumerate(beta):
        K[i,j] = anova(x + ai, y + aj, z)[0]

alpha, beta = np.meshgrid(alpha, beta)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(alpha, beta, K, vmin=K.min() * 2, cmap=cm.Blues)

ax.set(xlabel='$\\alpha$',
       ylabel='$\\beta$',
       zlabel='$F$-Score')

plt.savefig('anova_translation_surface.png', dpi=300, transparent=True)
plt.close()
