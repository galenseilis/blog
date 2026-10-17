# Explanation

## Two ways to describe the same system

The blog post exists because the same little car system can be written down in
two very different styles.

In the **process-interaction** (SimPy) style you write the life of one entity as
a generator. The car "parks", "charges", and "drives" in a `while` loop, and
another generator, the driver, reaches in and interrupts it. The control flow of
the program *is* the behaviour of the car, which makes the model easy to read
but couples the entity to its implementation.

In the **queueing-network** (Ciw) style you describe the system as nodes,
arrival and service distributions, servers, and a routing matrix. The car becomes
two nodes — parking/charging and driving — that route back and forth. The
control flow is gone; you declare the structure and the simulator executes it.

## Encoding the interruption

The interesting part of the Ciw version is that a queueing network has no
natural notion of "interrupt". The post fakes it by wrapping the service
distribution in `PrintDistWrapper`, which inspects the individual's current node
and the simulation time in `sample` and prints the interruption message when the
individual is on the driving node at `t = 3`. The service time itself still
comes from the wrapped `StepDist`.

This is a good illustration of the trade-off: declarative models are more
compact and composable, but unusual semantics sometimes have to be smuggled in
through a custom distribution.

## Trade-offs

- **Readability.** Process interaction mirrors how you would describe the
  system in words; queueing networks mirror its structure as a graph.
- **Scalability.** Ciw is designed for large, statistically rich networks where
  you care about throughput and waiting times rather than individual events.
- **Extensibility.** Adding a genuinely new behaviour is usually easier in the
  process style; adding many similar stations is easier in the network style.
- **Verification.** Neither model proves anything about the real system. Both
  are conditional on their timing assumptions, which here are arbitrary round
  numbers chosen to make the log legible.
