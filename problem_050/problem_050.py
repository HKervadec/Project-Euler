#!/usr/bin/env python3

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?


import sys
sys.path.insert(0, "..")
sys.path.insert(0, ".")

from tools.prime import prime
from tools.sorted_list import sortedList
from tools.utils import measure_func

def sumOfPrimes(n, primeSum):
    if n in primeSum:
        return primeSum.index(n)
        
    i = 0
    while primeSum[i] < n:
        d = n + primeSum[i]
        if d in primeSum:
            return primeSum.index(d) - i
            
        i += 1
            
    return -1


def solve(limit=1000000):
    primeSum = sortedList([2])

    iterator = 3
    max = 0
    maxConsecutive = 0

    while iterator < limit:
        if prime(iterator):
            primeSum.add(primeSum[-1] + iterator)
            
            consecutive = sumOfPrimes(iterator, primeSum)
            if consecutive > maxConsecutive:
                (max, maxConsecutive) = (iterator, consecutive)
                
        iterator += 2
        
    return max


def solve_2(limit=1000000):
    primeSum = [2]
    i = 3
    while primeSum[-1] < limit:
        if prime(i):
            primeSum.append(primeSum[-1] + i)
            
        i += 2  
          
    max = 0
    maxConsecutive = 0      
    for i in range(len(primeSum)):
        for j in range(i, len(primeSum)):
            tmp = primeSum[j] - primeSum[i]
            d = j - i

            if d > maxConsecutive and prime(tmp):
                    (max, maxConsecutive) = (tmp, d)
                    
    return max
        
        
        
if __name__ == "__main__":
    # measure_func(solve)
    # measure_func(solve_2)
    print(solve())