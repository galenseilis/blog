from script_1 import np
from script_1 import solve_ivp
from script_1 import plt
def van_der_pol(t, state, mu):
    x, y = state
    dxdt = y
    dydt = mu * (1 - x**2) * y - x
    return [dxdt, dydt]

mu = 1.0
y0 = [2.0, 0.0]
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(van_der_pol, t_span, y0, t_eval=t_eval, args=(mu,))

# Plot histograms
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Van der Pol Oscillator)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of y (Van der Pol Oscillator)')

plt.show()
