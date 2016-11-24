#!/bin/env python3
# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 
# 73, 79, and 97.

# How many circular primes are there below one million?

from tools.utils import measure_func
from time import time
from tools.prime import SuperPrime


def next(str):
    return str[1:] + str[0]


def circularPrime(n, prime):
    n = str(n)

    for c in circularPrime.evenDigits:
        if c in n:
            return False

    for _ in range(len(n)):
        if not prime(int(n)):
            return False

        n = next(n)

    return True
circularPrime.evenDigits = {str(i) for i in range(0, 9, 2)}


def solve(lim=1000000):
    primes = SuperPrime(lim + 1)

    tot = 1
    for i in range(3, lim, 2):
        if circularPrime(i, primes.prime):
            tot += 1

    return tot


if __name__ == "__main__":
    measure_func(solve)
    measure_func(solve, 10000000)