import time

delta = lambda x, y: x if sum(x) > sum(y) else y
delta_min = lambda x, y: x if sum(x) < sum(y) else y

def findbestSol(arr, user):
	if len(arr)==0:
		return []

	if user == 1:	
		opponent1 = findbestSol(arr[1:], 0)
		opponent1.append(arr[0])
		opponent2 = findbestSol(arr[:-1], 0)
		opponent2.append(arr[-1])
		print "User: ", (opponent1, opponent2)
	  	return delta(opponent1, opponent2)
	if user == 0:
		user1 = findbestSol(arr[1:], 1)
		user1.append(arr[0])
		user2 = findbestSol(arr[:-1], 1)
		user2.append(arr[-1])
		print "Opponent: ", (user1, user2)
	  	return delta(user1, user2)
		
def findbestSol_02(arr, user, user_val, opponent_val):
	if len(arr)==0:
		return [user_val, opponent_val]

	if user == 1:	
		user_val.append(arr[0])
		result1 = findbestSol_02(arr[1:], 0, user_val, opponent_val)
		user_val.pop() 	#BackTrace
		
		user_val.append(arr[-1])
		result2 = findbestSol_02(arr[:-1], 0, user_val, opponent_val)
		user_val.pop()
		
		if sum(result1[0]+[arr[0]]) > sum(result2[0]+[arr[-1]]):
			return [result1[0]+[arr[0]], result1[1]]

		else:
			return [result2[0]+[arr[-1]], result2[1]]
			

	if user == 0:
		opponent_val.append(arr[0])
		result1 = findbestSol_02(arr[1:], 1, user_val, opponent_val)
		opponent_val.pop()	#BackTrace

		opponent_val.append(arr[-1])
		result2 = findbestSol_02(arr[:-1], 1, user_val, opponent_val)
	  	opponent_val.pop()
		
		if sum(result1[0] + [arr[0]]) > sum(result2[0]+ [arr[-1]]):
			return [result1[0]+[arr[0]], result1[1]]

		else:
			return [result2[0]+[arr[-1]], result2[1]]

def findbestSol_03(arr, i, j):	
	if j == i:
		return arr[i]
	
	if j == i+1:
		return max(arr[i], arr[j])

	return max(arr[i] + min(findbestSol_03(arr, i+2, j), findbestSol_03(arr, i+1, j-1)),
		   (arr[j] + min(findbestSol_03(arr, i+1, j-1), findbestSol_03(arr, i, j-2))))

def findbestSol_04(arr):
	if len(arr) == 1:
		#print arr[0]
		return arr[0]

	if len(arr) == 2:
		#print max(arr[0], arr[1])
		return max(arr[0], arr[1])
	return max(arr[0] + min(findbestSol_04(arr[2:]), findbestSol_04(arr[1:-1])),
		   (arr[-1] + min(findbestSol_04(arr[1:-1]), findbestSol_04(arr[:-2]))))

#Done using Dynamic Programming, Memoization technique
def findbestSol_05(arr, i, j, dicti=None):
	if j == i:
		return [arr[i]]
		
	if j == i+1:
		return [arr[i]] if arr[i] > arr[j] else [arr[j]]

	if dicti == None:
		dicti = {}

	if dicti.get((i,j)):
		return dicti.get((i,j))
		

	dicti[(i,j)]=delta([arr[i]]+ delta_min(findbestSol_05(arr, i+2, j, dicti), findbestSol_05(arr, i+1, j-1, dicti)),
		[arr[j]]+ delta_min(findbestSol_05(arr, i+1, j-1, dicti), findbestSol_05(arr, i, j-2, dicti)))


	#dicti[(i,j)] = max(arr[i] + min(findbestSol_05(arr, i+2, j, dicti), findbestSol_05(arr, i+1, j-1, dicti)),
	#	   	arr[j] + min(findbestSol_05(arr, i+1, j-1, dicti), findbestSol_05(arr, i, j-2, dicti)))
	
	#print dicti
	return dicti.get((i,j))

def findbestSol_06(arr):
	dp = [[0]*len(arr) for x in range(len(arr)+1)]

	for gap in range(len(arr)):
		i = 0
		j = gap
		while j < n:
			pass
	pass

arr = [8,15,3,7,1,2] #,24,23,12,20]
#print findbestSol_02(arr, 1, [], [])
#print findbestSol_03(arr, 0, len(arr)-1)

t1 = time.time()
print findbestSol_04(arr)
t2 = time.time()
print t2-t1

dicti = {}
t1 = time.time()
print findbestSol_05(arr, 0, len(arr)-1, dicti)
t2 = time.time()
print dicti
print t2-t1

dp = [[0]*(len(arr)) for x in range(len(arr))]
print dp
