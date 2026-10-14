"""Plot the tangent space to a parabola at a point."""

import os

import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim([-5, 15])
# Plot of function
x = np.linspace(-5, 5, num=100)
y = x**2
ax.plot(x, y, color='y')
# Unit tangent vector
ax.plot([2, 2], [1, 3], '--', color='tab:blue')
ax.plot([1, 2], [1, 1], '--', color='tab:blue')
# Tangent space
ax.plot(x, 2 * x - 1, color='m')
ax.text(2, 1, r'$T_pC$', color='m')
ax.scatter(1, 1, color='m')
ax.text(1, 0, r'$p$', color='m')
# Pullbacks
ax.plot([1] * 2, [-5, 1], '--', color='m', alpha=0.5)
ax.text(1, -5, r'$a$', color='m')
ax.plot([-5, 1], [1] * 2, '--', color='m', alpha=0.5)
ax.text(-5, 1, 'f(a)', color='m')
plt.tight_layout()

here = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(here, os.pardir, "figures")
os.makedirs(figures_dir, exist_ok=True)
plt.savefig(os.path.join(figures_dir, "tangent_space_quadratic.png"), dpi=300, bbox_inches="tight")
plt.close()
