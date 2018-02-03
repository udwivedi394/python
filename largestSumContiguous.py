#Naive solution, with three loops
def largestSumContiSubarray(arr):
	max_sum = -451378945221
	n = len(arr)

	for i in range(0, n):
		for j in range(0, i+1):
			sumi = 0
			new_arr = []
			for k in range(j, i+1):
				sumi += arr[k]
				new_arr.append(arr[k])

			if sumi > max_sum:
				max_sum = sumi
				max_sum_arr = new_arr

	print max_sum_arr
	return max_sum

#Dynammic Programming, with linear time
def largestSumContibestSol(arr):
	lookup = []+arr
	n = len(arr)

	for i in range(1,n):
		lookup[i] = max(lookup[i-1]+lookup[i], lookup[i])

	print lookup
	return max(lookup)


arr= [-2,-3,4,-1,-2,1,5,-3,4]
print largestSumContiSubarray(arr)
print largestSumContibestSol(arr)
