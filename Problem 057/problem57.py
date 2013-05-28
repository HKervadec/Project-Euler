# It is possible to show that the square root of two can be expressed as an 
# infinite continued fraction.

# sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth
# expansion, 1393/985, is the first example where the number of digits in the 
# numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator 
# with more digits than 
from utils import fraction, digitNumber
from math import log10
from time import time

def next(expansion):
    un = fraction(1,1)
    expansion += un
    expansion.inverse()
    
    expansion += un
    
    return expansion
    
    
def prop(expansion):
    na = digitNumber(expansion.a)
    nb = digitNumber(expansion.b)
    
    if na > nb:
        return True
        
    return False
    
    
    
# ******************************************************************************
startTime = time()

expansion = fraction(3,2)
i = 1
total = 0

while i <= 1000:
    if not i % 10:
        print('.', end='', flush=True)
        
    test = prop(expansion)
    # print(i, expansion, test)
    
    if test:
        total += 1
    
    expansion = next(expansion)
    i += 1
    
    
print(total)
print(time() - startTime)