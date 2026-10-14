from script_1 import np
from script_1 import solve_ivp
from script_1 import plt
def lotka_volterra(t, z, a, b, c, d):
    x, y = z
    dxdt = a * x - b * x * y
    dydt = -c * y + d * x * y
    return [dxdt, dydt]

a, b, c, d = 1.0, 0.1, 1.5, 0.075
y0 = [10, 5]
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 200)

sol = solve_ivp(lotka_volterra, t_span, y0, t_eval=t_eval, args=(a, b, c, d))

# Plot histograms
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(sol.y[0], bins=10, edgecolor='black')
axs[0].set_xlabel('x (prey)')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of prey population')

axs[1].hist(sol.y[1], bins=10, edgecolor='black')
axs[1].set_xlabel('y (predator)')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of predator population')

plt.show()
