# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.


def decodings_count(a):
    if len(a) == 0:
        return 1
    if a[0] == "0":
        return 0
    if len(a) == 1:
        return 1

    count = decodings_count(a[1:])
    if int(a[0]) * 10 + int(a[1]) <= 26:
        count += decodings_count(a[2:])
    return count


assert 2 == decodings_count("11")  # aa, k
assert 1 == decodings_count("31")  # ca
assert 3 == decodings_count("111")  # aaa, ka, ak
assert 1 == decodings_count("110")  # ak
assert 8 == decodings_count("12121")  # ababa, abau, abla, auba, auu, laba, lau, lla
