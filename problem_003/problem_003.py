#!/usr/bin/env python3

#  https://projecteuler.net/
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from time import time
from tools.utils import measure_func
from tools.prime import prime


def solve_2():
    number = 600851475143
    i = 3
    maxPrimeFactor = 1 # Btw, 1 is not prime.
    lim = number**0.5

    while i < lim:
        if not (number % i):
            if prime(i):
                maxPrimeFactor = max(maxPrimeFactor, i)

            if prime(number/i):
                maxPrimeFactor = max(maxPrimeFactor, number/i)

        i += 2

    return maxPrimeFactor


def solve():
    number = 600851475143
    i = 2

    while i < number:
        if not number % i:
            number //= i
            i = 2
        else:
            i += 1

    return number


# **************************************
if __name__ == "__main__":
    measure_func(solve)
    measure_func(solve_2)
