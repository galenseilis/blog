# Explanation

## The general equation

The Fokker-Planck equation for the density `p(x, t)` of an animal's position, in
the form that carries all of the repairs at once, is

$$\frac{\partial p}{\partial t} = -\nabla \cdot (b[x,p]\,p) + \frac{1}{2}\,\partial_i \partial_j (D_{ij}(x)\,p) - \lambda(x)\,p.$$

Three things are general compared with the Ornstein-Uhlenbeck model:

- the drift `b` depends on space through a habitat potential `-grad U` and on
  the density through a nonlocal coupling;
- the diffusion `D_ij` is a field, so movement is easier in some terrain than
  others;
- the sink `lambda` removes mass, modelling mortality or emigration.

Each change answers a specific defect of the OU model: habitat instead of a
spring, a diffusion field, barriers as no-flux boundaries, interactions as
nonlocal coupling, behaviour as coupled states, and jumps as fractional
diffusion.

## The Boltzmann equilibrium

With constant scalar `D` and no-flux walls, the current

$$J = -\nabla U\,p - D\,\nabla p$$

vanishes for the Boltzmann equilibrium `p_inf ∝ exp(-U/D)`. This reduces to the
OU Gaussian when `U` is the spring and `D = sigma^2/2`. For constant `D`, habitat
alone determines where the animal concentrates, and this gives a checkable
target for the solver.

When `D` varies in space there is no universal closed form; the pattern of `D`
matters as much as the pattern of `U`, and solving the PDE is not optional.

## Why the numerical scheme is only part of the story

The two-dimensional solver is first-order upwind for the drift, which adds an
artificial diffusion of size roughly `|b| * dx / 2` on top of the physical `D`.
This inflates the effective diffusivity and leaves a residual error against
`exp(-U/D)` even at steady state. Refining the grid reduces the error at first
order, which is the expected convergence of the scheme. The lesson is the one
from the OU post: solving the Fokker-Planck equation always means solving a
discretization of it.

## Fractional diffusion and conservative flow

The fractional operator replaces the Laplacian by `(-Delta)^alpha`. It is
applied exactly in Fourier space, while the OU contraction is applied as an
exact conservative remap. On the periodic domain used here the contraction
points strictly inward, so the one-step map folds nothing across the seam.
Treating it as a wrap-around contraction would manufacture mass on every step
and the scheme would explode.

## Nonlocal interaction

Adding `chi * d/dx log(G * p)` pulls each animal up the smoothed density of
conspecifics. For a Gaussian `p` of variance `v`, the smoothed density is
Gaussian of variance `v + w^2`, so `log(G * p)` is exactly quadratic and the
self-consistency condition closes:

$$v = \frac{D}{\kappa + \chi/(v + w^2)}.$$

The simulation approaches that fixed point; the residual comes from the same
upwind numerical diffusion.

## Behavioural states

Two coupled densities, each with its own potential and diffusivity and linked by
switching rates, produce a bimodal total density that is far from any single
Gaussian. This is the quantitative form of the argument that made state-space
models standard in movement ecology: a single-state model fitted to such an
animal invents a home range centred in the gap between the two lobes.

## What generality does not buy

- **Fitting.** None of the parameters here are fitted; every value was chosen to
  make the mechanism legible. Inference is now the bottleneck.
- **Identifiability.** The equilibrium is shaped jointly by `U` and `D`, and
  multi-lobed densities arise from many mechanisms at once.
- **Infinite speed.** Fractional diffusion is nonlocal in space, so influence
  still propagates instantly; hard speed bounds live outside any Fokker-Planck
  model.
- **Time dependence.** Season, snow, and rut enter only through the choice of
  states.
- **Compute cost.** Two-dimensional grids, nonlocal couplings, and fractional
  operators turn closed forms into matrix and FFT work.
