#!/usr/bin/env python3

# https://projecteuler.net/problem=69

from tools.prime import prime
from tools.utils import measure_func


def solve(lim=1000000):
    old_p = 0

    p = 1
    k = 1
    while True:
        if p > lim:
            break

        if prime(k):
            old_p = p
            p *= k

        k += 1

    return old_p


if __name__ == "__main__":
    measure_func(solve, 10)
    measure_func(solve, 100)
    measure_func(solve, 1000)
    measure_func(solve, 10000)
    measure_func(solve, 100000)
    measure_func(solve, 1000000)
    # profile.run("solve(100000)")