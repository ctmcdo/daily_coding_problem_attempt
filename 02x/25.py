# Implement regular expression matching with the following special characters:
#
#     . (period) which matches any single character
#     * (asterisk) which matches zero or more of the preceding element That is, implement a function that takes in a
#     string and a valid regular expression and returns whether or not the string matches the regular expression.
#
# For example, given the regular expression "ra." and the string "ray", your function should return true.
# The same regular expression on the string "raymond" should return false.
#
# Given the regular expression ".*at" and the string "chat", your function should return true.
# The same regular expression on the string "chats" should return false.


# not allowing period and star literals.
def match_helper(r, i, s, j):
    if j == len(s):
        if len(r) > i + 1 and r[i + 1] == "*":
            return match_helper(r, i + 2, s, j)
        else:
            return i == len(r)
    elif i == len(r):
        return False

    if r[0] == "*":
        exit("The preceding token is not quantifiable")

    cj_is_matched = r[i] == "." or r[i] == s[j]
    if len(r) > i + 1 and r[i + 1] == "*":
        # 0 chars
        return match_helper(r, i + 2, s, j) or (
            cj_is_matched and match_helper(r, i, s, j + 1)
        )  # or 1 char
    return cj_is_matched and match_helper(r, i + 1, s, j + 1)


def is_whole_string_matched(r, s):
    return match_helper(r, 0, s, 0)


assert is_whole_string_matched("ra.", "ray")
assert not is_whole_string_matched("ra.", "raymond")
assert is_whole_string_matched(".*at", "chat")
assert not is_whole_string_matched(".*at", "chats")
assert is_whole_string_matched(".*", "chat")
assert is_whole_string_matched(".*.*", "chat")
assert is_whole_string_matched("chat.*", "chat")
assert is_whole_string_matched("chat.*.*", "chat")
assert is_whole_string_matched("chatz*", "chat")
assert is_whole_string_matched("chat*", "chat")
