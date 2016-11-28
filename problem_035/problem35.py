#!/bin/env python3
# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 
# 73, 79, and 97.

# How many circular primes are there below one million?

from tools.utils import measure_func
from tools.prime import SuperPrime, sieve, PrimeSet


forbiddenDigits = {str(i) for i in range(0, 9, 2)}
forbiddenDigits.add('5')


def next(str):
    return str[1:] + str[0]


def test_circular(n, prime):
    n = str(n)

    for c in forbiddenDigits:
        if c in n:
            return False

    for _ in range(len(n)):
        if not prime(int(n)):
            return False

        n = next(n)

    return True


def solve(lim=1000000):
    primes = SuperPrime(lim + 1)
    prime = primes.prime

    tot = len([i for i in forbiddenDigits if prime(int(i))])
    for i in range(3, lim, 2):
        if test_circular(i, prime):
            tot += 1

    return tot


def test(n, primes):
    if n not in primes:
        return False

    s = str(n)
    return all(int(s[i:]+s[:i]) in primes for i in range(len(s)))


def solve_2(lim=1000000):
    primes = sieve(lim)

    return sum((test(n, primes) for n in range(lim)))


def solve_3(lim=1000000):
    primes = PrimeSet()
    prime = primes.prime

    tot = len([i for i in forbiddenDigits if prime(int(i))])
    for i in range(3, lim, 2):
        if test_circular(i, prime):
            tot += 1

    return tot


if __name__ == "__main__":
    measure_func(solve)
    measure_func(solve_2)
    measure_func(solve_3)
    measure_func(solve, 10000000)
    measure_func(solve_2, 10000000)
    measure_func(solve_3, 10000000)
    measure_func(solve, 100000000)
    measure_func(solve_3, 100000000)
    measure_func(solve_2, 100000000)
