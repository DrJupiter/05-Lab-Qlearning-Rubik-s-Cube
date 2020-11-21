from fork import State, shuffle, move
from collections import defaultdict 
import hashlib
import random
import numpy as np


cube = State()

actions = ['left', 'right', 'front', 'back', 'top', 'bottom', 'c_left', 'c_right', 'c_front', 'c_back', 'c_top', 'c_bottom']

q_table = defaultdict(lambda: np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]))


def r(s,a):
    tmp_s = move(s, a)
    if tmp_s.isGoalState():
        return 10
    else:
        return -1

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
