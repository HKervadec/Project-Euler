# https://projecteuler.net
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = ^25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math
	
def prop(b,c):
	tmp = b*b - (1000*(b+c) - b*c)
	tmp2 = -(1000*1000)/2
	return tmp == tmp2
	
b = 1
c = 1
lim = 1001
while b < lim:
	c = 1
	while c < lim:
		if b + c > 1000:
			break
		
		
		if prop(b,c):
			a = int(math.sqrt(c**2 - b**2))
			# print(a,b,c)
			print(a*b*c)
			b = lim
			c = lim
		
		c += 1
	b += 1