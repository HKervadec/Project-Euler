#!/usr/bin/env python3

# https://projecteuler.net
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.

# What is the 10 001st prime number?
from tools.utils import measure_func
from tools.prime import prime


def solve():
    limit = 10001
    count = 1 # 2 is a prime number
    i = 1

    while count < limit:
        i += 2

        if prime(i):
            count += 1


    return i

# ******************************************************************************
if __name__ == "__main__":
    measure_func(solve)