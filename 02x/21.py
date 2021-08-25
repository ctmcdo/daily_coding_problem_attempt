# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
# find the minimum number of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

import bisect
from collections import defaultdict


def max_required_classrooms(intervals):
    significant_points = list()
    point_diff = defaultdict(int)

    for ival in intervals:
        bisect.insort(significant_points, ival[0])
        bisect.insort(significant_points, ival[1])
        point_diff[ival[0]] += 1
        point_diff[ival[1]] -= 1

    max_rooms = 0
    curr_rooms = 0
    for p in significant_points:
        curr_rooms += point_diff[p]
        if curr_rooms > max_rooms:
            max_rooms = curr_rooms

    return max_rooms


assert 2 == max_required_classrooms([(30, 75), (0, 50), (60, 150)])
assert 2 == max_required_classrooms([(0, 100), (10, 20), (20, 30)])
assert 3 == max_required_classrooms([(0, 100), (10, 30), (20, 40), (30, 50)])
assert 4 == max_required_classrooms([(0, 100), (10, 30), (20, 40), (29, 50)])
