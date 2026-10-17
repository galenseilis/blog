# Explanation

## States, actions, and behaviour

A **labelled transition system** (LTS) is a model of a system as a set of states
together with labelled transitions between them. A **state** is a possible
configuration of the system; an **action** moves the system from one state to
another; and the **behaviour** of the system is the set of allowed sequences of
actions. Writing the transitions as a ternary relation `(p, a, q)` separates the
*what* (which state follows which) from the *how* (which action caused it),
which is what makes LTSs composable.

The package represents an LTS as five pieces of data: the state set `S`, the
action set `A`, the transition mapping, an initial state, and a set of accepting
states. An accepting (final) state is a state in which the process ends.

## The synchronous product

The synchronous product is the standard way to build a larger system out of
smaller ones. Divide a problem into parts, model each part as its own LTS, and
then combine them. In the product:

- a state is a tuple of the components' states;
- an action is available only if *every* component can take it;
- a transition happens only when all components take the shared action
  together, at the same step.

This is the "synchronous" in the name: the operands march in lockstep on their
shared actions. Actions private to one operand disappear from the product,
because there is nothing for the other operands to synchronise with.

The worked example makes the effect concrete. Two two-state machines share the
action `a` and each has one private action (`b` and `c`). Their product has four
states, exactly one action (`a`), and four transitions — one for each pair of
states from which both machines can take `a`.

## What the model captures, and what it does not

The synchronous product gives a precise account of *allowed sequences of
actions*: a behaviour is a path through the product, and reachability is
graph reachability. That makes it a good language for asking structural
questions — which states are reachable, whether an accepting state is reachable
at all, and which actions must a system expose to interoperate with another.

What it does not carry is time, probability, or cost. The transitions are
possible, not scheduled; there is no notion of how long an action takes or how
likely it is. Those are exactly the concerns that a discrete-event simulation
such as Ciw adds, and it is no accident that the notes move from LTSs to queueing
simulations. The synchronous product answers "can this sequence happen?", while
a simulation answers "how often, and how long does it take?".

Two further limitations are worth stating. First, the product synchronises on
*all* shared actions, so there is no way to express optional synchronisation or
asynchronous interleaving without enriching the model. Second, the reference
implementation labels product states by concatenating the component labels
(`s1 + s2`), which assumes the labels are strings or otherwise addable; a more
general treatment would use tuples.
