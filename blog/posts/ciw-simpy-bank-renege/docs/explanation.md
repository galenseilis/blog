# Explanation

## Reneging in an M/M/1 queue

At first glance the Bank Renege example is an M/M/1 queue: Poisson arrivals,
exponential service, one server. Two custom features make it interesting. The
first is **reneging**: a waiting customer gives up after a patience time drawn
from a uniform distribution on one to three time units. Reneging is what keeps
the queue from growing without bound when it is unstable. Ciw supports it
directly through `reneging_time_distributions`.

The second feature is a **fixed total number of customers**. The arrival
process is exponential, but only for the first five customers; after that,
arrivals stop. This is encoded by wrapping the exponential distribution in
`MaxArrivalDist`, whose `sample` method returns a finite value for the first
five calls and positive infinity afterwards. Infinite inter-arrival time means
no further arrivals ever occur.

## An unstable queue that is still bounded

The traffic intensity is the ratio of arrival rate to service rate:
`rho = lambda / mu = (1/10) / (1/12) = 6/5`. Since `rho > 1`, the classic
M/M/1 queue is unstable and its waiting line would grow without bound. But that
asymptotic result assumes an endless stream of arrivals. Here only five
customers ever arrive, so the theoretical concern does not apply: the queue
simply cannot grow long enough to matter. Reneging provides a second bound,
since impatient customers leave rather than accumulate.

## Estimating the sojourn-time distribution

Even though the system is small, the distribution of the total sojourn time is
not easy to write down. One cannot simply add up the exponential random
variables, because doing so would ignore the waiting time in the queue and the
possibility of reneging. The post therefore estimates the distribution by
simulation: run the model many times, record the time at which the fifth
customer leaves, and fit a distribution to the resulting sample.

## Why a Gamma distribution?

The Gamma distribution is a natural guess. It generalizes several common
time-to-event distributions, including the exponential and Erlang
distributions, and it often gives a good approximation to waiting- and
sojourn-time distributions. The post is candid that the choice was a guess
rather than a derivation; the satisfaction is that the fitted Gamma curve
tracks the simulated histogram so closely. That correspondence between an
empirically fitted family and a simulated sample is itself a useful sanity
check on the model.
