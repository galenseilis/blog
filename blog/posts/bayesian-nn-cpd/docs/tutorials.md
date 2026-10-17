# Tutorials

Build the model.

```python
from bayesian_nn_cpd.model import build_model, simulate_data

observed, size = simulate_data(size=3)
model = build_model(size=size, observed=observed)
```
