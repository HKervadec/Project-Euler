#!/usr/bin/env python3

# https://projecteuler.net/
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from time import time
from tools.utils import palindrome, measure_func

def solve_2():
    palin = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            a = i * j
            if a >= palin and palindrome(str(a)):
                palin = a

    return palin


def solve():
    palin = 0

    for i in range(100, 1000):
        for j in range(i, 1000):
            a = i * j
            if a >= palin and palindrome(str(a)):
                palin = a

    return palin

# ***********************************************************************
if __name__ == "__main__":
    measure_func(solve)
    measure_func(solve_2)
		
	
