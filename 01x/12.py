# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
#
# What if, instead of being able to climb 1 or 2 steps at a time,
# you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

import math


def recurse_compositions(a, r, comp_size, f):
    s = 0
    if r == 0:
        return math.factorial(comp_size) // f
    elif r > 0 and len(a) > 0:
        for i in range(0, r // a[0] + 1):
            s += recurse_compositions(
                a[1:], r - i * a[0], comp_size + i, math.factorial(i) * f
            )
    return s


def count_restricted_compositions(a, n):
    return recurse_compositions(a, n, 0, 1)


assert 5 == count_restricted_compositions([1, 2], 4)

assert 3 == count_restricted_compositions([1, 3, 5], 4)  # 1111, 13, 31
assert 5 == count_restricted_compositions([1, 3, 5], 5)  # 11111, 113, 131, 311, 5
