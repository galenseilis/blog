"""Fixed routing example from the blog post."""

from __future__ import annotations

import ciw


def create_fixed_network():
    return ciw.create_network(
        arrival_distributions=[ciw.dists.Exponential(rate=0.3),
                               ciw.dists.Exponential(rate=0.2),
                               None],
        service_distributions=[ciw.dists.Exponential(rate=1.0),
                               ciw.dists.Exponential(rate=0.4),
                               ciw.dists.Exponential(rate=0.5)],
        routing=[[0.0, 0.3, 0.7],
                 [0.0, 0.0, 1.0],
                 [0.0, 0.0, 0.0]],
        number_of_servers=[1, 2, 2]
    )


def main() -> None:
    n = create_fixed_network()
    print(n)


if __name__ == "__main__":
    main()
