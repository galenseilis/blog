# Tutorial

This tutorial runs the hand-written queue simulation and reads its counters.

## 1. Install

```bash
pip install "git+https://github.com/galenseilis/blog.git#subdirectory=blog/posts/paul-grogan-des"
```

## 2. Create and step the simulation

```python
from paul_grogan_des import Simulation

S = Simulation()
print(S.clock, S.t_arrival, S.t_depart)
```

At construction the clock is `0`, the time of the first arrival is drawn from an
exponential distribution, and no departure is scheduled yet.

## 3. Advance by one event

```python
S.advance_time()
print(S.clock, S.num_arrivals, S.num_departs)
```

`advance_time` moves the clock to the earlier of `t_arrival` and `t_depart` and
handles whichever event it was.

## 4. Run a long simulation

```python
for _ in range(2018):
    S.advance_time()

print(S.num_arrivals, S.num_departs, S.total_wait)
```

`num_arrivals` and `num_departs` count events; `total_wait` is the accumulated
area of the system-content curve, so `total_wait / S.clock` estimates the mean
number in system (Little's law).

## 5. Run the Ciw version

```bash
paul-grogan-des
```

runs the hand-written model. To run the Ciw model, import its module:

```python
from paul_grogan_des import ciw_example  # runs on import
```

Continue with the [how-to guides](how-to-guides.md).
