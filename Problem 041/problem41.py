# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n 
# exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-digit pandigital prime that exists?

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
	
	return int(result)
	
	
def prime(n):
	if n == 2:
		return True

	if n < 2 or not n % 2:
		return False
		
	lim = int(n ** 0.5) + 1
	for i in range(3, lim, 2):
		if not n % i:
			return False
			
	return True
	

# ********************************************************************
factorielles = []

for i in range(10):
	factorielles.append(factorial(i))
	

# Le dernier numero sera retire de la boucle
# numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 8 et 9 chiffres toujours divisibles par 3
numList = [1, 2, 3, 4, 5, 6, 7, 8]

while True:
	del numList[len(numList)-1]
	
	start = factorielles[len(numList)]
	i = start
	pandigital = getNPermutation(numList, i)
	
	while not prime(pandigital) and i > 1:
		i -= 1
		pandigital = getNPermutation(numList, i)
		
	if prime(pandigital):
		break

print(pandigital)







