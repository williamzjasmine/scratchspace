# The sum of the squares of the first ten natural numbers is 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is (1+2+...+10)^2 = 3,025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3,025 - 385 = 2,640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

square_sum = 0
sum_square = 0
for i in range(101):
    sum_square += i*i
    square_sum += i
print(square_sum*square_sum - sum_square)