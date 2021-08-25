# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).
#
# For example, given the string "([])", you should return true.
#
# Given the string "([)]" or "((()", you should return false.

open_brackets = ["(", "{", "["]
close_brackets = [")", "}", "]"]


def are_parentheses_balanced(parentheses):
    stack = []
    for p in parentheses:
        if p in open_brackets:
            stack.append(p)
        elif p in close_brackets:
            if len(stack) == 0 or close_brackets.index(p) != open_brackets.index(
                stack.pop()
            ):
                return False
        else:
            exit("Unexpected character")

    return 0 == len(stack)


assert are_parentheses_balanced("([])")
assert not are_parentheses_balanced("([)]")
assert not are_parentheses_balanced("((()")
assert are_parentheses_balanced("[()()()(){(())}]")
