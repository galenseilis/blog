'''
This script loads the data generated in the previous script
and plots it.
'''
import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

post_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
figures_dir = os.path.join(post_dir, "figures")
os.makedirs(figures_dir, exist_ok=True)

# Load data
df = pd.read_csv(os.path.join(post_dir, 'select_dynamics_data.csv'))
all_df = pd.read_csv(os.path.join(post_dir, 'all_dynamics_data.csv'))

# Histogram
for time, dfi in df.groupby('Time'):
    if time in (0.1, 0.2):
        plt.hist(dfi.X, label=f'Time={time}')
    else:
        continue
plt.xlabel('X')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()

# Box Plot
sns.boxplot(data=df, x='Time', y='X', hue='Time', dodge=False)
plt.tight_layout()

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for time, dfi in df.groupby('Time'):
    ax.scatter(*dfi[['X', 'Y', 'Z']].to_numpy().T, label=f'Time={time}')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(figures_dir, 'dynamics_3D_scatter.png'), dpi=300, transparent=True)

ax.plot(*all_df[['X', 'Y', 'Z']].to_numpy().T, color='k')
plt.savefig(os.path.join(figures_dir, 'dynamics_3D_all.png'), dpi=300, transparent=True)
plt.close()
