from math import factorial
import sys

import pandas as pd

sys.set_int_max_str_digits(1_000_000)

k = 1000 + 1
m = 200

def is_pandigital(num):
	s = str(num)
	for i in range(10):
		if str(i) not in s:
			return False
	return True

results = []

for n in range(k):
	fact_n = factorial(n)
	fact_str = str(fact_n)[::-1][:m][::-1]

	results.append([n, is_pandigital(fact_str), fact_str])


df = pd.DataFrame(results, columns=["n", f"last_{m}_is_pandigital",  f"last_{m}"])

print(df.to_markdown(index=False))
