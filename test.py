import numpy as np

# Initial values
V = [0,0,0,0,0,0]
# Discount
gamma = 0.9
# Actions: 0=North,
# 1=South, 2=East, 3=West
actions = [0, 1, 2, 3]
# Next state table
F = [[1, 0, 2, 1],
[1, 5, 0, 0],
[0, 2, 4, 3],
[2, 3, 4, 5],
[4, 5, 2, 3],
[3, 5, 4, 1]]

#F = [1,0,2,1,1,5,0,0,0,2,4,3,2,3,4,5,4,5,2,3,3,5,4,1]

def Fat(stat):
    nxt_move = []
    for i in range(12)
        nxt_move[i] = current_state.move(actions[i])

print(Fat(0))

def Red(stat):
    if stat == 0:
        return 1
    else:
        return -1




# 1000 value iterations
for t in range(1000):
    # Loop over all states
    for s in range(6):
        # Update value
        V[s] = max([Red(s)+gamma*V[sp] for sp in F[s]])

print(V)

for t in range(1000):
    # Loop over all states
    for s in range(6):
        # Update value
        V[s] = Red(s)+max([gamma*V[sp] for sp in F[s]])

print(V)