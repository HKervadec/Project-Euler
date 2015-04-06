#!/usr/bin/env python3

# https://projecteuler.net
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 10 = 26.

# What is the sum of the digits of the number 2^1000?

from tools.utils import measure_func, gen_numbers

from functools import reduce
import operator


def solve(n=1000):
    i = 2**n

    sum = 0

    while i > 0:
        sum += i % 10
        i //= 10

    return sum


def solve_2(n=1000):
    return reduce(operator.add, gen_numbers(2**n))


if __name__ == "__main__":
    measure_func(solve)
    measure_func(solve_2)