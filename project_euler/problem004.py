# A palindromic number reads the same both ways. The largest palindrome made from the product of two-digit numbers is
# 9,099 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

nums = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if (ij := str(i*j)) == ij[::-1]:
            nums.append(i*j)
print(max(nums))