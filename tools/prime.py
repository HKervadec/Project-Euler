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


class SuperPrime():
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