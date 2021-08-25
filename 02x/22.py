# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
# If there is more than one possible reconstruction, return any of them.
# If there is no possible reconstruction, then return null.
#
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].
#
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
# return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].


class Node:
    def __init__(self, c, entry=None):
        self.char = c
        self.entry = entry
        self.children = dict()


class PrefixTree:
    def __init__(self, sentence_no_spaces):
        self.root = Node(None)
        self._sentence_no_spaces = sentence_no_spaces

    def insert(self, entry):
        curr = self.root
        for c in entry:
            if c in curr.children:
                curr = curr.children[c]
            else:
                child = Node(c)
                curr.children[c] = child
                curr = child
        curr.entry = entry

    def search_from_node(self, node, i):
        curr = node
        while self._sentence_no_spaces[i] in curr.children:
            child = curr.children[self._sentence_no_spaces[i]]
            if child.entry is not None:
                return child.entry, child
            curr = child
            i += 1

        return None, None


def find_sentence(dictionary, sentence_no_spaces):
    trie = PrefixTree(sentence_no_spaces)
    for word in dictionary:
        trie.insert(word)

    word_stack, node_stack = [], []
    curr = trie.root
    num_letters_accounted_for = 0
    continuation_word_len = 0
    while num_letters_accounted_for != len(sentence_no_spaces):
        word, node = trie.search_from_node(curr, num_letters_accounted_for)
        if word is not None:
            word_stack.append(word)
            node_stack.append(node)

            num_letters_accounted_for += len(word)
            if continuation_word_len:
                num_letters_accounted_for -= continuation_word_len
                continuation_word_len = 0

            curr = trie.root
        elif len(word_stack) > 0:
            last_word_len = len(word_stack.pop())
            if not continuation_word_len:
                continuation_word_len = last_word_len
            else:
                continuation_word_len = 0
                num_letters_accounted_for -= last_word_len

            curr = node_stack.pop()
        else:
            return None

    return word_stack


assert ["the", "quick", "brown", "fox"] == find_sentence(
    {"the", "quick", "brown", "fox"}, "thequickbrownfox"
)

assert ["bed", "bath", "and", "beyond"] == find_sentence(
    {"bed", "bath", "bedbath", "and", "beyond"}, "bedbathandbeyond"
)

assert None == find_sentence(
    {"beds", "bath", "bedbaths", "and", "beyond"}, "bedbathandbeyond"
)

# fmt: off
assert ["the", "perrin", "pages", "will", "help", "you", "find", "your", "calling", "but",
        "dont", "be", "duped", "cut", "down", "the", "woods", "they", "be", "erdos"] == \
       find_sentence({"the", "perrin", "pages", "will", "help", "you", "find",
                      "your", "calling", "but", "dont", "be", "duped", "cut",
                      "down", "the", "woods", "they", "be", "erdos"},
                     "theperrinpageswillhelpyoufindyourcallingbutdontbedupedcutdownthewoodstheybeerdos",
                     )
