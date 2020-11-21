from fork import State, shuffle, move
from collections import defaultdict 

cube = State()

actions = ['left', 'right', 'front', 'back', 'top', 'bottom', 'c_left', 'c_right', 'c_front', 'c_back', 'c_top', 'c_bottom']

def r(s,a):