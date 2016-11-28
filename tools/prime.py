from time import clock


def prime(n):
    if n == 2:
        return True

    if n < 2 or not n % 2:
        return False

    lim = n ** 0.5
    i = 3
    while i <= lim:
        if not n % i:
            return False

        i += 2

    return True


def sieve(limit):
    numbers = set(range(2, limit + 1))
    result = set()

    while numbers:
        p = numbers.pop()
        result.add(p)
        numbers.difference_update(range(p, limit, p))

    return result


class SuperPrime:
    """
        Keep track of previously results. Usefull if we have to test
        again and again the same numbers.

        Very simple, and possibly dangerous (if n > size for example)
    """
    def __init__(self, size):
        self.prime_list = size*[-1]

    def prime(self, n):
        if self.prime_list[n] == -1:
            self.prime_list[n] = prime(n)

        return self.prime_list[n]


class PrimeSet:
    """
    Pretty much the same as SuperPrime, but with a set to store the results.
    Slower, but less memory consuming.
    """
    def __init__(self):
        self.tested_list = set()
        self.prime_list = set()

    def prime(self, n):
        if n not in self.tested_list:
            self.tested_list.add(n)
            if prime(n):
                self.prime_list.add(n)
                return True
            return False

        return n in self.prime_list



if __name__ == "__main__":
    clock()
    lim = 1000000
    prime_set = sieve(lim)
    print(clock())

    for n in range(lim):
        assert(prime(n) == (n in prime_set))

    print(clock())














