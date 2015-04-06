# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions 
# with denominators 2 to 10 are given:

    # 1/2	= 	0.5
    # 1/3	= 	0.(3)
    # 1/4	= 	0.25
    # 1/5	= 	0.2
    # 1/6	= 	0.1(6)
    # 1/7	= 	0.(142857)
    # 1/10	= 	0.125
    # 1/9	= 	0.(1)
    # 1/10	= 	0.1

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 
# has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its 
# decimal fraction part.

from math import log

	
def cycle(n):
	maxJ = 3
	maxI = 1000
	
	for j in range(maxJ):
		for i in range(1, maxI):
			puissance = 10**i
			
			if puissance%n == 0:
				return -1
			
			tmp = int(puissance/n)
				
			compar = 10**(i-2)
			if tmp < compar:
				tmp = retireNDigit(tmp, j-2)
			elif tmp < 10*compar:
				tmp = retireNDigit(tmp, j-1)
			else:
				tmp = retireNDigit(tmp, j)
			
			
			puissance2 = 10**j
			tmp2 = int(puissance**2/puissance2/n) - tmp*puissance/puissance2
			tmp2 = retireNDigit(tmp2, j)
			# print(tmp, tmp2)
			if tmp == tmp2 and tmp != 0:
				return i-j
			
	return -1
	
def retireNDigit(n, i):
	if i == 0 or n <= 0:
		return n
		
	numberOfDigit = int(log(n, 10))
	puissance = numberOfDigit - i + 1
	
	return n - (n//10**puissance)*10**puissance

	
# ********************************************************************
import time


tests = [(3,1), (6,1), (7, 6), (9,1), (999,3), (73,8), (12,1), (2,-1), (4,-1), (5,-1)]
        
for tuple in tests:
    tmp = cycle(tuple[0])
    if tmp != tuple[1]:
        print(tuple[0], tuple[1], tmp)
		
        
print("************")
startTime = time.time()
nMax = 0
max = 0
lim = 1000

for n in range(1, lim + 1):
	if not n % 100:
		print("."),
		
	cycleN = cycle(n)
	if cycleN > max:
		(nMax, max) = (n, cycleN)
	# print(n, cycleN)

	
print(nMax, max)
print(time.time() - startTime)