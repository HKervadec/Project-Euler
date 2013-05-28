# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from utils import prime, sortedList
from time import time

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
        
    


# ********************************************************************
limit = 1000000

# Algo 2 beaucoup, beaucoup plus rapide

# Algo 1
startTime = time()

primeSum = sortedList([0,2])

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
    
print(max, maxConsecutive)
print(time() - startTime)



# Algo 2
startTime = time()
primeSum = [0,2]
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
        
        if prime(tmp):
            d = j - i
            
            if d > maxConsecutive:
                (max, maxConsecutive) = (tmp, d)
                
print(max, maxConsecutive)
print(time() - startTime)
        
        
        
        
        
        