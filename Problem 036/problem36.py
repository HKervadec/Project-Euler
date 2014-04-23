# The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in 
# base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def palindrome(list):
	a = 0
	b = len(list) -1
	
	while a < b:
		if list[a] != list[b]:
			return False
			
		a += 1
		b -= 1
			
	return True
	

def toListUnreversed(n):
	result = []
	
	while n > 0:
		result.append(n%10)
		n /= 10
		
	return result
	
	
def toBinListUnreversed(n):
	list = []
	
	while n > 0:
		list.append(n%2)
		n /= 2
		
	return list
	
	
def doublePalindrome(n):
	return palindrome(toListUnreversed(n)) and palindrome(toBinListUnreversed(n))
	
	
# ******************************************************************************
sum = 0
i = 1

while i < 1000000:
	if doublePalindrome(i):
		sum += i
		
	i += 2
		
print(sum)



