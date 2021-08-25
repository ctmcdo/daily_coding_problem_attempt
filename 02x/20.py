# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
#
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
#
# In this example, assume nodes with the same value are the exact same node objects.
#
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.


# assuming the lists don't have length properties
def intersecting_node(l1, l2):
    l1i = iter(l1)
    M = 0
    while True:
        try:
            next(l1i)
            M += 1
        except StopIteration:
            break

    l2i = iter(l2)
    N = 0
    while True:
        try:
            next(l2i)
            N += 1
        except StopIteration:
            break

    l1i = iter(l1)
    l2i = iter(l2)
    if M > N:
        smaller_len = N
        for i in range(0, M - N):
            next(l1i)
    else:
        smaller_len = M
        for i in range(0, N - M):
            next(l2i)

    for i in range(0, smaller_len):
        node1 = next(l1i)
        node2 = next(l2i)
        if node1 == node2:
            return node1

    return None


assert 8 == intersecting_node([3, 7, 8, 10], [99, 1, 8, 10])
assert 8 == intersecting_node([98, 97, 2, 3, 7, 8, 10], [99, 1, 8, 10])
assert 0 == intersecting_node([0, 1, 2], [0, 1, 2])
assert None is intersecting_node([1, 2, 3], [4, 5])
