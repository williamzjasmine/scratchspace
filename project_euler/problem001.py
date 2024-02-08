# Description: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum
# of these multiples 23. Find the sum of all the multiples of 3 and 5 below 1000.

def find_mult_sum(n):
    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

print(find_mult_sum(1000))




