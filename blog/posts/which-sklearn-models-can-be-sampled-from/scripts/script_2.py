import numpy as np
rng = np.random.RandomState(2018)
X = rng.randint(5, size=(6, 100))
Y = np.array([1, 2, 3, 4, 4, 5])
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
clf.fit(X, Y)
prob_first_entry = clf.predict_proba(X)[0]
first_row_sample = rng.multinomial(1, prob_first_entry, size=10_000)
