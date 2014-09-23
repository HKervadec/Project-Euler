#!/usr/bin/env python3

# https://projecteuler.net
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from tools.utils import measure_func


def prime(n):
    max = int(n**0.5)

    i = 3
    while i <= max:
        if not n % i:
            return False

        i += 2

    return True


def solve():
    sum = 2
    limit = 2000000

    for i in range(3, limit, 2):
        if prime(i):
            sum += i

    return sum


# ******************************************************************************
if __name__ == "__main__":
    measure_func(solve)