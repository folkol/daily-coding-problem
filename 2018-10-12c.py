"""A.k.a. ???

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i. For example, if our input was [1, 2, 3, 4, 5], the expected
output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_of_others(xs):
    # Generate prefix products
    prefix_products = []
    for x in xs:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * x)
        else:
            prefix_products.append(x)

    # Generate suffix products
    suffix_products = []
    for x in reversed(xs):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * x)
        else:
            suffix_products.append(x)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(xs)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(xs) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result


assert product_of_others([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_of_others([3, 2, 1]) == [2, 3, 6]
