# https://projecteuler.ne
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def puissance(n, p):
	if p == 1:
		return n
	else:
		return n * puissance(n, p - 1)
		
i = 2**1000

sum = 0

while i > 0:
	sum += i % 10
	i /= 10

print(sum)