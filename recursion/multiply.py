# build function
def multiply_recur(x, y):
    if y == 0 or x == 0:
        return 0
    elif x < 0 and y < 0:
        return multiply_recur(-x, -y)
    elif x < 0:
        return -1 * multiply_recur(-x, y)
    elif y < 0:
        return -1 * multiply_recur(x, -y)
    elif y == 1:
        return x
    else:
        return x + multiply_recur(x, y-1)


# test cases
assert multiply_recur(0, 1) == 0
assert multiply_recur(1, 0) == 0
assert multiply_recur(2, 3) == 6
assert multiply_recur(3, 2) == 6
assert multiply_recur(-3, 2) == -6
assert multiply_recur(-2, 3) == -6
assert multiply_recur(-2, -3) == 6
assert multiply_recur(125, 63) == 7875

# sample
print(multiply_recur(5, -52))
