import numpy as np

def does_recursion_work(n, step, step_max, gamma=0.9):
    new_n = n + 3
    print(new_n)
    if step == step_max:
        return new_n
#    print(f"{new_n} * 0.9 * ")
    print(f"{new_n} + 0.9 * {does_recursion_work(new_n, step+1, step_max)} at step {step}")
    return new_n + gamma*does_recursion_work(new_n, step+1, step_max) 

print(0.9*does_recursion_work(0,0,3))

"""
print(2 + 0.9*4+ 0.9*0.9 * 6 + 0.9*0.9*0.9 * 8)
print(0.9**4 * 8)

print(0.9**3*9)
"""
#0 + 0.9 * 3 + ()
#reward + gamma * q_cum
#print(0.9*(3+0.9**1*(  6+0.9**2*(  9+0.9**3*(   12+0.9**4  )  )  )  ))

print(0.9*(3+0.9*(6 + 0.9 *(9 + 0.9 * 12))))