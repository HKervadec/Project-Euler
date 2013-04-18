# https://projecteuler.net/
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import *

def prime(n):
	lim = int(sqrt(n))
	for i in range(2,lim):
		if not n % i:
			return False
			
	return True

	
# **********************************8	
number = 600851475143
i = 3
maxPrimeFactor = 1
lim = sqrt(number)

while i < lim:
	if not (number % i):
		if prime(i):
			maxPrimeFactor = max(maxPrimeFactor, i)
			
		if prime(number/i):
			maxPrimeFactor = max(maxPrimeFactor, number/i)
	
	i += 2
	
print(maxPrimeFactor)
