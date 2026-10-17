"""A labelled transition system (LTS) and its synchronous product.

An LTS is a tuple ``(S, A, transitions, initial_state, accepting_states)``:
a set of states ``S``, a set of actions ``A``, a transition relation
``transitions``, an initial state, and a set of accepting (final) states.

The synchronous product ``L1 * L2`` couples two systems so that they must take
a shared action together. This module implements the product by overloading
``*`` on the :class:`LTS` class, following the definition given in the
BPMAG process-modelling lectures: the product's state set is the Cartesian
product of the operands' states, its actions are the intersection of their
action sets, and a transition exists exactly when *both* operands can make that
transition.
"""

from __future__ import annotations


class LTS:
    """A labelled transition system.

    Attributes
    ----------
    S:
        List of states in the LTS.
    A:
        List (or set) of actions in the LTS.
    transitions:
        Mapping from a state to a mapping from action to next state.
    initial_state:
        The state the system starts in.
    accepting_states:
        List of accepting (final) states.
    """

    def __init__(
        self,
        S: list,
        A: list,
        transitions: dict,
        initial_state: object,
        accepting_states: list,
    ) -> None:
        self.S = S
        self.A = A
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def __mul__(self, other: "LTS") -> "LTS":
        """Return the synchronous product ``self * other``.

        The product is defined only when the operands share at least one
        action. A transition ``(s, a, s')`` of the product exists when both
        operands can take action ``a`` from the corresponding component state.
        """
        if not isinstance(other, LTS):
            raise TypeError("Operand must be an LTS")

        S = []
        for s1 in self.S:
            for s2 in other.S:
                S.append(s1 + s2)
        A = set(self.A).intersection(set(other.A))
        transitions = []
        initial_state = self.initial_state + other.initial_state
        accepting_states = []
        for a1 in self.accepting_states:
            for a2 in other.accepting_states:
                accepting_states.append(a1 + a2)

        for s1 in self.S:
            for s2 in other.S:
                for a in A:
                    if (s1 in self.transitions) and (s2 in other.transitions):
                        s1_prime = self.transitions[s1].get(a)
                        s2_prime = other.transitions[s2].get(a)
                        if s1_prime and s2_prime:
                            transitions.append((s1 + s2, a, s1_prime + s2_prime))

        return LTS(S, A, transitions, initial_state, accepting_states)

    def __repr__(self) -> str:
        return (
            f"LTS(S={self.S!r}, A={self.A!r}, transitions={self.transitions!r}, "
            f"initial_state={self.initial_state!r}, "
            f"accepting_states={self.accepting_states!r})"
        )
