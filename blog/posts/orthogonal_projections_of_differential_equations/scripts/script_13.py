import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def chuas_circuit(t, state, alpha, beta, m0, m1):
    x, y, z = state

    # Chua's diode piecewise-linear function
    h = m1 * x + 0.5 * (m0 - m1) * (np.abs(x + 1) - np.abs(x - 1))

    dxdt = alpha * (y - x - h)
    dydt = x - y + z
    dzdt = -beta * y

    return [dxdt, dydt, dzdt]

# Parameters
alpha = 15.6
beta = 28.0
m0 = -1.143
m1 = -0.714

# Initial conditions
y0 = [0.7, 0.0, 0.0]
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Solve the differential equations
sol = solve_ivp(chuas_circuit, t_span, y0, t_eval=t_eval, args=(alpha, beta, m0, m1))

# Plot histograms
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Chua\'s Circuit)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of y (Chua\'s Circuit)')

axs[2].hist(sol.y[2], bins=30, edgecolor='black')
axs[2].set_xlabel('z')
axs[2].set_ylabel('Frequency')
axs[2].set_title('Histogram of z (Chua\'s Circuit)')

plt.show()
