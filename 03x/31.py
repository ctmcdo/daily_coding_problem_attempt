# The edit distance between two strings refers to the minimum number of character insertions, deletions,
# and substitutions required to change one string to the other. For example, the edit distance between "kitten"
# and "sitting" is three: substitute the "k" for "s", substitute the "e" for "i", and append a "g".
#
# Given two strings, compute the edit distance between them.


def levenshtein_distance(s, t):
    v0 = [0] * (len(t) + 1)
    v1 = [0] * (len(t) + 1)

    for i in range(0, len(t) + 1):
        v0[i] = i

    for i in range(0, len(s)):
        v1[0] = i + 1

        for j in range(0, len(t)):
            deletion_cost = v0[j + 1] + 1
            insertion_cost = v1[j] + 1
            if s[i] == t[j]:
                substitution_cost = v0[j]
            else:
                substitution_cost = v0[j] + 1

            v1[j + 1] = min(deletion_cost, insertion_cost, substitution_cost)

        c = v0
        v0 = v1
        v1 = c

    return v0[len(t)]


assert 3 == levenshtein_distance("kitten", "sitting")
assert 2 == levenshtein_distance("shallow", "hollow")
assert 3 == levenshtein_distance("shallow", "hallowed")
assert 4 == levenshtein_distance("abcd", "efgh")
assert 2 == levenshtein_distance("abcd", "acbd")
