import numpy as np
from sklearn.mixture import BayesianGaussianMixture
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [12, 4], [10, 7]])
bgm = BayesianGaussianMixture(n_components=2, random_state=42).fit(X)
sampled_X, sampled_labels = bgm.sample(10_000)
