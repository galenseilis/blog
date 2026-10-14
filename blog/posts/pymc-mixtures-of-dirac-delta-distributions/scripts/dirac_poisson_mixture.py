"""Sample a PyMC mixture of Dirac delta and Poisson distributions and save its trace plot."""

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
data = np.concatenate((data, np.random.poisson(size=m)))

# Model
model = pm.Model()

# Mixture of Dirac Delta and Poisson
with model:
    w = pm.Dirichlet('w', a=np.array([1]*(k+1)))
    mu = pm.Poisson.dist(1)

    components = [pm.DiracDelta.dist(c=i) for i in range(k)]
    components += [mu]

    likelihood = pm.Mixture('like', w=w, comp_dists=components, observed=data)

with model:
    idata = pm.sample(2000)

with model:
    az.plot_trace(idata)
    plt.tight_layout()

os.makedirs("figures", exist_ok=True)
plt.savefig("figures/dirac_poisson_mixture_trace.png", dpi=300, bbox_inches="tight")
