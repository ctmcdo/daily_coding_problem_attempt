# Write an algorithm to justify text. Given a sequence of words and an integer line length k,
# return a list of strings which represents each line, fully justified.
#
# More specifically, you should have as many words as possible in each line. There should be at least one space
# between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be
# distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
#
# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
#
# Each word is guaranteed not to be longer than k.
#
# For example, given the list of words
# ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
#
# ["the quick brown", # 1 extra space on the left "fox jumps over", # 2 extra spaces distributed evenly "the lazy dog"]
# 4 extra spaces distributed evenly

import sys


def justified_line_breaks(words, max_line_width):
    min_costs = []
    line_breaks = []
    alphanumeric_lengths = []

    for i in range(0, len(words)):
        min_cost = sys.maxsize * 2 + 1
        min_line_break = -1
        min_alphanumeric_length = -1

        alphanumeric_length = 0
        for j in range(i, -1, -1):
            line_length_without_padding = alphanumeric_length + len(words[j]) + (i - j)
            if line_length_without_padding > max_line_width:
                break
            alphanumeric_length += len(words[j])

            cost = (max_line_width - line_length_without_padding) ** 2 + (
                min_costs[j - 1] if j > 0 else 0
            )
            if cost < min_cost:
                min_cost = cost
                min_line_break = j
                min_alphanumeric_length = alphanumeric_length

        min_costs.append(min_cost)
        line_breaks.append(min_line_break)
        alphanumeric_lengths.append(min_alphanumeric_length)

    return line_breaks, alphanumeric_lengths


def justify_text(words, max_line_width):
    line_breaks, alphanumeric_lengths = justified_line_breaks(words, max_line_width)

    lines = []
    word_slice_indices = [(line_breaks[-1], len(words))]
    while word_slice_indices[-1][0] != 0:
        word_slice_indices.append(
            (line_breaks[word_slice_indices[-1][0] - 1], word_slice_indices[-1][0])
        )

    for i in range(len(word_slice_indices) - 1, -1, -1):
        last_word = word_slice_indices[i][1] - 1
        alphanumeric_length = alphanumeric_lengths[last_word]
        spaces_remainder = max_line_width - alphanumeric_length

        num_words = word_slice_indices[i][1] - word_slice_indices[i][0]
        if num_words > 1:
            common_spaces = int(spaces_remainder / (num_words - 1))
            spaces_remainder -= common_spaces * (num_words - 1)

            line = []
            for j in range(word_slice_indices[i][0], last_word):
                num_spaces_suffix = common_spaces
                if spaces_remainder > 0:
                    num_spaces_suffix += 1
                line.append(words[j] + num_spaces_suffix * " ")
                spaces_remainder -= 1
            line.append(words[last_word])

            lines.append("".join(line))
        else:
            lines.append(words[last_word] + spaces_remainder * " ")

    return "\n".join(lines)


# the  quick brown
# fox  jumps  over
# the   lazy   dog
assert "the  quick brown\nfox  jumps  over\nthe   lazy   dog" == justify_text(
    ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16
)

# the   perrin   pages
# will  help  you find
# your   calling   but
# dont  be  duped  cut
# down    the    woods
# they     be    erdos
#
# fmt: off
assert "the   perrin   pages\nwill  help  you find\nyour   calling   but\ndont  be\
  duped  cut\ndown    the    woods\nthey     be    erdos" == justify_text(
        ["the", "perrin", "pages", "will", "help", "you", "find", "your", "calling",
         "but", "dont", "be", "duped", "cut", "down", "the", "woods", "they", "be",
         "erdos"], 20)
# fmt: on

assert "oneword   " == justify_text(["oneword"], 10)
