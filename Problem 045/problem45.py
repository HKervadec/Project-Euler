# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Pentagonal 	  	Pn=n(3n-1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal 	  	Hn=n(2n-1) 	  	1, 6, 15, 28, 45, ...

# It can be verified that T285 = P165 = H143 = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.

def Tn(n):
	return n*(n+1)/2

	
def Pn(n):
	return n*(3*n-1)/2

	
def Hn(n):
	return n*(2*n-1)


def nHn(Hn):
	return (1+(1+8*Hn)**0.5)/4
	
def nHnBool(Hn):
	tmp = nHn(Hn)
	return tmp == int(tmp)
	
	
def nPn(Pn):
	return (1 + (1+24*Pn)**0.5)/6
	
def nPnBool(Pn):
	tmp = nPn(Pn)
	return tmp == int(tmp)
	
	
def nTn(Tn):
	return ((1+8*Tn)**0.5 - 1)/2
	
def nTnBool(Tn):
	tmp = nTn(Tn)
	return tmp == int(tmp)
	

def prop(Tn):
	# return Pn(int(nPn(Tn))) == Tn and Hn(int(nHn(Tn))) == Tn
	return nHnBool(Tn) and nPnBool(Tn)
	
# ********************************************************************
n = 286
while not prop(Tn(n)):
	n += 1
	
print(n, Tn(n))

n = 1
while n < 100000000:
	if prop(Tn(n)):
		print(n, Tn(n))
	
	n += 1
