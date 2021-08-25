# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


class Node:
    def __init__(self, c, entry=None):
        self.char = c
        self.entry = entry
        self.children = dict()


class PrefixTree:
    def __init__(self):
        self._root = Node(None)

    def insert(self, entry):
        curr = self._root
        for c in entry:
            if c in curr.children:
                curr = curr.children[c]
            else:
                child = Node(c)
                curr.children[c] = child
                curr = child
        curr.entry = entry

    def _dfs_collect_subtree(self, root, collection):
        if root.entry is not None:
            collection.add(root.entry)

        for child in root.children.values():
            self._dfs_collect_subtree(child, collection)

        return collection

    def get_autocompletions(self, s):
        curr = self._root
        for c in s:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return set()

        return self._dfs_collect_subtree(curr, set())


pt = PrefixTree()
pt.insert("dog")
pt.insert("deer")
pt.insert("deal")

assert {"deal", "deer"} == pt.get_autocompletions("de")

pt.insert("do")
pt.insert("dogecoin")
pt.insert("dogged")
pt.insert("dougal")

assert {"do", "dog", "dogecoin", "dogged", "dougal"} == pt.get_autocompletions("do")
assert {"dog", "dogged", "dogecoin"} == pt.get_autocompletions("dog")
