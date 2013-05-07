# https://projecteuler.net/
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def prime(n):
	if not n % 2:
		return False
	
	lim = int(n**0.5)
	for i in range(3, lim + 1, 2):
		if not n % i:
			return False
			
	return True

	
# **********************************8	
number = 600851475143
i = 3
maxPrimeFactor = 1 #ceci dit en passant, 1 n'est pas premier
lim = number**0.5

while i < lim:
	if not (number % i):
		if prime(i):
			maxPrimeFactor = max(maxPrimeFactor, i)
			
		if prime(number/i):
			maxPrimeFactor = max(maxPrimeFactor, number/i)
	
	i += 2
	
print(maxPrimeFactor)
