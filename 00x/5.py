# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
#
# def cons(a, b):
#     return lambda f : f(a, b)
#
# Implement car and cdr.


def cons(a, b):
    return lambda f: f(a, b)


def car(u):
    return u(lambda a, b: a)


def cdr(u):
    return u(lambda a, b: b)


assert 3 == car(cons(3, 4))
assert 4 == cdr(cons(3, 4))
