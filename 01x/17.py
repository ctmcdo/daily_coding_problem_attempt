# Suppose we represent our file system by a string in the following manner:
#
# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
#
# dir
#     subdir1
#     subdir2
#         file.ext
#
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
#
# The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
#
# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
#
# The directory dir contains two sub-directories subdir1 and subdir2.
# subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
# subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.
#
# We are interested in finding the longest (number of characters) absolute path to a file within our file system.
# For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
# and its length is 32 (not including the double quotes).
#
# Given a string representing the file system in the above format, return the length of the longest absolute path
# to a file in the abstracted file system. If there is no file in the system, return 0.

import regex


# files starts with 'f'
def longest_path(fs):
    if len(fs) == 0:
        return 0

    max_filepath_length = 0
    dir_length = 0
    dir_stack = []
    previous_dir_level = -1

    matches = regex.findall(".+?(?=\\n(?:\\t)?|$)", fs)
    for m in matches:
        dir_level = m.count("\t")
        object_len = len(m) - dir_level
        if m[dir_level] == "f":
            if (dir_length + object_len) > max_filepath_length:
                max_filepath_length = dir_length + object_len
        else:
            if dir_level <= previous_dir_level:
                dir_length -= sum(
                    dir_stack.pop()
                    for _ in range(0, previous_dir_level - dir_level + 1)
                )

            dir_stack.append(object_len + 1)
            dir_length += object_len + 1

            previous_dir_level = dir_level

    return max_filepath_length


fs_ = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
assert 20 == longest_path(fs_)

fs_ = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
assert 32 == longest_path(fs_)

fs_ = "dir\ndir2\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
assert 33 == longest_path(fs_)

fs_ = "file.ext"
assert 8 == longest_path(fs_)
