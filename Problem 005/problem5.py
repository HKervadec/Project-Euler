# https://projecteuler.net
# 2520 is the smallest number that can be divided by each of the numbers from 1 
# to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

def divisible(n):
	for i in range(3, 20):
		if n % i:
			return False
			
	return True
	
	
# ******************************************************************************
i = 20

while not divisible(i):
	i += 20
	
print(i)