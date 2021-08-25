# Given an integer k and a string s,
# find the length of the longest substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

from collections import defaultdict


def rolling_longest_substring(s, k):
    longest_substring, i = "", 0
    d = defaultdict(int)
    for j in range(0, len(s)):
        d[s[j]] += 1
        if len(d) > k:
            if d[s[i]] == 1:
                del d[s[i]]
            else:
                d[s[i]] -= 1
            i += 1
        elif (j - i + 1) > len(longest_substring):
            longest_substring = s[i : j + 1]
    return longest_substring


assert "bcb" == rolling_longest_substring("abcba", 2)
assert "abcbaa" == rolling_longest_substring("abcbaa", 3)
assert "abcbaa" == rolling_longest_substring("dabcbaa", 3)
assert "bcdedcb" == rolling_longest_substring("abcdedcba", 4)
