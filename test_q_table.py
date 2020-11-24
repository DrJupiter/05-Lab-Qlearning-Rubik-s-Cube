import numpy as np, pycuber as pc, random
import pickle
import sys

def dd():
    return np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]) 

actions = ["U", "L", "F", "R", "B", "D","U'", "L'", "F'", "R'", "B'", "D'"]

SOLVED_CUBE = pc.Cube()


f = open("q_table", "rb")
q_table = pickle.load(f)
f.close()

def cube_shuffle(cube, n):
    for _ in range(n):
        cube(actions[random.randint(0, len(actions)-1)])


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

print(n_move_test(int(sys.argv[1])-1, int(sys.argv[2]))/int(sys.argv[2]))