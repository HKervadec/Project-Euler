# The nth term of the sequence of triangle numbers is given by, tn = 1/2*n(n+1); so the first ten 
# triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position 
# and adding these values we form a word value. For example, the word value for SKY is 
# 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt, a 16K text file containing nearly two-thousand common English words, 
# how many are triangle words?
	
	
# Renvoie le n ieme nombre triangulaire
def genTriangle(n):
	return (n*(n+1))/2
	
	
# Renvoie la valeur d'un mot
def wordValue(string):
	result = 0
	for char in string:
		result += ord(char) - 64

	return result
	


# *********************************************************************

# Recuperation des mots
file = open("words.txt", "r")

words = file.read().split(',')
file.close

retireGuillemets = lambda word: word[1:-1]
words = map(retireGuillemets, words)


# Trouve longueur max d'un mot
max = 0
for word in words:
	max = len(word) if len(word) > max else max

	
# Calcul des nombres triangulaires
valueMax = max*26 + 1
triangularNumbers = valueMax * [False]

n = 1
triangle = 1
while triangle < valueMax:
	triangularNumbers[triangle] = True
	n += 1
	triangle = genTriangle(n)
	

# Filtrage
test = lambda word : triangularNumbers[wordValue(word)]

words = filter(test, words)
print(len(words))