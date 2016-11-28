import itertools
import math
import time

prime_list = set()
# num = 14
count = 0
limit = 1000000
time.clock()


def get_primes(n):
    numbers = set(range(n, 1, -1))
    # primes = []
    while numbers:
        p = numbers.pop()
        prime_list.add(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    # return primes

get_primes(limit)

print("Done", time.clock())

for r in range(2, limit):
    # b = 1
    if r in prime_list:
        # print r,count
        num = str(r)
        if all(int(num[i:]+num[:i]) in prime_list for i in range(len(num))):
            count += 1

print(count, time.clock())
