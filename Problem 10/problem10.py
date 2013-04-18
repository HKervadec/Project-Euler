# https://projecteuler.net
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from math import *

def prime(n):
	max = int(sqrt(n))
	
	for i in range(2, max + 1):
		if not n % i:
			return False
			
	return True
	

sum = 2
limit = 2000000

for i in range(3, limit, 2):
	if prime(i):
		sum += i
		
print(sum)