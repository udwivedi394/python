def findWaterInGlass02(N,i,j):
	
	row = 1
	index = 0
	level = 1

	while row+index < N:
		index = 0
		while index < level:
			if index > 0 and index < level-1:
				print (row+index-level, row+index-level+1),
			else:
				print row+index,
			index += 1
		level += 1
		row += index
		print

def findWaterInGlass(N,i,j):	
	arr = [0 for z in range((i+1)*(i+2)/2)]
	row = 1
	index = 0
	level = 1

	arr[1] = N
	while level <= i:
		index = 0
		while index < level:
			if arr[row+index] > 1.0:
				arr[row+index+level] += (arr[row+index]-1)/2
				arr[row+index+level+1] += (arr[row+index]-1)/2
				arr[row+index] = 1.0

			#if level == i and index == j-1:
			#	return arr[row+index]
			index += 1
		level += 1
		row += index

	row = 1
	index = 0
	level = 1

	while level < i:
		index = 0
		while index < level:
			print arr[row+index],
			index += 1
		level += 1
		row += index
		print
i = 10
j = 6
N = 20.0

#print "Water at ith level and jth glass:", findWaterInGlass(N,i,j)
print findWaterInGlass(N,i,j)
