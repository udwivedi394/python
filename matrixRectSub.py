def maxRectangleSubarea(arr):
	lookup = []+arr
	
	m = len(arr)
	n = len(arr[0])
	
	for i in range(m):
		for j in range(n):
			if arr[i][j] == 1:
				arr[i][j] += arr[i-1][j]
	max_area = 0 
	for i in range(m):
		print lookup[i]
		max_area = max(max_area, findAreaHistogram(lookup[i]))

	return max_area

def findAreaHistogram(arr):
	if len(arr) == 1:
		return arr[0]
	
	if len(arr) == 0:
		return 0

	min_index = arr.index(min(arr))
	left_area = findAreaHistogram(arr[:min_index])
	right_area = findAreaHistogram(arr[min_index+1:])
	cur_area = arr[min_index]*len(arr)

	return max(left_area, right_area, cur_area)

mat =  [[0, 1, 1, 0, 1],
	[1, 1, 0, 1, 0],
	[0, 1, 1, 1, 0],
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0]]

print "Max Area:", maxRectangleSubarea(mat)
