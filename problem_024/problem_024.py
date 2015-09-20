<<<<<<< Updated upstream:problem_024/problem_024.py
# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 10 and 9?


from tools.utils import measure_func
from math import factorial
from problem_024.permutations import gen_permutations
from itertools import permutations
import profile


# Careful, it will destroy the initList argument
def getNPermutation(initList, n):
    """

    @param initList: list containing the elements to permute. It is the 0th permutation.
    @param n: the permutation index
    @return: the nth permutation, according to init list
    """
    pos = []
    n -= 1

    for div in range(len(initList) - 1, 0, -1):
        fac = factorial(div)

        pos.append(n//fac)
        n %= fac

    result = ""
    for k in pos:
        result += initList[k]
        del initList[k]
    result += initList[0]

    return result


def solve():
    return getNPermutation(list("0123456789"), 1000000)


def solve_2():
    i = 0
    for perm in gen_permutations(list("0123456789")):
        i += 1
        
        if i == 1000000:
            return ''.join(perm)


def solve_3():
    i = 0
    for perm in permutations(list("0123456789")):
        i += 1

        if i == 1000000:
            return ''.join(perm)

if __name__ == "__main__":
    # measure_func(solve)
    # measure_func(solve_2)
    # measure_func(solve_3)

    profile.run("solve()")
    profile.run("solve_2()")
    profile.run("solve_3()")