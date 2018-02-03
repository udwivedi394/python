"""def isSafe(x, y, maze):
	if x >= 0 and x < N && y >= 0 and y < N and maze[y][x] == 0:
		return True
	return False

def solveMazeUtil(x, y, maze, xMove, yMove):
	#if completed return True
	#loop for 2 (2 moves avail)
	#1. create a forward move
	#2. check if its safe
	#3. if yes then call solveMazeUtil with current maze, by changing the value of maze[y][x] = 1
	#4. if above function returns True, return True
	#5. else backtrack reverse the maze[y][x] = 0
	
	if x == N-1 and y == N-1:
		return True

	for i in range(2):
		next_x = x+xMove[i]
		next_y = y+yMove[i]

		if isSafe(next_x, next_y, maze):
			maze[next_y][next_x] = 1
			if solveMazeUtil(next_x, next_y, maze, xMove, yMove):
				return True
			else:
				maze[next_y][next_x] = 0
	return False

maze = [[1, 0, 0, 0, 0, 1],
	[1, 1, 0, 0, 0, 1],
	[0, 1, 1, 1, 1, 1],
	[0, 1, 0, 1, 0, 0],
	[1, 1, 0, 0, 1, 0],
	[1, 1, 1, 1, 1, 1]]

solveMaze(maze)

for i in range(N):
	   print(maze[i])

--------------------------------------------"""
N = 6

def solveMaze(maze):
	xMove = [0, 1]
	yMove = [1, 0]

	if solveMazeUtil(0, 0, maze, xMove, yMove):
		maze[0][0] = 2
		remake(maze)
		return maze
	else:
		print("No Solution")
		return


def remake(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] != 2:
                maze[i][j] = 0
    return maze

def isSafe(x, y, maze):
	if x >= 0 and x < N and y >= 0 and y < N and maze[y][x] == 1:
		return True
	return False

def solveMazeUtil(x, y, maze, xMove, yMove):
	#if completed return True
	#loop for 2 (2 moves avail)
	#1. create a forward move
	#2. check if its safe
	#3. if yes then call solveMazeUtil with current maze, by changing the value of maze[y][x] = 1
	#4. if above function returns True, return True
	#5. else backtrack reverse the maze[y][x] = 0

	if x == N-1 and y == N-1:
		return True

	for i in range(2):
		next_x = x+xMove[i]
		next_y = y+yMove[i]

		if isSafe(next_x, next_y, maze):
			maze[next_y][next_x] = 2
			if solveMazeUtil(next_x, next_y, maze, xMove, yMove):
				return True
			else:
				maze[next_y][next_x] = 1
	return False

maze = [[1, 0, 0, 0, 0, 1],
	    [1, 1, 0, 0, 0, 1],
	    [0, 1, 1, 1, 1, 1],
	    [0, 1, 0, 1, 0, 0],
	    [1, 1, 0, 0, 1, 0],
	    [1, 1, 1, 1, 1, 1]]

solveMaze(maze)

for i in range(N):
    print(maze[i])
