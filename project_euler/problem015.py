# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6
# routes to the bottom right corner. How many such routes are there through a 20x20 grid?

import random
import math


# This is a dumb way of doing it, in which we randomly choose to go left or right and see if we ever reach the end.
# If we go out of bounds, we start over, if we reach the end the path is recorded.
# This is repeated a number of times until hopefully all possible paths are found (but does not guarantee they all are).
# It will only work for smaller grid sizes, as the number of paths it needs to try for larger grids exceeds memory.
def drunk_man_method(s, attempts):
    winning_paths = []
    for i in range(attempts):
        x, y = 0, s
        path = [(x, y)]
        while x <= s and y >= 0:
            if random.randint(0, 1) == 0:
                x = x + 1
            else:
                y = y - 1
            path.append((x, y))
            if x == s and y == 0:
                winning_paths.append(path)
                break
        if i+1 % 100000 == 0:
            print(f'At attempt {i}...')

    winning_paths = [list(x) for x in set(tuple(x) for x in winning_paths)]
    num_winning_paths = len(winning_paths)
    return num_winning_paths

# Alternatively, this problem is the same as asking: how many ways can we place 20 objects in 40 empty spaces.
# There are always going to be 40 steps for a given path: 20 down, 20 to the right.
# If we figure out how the "down" steps are placed, we can fill in the remaining steps will the "right" steps.
# This is the same as asking, "what is 40 choose 20"?

# use dumb method for 2x2:
print(f'Num paths for 2x2 grid: {drunk_man_method(2, 1000)}')


# for 20 x 20 (can't use dumb method, too many paths)
print(f'Num paths for 20x20 grid: {math.comb(40, 20)}')

