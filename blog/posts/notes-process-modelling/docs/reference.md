# API reference

## `notes_process_modelling.lts.LTS`

```python
LTS(S, A, transitions, initial_state, accepting_states)
```

A labelled transition system.

| Argument | Meaning |
| --- | --- |
| `S` | List of states. |
| `A` | List (or set) of actions. |
| `transitions` | Mapping from state to a mapping from action to next state. |
| `initial_state` | The state the system starts in. |
| `accepting_states` | List of accepting (final) states. |

### `LTS.__mul__(other) -> LTS`

Return the synchronous product `self * other`.

The product's states are formed by adding each pair of component states
(`s1 + s2`), its actions are `set(self.A) & set(other.A)`, and it contains a
transition `(s1 + s2, a, s1_prime + s2_prime)` exactly when both operands can
take action `a` from their respective states.

Raises `TypeError` when `other` is not an `LTS`.

## `notes_process_modelling.example`

### `build_lts1() -> LTS`

The first two-state machine, with actions `a` and `b` (states `s1`, `s2`;
initial `s1`; accepting `s2`).

### `build_lts2() -> LTS`

The second two-state machine, with actions `a` and `c` (states `s3`, `s4`;
initial `s3`; accepting `s4`).

### `synchronous_product_demo() -> LTS`

Return `build_lts1() * build_lts2()`.

### `main() -> None`

Print the state set, action set, transitions, initial state, and accepting
states of `synchronous_product_demo()`.

## Console script

| Command | Prints |
| --- | --- |
| `notes-process-modelling` | The properties of the worked-example synchronous product |
