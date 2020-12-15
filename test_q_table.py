import numpy as np, pycuber as pc, random
import pickle
import sys
import time

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

CYELLOW = '\033[43m'
CSKYBLUE = '\033[44m'
CGREEN = '\033[41m'
CEND = '\033[0m'

W = """
           .---.
          /. ./| 
      .--'.  ' ; 
     /__./ \ : | 
 .--'.  '   \' . 
/___/ \ |    ' ' 
;   \  \;      : 
 \   ;  `      | 
  .   \    .\  ; 
   \   \   ' \ | 
    :   '  |--"  
     \   \ ;     
      '---"\r      
"""                 
O = """\r             
    ,----..
   /   /   \ 
  /   .     :  
 .   /   ;.  \ 
.   ;   /  ` ; 
;   |  ; \ ; | 
|   :  | ; | ' 
.   |  ' ' ' : 
'   ;  \; /  | 
 \   \  ',  /  
  ;   :    /   
   \   \ .'    
    `---`\r"""
print(f"{W}{O}{W}")
                                                 
                                            

def display_solve(n_moves):
    cube = pc.Cube()
    print(chr(27) + "[2J")
    print(cube.__repr__())
    print("Shuffling cube")
    time.sleep(1)
    cube_shuffle(cube, n_moves)
    shuffled_cube = cube.copy()
    print(cube.__repr__())
    print("Ready?")
    time.sleep(3)
    n = 8
    for _ in range(n_moves):
        a = np.argmax(q_table[str(cube)])
        cube(actions[a])
        print(chr(27) + "[1J")
        print("From\n{}\n{}{}\\/\nTo\n{}".format(shuffled_cube.__repr__(),f"{' '*n}||\n"*n,' '*n, cube.__repr__()))
        time.sleep(1)
#    print("From\n{}\n{}{}\\/\nTo\n{}".format(shuffled_cube.__repr__(),f"{' '*n}||\n"*n,' '*n, cube.__repr__()))
    print(f"\33[30m{CYELLOW}{W}{CSKYBLUE}{O}{CGREEN}{W}{CEND}")
        

#print(n_move_test(int(sys.argv[1])-1, int(sys.argv[2]))/int(sys.argv[2]))
display_solve(int(sys.argv[1]))

