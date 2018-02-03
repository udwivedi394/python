#Rotate matrix by 90 degrees in anticlockwise direction
def rotateMatrixby90(mat):
	n = len(mat)

	for i in range(n//2):
		for j in range(i,n-1-i):
			#rotation of elements in circular anticlockwise direction			
			temp = mat[i][j]
			
			mat[i][j] = mat[j][n-1-i]

			mat[j][n-1-i] = mat[n-1-i][n-1-j]

			mat[n-1-i][n-1-j] = mat[n-1-j][i]

			mat[n-1-j][i] = temp
		#print "After %dth Iteration:"%(i+1)
		#printMatrix(mat)
		#print
	return mat

def printMatrix(mat):
	for i in range(len(mat)):
		for j in range(len(mat)):
			print "%2d"%(mat[i][j]),
		print

mat =  [[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]]

printMatrix(mat)
rotateMatrixby90(mat)
print
printMatrix(mat)
