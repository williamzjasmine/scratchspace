# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one pythagorean triplet for which a + b + c = 1,000. Find the product abc.
import time


class Found(Exception):
    pass


st = time.time()
counter = 0
try:
    for a in range(1, 1000):
        for b in range(1, 1000):
            if a + b > 1000:                          # don't continue if sum too large
                break
            for c in range(max([a, b]), 1000):        # hypotenuse always has to be bigger
                counter += 1
                if a + b + c > 1000:                  # don't continue if sum too large
                    break
                if a ** 2 + b ** 2 == c ** 2:
                    if a + b + c == 1000:
                        et = time.time()
                        raise Found                   # stop all loops once answer is found

except Found:
    rt = round(et - st, 4)
    prod = a * b * c
    wc = 1000 ** 2 * (a - 1) + (b * c)
    rt_wc = round(rt * (wc / counter), 2)
    print(f'The pythagorean triplet that adds to 1,000 is: {a}, {b}, {c}')
    print(f'and has product {prod:,}.')
    print(f'Found in {rt}s after {counter:,} iterations...')
    print(f'Number of iterations needed if only using brute force is {wc:,} with estimated runtime of {rt_wc:}s')


# Much simpler and faster answer that I realized afterward...
# for a in range(1, 1000):
#     for b in range(1, 1000):
#         c = 1000 - a - b
#         if a ** 2 + b ** 2 == c **  2:
#             result = a * b * c
# print(result)