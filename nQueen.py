"""N = 4

def solveQT():
	board = [[0 for x in range(N)] for y in range(N)]
	
	if solveQT_utility(-1, -1, board):
		return board
	print ("No solution")
	return

def isSafe(x, y, board):
	for j in range(N):
		for i in range(N):
			if board[j][i] == 1:
				if (x == i or y == j or abs(x-i) == abs(y-j)):
					return False
	return True

def solveQT_utility(x, y, board):
	sumi = 0
	for k in range(N):
	   sumi += sum(board[k])
	
	if sumi == N:
	     return True
	
	for i in range(N):
		if isSafe(x+1, y, board):
			board[y][x+1] = 1
			if solveQT_utility(x+1, y, board):
				return True
			else:
				board[y][x+1] = 0
	
		if isSafe(x, y+1, board):
			board[y+1][x] = 1
			if solveQT_utility(x, y+1, board):
				return True
			else:
				board[y+1][x] = 0

		if isSafe(x+1, y+1, board):
			board[y+1][x+1] = 1
			if solveQT_utility(x, y+1, board):
				return True
			else:
				board[y+1][y+1] = 0
	return False

board = solveQT()

for k in range(N):
    print (board[k])

-------------------------------------
"""
N = 8
def solveQT():
	board = [[0 for x in range(N)] for y in range(N)]
	if solveQT_utility(0, board):
		return board
	print ("No solution")
	return

def isSafe(row, col, board):
	for i in range(col, -1, -1):
		if board[row][i] == 1:
			return False

	for i in range(row, -1, -1):
		if board[i][col] == 1:
			return False

	for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	for i,j in zip(range(row, N, 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	return True

def solveQT_utility(col, board):
	if col >= N:
		return True
	
	#for present column, try to fill in each row
	for row in range(N):
		if isSafe(row, col, board):
			board[row][col] = 1
			if solveQT_utility(col+1, board):
				return True
			board[row][col] = 0
	return False

def printSol(board):
	if board == None:
		return
	for i in range(N):
		print board[i]


printSol(solveQT())

#for k in range(N):

#    print (board[k])
