# How-to guides

```python
import numpy as np
from parity_decomposition_in_python.parity import even_part, odd_part

f = lambda x: np.sin(x) + np.cos(x)
t = np.array([0, 1, 2])
print(even_part(f, t), odd_part(f, t))
```
