# ciw-simpy-bank-renege documentation

`ciw-simpy-bank-renege` implements SimPy's Bank Renege example in
[Ciw](https://ciw.readthedocs.io/en/latest/): an M/M/1 queue with a fixed
number of customers and uniformly distributed reneging patience, then estimates
the distribution of the total sojourn time.

The package follows the [Diátaxis](https://diataxis.fr/) structure:

| I want to... | Read |
| --- | --- |
| learn the package by doing | [Tutorial](tutorials.md) |
| solve a specific problem | [How-to guides](how-to-guides.md) |
| look up functions and classes | [Reference](reference.md) |
| understand the ideas and trade-offs | [Explanation](explanation.md) |

## Contents

- [Tutorial](tutorials.md): build the network, simulate, and fit the run-time
  distribution.
- [How-to guides](how-to-guides.md): change the parameters, the number of
  simulations, and the output path.
- [Reference](reference.md): the three modules and the console script.
- [Explanation](explanation.md): reneging, why the queue is unstable yet
  bounded, and why a Gamma distribution fits.
