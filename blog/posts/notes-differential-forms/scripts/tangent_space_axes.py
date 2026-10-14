"""Visualize a tangent vector in terms of the differential axes."""

import os

import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
ax.spines[['top', 'right']].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
ax.annotate("", xy=(2, 2), xytext=(1, 1),
            arrowprops=dict(color='tab:blue'))
plt.text(2, 2, r'$\langle c,d \rangle_{(a,b)}$', color='gray')
ax.annotate("", xy=(1, 2.5), xytext=(1, 0.9),
            arrowprops=dict(color='m'))
ax.annotate("", xy=(2.5, 1), xytext=(0.9, 1),
            arrowprops=dict(color='m'))
ax.text(2.5, 1, 'dx', color='grey')
ax.text(1, 2.5, 'dy', color='grey')
ax.text(2, 1, 'c', color='grey')
ax.text(1, 2, 'd', color='grey')
ax.text(2, 0, 'a', color='grey')
ax.text(0, 2, 'b', color='grey')
plt.tight_layout()

here = os.path.dirname(os.path.abspath(__file__))
figures_dir = os.path.join(here, os.pardir, "figures")
os.makedirs(figures_dir, exist_ok=True)
plt.savefig(os.path.join(figures_dir, "tangent_space_axes.png"), dpi=300, bbox_inches="tight")
plt.close()
