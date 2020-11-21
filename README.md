# 05-Lab-Qlearning-Rubik-s-Cube

## Q-Learning

### Environment

Our Environment is the Rubik's Cube.

### Actions

Our actions consist of rotating each of the cube's sides
by 90 degrees.
> See [Cube](#the-cube) section for sudo code 
### Reward

The agent receives a reward when ever the cube is brought in a state closer to
being solved as well as a bigger reward for actually solving the cube.

However each time a move is taken some amount of points is deducted from its score.

### The table

_The table of truth_:rainbow:
```Python
from collections import defaultdict
default_dict = defaultdict(lambda: [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
```

The first 6-spaces in the table represent the reward for the rotation of a side 90 degrees clockwise. The subsequent spaces represent the reward for a 90 degree rotation counterclockwise:
Sides/Spaces = [_left, right, front, back, top, bottom, c_left, c_right, c_front, c_back, c_top, c_bottom_]

### Q-function

$q(s,a) =r(s,a) + \gamma \cdot \underset{a'}{\text{max}}~q(s',a')$ 

Where $a'$ is the action which leads to the highest reward and $s'$ the state achived from that action.
$\gamma$ is the discount factor, which is a value from 0 up to 1 - $\gamma \in ~]0;1[$.
The discount factor determains how much "immidiate" reward is valued. For low discount values immidiate reward is valued higher, since we multiply the next qualia with a low value, where a higher value in turn makes the rewards of subsequent states more valued.
> Since the value is between 0 and 1 q(s,a) is guaranteed to converge to some number R. 

### R-function

```Ocaml
def r(s):
    if s != SOLVED_STATE:
        return -1
    elif s == SOLVED_STATE:
        return 1
```

## The Cube
### Initialize Rubik's Cube

```Python
cube = State()
```

### How to move

```Python
cube.move('side') -> Rotates the side of the cube specified 90 degrees clockwise
```
#### Available moves

`moves = [left, right, front, back, top, bottom]`


###
    # AI controller (enable/disable by pressing 'a')
    if runai:
        # INSERT YOUR CODE HERE (2/2)
        #
        # Implement a Grid World AI (q-learning): Control the person by 
        # learning the optimal actions through trial and error
        #
        # The state of the environment is available in the variables
        #    x, y     : Coordinates of the person (integers 0-9)
        #    has_key  : Has key or not (boolean)
        #
        # To take an action in the environment, use the call
        #    (x, y, has_key), reward, done = env.step(action)
        #
        #    This gives you an updated state and reward as well as a Boolean 
        #    done indicating if the game is finished. When the AI is running, 
        #    the game restarts if done=True

        # 1. choose an action
        # 2. step the environment
        (x, y, has_key), reward, done = env.step(action)
        # 3. update q table

        # END OF YOUR CODE (2/2)