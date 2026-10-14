from script_1 import np
from script_1 import solve_ivp
from script_1 import plt
def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
y0 = [1.0, 1.0, 1.0]
t_span = (0, 40)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

sol = solve_ivp(lorenz, t_span, y0, t_eval=t_eval, args=(sigma, rho, beta))

# Plot histograms
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Lorenz system)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of y (Lorenz system)')

axs[2].hist(sol.y[2], bins=30, edgecolor='black')
axs[2].set_xlabel('z')
axs[2].set_ylabel('Frequency')
axs[2].set_title('Histogram of z (Lorenz system)')

plt.show()
