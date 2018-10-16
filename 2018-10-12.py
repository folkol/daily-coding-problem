"""A.k.a. ???

    Follow-up: what if you can't use division?
"""
from functools import reduce
from operator import mul


def product_of_others(xs):
    return [reduce(mul, xs[:i] + xs[i + 1:]) for i, x in enumerate(xs)]


assert product_of_others([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert product_of_others([3, 2, 1]) == [2, 3, 6]
