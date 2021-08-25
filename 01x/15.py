# Given a stream of elements too large to store in memory,
# pick a random element from the stream with uniform probability.

import random


def sequence_with_unknown_size(n):
    i = 0
    a = n
    while True:
        yield i, a
        if a == 1:
            return
        i += 1
        if a % 2 == 0:
            a //= 2
        else:
            a = 3 * a + 1


def reservoir_sample(generator):
    _, s = next(generator)
    for i, a in generator:
        r = random.randint(0, i)
        if r == 1:
            s = a
    return s


print(reservoir_sample(sequence_with_unknown_size(10)))

# results from 7 runs:
# 4
# 2
# 2
# 1
# 1
# 8
# 16
