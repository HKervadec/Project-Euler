# We shall say that an n-digit number is pandigital if it makes use of all the digits 
# 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand,
 # multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can 
# be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.


class sortedList(object):
		
	def __init__(self, list):
		self.list = []
		for i in list:
			self.add(i)
			# self.show()
			
	def addList(self, list):
		for i in list:
			self.add(i)
			
	def add(self, n):
		# print("Adding %d to the list" % n)
		if len(self.list) == 0 or n > self.list[-1]:
			self.list.append(n)
			return 1
			
		a = 0
		b = len(self.list) - 1
		
		while True:
			i = (a + b)//2
					
			di = n - self.list[i]
			
			if di == 0:#n deja dans la liste\
				# print("deja dans la liste", n)
				return 0
			
			if a == i:#a+1 == b
				if self.list[a] > n:
					self.list.insert(a, n)
					return 1
				else:
					self.list.insert(a+1, n)
					return 1
				
			if di > 0:
				a = i
			elif di < 0:
				b = i
				
	def __contains__(self, n):
		# print("Teste l'appartenance de %d" % n)
		# self.show()
		if n < self.list[0] or n > self.list[-1]:
			return False
			
		if n == self.list[-1]:
			return True
			
		a = 0
		b = len(self.list) - 1
		
		while True:
			i = (a + b)//2
			
			di = n - self.list[i]
			
			if di == 0:
				return True
				
			if a == i:
				return n == self.list[a]
				
			if di > 0:
				a = i
			elif di < 0:
				b = i
	
	def __add__(self, stranger):
		newList = sortedList([])
		newList.list = self.list.copy()
		
		for i in stranger.list:
			newList.add(i)
			
		return newList
				
	def show(self):
		print(self.str())
		
	def str(self):
		return str(self.list)
		
	def size(self):
		return len(self.list)
		
	def sum(self):
		result = 0
		
		for i in self.list:
			# print(i)
			result += i
			
		return result		
				
	
	
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
