# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


def list_contains_pair_whose_sum_is(a, k):
    d = dict()
    for a_i in a:
        diff = k - a_i
        if (diff,) in d:
            return True
        d[(a_i,)] = True
    return False


assert list_contains_pair_whose_sum_is([10, 15, 3, 7], 17)
assert not list_contains_pair_whose_sum_is([10, 15, 3, 7], 16)
assert list_contains_pair_whose_sum_is([10, 15, 3, 7], 18)
