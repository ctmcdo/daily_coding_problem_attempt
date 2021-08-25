# Given a singly linked list and an integer k,
# remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.
#
# The list is very long, so making more than one pass is prohibitively expensive.
#
# Do this in constant space and in one pass.


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def __add__(self, value):
        node = Node(value)
        if not self._head:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node

    def remove_kth_last(self, k):
        if k == 0:
            exit("Using 1 indexing")

        count = 0
        curr = self._head
        while count <= k:
            if curr:
                curr = curr.next
                count += 1
            else:
                self._head = self._head.next
                return

        prev = self._head
        while curr:
            prev = prev.next
            curr = curr.next

        prev.next = prev.next.next

    def values(self):
        curr = self._head
        values = []
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values


ll = LinkedList()
for i in range(0, 10):
    ll.__add__(i)
assert [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == ll.values()

ll.remove_kth_last(4)
assert [0, 1, 2, 3, 4, 5, 7, 8, 9] == ll.values()

ll.remove_kth_last(2)
assert [0, 1, 2, 3, 4, 5, 7, 9] == ll.values()

ll.remove_kth_last(8)
assert [1, 2, 3, 4, 5, 7, 9] == ll.values()

for i in range(0, 7):
    ll.remove_kth_last(1)
assert [] == ll.values()
