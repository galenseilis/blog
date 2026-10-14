from script_10 import np
from script_10 import solve_ivp
from script_10 import plt
def seir_model(t, y, beta, sigma, gamma):
    S, E, I, R = y
    dSdt = -beta * S * I
    dEdt = beta * S * I - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

beta = 0.3
sigma = 0.1
gamma = 0.1
y0 = [0.99, 0.01, 0.0, 0.0]
t_span = (0, 160)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(seir_model, t_span, y0, t_eval=t_eval, args=(beta, sigma, gamma))

# Plot histograms
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

axs[0, 0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0, 0].set_xlabel('S')
axs[0, 0].set_ylabel('Frequency')
axs[0, 0].set_title('Histogram of S (Susceptible)')

axs[0, 1].hist(sol.y[1], bins=30, edgecolor='black')
axs[0, 1].set_xlabel('E')
axs[0, 1].set_ylabel('Frequency')
axs[0, 1].set_title('Histogram of E (Exposed)')

axs[1, 0].hist(sol.y[2], bins=30, edgecolor='black')
axs[1, 0].set_xlabel('I')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].set_title('Histogram of I (Infected)')

axs[1, 1].hist(sol.y[3], bins=30, edgecolor='black')
axs[1, 1].set_xlabel('R')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('Histogram of R (Recovered)')

plt.show()
