# Given the root to a binary tree, implement serialize(root),
# which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.


import networkx as nx


# I serialise/deserialise general trees
def serialise_tree_helper(tree_graph, root):
    s = "("
    for _, child in tree_graph.out_edges(root):
        s += str(child) + serialise_tree_helper(tree_graph, child)
    return s + ")"


def serialise_tree(tree_graph, root):
    s = str(root)
    return s + serialise_tree_helper(tree_graph, root)


def deserialise_tree(serialised_tree):
    tree = nx.DiGraph()

    stack = []
    for ci in range(1, len(serialised_tree)):
        c = serialised_tree[ci]
        if c == "(":
            stack.append(serialised_tree[ci - 1])
        elif c == ")":
            stack.pop()
        else:
            tree.add_edge(int(stack[-1]), int(c))
    return tree


tree_ = nx.random_tree(n=10, seed=2, create_using=nx.DiGraph)
assert nx.forest_str(
    deserialise_tree(serialise_tree(tree_, 0)), sources=[0]
) == nx.forest_str(tree_, sources=[0])
