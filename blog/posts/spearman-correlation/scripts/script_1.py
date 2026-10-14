from itertools import permutations

import pandas as pd

perms = list(permutations(range(1,5)))
cols = [f'$\\operatorname{{rank}}(X_{i})$' for i in range(1,5)]
df = pd.DataFrame(data=perms, columns=cols)
print(df.to_markdown(index=False))
