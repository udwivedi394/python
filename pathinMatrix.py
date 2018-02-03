def findPath(arr):
	N = len(arr)

	src_i = -1
	src_j = -1

	for i in range(N):
		if src_i != -1:
			break
		for j in range(N):
		 	if arr[i][j] == 1:
				src_i = i
				src_j = j
				break

	###print (src_i, src_j)
	return findPathUtility(arr, src_j, src_i)

def findPathUtility02(arr, x, y, lookup=None):
	if arr[y][x] == 2:
		return True

	if lookup == None:
		lookup = {}

	i = len(arr)
	mult = 1
	while i:
		mult *= 10
		i /= 10

	#Move UP, check safe
	if isSafe(arr, x, y-1, lookup):
		lookup[x*mult+(y-1)] = 1
		if findPathUtility(arr, x, y-1, lookup):
			return True
	
	#Move Down, check safe
	if isSafe(arr, x, y+1, lookup):
		lookup[x*mult+(y+1)] = 1
		if findPathUtility(arr, x, y+1, lookup):
			return True
	
	#Move Left, check safe
	if isSafe(arr, x-1, y, lookup):
		lookup[(x-1)*mult+y] = 1
		if findPathUtility(arr, x-1, y, lookup):
			return True
	
	#Move Down, check safe
	if isSafe(arr, x+1, y, lookup):
		lookup[(x+1)*mult+y] = 1
		if findPathUtility(arr, x+1, y, lookup):
			return True

	print lookup
	return False

#Short version of above code, recursive call, BackTracking
def findPathUtility(arr, x, y, lookup=None):
	if lookup == None:
		lookup = {}
	
	if isSafe(arr,x,y,lookup)==False:
		return False

	if arr[y][x] == 2:
		return True

	#Move UP, check safe
	if findPathUtility(arr, x, y-1, lookup) or findPathUtility(arr, x, y+1, lookup) or findPathUtility(arr, x-1, y, lookup) \
		or findPathUtility(arr, x+1, y, lookup):
		return True
	return False

def isSafe(arr, x, y, lookup):
	N = len(arr)

	if x >= N or y >= N or x < 0 or y < 0:
		return False
	
	i = len(arr)
	mult = 1
	while i:
		mult *= 10
		i /= 10
	
	if lookup.get(x*mult+y):
		return False

	lookup[x*mult+y] = 1

	if arr[y][x] in (1,2,3):
		return True
	return False

M1 = [[0,3,2],
      [3,3,0],
      [1,3,0]]

M2 = [[0,3,1,0],
      [3,0,3,3],
      [2,3,0,3],
      [0,3,3,3]]

M3 = [[0,3,1,3],
      [3,0,0,3],
      [2,0,0,3],
      [0,3,3,3]]

print findPath(M1)
print findPath(M2)
print findPath(M3)
