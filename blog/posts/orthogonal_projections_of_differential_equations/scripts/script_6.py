from script_1 import np
from script_1 import solve_ivp
from script_1 import plt
def brusselator(t, state, A, B):
    x, y = state
    dxdt = A + x**2 * y - (B + 1) * x
    dydt = B * x - x**2 * y
    return [dxdt, dydt]

A = 1.0
B = 3.0
y0 = [1.0, 1.0]
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(brusselator, t_span, y0, t_eval=t_eval, args=(A, B))

# Plot histograms
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('x')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of x (Brusselator)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('y')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of y (Brusselator)')

plt.show()
