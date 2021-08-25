# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

import networkx as nx


def count_unival_subtrees(t, node):
    parity = node % 2
    t.nodes[node][0] = parity == 0
    t.nodes[node][1] = parity == 1

    subtree_sum = 0
    for _, child in t.out_edges(node):
        subtree_sum += count_unival_subtrees(t, child)
        t.nodes[node][0] |= t.nodes[child][0]
        t.nodes[node][1] |= t.nodes[child][1]

    return subtree_sum + int(t.nodes[node][0] != t.nodes[node][1])


tree_ = nx.DiGraph()
tree_.add_edge(0, 1)
tree_.add_edge(0, 2)
tree_.add_edge(2, 3)
tree_.add_edge(2, 4)
tree_.add_edge(3, 5)
tree_.add_edge(3, 7)

# tree_str = nx.forest_str(tree_, sources=[0])
# mod_tree_str = "".join([c if not c.isdigit() else str(int(c) % 2) for c in tree_str])
# print(mod_tree_str)
#
# ╙── 0
#     ├─╼ 1
#     └─╼ 0
#         ├─╼ 1
#         │   ├─╼ 1
#         │   └─╼ 1
#         └─╼ 0

assert 5 == count_unival_subtrees(tree_, 0)

tree_ = nx.random_tree(n=10, seed=12, create_using=nx.DiGraph)

# tree_str = nx.forest_str(tree_, sources=[0])
# mod_tree_str = "".join([c if not c.isdigit() else str(int(c) % 2) for c in tree_str])
# print(mod_tree_str)
#
# ╙── 0
#     ├─╼ 0
#     │   └─╼ 0
#     │       └─╼ 0
#     │           └─╼ 0
#     │               └─╼ 1
#     └─╼ 1
#         ├─╼ 1
#         │   └─╼ 1
#         └─╼ 1

assert 5 == count_unival_subtrees(tree_, 0)
