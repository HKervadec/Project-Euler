# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of 
# the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    # d2d3d4=406 is divisible by 2
    # d3d4d5=063 is divisible by 3
    # d4d5d6=635 is divisible by 5
    # d5d6d7=357 is divisible by 7
    # d6d7d8=572 is divisible by 11
    # d7d8d9=728 is divisible by 13
    # d8d9d10=289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property.

def factorial(n):
	if n < 2:
		return 1
		
	return n * factorial(n-1)

	
def getNPermutation(numberList, n):
	global factorielles

	listCopy = []
	for i in numberList:
		listCopy.append(i)

	pos = []
	div = len(listCopy) - 1
	n -= 1
	
	while div > 0:
		tmp = factorielles[div]
		
		pos.append(n//tmp)
		n %= tmp
		div -= 1
		
	result = ""
	
	for k in pos:
		result += str(listCopy[k])
		del listCopy[k]
	result += str(listCopy[0])
	
	return result
	

def prop(perm):
	global primes
	start  = 1
	end = 7
	
	iter = start
	while iter <= end:
		number = int(perm[iter])*100
		number += int(perm[iter+1])*10
		number += int(perm[iter+2])
		
		if number % primes[iter]:
			return False
			
		iter += 1
			
	return True


# ********************************************************************
factorielles = []
primes = [-1, 2, 3, 5, 7, 11, 13, 17] # le -1 ne servira pas

for i in range(10):
	factorielles.append(factorial(i))
	
	

liste = [0,1,2,3,4,5,6,7,8,9]
lim = factorial(len(liste))
i = 1
sum = 0

while i <= lim:
	permutation = getNPermutation(liste, i)
	
	if prop(permutation):
		sum += int(permutation)
		
	i += 1	
		
print(sum)