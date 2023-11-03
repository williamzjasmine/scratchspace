# build function
def exponentiate_recur(x, y):
    if y == 0:
        return 1
    elif y < 0:
        return 1 / exponentiate_recur(x, -y)
    elif x < 0:
        if y % 2 != 0:
            return -exponentiate_recur(-x, y)
        else:
            return exponentiate_recur(-x, y)
    elif y == 1:
        return x
    else:
        return x * exponentiate_recur(x, y-1)


# test cases
assert exponentiate_recur(0, 0) == 1
assert exponentiate_recur(1, 0) == 1
assert exponentiate_recur(5, 2) == 25
assert exponentiate_recur(5, -2) == 1/25
assert exponentiate_recur(-5, 2) == 25
assert exponentiate_recur(-5, 3) == -125
assert exponentiate_recur(-5, -2) == 1/25
assert exponentiate_recur(-5, -3) == -1/125

# sample
print(exponentiate_recur(-5, -3))