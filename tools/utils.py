from math import *
from time import time


def measure_func(func):
    """
    Run the function given as parameter and print the output and time needed to run the function.
    @param func: The function to measure
    """
    startTime = time()
    print(func())
    tot = time() - startTime
    print(tot)

    return tot


def fact(n):
    """
    Return !n
    @param n: int n
    @return: !n
    """
    for i in range(n - 1, 0, -1):
        n *= i

    return n


# Supprime les doublons de la liste passee en parametre
def uniq(list):
    list.sort()

    size = len(list)
    i = 0
    while i < size - 1:
        if list[i] == list[i+1]:
            del list[i]
            size -= 1
            continue

        i += 1

    return list


def toList(n):
    """
    Take a number and transform it to a list.

    @param n: int The number to transform
    @return: The number as a list
    @rtype: list of int
    """
    result = []

    while n > 0:
        result.append(n%10)
        n //= 10

    result.reverse()

    return result


def palindrome(string):
    """
    Test if the given string is a palindrome.
    @param string: str The string to test
    @return: True if palindrome, False otherwise.
    @rtype bool
    """
    a = 0
    b = len(string) -1

    while a < b:
        if string[a] != string[b]:
            return False

        a += 1
        b -= 1

    return True


def reverseString(string):
    return string[::-1]


def digitsSum(n):
    sum = 0

    while n > 0:
        sum += n % 10
        n //= 10

    return sum


def digitNumber(n):
    total = 0

    while n > 0:
        total += 1
        n //= 10

    return total

class fraction:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
        self.simplifie()


    def __add__(self, frac):
        self.a *= frac.b
        self.a += frac.a * self.b
        self.b *= frac.b

        # self.simplifie()

        return self


    def __sub__(self, frac):
        self.a *= frac.b
        self.a -= frac.a * self.b
        self.b *= frac.b

        # self.simplifie()

        return self


    def __mul__(self, frac):
        self.a *= frac.a
        self.b *= frac.b

        # self.simplifie()

        return self


    def __truediv__(self, frac):
        self.a *= frac.b
        self.b *= frac.a

        # self.simplifie()

        return self


    def __str__(self):
        return str(self.a) + '/' + str(self.b)


    def simplifie(self):
        while not self.a % 2 and not self.b % 2:
            self.a //= 2
            self.b //=2

        i = 3
        lim = sqrt(self.a)
        while i <= lim:
            if not self.a % i and not self.b % i:
                self.a //= i
                self.b //= i
                lim = sqrt(self.a)
                i = 3

            i += 2


    def inverse(self):
        (self.a, self.b) = (self.b, self.a)