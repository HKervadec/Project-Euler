# https://projecteuler.net
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.

# What is the 10 001st prime number?
from math import *

def prime(n):
	lim = int(sqrt(n))
	for i in range(2, lim):
		if not n % i:
			return False

	return True

limite = 10001
count = 1 # 2 is a prime number
i = 1

while count < limite:
	i += 2
	
	if prime(i):
		count += 1
		
	
print(i)