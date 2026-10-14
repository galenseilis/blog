import pandas as pd

d = {}
d['rank'] = list(range(1,11))

for i in range(1,11):
    d[f'$\\mathbb{{I}}(\\operatorname{{rank}} \\leq {i})$'] = [int(j <= i) for j in d['rank']]

df = pd.DataFrame(d)

print(df.to_markdown(index=False))
