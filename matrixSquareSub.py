def maxSquareSubMatrix(mat):
	m = len(mat)
	n = len(mat[0])

	lookup = [[mat[j][i] for i in range(n)] for j in range(m)]

	max_size = 0
	x_coord = -1
	y_coord = -1

	for i in range(1,m):
		for j in range(1,n):
			if mat[i][j] == 1:
				lookup[i][j] = min(lookup[i][j-1],lookup[i-1][j],lookup[i-1][j-1])+1
				if lookup[i][j] > max_size:
					max_size = lookup[i][j]
					x_coord = i
					y_coord = j
	#for i in range(m):
	#	print lookup[i]
	
	#print (x_coord, y_coord)

	for i in range(x_coord-max_size+1, x_coord+1):
		for j in range(y_coord-max_size+1, y_coord+1):
			print "%2s"%(mat[i][j]),
		print

mat =  [[0, 1, 1, 0, 1],
	[1, 1, 0, 1, 0],
	[0, 1, 1, 1, 0],
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0]]

mat =  [[0, 1, 1, 0, 1],
	[1, 1, 0, 1, 0],
	[0, 1, 0, 1, 0],
	[1, 1, 0, 1, 0],
	[0, 1, 1, 1, 1],
	[0, 0, 0, 0, 0]]
#for i in range(len(mat)):
#	print mat[i]

maxSquareSubMatrix(mat)
