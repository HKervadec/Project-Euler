# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit 
# numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this 
# property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?


from utils import prime, toList
from time import time


def prop(n):
    if not prime(n):
        return False

    listN = toList(n)
    listN.sort()
    
    i = 1
    while i <= 2:
        m = n + i*3330
        
        if not prime(m):
            return False
            
        listN2 = toList(m)
        listN2.sort()
        
        if listN != listN2:
            return False
            
        i += 1
            
    return True
        

# ********************************************************************
startTime = time()

start = 1001
end = 3340
pas = 2
n = start
discardList = [1487]

while n <= end:
    if prop(n) and n not in discardList:
        tmp = str(n)
        tmp += str(n+3330)
        tmp += str(n+2*3330)
        print(tmp)
        break
        
    n += pas
    
print(time() - startTime)