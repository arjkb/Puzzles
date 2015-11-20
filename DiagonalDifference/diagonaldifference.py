def getMainSum(mat, n):
	s = 0	
	for i in range(n):
		s += mat[i][i]
	return s

def getSecondarySum(mat, n):
	s = 0
	for i in range(n):
		s += mat[n-i-1][i]
	return s

n = int(input())
matrix = []

for i in range(n):
	current = input()
	current = [int(i) for i in current.split()]
	matrix.append(current)

print(abs(getMainSum(matrix, n) - getSecondarySum(matrix, n)))
