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

# FOR FILE SAVING
from datetime import datetime
import sys

#actions = ['left', 'right', 'front', 'back', 'top', 'bottom', 'c_left', 'c_right', 'c_front', 'c_back', 'c_top', 'c_bottom']
#q_table = defaultdict(lambda: np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]))
#actions = ['left', 'right', 'front', 'back', 'top', 'bottom']

# The unholy 18 actions
#actions = ["U", "L", "F", "R", "B", "D","U'", "L'", "F'", "R'", "B'", "D'", "M", "M'", "E", "E'", "S", "S'"]
#q_table = defaultdict(lambda: np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]))

# The holy 12 actions
actions = ["U", "L", "F", "R", "B", "D","U'", "L'", "F'", "R'", "B'", "D'"]
q_table = defaultdict(lambda: np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]))

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

# It measures the value of taking action a in state s
# which means that we should check the value of each state action pair for an action?
# No not quite, we use the epsilon_greedy function to determine, if we should
# Do the action with the current highest quality or try something random
def epsilon_greedy(epsilon=0.9):
    if np.random.random() <= epsilon:
        return True
    return False
# So from an initial state s_initial we look at our available actions
# which in our case is a constant list of actions, which can be found in the actions list
# We then call our epsilon function to see whether or not we should take a random action or the best possible action
# We then take the action and then update the q_table value for that action for the now previous state
# The update is based on checking if the new state is the goal state and then continuously adding
# the values from the best state after the new state

# NOTE: WE COULD MAKE A TRAIN REWARD FUNCTION THAT GIVES A LARGE PENALTY
# IF WE EXCEED THE MIN_AMOUNT_OF_SOLVE_STEPS: r_train(s, a, BOOL_TRAIN, OPTIMAL_STEP)


# REFACTORED TO pycuber
def r(s):
    if s.__ne__(SOLVED_CUBE):
        return -0.1
    else:
        return 5

# REFACTORED TO pycuber
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
def q_update(key, index, current_state, gamma=0.5):
    reward = r(current_state)
    # s, s', men vi vil gerne have reward for s' = (s,a)
    # check with +=
    # We start with a cc_q of 0
    q_table[key][index] = reward + gamma * cumulative_quality(current_state, 0)


# STAMP OF APPROVAL
# Remember to pass a copy on the top level
# NOTE: ACCOUNT FOR DIVISION BY 0
def cumulative_quality(s, current_quality, gamma=0.5):
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
    

def testhash():
    cube = State()
    print(cube.__hash__())
    print(q_table[cube.__hash__()])
    q_table[cube.__hash__()][0] = 1
    print(q_table[cube.__hash__()])

#testhash()

# def flatten(A):
#     rt = []
#     for i in A:
#         if isinstance(i,list): rt.extend(flatten(i))
#         else: rt.append(i)
#     return rt

def train(n_moves, iterations):
    for _ in range(iterations):
        cube = pc.Cube()
        cube_shuffle(cube, n_moves)
        for _ in range(n_moves):
            q_action(cube)

    aq = list(q_table.values())
    good_paths = 0
    for element in aq:
        if any(element):
            good_paths += 1
            #print(element)
    #print(f"number of paths: {len(aq)}")
    #print(f"good paths: {good_paths}")


def n_move_test(n_moves,test_size):
    correct = 0
    for _ in range(test_size):
        test_cube = pc.Cube()
        cube_shuffle(test_cube, n_moves)
        for _ in range(n_moves): 
            a=np.argmax(q_table[str(test_cube)])
            test_cube(actions[a])
        if test_cube.__ne__(SOLVED_CUBE) == False:
            correct += 1
    return correct

def train_and_test(n_moves, iterations, test_size):
    #print("-------------------------------------------")
    #print(f"iterations = {iterations}")
    #print(f"n_moves = {n_moves}")
    #print(f"test_size = {test_size}")
    #print(" ")
    train(n_moves, iterations)
    correct = n_move_test(n_moves,test_size)
    #print(f"Number of correctly solved cubes = {correct}")
    #print(f"% solved: {correct/test_size*100}%")

    #print("-------------------------------------------")
    return correct/test_size

#print(train_and_test(2,1000,200))


"""i=0
while i < 10:

    i+=1
    print(i)
"""


def grafing(n_moves, iterations, test_size):
    procent=0
    inter = 0
    while procent < 0.95:
        procent = train_and_test(n_moves, iterations, test_size)
        inter += iterations
        print(f"{procent} at {n_moves} with {inter}      ", flush=True, end="\r")

    return inter, procent, n_moves




def to_txt(n_moves,iterations,test_size):
    inter, procent, n_moves = grafing(n_moves,iterations,test_size)

    text_file.write(f"n_moves: {n_moves}, ")
    text_file.write(f"inter: {inter}, ")
    text_file.write(f"%: {procent}, \n")

    return None

#train_and_test(5,20000,1000)

path_to_save_file, depth, steps_pr_test, n_tests = sys.argv[1:]
depth = int(depth)
steps_pr_test = int(steps_pr_test)
n_tests = int(n_tests)


print(f"Path: {path_to_save_file}<date>.txt \nTraining depth: {depth} \nSteps per test: {steps_pr_test} \nNumber of tests: {n_tests}")

text_file = open(f"{path_to_save_file}{datetime.now()}.txt", "a+")

for d in range(depth):
    to_txt(d, steps_pr_test, n_tests)
    print(f"Finished training at depth level {d}")

text_file.close()
