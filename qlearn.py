from fork import State, shuffle, move
import fork
from collections import defaultdict 
import hashlib
import random
import numpy as np
from copy import deepcopy

#actions = ['left', 'right', 'front', 'back', 'top', 'bottom', 'c_left', 'c_right', 'c_front', 'c_back', 'c_top', 'c_bottom']
#q_table = defaultdict(lambda: np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]))
actions = ['left', 'right', 'front', 'back', 'top', 'bottom']
q_table = defaultdict(lambda: np.array([0., 0., 0., 0., 0., 0.]))

"""
q_action(s) -> q_update(state_key, action_index, copy_of(s'')) -> cumulative_quality(copy_of(s''), 0)
                                                                                        |
                                                                                        |
                                                                                    Fordi vi vil muterer s'', men bevare,
                                                                                    hvor vi er lige nu i forhold til q_action(s)
"""


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

def r(s):
    if s.isGoalState():
        return 1
    else:
        return -0.1
    

def q_action(s):
    if epsilon_greedy():
        a = random.randint(0,len(actions)-1)
    else:
        a = np.argmax(q_table[s.__hash__()])
    # We store the key of the previous state
    cube_hash = s.__hash__()
    # the state s is mutated by taking the action determined by the epsilon_greedy() function call
    s.move(actions[a])
    # We then pass the q_update function the key: cube_hash, index into quality array at key: a, current_state: s
    q_update(cube_hash, a, deepcopy(s))
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
    key = s.__hash__()
    action, value = find_max_index_value(q_table[key])
    new_quality = current_quality + value
    if abs((current_quality-new_quality)/(current_quality+10**(-9))) < 0.1 or s.isGoalState():
        return new_quality
    
    return new_quality + gamma*cumulative_quality(s.move(actions[action]),new_quality)


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

for _ in range(100000):
    cube = State()
    cube.n_move_shuffle(2, actions)
    for _ in range(2):
        q_action(cube)

aq = list(q_table.values())
good_paths = 0
for element in aq:
    if any(element):
        good_paths += 1
        print(element)
print(f"number of paths: {len(aq)}")
print(f"good paths: {good_paths}")

