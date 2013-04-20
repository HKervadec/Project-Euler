# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
# correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.
def cut(n):
	result = []
	
	while n > 0:
		result.append(n%10)
		n /= 10
		
	return result

	
def simplificationFausse(list):
	a = cut(list[0])
	b = cut(list[1])
	
	for i in a:
		if i in b:
			b.remove(i)
			a.remove(i)
			return [a[0],b[0]]
			
	return list
	
	
def simplification(list):
	a = list[0]
	b = list[1]
	i = 2
	
	while i <= a:
		if (not a%i) and (not b%i):
			return simplification([a/i,b/i])
		i += 1
		
	return [a,b]
	
	
def multiplie(list1, list2):
	a = list1[0] * list2[0]
	b = list1[1] * list2[1]
	
	return [a,b]
	
	
def toInt(list):
	tmp = map(str, list)
	tmp = ''.join(tmp)
	
	return int(tmp)

# ******************************************************************************
prod = [1,1]
for a in range(10,100):
	for b in range(10,100):
		if a%10 and b%10:
			badSimplifie = [0,0]
			tmp = [a,b]
			bad = simplificationFausse(tmp)
			good = simplification(tmp)
			
			if bad != tmp:
				badSimplifie = simplification(bad)
			
			if badSimplifie == good and good[0] < good[1]:
				prod = multiplie(prod, tmp)
			
print(simplification(prod)[1])
