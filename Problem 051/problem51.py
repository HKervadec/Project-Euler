# By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
# number is the first example having seven primes among the ten generated numbers, 
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
# Consequently 56003, being the first member of this family, is the smallest prime 
# with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily 
# adjacent digits) with the same digit, is part of an eight prime value 
# family.

from time import time
from utils import toList, SuperPrime
import cProfile


class Truc(object):
    def __init__(self):
        self.patterns = []
        self.pattern_size = 1
        self.upgrade_patterns(self.pattern_size)
        self.pc = SuperPrime(1000000)

    @staticmethod
    def replace(list_n, pattern, a):
        result = 0

        for i in range(len(list_n)):
            result *= 10
            if not pattern[i]:
                result += list_n[i]
            else:
                result += a

        return result

    def upgrade_patterns(self, size):
        self.pattern_size = size
        self.patterns = []

        self.gen_pattern(self.pattern_size, [])
        # print(self.patterns)

    def gen_pattern(self, n, current):
        if n <= 0:
            if self.check_pattern(current):
                self.patterns.append(current)
        else:
            l1 = current[:]
            l1.append(True)

            l2 = current[:]
            l2.append(False)

            self.gen_pattern(n-1, l1)
            self.gen_pattern(n-1, l2)

    @staticmethod
    def check_pattern(pattern):
        """
        We have to replace at least one digit
        @param pattern:
        @return: True is we replace one or more digit, false otherwise
        """
        for boolean in pattern:
            if boolean:
                return True
        return False

    def score(self, n):
        list_n = toList(n)

        if len(list_n) > len(self.patterns[0]):
            self.upgrade_patterns(len(list_n))

        max_score = 0
        min_prime = n**2

        for pattern in self.patterns:
            # print(pattern)
            local_score = 0
            local_min = min_prime
            for i in range(10):
                replaced = self.replace(list_n, pattern, i)

                if replaced >= n and self.pc.prime(replaced):
                    # print(replaced)
                    local_min = min(local_min, replaced)
                    local_score += 1

            # print(local_score)
            if local_score > max_score:
                max_score = local_score
                min_prime = local_min

        return max_score, min_prime


# ##############################################################################
def main():
    start_time = time()

    machin = Truc()

    # print("Score: %d %d %d" %(13, machin.score(13)[0], machin.score(13)[1]))
    # print("Score: %d %d %d" %(56003, machin.score(56003)[0], machin.score(56003)[1]))
    # print("Score: %d %d %d" %(120383, machin.score(120383)[0], machin.score(120383)[1]))
    # print(len(machin.patterns))
    # print(machin.patternSize)
    # print(2**machin.patternSize -1)

    machin.__init__()
    i = 1
    # i = 56003
    goal = 8
    while True:
        tmp, result = machin.score(i)

        # print(i, tmp)
        if tmp >= goal:
            break

        i += 2

    print(result)


    print(time() - start_time)

cProfile.run("main()")
# main()