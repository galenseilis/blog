# moose-ou documentation

`moose-ou` is the Ornstein-Uhlenbeck model of moose movement: a pair of coupled
packages that simulate a virtual population and solve the density equation that
those paths obey.

The model has two interpretable parameters. The **fidelity** `kappa` (1/h) pulls
each animal back towards a home-range centre, and the **restlessness** `sigma`
(km/sqrt(h)) is the strength of the exploratory noise. Their ratio sets the
home-range size, `s = sigma / sqrt(2 kappa)`.

The project follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): simulate a small population and solve the
  Fokker-Planck equation for the first time.
- [How-to guides](how-to-guides.md): reproduce the blog figure, change the
  parameters, and tune the finite-volume grid.
- [Reference](reference.md): the Rust and Python APIs and the console script.
- [Explanation](explanation.md): why the OU density stays Gaussian, what the
  finite-volume scheme actually solves, and where the model breaks down.
