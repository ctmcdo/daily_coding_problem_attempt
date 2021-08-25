# Implement locking in a binary tree.
# A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
#
# Design a binary tree node class with the following methods:
# is_locked, which returns whether the node is locked
#
# lock, which attempts to lock the node. If it cannot be locked, then it should return false.
# Otherwise, it should lock it and return true.
#
# unlock, which unlocks the node. If it cannot be unlocked, then it should return false.
# Otherwise, it should unlock it and return true.
#
# You may augment the node to add parent pointers or any other property you would like.
# You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
# Each method should run in O(h), where h is the height of the tree.


class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value

        self.left = None
        self.right = None
        self.locked = False
        self.lock_exclusions = {}

    def lock(self):
        if not self.locked and len(self.lock_exclusions) == 0:
            self.locked = True
            if self.parent:
                self.parent.exclude_ancestors(self)
            return True
        return False

    def exclude_ancestors(self, locking_node):
        self.lock_exclusions[locking_node] = True
        if self.parent:
            self.parent.exclude_ancestors(locking_node)

    def unlock(self):
        if self.locked:
            self.locked = False
            if self.parent:
                self.parent.revert_exclusions(self)
            return True
        return False

    def revert_exclusions(self, locking_node):
        del self.lock_exclusions[locking_node]
        if self.parent:
            self.parent.revert_exclusions(locking_node)


class BinaryTree:
    def __init__(self):
        self.nodes = []

    def __add__(self, insert_index, value):
        node = None
        parent_index = int((insert_index - 1) / 2)
        if insert_index == 0 and len(self.nodes) == 0:
            node = Node(None, value)
            self.nodes.append(node)
        elif 0 <= parent_index < len(self.nodes):
            parent = self.nodes[parent_index]
            node = Node(parent, value)
            if insert_index == (2 * parent_index + 1):
                parent.left = node
            else:
                parent.right = node
            self.nodes.insert(insert_index, node)
        return node


tree = BinaryTree()
#               0
#       1               2
#   3      4         5      6
# 7   8  9   10   _    _  _   14
for i in range(0, 10):
    assert tree.__add__(i, i)
assert tree.__add__(14, 14)

assert tree.nodes[4].lock()
assert not tree.nodes[1].lock()
assert list(tree.nodes[1].lock_exclusions.keys()) == [tree.nodes[4]]
assert list(tree.nodes[0].lock_exclusions.keys()) == [tree.nodes[4]]
assert list(tree.nodes[10].lock_exclusions.keys()) == []
assert list(tree.nodes[3].lock_exclusions.keys()) == []
assert list(tree.nodes[2].lock_exclusions.keys()) == []

assert not tree.nodes[1].unlock()
assert not tree.nodes[10].unlock()
assert tree.nodes[4].unlock()
assert list(tree.nodes[1].lock_exclusions.keys()) == []
assert list(tree.nodes[0].lock_exclusions.keys()) == []
assert list(tree.nodes[10].lock_exclusions.keys()) == []
