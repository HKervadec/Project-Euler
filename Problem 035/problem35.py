# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 
# 73, 79, and 97.

# How many circular primes are there below one million?

	
def next(str):
	return str[1:] + str[0]
	
	
def prime(n):
	global primes
	
	if primes[n] != -1:
		return primes[n]
	
	if not n % 2:
		primes[n] = False
		return False
		
		
	lim = n ** 0.5
	i = 3
	
	while i <= lim:
		if not n % i:
			primes[n] = False
			return False
			
		i += 2
		
		
	primes[n] = True
	return True
	
	
	
def circularPrime(n):
	n = str(n)
	
	global badGuys	
	for c in badGuys:
		if c in n:
			return False
	
	
	i = 0
	max = len(n)
	
	while i < max:
		if not prime(int(n)):
			return False
		
		n = next(n)
		i += 1
		
	return True
		
	
	
# ******************************************************************************
primes = 1000001 * [-1]
primes[2] = True
badGuys = {'0', '2', '4', '6', '8'}

i = 3
counter = 1
while i < 1000000:
	# if not (i-1) % 10000:
		# print("."),
		
	if circularPrime(i):
		counter += 1
	
	i += 2
		
print(counter)