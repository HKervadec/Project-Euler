# Euler's Totient function, phi(n) [sometimes called the phi function], is used 
# to determine the number of numbers less than n which are relatively prime to n. 
# For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively 
# prime to nine, phi(9)=6.

# n 	Relatively Prime 	phi(n) 	n/phi(n)
# 2 	1 	1 	2
# 3 	1,2 	2 	1.5
# 4 	1,3 	2 	2
# 5 	1,2,3,4 	4 	1.25
# 6 	1,5 	2 	3
# 7 	1,2,3,4,5,6 	6 	1.1666...
# 8 	1,3,5,7 	4 	2
# 9 	1,2,4,5,7,8 	6 	1.5
# 10 	1,3,7,9 	4 	2.5

# It can be seen that n=6 produces a maximum n/phi(n) for n ≤ 10.

# Find the value of n ≤ 1,000,000 for which n/phi(n) is a maximum.

from time import time
from tools.sorted_list import sortedList


def phi(n):
	total = 1
	i = 2
	while i < n:
		if relativePrime(i, n):
			total += 1

		i += 1

	return total


def relativePrime(a, b):
	global decomps

	if a in decomps:
		listA = decomps[a]
	else:
		listA = sortedList(primeFactors(a))
		decomps[a] = listA

	if b in decomps:
		listB = decomps[b]
	else:
		listB = sortedList(primeFactors(b))
		decomps[b] = listB

	tmp = listA.union(listB)
	# print(tmp)

	return len(tmp) == 0



# ******************************************************************************
starTime = time()

decomps = {}

tests = []
# tests += [(2,1), (3,2), (4,2), (5,4), (6,2), (7,6), (8,4), (9,6), (10,4)]

for test in tests:
	result = phi(test[0])
	if result != test[1]:
		print("{0}: Expect {1}, Get {2}"\
			.format(test[0], test[1], result))

# for i in range(11):
# 	print("{0}: {1}".format(i, primeFactors(i)))

maxN = 0
maxRatio = 0

lim = 100000
n = 2
while n <= lim:
	ratio = n/phi(n)

	if ratio > maxRatio:
		maxRatio = ratio
		maxN = n

	n += 1

print("{0}: {1}".format(maxN, maxRatio))
print(time() - starTime)