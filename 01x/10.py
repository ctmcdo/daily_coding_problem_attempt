# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import decimal
import time


def call_after_n_msecs(f, n):
    time.sleep((decimal.Decimal(n) / decimal.Decimal(1000)).__float__())
    return f()


t1 = time.time_ns()
assert 500 == call_after_n_msecs(lambda: time.time_ns() - t1, 500) // 10 ** 6
