# Explanation

## Snakes and Ladders as a Markov chain

It has been known for decades that Snakes and Ladders is a Markov chain. A
player's position is the state, and the probability of moving to any other
position depends only on the current position, not on how the player got there.
That makes the board a stochastic matrix — the routing matrix this package
builds — and the game a random walk on thirty states.

## What Ciw adds, and where it differs

Modelling the board as a Ciw network means treating each tile as a queueing
node. The routing matrix plays the role of the transition probabilities; the
service distribution at a node is the time until the next move. Ordinary moves
take one discrete unit of time, while snakes and ladders are instantaneous,
which is modelled with a zero-service-time node. All six players enter at the
first tile at time zero, via a single batched arrival.

The important difference from the original game is the simultaneity of turns.
In the original game players take strictly ordered turns; in a discrete-event
simulation, events at the same time are resolved by Ciw randomly choosing
which happens first, to avoid contradictory state. That is why the winner can
depend on the seed, and why the shuffle of simultaneous events rather than a
fixed turn order drives the outcome.

A second difference is that the queueing machinery is essentially irrelevant
here. With an unlimited number of servers and infinite queue capacity, pieces
never block each other, so the network is really a way to reuse Ciw's
event-scheduling engine for a Markov chain rather than a genuine queueing
model. That is precisely the point: Ciw's generalization is powerful enough to
simulate games, not just queues.

## Why the routing rows must sum to one

Ciw interprets any probability a routing row leaves unassigned as a chance of
leaving the system. Near the end of the board a die roll can overshoot the
final square, so a naive construction leaves tiles 25 to 29 with rows that sum
to less than one — which Ciw silently turns into an early exit. A player could
then leave the board without reaching the thirtieth square, and "the winner"
would mean "the first to leave", not "the first to reach the end".

The fix is to give the overshooting outcomes to the final square, so ordinary
rows sum to one and the only way off the board is to reach the end. With that
normalization, the first player to finish is exactly the first player to reach
the final square.

## Connection to labelled transition systems

A labelled transition system models *which* sequences of actions are possible;
a Markov chain adds the probabilities; and a Ciw network adds timing and
scheduling. Snakes and Ladders sits at the last of these levels: the moves are
probabilistic, but the interesting behaviour only emerges once events are
given times and resolved in simulation.
