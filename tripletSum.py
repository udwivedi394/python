#For this algo to work array must be sorted
def findPair(arr, k):
	lower_bound = 0
	upper_bound = len(arr)-1

	while lower_bound < upper_bound:
		if arr[lower_bound]+arr[upper_bound] == k:
			print lower_bound, upper_bound,
			return True
		if arr[upper_bound]+arr[lower_bound] > k:
			upper_bound -= 1
		if arr[lower_bound]+arr[upper_bound] < k:
			lower_bound += 1
	return False

#For this algo, sorting is not required
def findPair02(arr, k):
	lookup_dict = {}
	
	for i in range(len(arr)):
		if lookup_dict.get(arr[i]):
			print arr[lookup_dict[arr[i]]], arr[i],
			return True
		lookup_dict[k-arr[i]] = i
	return False

def tripletSum(arr, sumi):
	for i in range(len(arr)-1,-1,-1):
		#Array must be sorted
		#if findPair(arr[:i], sumi - arr[i]):
		if findPair02(arr[:i], sumi - arr[i]):
			print arr[i]
			return True
	return False

arr = [1,3,5,6,9,12]
print tripletSum(arr,24)
