# TODO: Test that this code actually works.
class LTS:
    """
    Class representing a Labelled Transition System (LTS).

    Attributes:
        S (list): List of states in the LTS.
        A (list): List of actions in the LTS.
        transitions (dict): Dictionary representing transitions in the LTS.
                            Key: state, Value: dict representing actions and their corresponding next states.
        initial_state: Initial state of the LTS.
        accepting_states (list): List of accepting states in the LTS.

    Methods:
        __mul__(other): Overloaded multiplication operator to perform the synchronous product of two LTSs.
    """

    def __init__(self, S, A, transitions, initial_state, accepting_states):
        """
        Initialize the LTS object.

        Args:
            S (list): List of states in the LTS.
            A (list): List of actions in the LTS.
            transitions (dict): Dictionary representing transitions in the LTS.
                                Key: state, Value: dict representing actions and their corresponding next states.
            initial_state: Initial state of the LTS.
            accepting_states (list): List of accepting states in the LTS.
        """
        self.S = S
        self.A = A
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def __mul__(self, other):
        """
        Overloaded multiplication operator to perform the synchronous product of two LTSs.

        Args:
            other (LTS): The other LTS object to perform the synchronous product with.

        Returns:
            LTS: Resulting LTS after performing the synchronous product.
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
