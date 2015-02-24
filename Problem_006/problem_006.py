#!/usr/bin/env python3

# https://projecteuler.net
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

from tools.utils import measure_func


def solve():
    sum_square = 0
    square_sum = 0

    for i in range(1, 101):
        sum_square += i*i
        square_sum += i

    square_sum *= square_sum

    return abs(sum_square - square_sum)

# ******************************************************************************
if __name__ == "__main__":
    measure_func(solve)