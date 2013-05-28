# It can be seen that the number, 125874, and its double, 251748, contain exactly
# the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain 
# the same digits.

from utils import toList
from time import time

def prop(n):
    save = toList(n)
    save.sort()
    
    factors = [2, 3, 4, 5, 6]
    
    for i in factors:
        tmp = toList(i*n)
        tmp.sort()
        
        if tmp != save:
            return False
            
    return True


# ******************************************************************************
startTime = time()

i = 1
while not prop(i):
    i += 1
    
print(i)
print(time() - startTime)