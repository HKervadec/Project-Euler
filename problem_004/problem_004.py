#!/usr/bin/env python3

# https://projecteuler.net/
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from tools.utils import palindrome, measure_func

start = 100
end = 1000


def solve_2():
    palin = 0

    for i in range(start, end):
        for j in range(start, end):
            a = i * j
            if a >= palin and palindrome(str(a)):
                palin = a

    return palin


def solve():
    palin = 0

    for i in range(start, end):
        for j in range(i, end):
            a = i * j
            if a >= palin and palindrome(str(a)):
                palin = a

    return palin


def solve_3():
    palin = 0

    for i in range(end, start - 1, -1):
        for j in range(end, i - 1, -1):
            a = i * j

            if a < palin:
                break

            if palindrome(str(a)):
                palin = a

    return palin


def solve_4():
    return max(filter(lambda x: palindrome(str(x)), (a * b for a in range(start, end + 1) for b in range(a, end+1))))

# ***********************************************************************
if __name__ == "__main__":
    measure_func(solve)
    measure_func(solve_2)
    measure_func(solve_3)
    measure_func(solve_4)