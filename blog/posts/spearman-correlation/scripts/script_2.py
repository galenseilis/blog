from itertools import permutations

import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import pearsonr
corr = lambda x,y: pearsonr(x,y)[0]

fig, axes = plt.subplots(6,4)
axes = axes.flatten()

x = list(range(1,5))
perms = permutations(x)
for k, y in enumerate(perms):
    img = np.zeros((4,4))
    for i,j in zip(x,y):
        img[i-1,j-1] = 1
    axes[k].imshow(img, origin='lower')
    axes[k].axis('off')
    
axes = axes.reshape((6,4))
plt.tight_layout()
plt.savefig("perm_grid.png", bbox_inches='tight', dpi=300, transparent=True)
plt.close()
