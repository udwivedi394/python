def isSafe(x, k, new_arr):
	if x <= k: 
		if len(new_arr)==0:
			return True
		if sum(new_arr)+x <= k:
			return True
	return False

def sumSubset(arr, k, new_arr=None, complete_list=None):
	if new_arr == None:
		new_arr = []
	
	if complete_list == None:
		complete_list = []
	
	if len(arr) == 0:
		if sum(new_arr) == k:
			complete_list.append([]+new_arr)
			return True
		return False

	if isSafe(arr[0], k, new_arr):
		new_arr.append(arr[0])
		sumSubset(arr[1:], k, new_arr, complete_list)
		#if arr1 == 1:
		#	return new_arr
		#else:
		new_arr.pop()
		sumSubset(arr[1:], k, new_arr, complete_list)
	else:
		sumSubset(arr[1:], k, new_arr, complete_list)

def sumSubsetDyn(arr, k):
	lookup = []+arr
	result = [i for i in range(len(arr))]

	for i in range(1, len(arr)):
		for j in range(0, i+1):
			if lookup[i]+lookup[j] == k:
				pass		

#If array is sorted
def findSumPairSort(arr, k, lookup_dict):
	lower_bound = 0
	upper_bound = len(arr)-1

	while lower_bound < upper_bound:
		cur_sum = arr[lower_bound]+arr[upper_bound]

		if cur_sum == k:
			return (lower_bound, upper_bound)
		if cur_sum > k:
			upper_bound -= 1
		if cur_sum < k:
			lower_bound += 1

	return False

#Regardless array sorted or not
def findSumPairGeneral(arr, k, lookup_dict):
	#lookup_dict = {}

	for i in range(len(arr)):
		#Check if the current value is in lookup_dict
		if lookup_dict.get(arr[i]):
			#The lookup returns the index of the element where its compliment existed
			return (lookup_dict.get(arr[i]), i)

		#Store the compliment of current_element with index
		lookup_dict[k-arr[i]] = i
	
	return False

#[2, 3, 4, 5, 12, 34]
arr3 = [3, 34, 4, 12, 5, 2]
cp = []
print sumSubset(arr3, 9, None, cp)
print cp

lookup = {}
arr1 = [1,2,3,9]
arr2 = [1,2,4,4]
print findSumPairSort(arr2, 8, lookup)

print arr3
print findSumPairGeneral(arr3, 36, lookup)
#print lookup
