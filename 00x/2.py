# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in the original
# array except the one at i. For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?


# Without division, we can minimise the number of multiplications using cumulative product.
def transform_list(a):
    cum_prods_from_left = [a[0]]
    cum_prods_from_right = [a[-1]]
    for i in range(1, len(a)):
        cum_prods_from_left.append(cum_prods_from_left[i - 1] * a[i])
        cum_prods_from_right.append(cum_prods_from_right[i - 1] * a[len(a) - 1 - i])

    exclusive_products = [cum_prods_from_right[-2]]
    for i in range(1, len(a) - 1):
        exclusive_products.append(
            cum_prods_from_left[i - 1] * cum_prods_from_right[(len(a) - 1) - (i + 1)]
        )
    exclusive_products.append(cum_prods_from_left[-2])

    return exclusive_products


assert [120, 60, 40, 30, 24] == transform_list([1, 2, 3, 4, 5])
assert [2, 3, 6] == transform_list([3, 2, 1])
