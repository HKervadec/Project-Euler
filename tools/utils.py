from math import *
from time import time


def is_square(a):
    sqr = sqrt(a)

    return sqr**2 == a

def measure_func(func, args=None):
    """
    Run the function given as parameter and print the output and time needed to run the function.
    @param func: The function to measure
    """
    startTime = time()
    if args:
        print(func(args))
    else:
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


def gen_numbers(n):
    """
    Generate the numbers of the parameters, in reverse order.

    :param n:
    :return:
    :rtype: generator of int
    """
    while n > 0:
        yield n % 10
        n //= 10


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

