# Take the number 192 and multiply it by each of 1, 2, and 3:

    # 192 x 1 = 192
    # 192 x 2 = 384
    # 192 x 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576. 
# We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
# giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as 
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

def toList(n):
	result = []
	
	while n > 0:
		result.append(n%10)
		n //= 10
		
	result.reverse()
	
	return result
	
def toInt(list):
	result = map(str, list)
	result = "".join(result)
	
	return int(result)
	

def pandigital(list):
	list2 = list.copy()
	
	if len(list2) != 9:
		return False

	list2.sort()
	
	for i in range(len(list2)):
		if i+1 != list2[i]:
			return False
			
	return True
	

# ******************************************************************************
limit = 70711

i = 1
max = -1
while i < limit:
	result = toList(i)
	j = 2
	while len(result) < 9:
		result += toList(i*j)
		j += 1
	
	if pandigital(result):
		tmp = toInt(result)
		max =  tmp if tmp > max else max
	
	i += 1
	
print(max)
	