# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit 
# number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

from utils import digitNumber
from time import time


startTime = time()

total = 0

lim = 100
for n in range(1, lim):
	for m in range(1, lim):
		tmp = digitNumber(m**n)

		if tmp == n:
			print(m**n, n)
			total += 1
		elif tmp > n:
			break

print(total)

print(time() - startTime)