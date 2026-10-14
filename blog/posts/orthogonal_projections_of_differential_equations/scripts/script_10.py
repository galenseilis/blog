import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def double_pendulum(t, state, m1, m2, L1, L2, g):
    theta1, omega1, theta2, omega2 = state
    delta = theta2 - theta1

    denominator1 = (m1 + m2) * L1 - m2 * L1 * np.cos(delta) ** 2
    denominator2 = (L2 / L1) * denominator1

    dtheta1_dt = omega1
    dtheta2_dt = omega2

    domega1_dt = ((m2 * L1 * omega1 ** 2 * np.sin(delta) * np.cos(delta) +
                   m2 * g * np.sin(theta2) * np.cos(delta) +
                   m2 * L2 * omega2 ** 2 * np.sin(delta) -
                   (m1 + m2) * g * np.sin(theta1)) / denominator1)

    domega2_dt = ((- m2 * L2 * omega2 ** 2 * np.sin(delta) * np.cos(delta) +
                   (m1 + m2) * (g * np.sin(theta1) * np.cos(delta) -
                   L1 * omega1 ** 2 * np.sin(delta) - g * np.sin(theta2))) / denominator2)

    return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

m1 = 1.0
m2 = 1.0
L1 = 1.0
L2 = 1.0
g = 9.81

y0 = [np.pi / 2, 0, np.pi, 0]  # Initial angles and angular velocities
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

sol = solve_ivp(double_pendulum, t_span, y0, t_eval=t_eval, args=(m1, m2, L1, L2, g))

# Plot histograms
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

axs[0, 0].hist(sol.y[0], bins=30, edgecolor='black')
axs[0, 0].set_xlabel('theta1')
axs[0, 0].set_ylabel('Frequency')
axs[0, 0].set_title('Histogram of theta1 (Double Pendulum)')

axs[0, 1].hist(sol.y[1], bins=30, edgecolor='black')
axs[0, 1].set_xlabel('omega1')
axs[0, 1].set_ylabel('Frequency')
axs[0, 1].set_title('Histogram of omega1 (Double Pendulum)')

axs[1, 0].hist(sol.y[2], bins=30, edgecolor='black')
axs[1, 0].set_xlabel('theta2')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].set_title('Histogram of theta2 (Double Pendulum)')

axs[1, 1].hist(sol.y[3], bins=30, edgecolor='black')
axs[1, 1].set_xlabel('omega2')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('Histogram of omega2 (Double Pendulum)')

plt.show()
