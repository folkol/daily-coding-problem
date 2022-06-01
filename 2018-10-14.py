"""A.k.a. ???

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
import re


def find_lowest_missing(xs):
    xs = list(xs)
    for i, e in enumerate(xs):
        print(', '.join(str(x) for x in xs))
        print('  '.join(re.sub('.', '^', str(e)) if i == j else re.sub('.', ' ', str(e)) for j, e in enumerate(xs)))
        if e in range(1, len(xs) - 1):
            xs[e - 1], xs[i] = e, xs[e - 1]
    for i, e in enumerate(xs, start=1):
        if i != e:
            return i


# assert find_lowest_missing([3, 4, -1, 1]) == 2
# assert find_lowest_missing([1, 2, 0]) == 3
assert find_lowest_missing([25, 29, 4, 8, 2, 1, 21, 28, 7, 3, 24, 26, 20, 9, 5, 0, 27, 6, 23, 22]) == 10

from random import shuffle

seq = list(range(10))
seq.extend((range(20, 30)))
shuffle(seq)

missing = find_lowest_missing(seq)
assert missing == 10, f'Expected 100, got {missing}'
