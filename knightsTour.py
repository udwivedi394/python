N = 5
def solveKT():
	sol = [[-1 for x in range(N)] for y in range(N)]
	for i in range(N):
		print sol[i]
	
	xMove = [1,  1, -1, -1, 2,  2, -2, -2]
	yMove = [2, -2,  2, -2, 1, -1,  1, -1]

	
	#set initial position of knight
	x = 2
	y = 2
	sol[y][x] = 0
	"""ctr = 0
	for x in range(N):
		for y in range(N):
			sol = [[-1 for j in range(N)] for k in range(N)]
			sol[y][x] = 0

			print
	
	#if (solveKTUtil(0, 0, 1, sol, xMove, yMove) == False):
			if (solveKTUtil_Heuristic(x, y, 1, sol, xMove, yMove) == False):
				print "No Solution"
				ctr += 1
				continue
				#return

			for i in range(N):
				print '[',
				for j in range(N):
					print '%3d,' % sol[i][j],
				print ']'
	print ctr"""

	if (solveKTUtil_Heuristic(x, y, 1, sol, xMove, yMove) == False):
		print "No Solution"
	for i in range(N):
		print '[',
		for j in range(N):
			print '%3d,' % sol[i][j],
		print ']'

def isSafe(x, y, sol):
	if (x >= 0 and x < N and y >= 0 and y < N and sol[y][x] == -1):
		return True
	return False


#BackTracking algorithm
def solveKTUtil(x, y, movei, sol, xMove, yMove):
	
	if movei >= N*N:
		return True

	#try all moves from the current coordinate x,y

	for i in range(8):
		next_x = x+xMove[i]
		next_y = y+yMove[i]

		if isSafe(next_x, next_y, sol):
			sol[next_x][next_y] = movei
			if solveKTUtil(next_x, next_y, movei+1, sol, xMove, yMove):
				return True
			else:
				return False
				sol[next_x][next_y] = -1 #Backtracking, reversing the current move
	return False

#Warnsdorff's Algorithm, Heuristic: for the current available moves, choose the move with minimum number od consequent moves
def solveKTUtil_Heuristic(x, y, movei, sol, xMove, yMove):
	if movei >= N*N:
		sol[y][x] = movei
		return True

	#Initialising the array to store the no. of next valid for each subsequent current moves
	no_of_next_legal_move = [0]*8

	for i in range(8):
		
		#Make the current move using all available move
		next_x = x+xMove[i]
		next_y = y+yMove[i]
		
		#Check whether current move is safe or not
		if isSafe(next_x, next_y, sol):
			
			#Limiting condition: if last movei reaches in this block safely, then it means matrix is full now, return True
			if movei == N*N-1:
				sol[next_y][next_x] = movei
				return True
			#Otherwise create list of no. of next valid moves for each subsequent move
			no_of_next_legal_move[i] = check_for_legal_case(next_x, next_y, sol, xMove, yMove)
	
	#if no next move available for all current moves, return False
	if sum(no_of_next_legal_move) == 0:
		return False

	#changing the reference to current list objects
	temp_list = no_of_next_legal_move

	#convert all the 0's with max value 64 (arbitray value), max_no_of_moves = 8
	while min(temp_list) == 0:
		temp_list[temp_list.index(min(temp_list))] = 64

	#Loop until valid moves are available or, all values are not 0 i.e, 64
	while sum(temp_list) != 512:

		#Heuristic: find the move with minimum number of valid next moves
		n = temp_list.index(min(temp_list))
		
		#Prepare the next move
		next_x = x+xMove[n]
		next_y = y+yMove[n]
		sol[next_y][next_x] = movei
		
		#For current position in the matrix, find the next move recursivily
		if solveKTUtil_Heuristic(next_x, next_y, movei+1, sol, xMove, yMove):
			return True
		else:
			#Backtracking: if last move failed in achieving result, reverse the last step
			sol[next_y][next_x] = -1
			#Mark the current move as Max, to visit next minimum
			temp_list[n] = 64
	#if the entire list of no_of_next_legal_moves has been exhausted
	return False
	

def check_for_legal_case(x, y, sol, xMove, yMove):
	no_of_legal_moves = 0

	for i in range(8):
		next_x = x+xMove[i]
		next_y = y+yMove[i]
		
		if isSafe(next_x, next_y, sol):
			no_of_legal_moves += 1
	return no_of_legal_moves

solveKT()
