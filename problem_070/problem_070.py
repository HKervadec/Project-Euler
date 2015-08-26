#!/usr/bin/env python3

# https://projecteuler.net/problem=70

from sys import argv

# from tools.utils import measure_func, gen_numbers
from functools import reduce
from operator import __or__

# import profile

def measure_func(func, args=None):
    """
    Run the function given as parameter and print the output and time needed to run the function.
    @param func: The function to measure
    """
    startTime = time()
    if args:
        print(func(args))
    else:
        print(func())
    tot = time() - startTime
    print(tot)

    return tot

def gen_numbers(n):
    """
    Generate the numbers of the parameters, in reverse order.

    :param n:
    :return:
    :rtype: generator of int
    """
    while n > 0:
        yield n % 10
        n //= 10


def gen_primes(lim):
    primes = [True] * lim

    primes[0] = False
    primes[1] = False

    for n in range(2, lim):
        if primes[n]:
            k = 2
            while True:
                tmp = n * k

                if tmp >= lim:
                    break

                primes[tmp] = False

                k += 1

    r = []
    toto = r.append
    for n in range(lim):
        if primes[n]:
            toto(n)

    return r


def gen_phi(lim):
    phi = [n for n in range(lim)]

    for p in gen_primes(lim):
        phi[p] = p-1

        k = 2
        r = 1 - 1/p
        while True:
            tmp = p * k
            if tmp >= lim:
                break

            phi[tmp] *= r

            k += 1

    return list(map(int, phi))


def are_perm(a, b):
    l = [0] * 10
    for n in gen_numbers(a):
        l[n] += 1
    for n in gen_numbers(b):
        l[n] -= 1

    return not reduce(__or__, l)


def are_perm_2(a, b):
    return ''.join(sorted(str(a))) == ''.join(sorted(str(b)))


def solve(lim=10000000):
    lim += 1
    phi = gen_phi(lim)

    min_r = 2
    min_n = 0
    for n in range(2, lim):
        r = n / phi[n]

        if r < min_r and are_perm(n, phi[n]):
            min_r = r
            min_n = n

    return min_n


if __name__ == "__main__":
    # measure_func(solve, 10000000)

    if len(argv) > 1:
        print(solve(int(argv[1])))
    else:
        print(solve())

    # profile.run("solve(10000000)")