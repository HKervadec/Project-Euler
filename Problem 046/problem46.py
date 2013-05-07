# It was proposed by Christian Goldbach that every odd composite number can be written 
# as the sum of a prime and twice a square.

# 9 = 7 + 2x12
# 15 = 7 + 2x22
# 21 = 3 + 2x32
# 25 = 7 + 2x32
# 27 = 19 + 2x22
# 33 = 31 + 2x12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime 
# and twice a square?

# a = b + c^2 ?   
def conjecture(a):
    global primeList
    global squareList
    
    for c in squareList:
        c *= 2
        if c > a:
            break
            
        if a-c in primeList:
            return True
            
    return False

# ********************************************************************
from sortedList import sortedList
from utils import prime
import time

startTime = time.time()

primeList = sortedList([])
primeList.add(2)

squareList = sortedList([])
squareList.addList([1,4])


start = 1 # en fait, 3
n = start
bool = True
while bool:
    n += 2
    squareList.add(n**2)
    squareList.add((n+1)**2)
    
    if prime(n):
        primeList.add(n)
    else:
        bool = conjecture(n)

    
print("Result :", n)
print(time.time() - startTime)
    
