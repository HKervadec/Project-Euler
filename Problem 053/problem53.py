#!/usr/bin/
# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# In general,
# nCr = 	n!/(r!(n−r)!)
    # ,where r <= n, n! = nx(n−1)x...x3x2x1, and 0! = 1.

# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, 
# are greater than one-million?
from time import time


def printMatrix(matrix):
    for line in matrix:
        print(line)


def printTriangle(matrix):
    for i in range(len(matrix)):
        print(matrix[i][:i+1])

        
# ******************************************************************************
startTime = time()

size = 101
tab = size*[0]
matrice = size*[1]

for i in range(size):
    # matrice[i] = tab.copy()
    matrice[i] = tab[:]
    matrice[i][0] = matrice[i][i] = 1
    

total = 0
goal = 1000000

for i in range(1, size):
    for j in range(1, i):
        matrice[i][j] = matrice[i-1][j] + matrice[i-1][j-1]
        if matrice[i][j] > goal:
            total += 1
        
print(total)
print(time() - startTime)