# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log get_last(i): gets the ith last element from the log.
# i is guaranteed to be smaller than or equal to N. You should be as efficient with time and space as possible.


class CircularBuffer:
    def __init__(self, n):
        self._n = n
        self.a = [None] * n
        self._head = -1

    def record(self, order_id):
        self._head += 1
        self._head %= self._n
        self.a[self._head] = order_id

    def get_last(self, i):
        return self.a[self._head - i]


buffer = CircularBuffer(5)
for i in range(0, 8):
    buffer.record(i)

for i in range(0, 5):
    assert (7 - i) == buffer.get_last(i)

assert 5 == buffer.a[0]
assert 6 == buffer.a[1]
assert 7 == buffer.a[2]
assert 3 == buffer.a[3]
assert 4 == buffer.a[4]
