# A permutation is an ordered arrangement of objects. 
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def factorial(n):
	if n < 2:
		return 1
		
	return n * factorial(n-1)
	

def getNPermutation(numberList, n):
	listCopy = []
	for i in numberList:
		listCopy.append(i)

	pos = []
	div = len(listCopy) - 1
	n -= 1
	
	while div > 0:
		tmp = factorial(div)
		
		pos.append(n//tmp)
		n %= tmp
		div -= 1
		
	result = ""
	
	for k in pos:
		result += str(listCopy[k])
		del listCopy[k]
	result += str(listCopy[0])
	
	return result


# ********************************************************************
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutationList = [1000000, factorial(10)]

for n in permutationList:
	print(getNPermutation(liste, n))