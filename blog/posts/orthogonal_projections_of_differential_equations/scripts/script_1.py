import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def decay(t, y, k):
    return -k * y

k = 0.5
y0 = [10]
t_span = (0, 10)
t_eval = np.linspace(t_span[0], t_span[1], 100)

sol = solve_ivp(decay, t_span, y0, t_eval=t_eval, args=(k,))

# Plot histogram
plt.hist(sol.y[0], bins=10, edgecolor='black')
plt.xlabel('x')
plt.ylabel('Frequency')
plt.title('Histogram of x over time')
plt.show()
