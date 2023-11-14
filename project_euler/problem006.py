# The sum of the squares of the first ten natural numbers is 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is (1+2+...+10)^2 = 3,025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3,025 - 385 = 2,640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# brute force method
square_sum = 0
sum_square = 0
n = 100
for i in range(n+1):
    sum_square += i*i
    square_sum += i
print(f'Via brtue force: {square_sum*square_sum - sum_square}')

# using commonly known formulas for these sums. See: https://byjus.com/maths/sum-of-squares/

square_sum = ((n*(n+1))/2) ** 2
sum_square = (n*(n+1)*(2*n+1)) / 6
print(f'Via summation formulas: {square_sum - sum_square}')