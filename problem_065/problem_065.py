#!/usr/bin/env python3

# https://projecteuler.net/problem=65

from tools.utils import measure_func, gen_numbers
from functools import reduce


def gen_e_divisors(n):
    while n > 2:
        if not n % 3:
            yield (n // 3) * 2
        else:
            yield 1

        n -= 1

    if n == 2:
        yield 1
        n -= 1
    if n <= 1:
        yield 2


class Div:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def swap(self):
        self.num, self.den = self.den, self.num
        return self

    def plus(self, n):
        self.num += n*self.den
        return self


def apply(d, n):
    return d.swap().plus(n)


def solve(n=100):
    d = Div(1, 0)

    for k in gen_e_divisors(n):
        apply(d, k)

    return sum(gen_numbers(d.num))


def solve_2(n=100):
    return sum(gen_numbers(reduce(apply, gen_e_divisors(n), Div(1, 0)).num))


if __name__ == "__main__":
    measure_func(solve)
    measure_func(solve_2)

    measure_func(solve, args=10000)
    measure_func(solve_2, args=10000)
