import ciw


class StepDist(ciw.dists.Distribution):
    """A custom distribution representing a step function with two values."""

    def __init__(self, first_value: float, second_value: float, step_t: float) -> None:
        """
        Initializes a new instance of the StepDist class.
        """
        super().__init__()
        self.first_value: float = first_value
        self.second_value: float = second_value
        self.step_t: float = step_t

    def sample(self, t: float = None, ind: ciw.Individual = None) -> float:
        """
        Samples the step function at a given time.
        """
        if t is not None and t <= self.step_t:
            return self.first_value
        else:
            return self.second_value


class PrintDistWrapper(ciw.dists.Distribution):
    """
    A wrapper class for a probability distribution that adds a print statement
    before sampling from the underlying distribution.
    """

    def __init__(self, dist: ciw.dists.Distribution, message) -> None:
        super().__init__()
        self.dist = dist
        self.message = message

    def sample(self, t=None, ind=None):
        """
        Generate a sample from the underlying distribution, printing a custom message.
        """
        if ind is not None and getattr(ind, "node", None) == 2 and t == 3:
            if t == 3:
                print("Was interrupted. Hope, the battery is full enough ...")
        else:
            print(self.message, t)

        return self.dist.sample(t, ind)


def build_network() -> ciw.network.Network:
    """Build the two-node car network used in the post."""
    arrival_dists = [ciw.dists.Sequential([0, float("inf")]), None]
    service_dists = [
        PrintDistWrapper(StepDist(3, 5, 3), "Start parking at"),
        PrintDistWrapper(ciw.dists.Deterministic(2), "Start driving at"),
    ]
    num_servers = [1, 1]
    R = [[0.0, 1.0], [1.0, 0.0]]

    return ciw.create_network(
        arrival_distributions=arrival_dists,
        service_distributions=service_dists,
        number_of_servers=num_servers,
        routing=R,
    )


def run_simulation(max_time: float = 15) -> ciw.Simulation:
    """Run the car simulation up to ``max_time`` and return it."""
    network = build_network()
    simulation = ciw.Simulation(network)
    simulation.simulate_until_max_time(max_time)
    return simulation


def main() -> None:
    run_simulation()


if __name__ == "__main__":
    main()
