# Tutorial

```python
import numpy as np
from parity_decomposition_in_python.parity import plot_parity_decomposition

f = lambda t: np.exp(np.cos(t) + np.sin(t))
t = np.linspace(-2*np.pi, 2*np.pi, 1000)
plot_parity_decomposition(f, t)
```
