# If p is the perimeter of a right angle triangle with integral length sides, 
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?
	
def prop(a, p):
	tmp = (p*(p-2*a))%(2*(p-a))
	tmp2 = (p*(p-2*a))/(2.0*(p-a))
	return (tmp == 0 and tmp2 > 0, tmp2)

	
def numberOfSolutions(p):
	result = 0

	a = 1
	(bool, b) = prop(a, p)
	while a < b:
		(bool, b) = prop(a, p)
		if bool:
			result += 1
		a += 1
		
	return result
	
# ******************************************************************************
solutions = 0
pMax = -1

for p in range(4, 1001, 2):
	if not p % 100:
		print('.'),

	tmp = numberOfSolutions(p)
	
	if tmp > solutions:
		(solutions, pMax) = (tmp, p)

print(pMax)