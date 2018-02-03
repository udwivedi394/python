import time
N = 9

def solveSudoku(grid):
	if grid == None:
		return False
	
	if solveSudoku_utility(0,0,grid):
		return True

	return False

def isSafe(row, col, num, grid):
	#check the number in entire column, return False if found
	if row == N or col == N:
		return True
	#print "01. Num:", num

	if grid[row][col] != 0:
		return False
	#print "02. Num:", num

	
	for i in range(N):
		if grid[i][col] == num:
			return False
	#print "03. Num:", num

	for i in range(N):
		if grid[row][i] == num:
			return False
	#print "04. Num:", num

	lower_limits = [0,3,6]
	upper_limits = [3,6,9]

	for i in range(lower_limits[row//3], upper_limits[row//3]):
		for j in range(lower_limits[col//3], upper_limits[col//3]):
			if grid[i][j] == num:
				return False
	#print "05. Num:", num
	return True

def solveSudoku_utility(row, col, grid):
	if col == N:
		return True
	
	sumi = 0
	for i in range(N):
		sumi = sum(grid[i])
	if sumi == N*N:
		return True
	for i in range(row, N):
		#For each row, trying to fill all the numbers from 1 to 9
		for num in range(1, N+1):
			if isSafe(i, col, num, grid):
				grid[i][col] = num
				if col < N-1:
					if solveSudoku_utility(i, col+1, grid):
						continue
					grid[i][col] = 0
				else:
					return True
	return False
def findEmptyLocation(grid, ll):
	for i in range(ll[1], N):
		for j in range(ll[0], N):
			if grid[i][j] == 0:
				ll[0] = i
				ll[1] = j
				return True
	return False

def solveSudoku_02(grid):
	ll = [0, 0]

	if findEmptyLocation(grid, ll) == False:
		return True
	
	row = ll[0]
	col = ll[1]
	
	for num in range(1, 10):
		if isSafe(row, col, num, grid):
			grid[row][col] = num
			if solveSudoku_02(grid):
				return True
			grid[row][col] = 0
	return False
#Unsolved Grid
grid = [[3,0,6,5,0,8,4,0,0],
	[5,2,0,0,0,0,0,0,0],
	[0,8,7,0,0,0,0,3,1],
	[0,0,3,0,1,0,0,8,0],
	[9,0,0,8,6,3,0,0,5],
	[0,5,0,0,9,0,6,0,0],
	[1,3,0,0,0,0,2,5,0],
	[0,0,0,0,0,0,0,7,4],
	[0,0,5,2,0,6,3,0,0]]

#Solved Grid
grid_orig = [[3,1,6,5,7,8,4,9,2],
	[5,2,9,1,3,4,7,6,8],
	[4,8,7,6,2,9,5,3,1],
	[2,6,3,4,1,5,9,8,7],
	[9,7,4,8,6,3,1,2,5],
	[8,5,1,7,9,2,6,4,3],
	[1,3,8,9,4,7,2,5,6],
	[6,9,2,3,5,1,8,7,4],
	[7,4,5,2,8,6,3,1,9]]

#Solved Grid
grid_03 = [[3,1,6,5,7,8,4,9,2],
	[5,2,0,1,3,4,7,6,8],
	[4,8,7,6,2,0,5,3,1],
	[2,6,3,4,1,5,9,8,7],
	[9,7,4,0,6,3,1,2,5],
	[8,5,1,7,9,2,0,4,3],
	[1,3,8,9,4,7,2,5,6],
	[6,9,2,3,5,1,8,7,4],
	[7,4,5,2,8,6,3,1,9]]

for i in range(N):
	print grid[i]
print(solveSudoku_02(grid))
for i in range(N):
	print grid[i]

