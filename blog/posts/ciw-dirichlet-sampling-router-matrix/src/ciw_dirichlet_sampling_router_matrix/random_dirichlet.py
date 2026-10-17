"""Random Dirichlet list for stochastic routing matrices."""

from __future__ import annotations

import numpy as np


class RandomDirichletList(list):
    """
    List that contains and resamples from a Dirichlet distribution.

    This class represents a list-like structure that contains and
    resamples from a Dirichlet distribution. It is designed for
    working with probabilistic values that sum to 1, such as probability
    distributions. The Dirichlet distribution is used to generate
    such values.
    """

    def __init__(self, alphas) -> None:
        alphas = np.asarray(alphas)
        if np.any(alphas <= 0):
            raise ValueError("Alpha parameters must be positive")
        self.alphas = alphas
        self.probs = np.array([])
        self.sample()
        super().__init__(self.probs.tolist())

    def _renormalize_probs(self) -> None:
        """Sum renormalize probabilities."""
        self.probs = self.probs / sum(self.probs)

    def sample(self) -> None:
        self.probs = np.random.dirichlet(self.alphas)
        self._renormalize_probs()
        while sum(self.probs) != 1.0:
            self.probs = np.random.dirichlet(self.alphas)
            self._renormalize_probs()

    def __getitem__(self, index):
        self.sample()
        return float(self.probs[index])

    def __min__(self):
        return float(min(self.probs))

    def __max__(self):
        return float(max(self.probs))

    def __len__(self):
        return len(self.probs)

    def __repr__(self):
        return f"RDL{self.probs.tolist()}"
