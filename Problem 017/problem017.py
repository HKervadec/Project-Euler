# https://projecteuler.net

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?

# NOTE: Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.
	
def toString(n):
	if n == 1000:
		return 'one thousand'
	
	result = ''
	
	temp = n / 100
	if temp > 0:
		result += unite[temp] + ' hundred' 
		
	temp = n % 100
	
	if temp != 0 and n > 100:
		result += ' and'
		
	if temp < 20 and temp > 10:
		return result + ' ' + exception[temp]
		
	temp = (n % 100) / 10
	result += ' ' + dixaine[temp]
	
	temp = (n % 100) % 10
	result += ' ' + unite[temp]
	
	return result

unite = {0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5: 'five', 
		6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine'}
		
dixaine = {0 : '', 1 : 'ten' , 2 : 'twenty', 3 : 'thirty', 4 : 'forty', 5 : 'fifty',
			6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety'}
			
exception = {11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
			15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
			19 : 'nineteen'}
			
# #########################################################
sum = 0

for i in range(1001):
	result = toString(i)

	for l in result.split(" "):
		sum += len(l)
	
	
print sum
