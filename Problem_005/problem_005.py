#!/usr/bin/env python3

# https://projecteuler.net
# 2520 is the smallest number that can be divided by each of the numbers from 1 
# to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?
from tools.utils import measure_func

def divisible(n):
    for i in range(3, 20):
        if n % i:
            return False

    return True


def solve():
    i = 20

    while not divisible(i):
        i += 20

    return i

# ******************************************************************************
if __name__=="__main__":
    measure_func(solve)