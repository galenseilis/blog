from script_1 import np
from script_1 import solve_ivp
from script_1 import plt
def hodgkin_huxley(t, state):
    V, m, h, n = state

    C_m = 1.0
    g_Na = 120.0
    g_K = 36.0
    g_L = 0.3
    V_Na = 115.0
    V_K = -12.0
    V_L = 10.6
    I = 10.0

    alpha_m = 0.1 * (25 - V) / (np.exp((25 - V) / 10) - 1)
    beta_m = 4.0 * np.exp(-V / 18)
    alpha_h = 0.07 * np.exp(-V / 20)
    beta_h = 1.0 / (np.exp((30 - V) / 10) + 1)
    alpha_n = 0.01 * (10 - V) / (np.exp((10 - V) / 10) - 1)
    beta_n = 0.125 * np.exp(-V / 80)

    dVdt = (I - g_Na * m**3 * h * (V - V_Na) - g_K * n**4 * (V - V_K) - g_L * (V - V_L)) / C_m
    dmdt = alpha_m * (1 - m) - beta_m * m
    dhdt = alpha_h * (1 - h) - beta_h * h
    dndt = alpha_n * (1 - n) - beta_n * n

    return [dVdt, dmdt, dhdt, dndt]

y0 = [-65.0, 0.05, 0.6, 0.32]
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(hodgkin_huxley, t_span, y0, t_eval=t_eval)

# Plot histograms
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

axs[0, 0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0, 0].set_xlabel('V')
axs[0, 0].set_ylabel('Frequency')
axs[0, 0].set_title('Histogram of V (Hodgkin-Huxley)')

axs[0, 1].hist(sol.y[1], bins=30, edgecolor='black')
axs[0, 1].set_xlabel('m')
axs[0, 1].set_ylabel('Frequency')
axs[0, 1].set_title('Histogram of m (Hodgkin-Huxley)')

axs[1, 0].hist(sol.y[2], bins=30, edgecolor='black')
axs[1, 0].set_xlabel('h')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].set_title('Histogram of h (Hodgkin-Huxley)')

axs[1, 1].hist(sol.y[3], bins=30, edgecolor='black')
axs[1, 1].set_xlabel('n')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('Histogram of n (Hodgkin-Huxley)')

plt.show()
