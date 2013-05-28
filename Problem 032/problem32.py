# We shall say that an n-digit number is pandigital if it makes use of all the digits 
# 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand,
 # multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can 
# be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

from utils import sortedList
				
# ******************************************************************************
# retourne une liste contenant tout les chiffres d'un nombre
def cut(n):
	result = []
	while n >0:
		result.append(n%10)
		n //= 10
	
	return result
	
# teste si la liste est "pandigitale"
def pandigital(list):
	if len(list) != 9:
		return False
		
	for i in range(len(list)):
		if list[i] != i+1:
			return False
	
	return True
	
# retourne une liste contenant tout les chiffres de a, b et a*b
def mk(a,b):
	result = cut(a)
	result.extend(cut(b))
	result.extend(cut(a*b))
	result.sort()
	
	return result
	
# ******************************************************************************
result = sortedList([])

for i in range(1,1000):
	for j in range(1,10000):
		if i*j >= 10000:
			break;
			
		if pandigital(mk(i,j)):
			result.add(i*j)
			
print(result.sum())
