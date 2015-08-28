#!/usr/bin/env python3

# https://projecteuler.net/
# If we list all the natural numbers below 10 that are multiples of 3 
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

from tools.utils import measure_func


def solve(l=1000):
    f = lambda n:  (l // n)*(n + (l // n)*n)/2

    return f(3) + f(5) - f(15)


def solve_2(l=1000):
    s = 0

    for n in range(l):
        if not(n % 3 and n % 5):
            s += n

    return s


def solve_3(l=1000):
    return sum(filter(lambda n: not(n%3 and n%5), range(l)))


if __name__ == "__main__":
    measure_func(solve)
    measure_func(solve_2)
    measure_func(solve_3)

    measure_func(solve, args=10000000)
    measure_func(solve_2, args=10000000)
    measure_func(solve_3, args=10000000)