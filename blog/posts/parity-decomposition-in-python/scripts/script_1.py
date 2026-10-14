import numpy as np
import matplotlib.pyplot as plt


# Whatever function you are interested in
f = lambda t : np.exp(np.cos(t) + np.sin(t))
t = np.linspace(-2*np.pi, 2*np.pi, num=1000)

# Decomposition Functionals
even = lambda t: 0.5*(f(t) + f(-t))
odd = lambda t: 0.5*(f(t) - f(-t))

# Plot
plt.plot(even(t), odd(t))
plt.xlabel('Even Part')
plt.ylabel('Odd Part')
plt.savefig('example_parity_decomposition.png', dpi=300, transparent=True)
plt.close()
