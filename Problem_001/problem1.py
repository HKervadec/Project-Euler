#!/usr/bin/env python3

# https://projecteuler.net/
# If we list all the natural numbers below 10 that are multiples of 3 
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

from tools.utils import measure_func

def solve():
    sum = 0

    for n in range(1000):
        if not(n % 3) or not(n % 5):
            sum += n

    return sum


if __name__ == "__main__":
    measure_func(solve)