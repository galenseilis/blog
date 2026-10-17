# Explanation

## Event-advance simulation

A discrete-event simulation maintains a clock and a set of pending events, each
with a time. To step, it finds the earliest pending event, moves the clock to
that time, and processes it — possibly scheduling further events. Between two
events nothing happens, so the clock jumps rather than ticking.

Paul Grogan's example is the smallest interesting instance of this idea: an
M/M/1 queue with two kinds of event (arrival and departure). The whole model is
a handful of lines: keep the next arrival and next departure times, advance to
the earlier, and update counters. It is a good first project precisely because
every piece is explicit.

## Why it is worth hand-rolling once

Writing the loop yourself makes several things concrete that a library hides:

- The clock is a variable you control, not a black box.
- `total_wait` is the area under the number-in-system curve, which is the
  quantity Little's law relates to the mean number in system
  (`L = λW`); accumulating it as `num_in_system * dt` shows where that comes
  from.
- The idle state is represented by `t_depart = inf`, a small trick worth seeing.

## What Ciw adds

The Ciw version declares the same system as a one-node network with an
exponential arrival distribution (`rate = 3`), an exponential service
distribution (`rate = 4`), and one server. You no longer write the event loop;
you describe the system and read back records.

The trade-off mirrors the one in the [car
post](https://galenseilis.github.io/blog/posts/car-process-interaction-simpy-ciw/):
hand-rolled code is transparent and easy to modify but does not scale, while a
library is compact and fast on large networks but hides the mechanics.

## Caveats

- **Rate versus mean.** `numpy.random.exponential` takes a scale (the mean),
  while `ciw.dists.Exponential` takes a rate. The two modules use the correct
  convention for each library, so do not copy a number between them without
  converting.
- **Estimation.** A single long run gives one sample path. Steady-state
  estimates need a warm-up period, independent replications, or both.
- **No proof.** The model assumes exponential, independent, stationary arrivals
  and services with a single server. Real queues violate all three.
