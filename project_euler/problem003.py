# The prime factors of 13,195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600,851,475,143?

og = 13195
num = og
fact = num
while num > 1:
    for i in reversed(range(int(num/2)+1)):      # start by seeing if number is divisible by 2.
        if i == 1:                               # means we found the largest prime factor (can't be divided further)
            num = 1
            break
        if num % i == 0:                         # keep dividing the num down until we find the largest prime factor
            num = i
            fact = num
            break
        num = 1

print(f'The largest prime factor of {og} is {fact}.')