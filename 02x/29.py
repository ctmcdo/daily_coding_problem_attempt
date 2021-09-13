# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
#
# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.


def run_length_encoding(s):
    parts = []
    run = 0
    last_char = s[0]
    for c in s:
        if c == last_char:
            run += 1
        else:
            parts.append(str(run) + last_char)
            run = 1
            last_char = c
    parts.append(str(run) + last_char)

    return "".join(parts)


def decode_run_length_encoding(s):
    return "".join([int(s[i * 2]) * s[i * 2 + 1] for i in range(0, int(len(s) / 2))])


assert "4A3B2C1D2A" == run_length_encoding("AAAABBBCCDAA")
assert "AAAABBBCCDAA" == decode_run_length_encoding("4A3B2C1D2A")
