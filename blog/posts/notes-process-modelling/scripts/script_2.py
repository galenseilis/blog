from script_1 import LTS
# TODO: Test that this code actually works.
# Define LTS1
S1 = ['s1', 's2']
A1 = ['a', 'b']
transitions1 = {'s1': {'a': 's2', 'b': 's1'}, 's2': {'a': 's1', 'b': 's2'}}
initial_state1 = 's1'
accepting_states1 = ['s2']

lts1 = LTS(S1, A1, transitions1, initial_state1, accepting_states1)

# Define LTS2
S2 = ['s3', 's4']
A2 = ['a', 'c']
transitions2 = {'s3': {'a': 's4', 'c': 's3'}, 's4': {'a': 's3', 'c': 's4'}}
initial_state2 = 's3'
accepting_states2 = ['s4']

lts2 = LTS(S2, A2, transitions2, initial_state2, accepting_states2)

# Perform synchronous product
product_lts = lts1 * lts2

# Access the properties of the product LTS
print(product_lts.S)
print(product_lts.A)
print(product_lts.transitions)
print(product_lts.initial_state)
print(product_lts.accepting_states)
