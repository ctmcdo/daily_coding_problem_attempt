# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.


# I'm using 2 sweeps, which is still linear time.
# So hopefully this is what's being asked for.
def find_smallest_missing_positive_integer(a):
    for i in range(0, len(a)):
        cyclic_permutation(a, i)

    for i in range(0, len(a)):
        if a[i] != i + 1:
            return i + 1
    return len(a) + 1


def cyclic_permutation(a, i):
    if 0 < a[i] <= len(a):
        j = a[a[i] - 1]
        if j == a[i]:
            return
        a[a[i] - 1] = a[i]
        cyclic_permutation(a, j)


assert 2 == find_smallest_missing_positive_integer([3, 4, -1, 1])
assert 3 == find_smallest_missing_positive_integer([1, 2, 0])
assert 1 == find_smallest_missing_positive_integer([-1, 2, 0])
