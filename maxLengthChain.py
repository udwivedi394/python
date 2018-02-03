#Naive Solution using backTrace
def maxLengthChainBackTrace(arr, index=0, new_arr=None):
	if index == len(arr):
		return len(new_arr)

	if new_arr == None:
		new_arr = []

	len1 = 0
	len2 = 0

	if len(new_arr) == 0 or arr[index][0] > new_arr[-1][1]:
		new_arr.append(arr[index])
		length1 = maxLengthChainBackTrace(arr, index+1, new_arr)

		new_arr.pop()
		length2 = maxLengthChainBackTrace(arr, index+1, new_arr)
		len1 = max(length1, length2)
	else:
		len2 = maxLengthChainBackTrace(arr, index+1, new_arr)

	return max(len1, len2)

#Solution using dynammic programming
def maxLengthChainDynamic(arr):
	lookup = [1]*len(arr)

	for i in range(1, len(arr)):
		for j in range(i):
			if arr[j][1] < arr[i][0]:
				lookup[i] = max(lookup[j]+1, lookup[i])

	return max(lookup)

arr =[[5, 24], [39, 60], [15, 28], [27, 40], [50, 90], [100,120]]
print "Using Backtrace Algo: ", maxLengthChainBackTrace(arr)
print "Using Dynamic Programming: ", maxLengthChainDynamic(arr)
