# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.


def greatest_non_adjacent_pair_sum(a):
    s = a[0]
    t = max(s, a[1])

    for u in a[2:]:
        u = max(s + u, t)
        s = t
        t = u

    return t


assert 12 == greatest_non_adjacent_pair_sum([2, 4, 6, 8])
assert 10 == greatest_non_adjacent_pair_sum([5, 1, 1, 5])

assert 5 ** 2 == greatest_non_adjacent_pair_sum([1, 2, 3, 4, 5, 6, 7, 8, 9])
