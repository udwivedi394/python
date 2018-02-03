def findBestSolution(moves):
	#Find the ladders, along with their cost and benifits
	ladders_index = []
	ladders_benifit=[]
	for i in range(len(moves)):
		if moves[i] != -1 and moves[i] > i:
			ladders_index.append(i)
			ladders_benifit.append(moves[i])

	print ladders_index
	print ladders_benifit

	min_sol = 30
	for i in range(len(ladders_index)):
		n = ladders_index[i]
		total_moves = (n+1)//6 + (1 if (n+1)%6 > 0 else 0)
		cur_sol = findBestSolutionUtility(moves, ladders_benifit[i], total_moves, ladders_index, ladders_benifit)
		if cur_sol < min_sol:
			min_sol = cur_sol
	return min_sol

def findBestSolutionUtility(moves, cur_move, total_moves, ladders_index, ladders_benifit):
	if cur_move == len(moves)-1:
		print "Return 01:", total_moves
		return total_moves
	
	found_ladder = 0
	for i in range(len(ladders_index)):
		if cur_move < ladders_index[i]:
			found_ladder = 1
			break

	if not found_ladder:
		total_moves += (len(moves)-1-cur_move)//6 + (1 if (len(moves)-1-cur_move)%6 > 0 else 0)
		print "Return 01:", total_moves
		return total_moves
		
	n = ladders_index[i]
	total_moves += (n-cur_move)//6 + (1 if (n-cur_move)%6 > 0 else 0)
	cur_move = ladders_benifit[i]
	return findBestSolutionUtility(moves, cur_move, total_moves, ladders_index, ladders_benifit)

moves = [-1 for i in range(30)]

#Ladders
moves[2] = 30
moves[4] = 7
moves[10] = 25
moves[19] = 28

#Snakes
moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

print findBestSolution(moves)
