# If p is the perimeter of a right angle triangle with integral length sides, 
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?


def prop(b, c, p):
	tmp = b*b - (p*(b+c) - b*c)
	tmp2 = -(p**2)/2
	return tmp == tmp2
	
def numberOfSolutions(p):
	result = 0
	lim = p/2
	
	for b in range(1,lim):
		for c in range(1,lim):
			if b + c > p:
				break
				
			if prop(b, c, p):
				result += 1
				
	return result
	
	
# ******************************************************************************
solutions = 0
pMax = -1

for p in range(3,1001):
	if not p % 100:
		print('.'),
		
	tmp = numberOfSolutions(p)
	if tmp > solutions:
		solutions = tmp
		pMax = p
	
print(pMax)