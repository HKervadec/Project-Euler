#!/usr/bin/env python3

from math import factorial

def getJthPermutation(initList, j):
    j -= 1

    result = ""
    fac = factorial(len(initList) - 1)
    for div in range(len(initList) - 1, 0, -1):
        k = j // fac
        result += initList[k]
        del initList[k]

        j %= fac

        fac //= div
    result += initList[0]

    return result

def fct(i, j, n):
    list = [str(k) for k in range(n+1)]

    permutation = getJthPermutation(list[:], j)
    print(permutation)

    return permutation[i]


if __name__ == "__main__":
    print(fct(3,1000000,9))
    print(fct(3,1,9))
    print(fct(1, factorial(10), 9))
