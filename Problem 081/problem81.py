# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and
# down, is indicated in bold red and is equal to 2427.
#
#
#   131	673	234	103	18
#   201	96	342	965	150
#   630	803	746	422	111
#   537	699	497	121	956
#   805	732	524	37	331
#
#
# Find the minimal path sum, in matrix.txt , a 31K text file containing a 80 by 80 matrix, from the top left to the
# bottom right by only moving right and down.

from time import time

def minPath(i, j, matrix):
    if i >= len(matrix) or j >= len(matrix):
        return 9999999999999999999999

    global tabSum

    if tabSum[i][j] != -1:
        return tabSum[i][j]
    else:
        if j == i and i == len(matrix)-1:
            return matrix[i][j]

        tmp = min(matrix[i][j] + minPath(i+1, j, matrix),
                   matrix[i][j] + minPath(i, j+1, matrix))

        tabSum[i][j] = tmp

        return tmp


# ***********************************************************
startTime = time()

file = open("matrix.txt", 'r')

matrix = [[int(n) for n in line.split(',')] for line in file.read().split('\n')]
tabSum = [len(matrix)*[-1] for i in range(len(matrix))]

result = minPath(0, 0, matrix)

print(result)
print(time() - startTime)