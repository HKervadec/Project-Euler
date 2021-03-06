#!/usr/bin/env python3

# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 10, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms.

from tools.utils import measure_func

def solve():
    sum = 0

    u = 1
    u1 = 2

    while u1 <= 4000000:
        if not u1 % 2:
            sum += u1

        (u, u1) = (u1, u1 + u)

    return sum


if __name__ == "__main__":
    measure_func(solve)