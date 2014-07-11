#!/usr/bin/python3

from math import sqrt

def factorNumber(n):
    factor = 2
    max = int(sqrt(n))

    for i in range(2, max + 1):
        if not (n % i):
            factor += 2

    return factor


if __name__ == "__main__":
    number = 1
    numberOfFactor = 1
    limit = 500

    i = 2
    while True:
        numberOfFactor = factorNumber(number)

        if numberOfFactor >= limit:
            break

        number += i
        i += 1

    print(number)
