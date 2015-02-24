#!/usr/bin/env python3

# https://projecteuler.net
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = ^25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt
from tools.utils import measure_func

def prop(b,c):
    tmp = b*b - (1000*(b+c) - b*c)
    tmp2 = -(1000**2)//2
    return tmp == tmp2


def solve():
    b = 1
    lim = 1001
    while b < lim:
        c = 1
        while c < lim:
            if b + c > lim - 1:
                break

            if prop(b,c):
                a = int(sqrt(c**2 - b**2))
                return a*b*c

            c += 1
        b += 1


# ******************************************************************************
if __name__ == "__main__":
    measure_func(solve)