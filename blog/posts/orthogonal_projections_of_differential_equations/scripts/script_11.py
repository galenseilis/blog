from script_10 import np
from script_10 import solve_ivp
from script_10 import plt
def rossler(t, state, a, b, c):
    x, y, z = state
    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

a = 0.2
b = 0.2
c = 5.7
y0 = [1.0, 1.0, 1.0]
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

sol = solve_ivp(rossler, t_span, y0, t_eval=t_eval, args=(a, b, c))

# Plot histograms
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Rössler Attractor)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of y (Rössler Attractor)')

axs[2].hist(sol.y[2], bins=30, edgecolor='black')
axs[2].set_xlabel('z')
axs[2].set_ylabel('Frequency')
axs[2].set_title('Histogram of z (Rössler Attractor)')

plt.show()
