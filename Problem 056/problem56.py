# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 
# is almost unimaginably large: one followed by two-hundred zeros. Despite their 
# size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the ]
# maximum digital sum?
from utils import digitsSum
from time import time

startTime = time()

max = 0
for a in range(1, 101):
    for b in range(1, 101):
        sum = digitsSum(a**b)
        max = sum if sum > max else max
        
print(max)
print(time() - startTime)