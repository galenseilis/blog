from script_1 import np
from script_1 import solve_ivp
from script_1 import plt
def fitzhugh_nagumo(t, state, a, b, tau, I):
    v, w = state
    dvdt = v - (v**3) / 3 - w + I
    dwdt = (v + a - b * w) / tau
    return [dvdt, dwdt]

a = 0.7
b = 0.8
tau = 12.5
I = 0.5
y0 = [0.0, 0.0]
t_span = (0, 200)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(fitzhugh_nagumo, t_span, y0, t_eval=t_eval, args=(a, b, tau, I))

# Plot histograms
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('v')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of v (FitzHugh-Nagumo)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('w')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of w (FitzHugh-Nagumo)')

plt.show()
