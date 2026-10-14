"""Plot the tangent space to a cubic curve at a point."""

import os

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim([-30, 15])
# Plot of function
x = np.linspace(-5, 5, num=100)
y = x ** 3 - 10 * x
ax.plot(x, y, color='y')
# Unit tangent vector
ax.plot([2, 3], [-12] * 2, '--', color='tab:blue')
ax.plot([3, 3], [-11, -12], '--', color='tab:blue')
# Tangent space
ax.plot(x, 2 * x - 16, color='m')
ax.text(3, -12, r'$T_pC$', color='m')
ax.scatter(2, -12, color='m')
ax.text(2, -14, r'$p$', color='m')
ax.annotate(r'slope$=f^{\prime}(a)$', xy=(4, -8), xytext=(4, 0),
             arrowprops=dict(facecolor='black', shrink=0.05), color='grey')
# Pullbacks
ax.plot([2] * 2, [-30, -12], '--', color='m', alpha=0.5)
ax.text(2, -30, r'$a$', color='m')
ax.plot([x.min(), 2], [-12] * 2, '--', color='m', alpha=0.5)
ax.text(x.min(), -12, 'f(a)', color='m')

here = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(here, os.pardir, "figures")
os.makedirs(figures_dir, exist_ok=True)
plt.savefig(os.path.join(figures_dir, "tangent_space_cubic.png"), dpi=300, bbox_inches="tight")
plt.close()
