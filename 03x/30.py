# You are given an array of non-negative integers that represents a two-dimensional
# elevation map where each element is unit-width wall and the integer is the height.
# Suppose it will rain and all spots between two walls get filled up.
#
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
#
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
#
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the
# second, and 3 in the fourth index (we cannot hold 5 since it would run off to the
# left), so we can trap 8 units of water.


# this one is very tricky IMO.
# the water above any wall/index is determined by the the highest walls to left
# and right. In fact we only need to know the lesser of these two.
# By iterating from 0 and n-1 until we meet at some index, we can track maximum
# value to left of left pointer and maximum value to right of right pointer.
# The trick is to notice that we can choose which pointer to increment inwards
# such that either the left pointer's curr maximum or the right pointer's curr
# maximum is the minimum of the real maximums at the left/right pointer.
# Increment the pointer which currently points to the lesser element and we can
# be sure that the untracked maximum (right in case of left pointer and right in
# case of left pointer) is greater than the tracked maximum.
def water_capacity(walls):
    left_max = 0
    right_max = 0

    left = 0
    right = len(walls) - 1
    units = 0
    while left <= right:
        if walls[left] < walls[right]:
            if walls[left] > left_max:  # no water can be stored on top
                left_max = walls[left]
            else:
                units += left_max - walls[left]
            left += 1
        else:
            if walls[right] > right_max:
                right_max = walls[right]
            else:
                units += right_max - walls[right]
            right -= 1

    return units


assert 1 == water_capacity([2, 1, 2])
assert 8 == water_capacity([3, 0, 1, 3, 0, 5])

#       .
#     . .
#   . . .
# . . . .
assert 0 == water_capacity([1, 2, 3, 4])

# .   .
# .   .   .
# . . .   .   .
# . . . . . . .
assert 5 == water_capacity([4, 2, 4, 1, 3, 1, 2])
