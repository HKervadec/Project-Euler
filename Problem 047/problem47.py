# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 x 7
# 15 = 3 x 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.

# Find the first four consecutive integers to have four distinct prime factors. 
# What is the first of these numbers?
from utils import prime
from utils import uniq
import time


def primeFactors(n):
    result = []
    
    while n > 1:
        i = 2
        while i <= n:
            if not n % i and prime(i):
                result.append(i)
                n //= i
                break
               
            i += 1
            
    return result
    
    
def numberOfPrimeFactors(n):
    return len(uniq(primeFactors(n)))
    
    
def nConsecutif(n, m):
    result = 0
    while numberOfPrimeFactors(n) == m:
        n += 1
        result += 1
    
    return result

    
# ********************************************************************
startTime = time.time()
      
start = 7*11*13*17
n = start
value = 4
   
while True:
    if not prime(n):
        consecutif = nConsecutif(n, value)
        if consecutif >= value:
            break
            
        n += consecutif + 1
    else:
        n += 1
    
print(n)
print(time.time() - startTime)

