# https://projecteuler.net/
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

from time import time

def palindrome(n):
	numbers = []
	
	while n > 0:
		numbers.append(n % 10)
		n //= 10
	
	indiceMax = int(len(numbers) // 2)
	a = 0
	b = len(numbers) - 1
	
	for i in range(indiceMax):
		if numbers[a] != numbers[b]:
			return False
		a += 1
		b -= 1
	
	return True

# ***********************************************************************
startTime = time()

palin = 0

for i in range(100, 1000):
	for j in range(100, 1000):
		a = i * j
		if a >= palin and palindrome(a):
			palin = a
			
print(palin)
print(time() - startTime)


startTime = time()

palin = 0

for i in range(100, 1000):
	for j in range(i, 1000):
		a = i * j
		if a >= palin and palindrome(a):
			palin = a

print(palin)
print(time() - startTime)
		
	
