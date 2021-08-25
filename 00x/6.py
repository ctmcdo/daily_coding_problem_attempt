# An XOR linked list is a more memory efficient doubly linked list.
# Instead of each node holding next and prev fields, it holds a field named both,
# which is an XOR of the next node and the previous node. Implement an XOR linked list;
# it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
#
# If using a language that has no pointers (such as Python), you can assume you have access
# to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.


pointer_map = {}


def dereference_pointer(memory_address):
    return pointer_map[memory_address]


def get_pointer(node):
    return id(node)


class Node:
    def __init__(self, prev, value):
        self.both = prev
        self.value = value
        pointer_map[id(self)] = self


class XORLinkedList:
    def __init__(self):
        self._root = 0
        self._tail = 0
        self._len = 0

    def __add__(self, item):
        node = Node(self._tail, item)
        if self._len == 0:
            self._root = get_pointer(node)
        else:
            tnode = dereference_pointer(self._tail)
            tnode.both = tnode.both ^ get_pointer(node)
        self._tail = get_pointer(node)
        self._len += 1

    def get(self, index):
        prev = 0
        curr = self._root
        for _ in range(index):
            tmp = dereference_pointer(curr).both ^ prev
            prev = curr
            curr = tmp

        return dereference_pointer(curr)


ll = XORLinkedList()

for i in range(0, 10):
    ll.__add__(i)

for i in range(0, 10):
    assert i == ll.get(i).value
