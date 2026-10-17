# Explanation

## Why the OU density stays Gaussian

An Ornstein-Uhlenbeck process is the diffusion whose drift is linear,

$$\mu(x) = -\kappa\,(x - c),$$

and whose diffusion is constant and isotropic, $D = \sigma^2$. Linear drift
means the deterministic part of the dynamics is a contraction towards the
centre, and a single Gaussian step is mapped to another Gaussian, so a Gaussian
initial condition stays Gaussian forever. Starting from a point mass at the
centre, the position at time $t$ is

$$X_t \sim \mathrm{Normal}\!\left(c,\ \frac{\sigma^2}{2\kappa}\left(1 - e^{-2\kappa t}\right)\right),$$

which relaxes to the stationary law $\mathrm{Normal}(c, \sigma^2 / 2\kappa)$ at
rate $\kappa$. In two dimensions the same argument gives an isotropic Gaussian
per axis, so the radius from the centre follows a Rayleigh distribution with
mean $s\sqrt{\pi/2}$.

## Paths and densities are two views of one process

The particle simulation integrates the Itô stochastic differential equation

$$dX_t = -\kappa\,(X_t - c)\,dt + \sigma\,dW_t.$$

What the particles *collectively* satisfy is the Fokker-Planck equation, the
deterministic PDE for their density:

$$\frac{\partial p}{\partial t} = \kappa\,\frac{\partial}{\partial x}\bigl[(x - c)\,p\bigr] + \frac{\sigma^2}{2}\,\frac{\partial^2 p}{\partial x^2}.$$

It is a common slip to call the Euler-Maruyama update a "Fokker-Planck update
step". It is not: the update advances one sample path, while the density
equation advances the whole ensemble at once. The two agree because the noise
average of many paths reproduces the PDE, but they are different objects, and
this project deliberately computes both so they can be checked against each
other.

## What the finite-volume scheme solves

The Python solver discretises the flux form of the conservation law. With the
probability current

$$J = -\kappa\,(x - c)\,p - \frac{\sigma^2}{2}\frac{\partial p}{\partial x},$$

the update is $p_i^{n+1} = p_i^n - \frac{\Delta t}{\Delta x}(J_{i+1/2} -
J_{i-1/2})$ with the advective part upwinded and the diffusive part centred.
Setting the boundary fluxes to zero makes total probability telescope to
exactly one, so mass is conserved to machine precision, and positivity is
preserved for small enough $\Delta t$.

The cost of upwinding is numerical diffusion. A first-order upwind scheme
solves not the original equation but a modified one with an extra diffusivity of
roughly $|v|\,\Delta x / 2$. That is why the PDE variance at the end of the run
is about $0.8\%$ high while the analytic variance is unit: the scheme is
solving a slightly more diffuse equation. Halving $\Delta x$ roughly halves the
bias, which is the usual first-order convergence.

## Where the model fails

The OU model is exactly solvable and that is precisely its limitation.

- **A single Gaussian blob.** Real home ranges are multi-modal, elongated along
  valleys and ridges, and asymmetric. An isotropic OU process cannot represent
  any shape beyond a circle.
- **Linear drift, no habitat.** Food, cover, and terrain should bend the drift,
  not a spring pulling towards a point.
- **Constant, isotropic diffusion.** Movement is not equally easy in all
  directions or everywhere, and it is very different along corridors and across
  barriers.
- **No boundaries.** Rivers, lakes, highways, and cliffs are invisible, even
  though they dominate where an animal can go.
- **No interactions or behaviour.** The model describes one Markovian animal
  with white noise and Gaussian steps, without memory, behavioural states, or
  heavy-tailed excursions.
- **Constant parameters.** Fidelity and restlessness vary with season, snow, and
  time of day; a stationary model over months is an average.
- **Infinite propagation speed.** For $\sigma > 0$ the equation is parabolic, so
  a point mass instantly has nonzero density everywhere. The moose could be
  anywhere with minuscule but positive probability, which is in direct tension
  with the hard maximum-speed bound of the ellipse method.

These defects define the agenda of the general Fokker-Planck model, which
replaces the spring with a habitat potential, the constant diffusion with a
spatial field, and adds boundaries, interactions, multiple behavioural states,
and jumps.
