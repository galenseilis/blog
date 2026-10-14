import matplotlib.pyplot as plt
import numpy as np
import pymc as pm
import arviz as az

with pm.Model() as model:
    kappa = pm.Exponential('kappa', lam=1)
    mu = pm.Uniform('mu', lower=-np.pi, upper=np.pi)
    theta = pm.VonMises('theta', mu=mu, kappa=kappa, observed=[-2]*10 + [2]*10)

with model:
    data = pm.sample(chains=4)
    az.plot_trace(data)
    plt.tight_layout()
    plt.show()
