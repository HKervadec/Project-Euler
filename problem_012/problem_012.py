#!/usr/bin/python3

from math import sqrt
from tools.utils import measure_func


def count_factors(n):
    factor = 2

    for i in range(2, int(sqrt(n)) + 1):
        if not (n % i):
            factor += 2

    return factor


def solve():
    number = 1
    limit = 500

    i = 2
    while True:
        n_factors = count_factors(number)

        if n_factors >= limit:
            break

        number += i
        i += 1

    return number


if __name__ == "__main__":
    measure_func(solve)
