from fork import State, shuffle, move
from collections import defaultdict 
import hashlib
import random
import numpy as np


cube = State()

actions = ['left', 'right', 'front', 'back', 'top', 'bottom', 'c_left', 'c_right', 'c_front', 'c_back', 'c_top', 'c_bottom']

q_table = defaultdict(lambda: np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]))



### Somthing somthing

Q = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]

gamma = 0.9

def Nxt_move_list(stat):
    nxt_move = []
    for i in range(12)
        nxt_move[i] = current_state.move(actions[i])
    return nxt_move

def Reward_minus(stat):
    if stat == 0:
        return 1
    else:
        return -1


for t in range(1000):
    # Loop over all states
    for s in range(12):
        # Update value
        Q[s] = Red(s)+max([gamma*Q[sp] for sp in F[s]])

print(V)


###




def r(s,a):
    tmp_s = move(s, a)
    if tmp_s.isGoalState():
        return 10
    else:
        return -1
###
reward_ex=-1
gamma_ex) 0.9
for _ in range(10):
    for s in range(12):
        for r,sp in zip(F[s])
            q[s] = max(reward_ex+gamma_ex*q[sp])

# F = Next step table
    # altså hvor man næste gang ender
        # Vi må beskrive dette på en eller anden måde. måske muligt at få den til at gøre det inplicit
        # da den kan finde det næste stadie og "hash" det, og dermed finde dens værdi

"""
# 1000 value iterations
for t in range(1000):
    # Loop over all states
    for s in range(6):
        # Update value
        V[s] = max([r+gamma*V[sp] for r,sp in zip(R[s], F[s])])
"""

###

def q(s,a, gamma):
    current_score = r(s,a)
    if abs(gamma *) < 0.04:
        return 
    current_score = r(s,a) + max(q_table[move(s,a).__hash__()])



    


def find_max_reward(iterable):


def find_max_index(iteratable)
    g_index = 0
    for index, value in enumerate(iterable):
        if value > iterable[g_index]:
            g_index = index
    return g_index

    








def testhash():
    cube = State()
    print(cube.__hash__())
    print(q_table[cube.__hash__()])
    q_table[cube.__hash__()][0] = 1
    print(q_table[cube.__hash__()])
