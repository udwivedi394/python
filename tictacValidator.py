def tictactoeValidator(arr, moves):
	count_x = 0
	count_o = 0
	for i in range(len(arr)):
		if arr[i] == 'X':
			count_x += 1
		else:
			count_o += 1
	#In tictactoe Game X is always the first move
	if count_x-count_o not in [0,1]:
		return False
	
	
	x_win = False
	o_win = False
	#Naive Solution, consider each valid move and check if somebody is winning
	for cur_move in moves:
		if arr[cur_move[0]] != '' and arr[cur_move[0]] == arr[cur_move[1]] and arr[cur_move[1]] == arr[cur_move[2]]:
			if arr[cur_move[0]] == 'X':
				x_win = True
				print "X Wins", cur_move
			else:
				print "O Wins", cur_move
				o_win = True

	if x_win == o_win and o_win == True:
		return False
	return True

arr =  ['X', 'X', 'O',
	'O', 'O', 'X',
	'X', 'O', 'X']

arr2 = ['O', 'X', 'X', 
	'O', 'X', 'X',
	'O', 'O', 'X']
moves = [[0,1,2],
	 [0,3,6],
	 [0,4,8],
	 [1,4,7],
	 [2,5,8],
	 [2,4,6],
	 [3,4,5],
	 [6,7,8]]

print tictactoeValidator(arr2, moves)
