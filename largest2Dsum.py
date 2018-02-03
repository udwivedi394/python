import time

#Naive solution, 2D matrix of m*n
def largest2Dsum(arr):
	n = len(arr)
	m = len(arr[0])
	max_sum = -99999999999

	for i in range(n):
		for j in range(m):
			for k in range(i,n):
				for l in range(j,m):
					sumi = 0
					for y in range(i, k+1):
						sumi += sum(arr[y][j:l])
					
					if sumi > max_sum:
						max_sum = sumi
	return max_sum

def kadaneSum(arr):
	n = len(arr)
	lookup = []+arr

	for i in range(1,n):
		lookup[i] = max(lookup[i-1]+lookup[i], lookup[i])

	return max(lookup)

def largest2Dsumbest(arr):
	
	n = len(arr)
	m = len(arr[0])
	
	maxSum = -99999999999
	maxLeft = -1
	maxRight = -1
	maxUp = -1
	maxDown = -1

	for left in range(n):
		lookup = [0]*n
		for right in range(left, n):
			column = [row[right] for row in arr]
			#Elementwise addition of two lists
			lookup = [sum(x) for x in zip(lookup, column)]
			#print "(left, right):", (left, right), lookup
			#currentSum = kadaneSum(lookup)

			temp = []+lookup

			curUp = -1
			curDown = -1
			for i in range(1,n):
				if temp[i-1]+temp[i] > temp[i]:
					if curUp == -1:
						curUp = i-1
					curDown = i
					temp[i] = max(temp[i-1]+temp[i], temp[i])
			currentSum = max(temp)
		if currentSum > maxSum:
			maxLeft = left
			maxRight = right
			maxUp = curUp
			maxDown = curDown
			maxSum = currentSum

	print (maxLeft, maxRight), (maxUp, maxDown)
	for i in range(maxUp, maxDown+1):
		print arr[i][maxLeft:maxRight+1]
	return maxSum

arr =  [[1,2,-1,-4,-20],
	[-8,-3,4,2,1],
	[3,8,10,1,3],
	[-4,-1,1,7,-6]]

t1 = time.time()
print largest2Dsum(arr)
t2 = time.time()
print t2-t1

t1 = time.time()
print largest2Dsumbest(arr)
t2 = time.time()
print t2-t1
