"""Sample a PyMC mixture of Dirac delta distributions and save its trace plot."""

import os

import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
import numpy as np

# Sample size
m = 10**3

# Number of distributions in mixture
k = 3

# Generate data
data = np.random.randint(0,k,size=m)

# Model
basic_model = pm.Model()

# Mixture of Dirac Delta
with basic_model:
    w = pm.Dirichlet('w', a=np.array([1]*k))

    components = [pm.DiracDelta.dist(c=i) for i in range(k)]

    like = pm.Mixture('like', w=w, comp_dists=components, observed=data)

with basic_model:
    idata = pm.sample(2000)

with basic_model:
    az.plot_trace(idata)
    plt.tight_layout()

os.makedirs("figures", exist_ok=True)
plt.savefig("figures/dirac_mixture_trace.png", dpi=300, bbox_inches="tight")
