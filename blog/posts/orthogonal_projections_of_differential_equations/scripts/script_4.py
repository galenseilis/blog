from script_1 import np
from script_1 import solve_ivp
from script_1 import plt
def sir_model(t, y, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

beta = 0.3
gamma = 0.1
y0 = [0.99, 0.01, 0.0]
t_span = (0, 160)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(sir_model, t_span, y0, t_eval=t_eval, args=(beta, gamma))

# Plot histograms
fig, axs = plt.subplots(1, 3, figsize=(18, 5))

axs[0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0].set_xlabel('S')
axs[0].set_ylabel('Frequency')
axs[0].set_title('Histogram of S (Susceptible)')

axs[1].hist(sol.y[1], bins=30, edgecolor='black')
axs[1].set_xlabel('I')
axs[1].set_ylabel('Frequency')
axs[1].set_title('Histogram of I (Infected)')

axs[2].hist(sol.y[2], bins=30, edgecolor='black')
axs[2].set_xlabel('R')
axs[2].set_ylabel('Frequency')
axs[2].set_title('Histogram of R (Recovered)')

plt.show()
