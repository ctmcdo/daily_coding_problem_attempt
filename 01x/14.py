# The area of a circle is defined as r^2. Estimate \pi to 3 decimal places using a Monte Carlo method.
#
# Hint: The basic equation of a circle is x^2 + y^2 = r^2.

import cython
import random


def pi_estimation(sample_size: cython.int):
    pos: cython.int = 0
    i: cython.int
    for i in range(0, sample_size):
        x: cython.double = random.random()
        y: cython.double = random.random()
        if x ** 2 + y ** 2 <= 1:
            pos += 1
    return 2 ** 2 * pos / sample_size


# given we know pi is of the order of 10^0,
# and we require 10^-3 precision, we require roughly 10^4^2 = 10^8 samples
assert "3.141" == str(pi_estimation(10 ** 8))[0:5]
