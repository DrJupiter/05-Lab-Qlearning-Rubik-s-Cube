############ GUIDE ################
"""
This script requires that you give the following parameters:

path_to_save_file depth_of_cube_shuffle steps_pr_test number_of_tests

"""



#from fork import State, shuffle, move
#import fork
from collections import defaultdict 
import hashlib
import random
import numpy as np
from copy import deepcopy
import pycuber as pc
from math import floor

# FOR FILE SAVING
from datetime import datetime
import sys
import os
import pickle


# The holy 12 actions
def dd():
    return np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]) 

def load_q_table():
    try:
        f = open("q_table", "rb")
        tmp = pickle.load(f)
        f.close()
        print("Succesfully loaded q_table")
        return tmp 
    except:
        return defaultdict(dd)

actions = ["U", "L", "F", "R", "B", "D","U'", "L'", "F'", "R'", "B'", "D'"]
q_table = load_q_table()
print(len(q_table.values()))
print(np.max(q_table.values()))

SOLVED_CUBE = pc.Cube()

"""
q_action(s) -> q_update(state_key, action_index, copy_of(s'')) -> cumulative_quality(copy_of(s''), 0)
                                                                                        |
                                                                                        |
                                                                                    Fordi vi vil muterer s'', men bevare,
                                                                                    hvor vi er lige nu i forhold til q_action(s)
"""

def cube_shuffle(cube, n):

    for _ in range(n):
        cube(actions[random.randint(0, len(actions)-1)])

def epsilon_greedy(epsilon=0.9):
    if np.random.random() <= epsilon:
        return True
    return False

def r(s):
    if s.__ne__(SOLVED_CUBE):
        return -0.1
    else:
        return 0.4

def q_action(s):
    cube_hash = str(s)
    if epsilon_greedy():
        a = random.randint(0,len(actions)-1)
    else:
        a = np.argmax(q_table[cube_hash])
    # We store the key of the previous state

    # the state s is mutated by taking the action determined by the epsilon_greedy() function call
    s(actions[a])
    # We then pass the q_update function the key: cube_hash, index into quality array at key: a, current_state: s
    q_update(cube_hash, a, s.copy())
# Maybe the return isn't needed
#    return s

# the current_state should represent a (state,action)-pair
def q_update(key, index, current_state, gamma=0.4):
    reward = r(current_state)
    # s, s', men vi vil gerne have reward for s' = (s,a)
    # check with +=
    # We start with a cc_q of 0
    q_table[key][index] = reward + gamma * cumulative_quality(current_state, 0)


# STAMP OF APPROVAL
def cumulative_quality(s, current_quality, gamma=0.4):
    key = str(s)
    action, value = find_max_index_value(q_table[key])
    new_quality = current_quality + value
    if abs((current_quality-new_quality)/(current_quality+10**(-9))) < 0.1 or (s.__ne__(SOLVED_CUBE) == False):
        return new_quality
    
    return new_quality + gamma*cumulative_quality(s(actions[action]),new_quality)


# STAMP OF APPROVAL
def find_max_index_value(iteratable):
    g_index = 0
    g_value = 0
    for index, value in enumerate(iteratable):
        if value > g_value:
            g_index = index
            g_value = value
    return (g_index,g_value)

####### TRAIN FUNCTIONS

def train(n_moves, iterations):
    for _ in range(floor(iterations/100)):
        print(_, flush=True, end="\r")
        for __ in range(100):
            cube = pc.Cube()
            cube_shuffle(cube, n_moves)
            for ___ in range(1):
                q_action(cube)


def n_move_test(n_moves,test_size):
    correct = 0
    for _ in range(test_size):
        test_cube = pc.Cube()
        cube_shuffle(test_cube, n_moves)
        for __ in range(n_moves): 
            a=np.argmax(q_table[str(test_cube)])
            test_cube(actions[a])
        if test_cube.__ne__(SOLVED_CUBE) == False:
            correct += 1
    return correct

def train_and_test(n_moves, iterations, test_size):
    train(n_moves, iterations)
    correct = n_move_test(n_moves,test_size)

    return correct/test_size


def grafing(n_moves, iterations, test_size):
    procent=0
    inter = 0
    while procent < 0.95:
        procent = train_and_test(n_moves, iterations, test_size)
        inter += iterations
        print(f"      {procent} at {n_moves} with {inter}      ", flush=True, end="\r")
        q_file = open(f"q_table_{n_moves}", "wb")
        pickle.dump(q_table,q_file)
        q_file.close()
        if inter % 10000 == 0:
            for i in range(n_moves):
                print(f"Updating depth-level: {i}          ")
                train(i, iterations)
    return inter, procent, n_moves




def to_txt(n_moves,iterations,test_size):
    inter, procent, n_moves = grafing(n_moves,iterations,test_size)

    text_file.write(f"n_moves: {n_moves}, ")
    text_file.write(f"inter: {inter}, ")
    text_file.write(f"%: {procent}, \n")

    return None

path_to_save_file, depth, steps_pr_test, n_tests = sys.argv[1:]
depth = int(depth)
steps_pr_test = int(steps_pr_test)
n_tests = int(n_tests)


print(f"Path: {path_to_save_file}<date>.txt \nTraining depth: {depth} \nSteps per test: {steps_pr_test} \nNumber of tests: {n_tests}")

text_file = open(f"{path_to_save_file}{datetime.now()}.txt", "a+")

for d in range(depth):
    to_txt(d, steps_pr_test, n_tests)
    print(f"Finished training at depth level {d}")

q_file = open(f"q_table", "wb")
pickle.dump(q_table,q_file)
q_file.close()
text_file.close()

print(n_move_test(depth-1, 2000)/2000)
