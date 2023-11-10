import random

s = 8
attempts = 500000
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
            #if path not in winning_paths:
            winning_paths.append(path)
            break
    if i % 100000 == 0:
        print(f'At attempt {i}...')

winning_paths = [list(x) for x in set(tuple(x) for x in winning_paths)]
num_winning_paths = len(winning_paths)
print(f'There were {num_winning_paths} winning paths found.')

