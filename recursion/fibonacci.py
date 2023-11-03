# build function - print the first n numbers of the fibonacci sequence
def fibonacci_recur(n):
    if n < 1:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)


# test function
fibs = []
for i in range(1, 20):
    fibs.append(str(fibonacci_recur(i)))
print(",".join(fibs))
