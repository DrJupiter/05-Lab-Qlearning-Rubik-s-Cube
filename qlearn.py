from fork import State, shuffle, move
from collections import defaultdict 
import hashlib
import random
import numpy as np
from copy import deepcopy


cube = State()

actions = ['left', 'right', 'front', 'back', 'top', 'bottom', 'c_left', 'c_right', 'c_front', 'c_back', 'c_top', 'c_bottom']

q_table = defaultdict(lambda: np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]))



### Somthing somthing

#V = [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]

gamma = 0.9

#def Fat(stat):
#    nxt_move = []
#    for i in range(12)
#        nxt_move[i] = current_state.move(actions[i])
#
#
#def Red(stat):
#    if stat == 0:
#        return 1
#    else:
#        return -1


#for t in range(1000):
#    # Loop over all states
#    for s in range(6):
#        # Update value
#        V[s] = Red(s)+max([gamma*V[sp] for sp in F[s]])
#
#print(V)

###


# It measures the value of taking action a in state s
# which means that we should check the value of each state action pair for an action?
# No not quite, we use the epsilon_greedy function to determine, if we should
# Do the action with the current highest quality or try something random
def epsilon_greedy(epsilon=0.1):
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
def r(s,a):
    tmp_s = move(s, a)
    if tmp_s.isGoalState():
        return 10
    else:
        return -1

def q(s,a, gamma=0.9):
    current_score = r(s,a)
    if abs(gamma *) < 0.04:
        return 
    current_score = r(s,a) + max(q_table[move(s,a).__hash__()])

def q_action(s):
#    q_update(s)
    if epsilon_greedy():
        a = random.randint(0,len(actions)-1)
    else:
        a = np.argmax(q_table[s.__hash__()])
    # We store the key of the previous state
    cube_hash = s.__hash__()
    # the state s is mutated by taking the action determined by the epsilon_greedy() function call
    s.move(actions[a])
    # We then pass the q_update function the key: cube_hash, index into quality array at key: a, current_state: s
    q_update(cube_hash, a, s)
# Maybe the return isn't needed
#    return s

# the current_state should represent a (state,action)-pair
def q_update(key, index, current_state):
    reward = r(current_state)
    current_quality = deepcopy(q_table[key][index])
    # check with +=
    q_table[key][index] += reward + cumulative_quality(current_state, current_quality, step=1)

# q_table[key][index] += reward + cumulative_quality(current_state,
# q_table[current_state] = should be 
#)

    
def cumulative_quality(s, current_quality, gamma=0.9, step):
    key = s.__hash__()
    action, value = find_max_index_value(q_table[key])
    new_quality = current_quality + gamma * value
    if abs((current_quality-new_quality)/current_quality) < 0.1:
        return current_quality
    
    return gamma*cumulative_quality(move(s,action),new_quality)
    

    return gamma*cumulative_quality


def find_max_index_value(iteratable)
    g_index = 0
    g_value = 0
    for index, value in enumerate(iterable):
        if value > iterable[g_index]:
            g_index = index
            g_value = value
    return (g_index,g_value)

    

def testhash():
    cube = State()
    print(cube.__hash__())
    print(q_table[cube.__hash__()])
    q_table[cube.__hash__()][0] = 1
    print(q_table[cube.__hash__()])
