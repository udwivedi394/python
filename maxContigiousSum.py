def maxSumContiguous(arr):
	lookup = []+arr
	for i in range(1,len(arr)):
		lookup[i] = max(lookup[i]+lookup[i-1], lookup[i])

	#Code to get the maxSum subarray
	max_index = lookup.index(max(lookup))

	#loop in reverse from the max sum index
	i = max_index
	while i>=0 and lookup[i] > arr[i]:
		i -= 1

	print "Original Array:",arr
	print "Lookup Array:",lookup
	print "Subarray:",arr[i:max_index+1]
	return max(lookup)

arr = [-2,-3,4,-1,-2,1,5,-10,1,2,3,4,5,6,7,-34,100]
arr = [-2,-3,4,-1,-2,1,5,-3]
arr = [-2,-3,4,-1,-2,1,5,-3,-8,19,20]
print maxSumContiguous(arr)
