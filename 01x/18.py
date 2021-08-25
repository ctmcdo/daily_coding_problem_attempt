# Given an array of integers and a number k, where 1 <= k <= length of the array,
# compute the maximum values of each subarray of length k.
#
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
#
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
# You can simply print them out as you compute them.

from collections import deque


def rolling_max(A, k):
    if k == 1:
        return A

    d = deque()
    d.append(0)
    for i in range(1, k):
        while d and A[i] >= A[d[-1]]:
            d.pop()
        d.append(i)
    A[0] = A[d[0]]

    for i in range(k, len(A)):
        if d and d[0] == (i - k):
            d.popleft()

        while d and A[i] >= A[d[-1]]:
            d.pop()
        d.append(i)
        A[i - k + 1] = A[d[0]]

    return A


assert [10, 7, 8, 8] == rolling_max([10, 5, 2, 7, 8, 7], 3)[:4]
assert [6, 5, 4, 3, 2, 1] == rolling_max([6, 5, 4, 3, 2, 1], 4)
assert [4, 5, 6] == rolling_max([1, 2, 3, 4, 5, 6], 4)[:3]
