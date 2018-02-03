def sumPair(arr, k):
	lookup_dict = {}

	for i in range(len(arr)):
		if lookup_dict.get(arr[i]):
			print arr[lookup_dict[arr[i]]], arr[i],
			return True
		else:
			lookup_dict[k-arr[i]] = i
	return False

def tripletSum(arr, k):
	
	for i in range(len(arr)):
		if arr[i] >= k:
			continue
		temp = []+arr
		temp.pop(i)
		if sumPair(temp, k-arr[i]):
			print arr[i],
			return True
	return False

#This solution uses O(n^3) Complexity
def fourSum(arr, k):
	for i in range(len(arr)):
		if arr[i] >= k:
			continue
		temp = []+arr
		temp.pop(i)
		if tripletSum(temp, k-arr[i]):
			print arr[i]
			return True
	return False

#This solution uses O(n^2) Complexity
def fourSum02(arr, k):
	aux_arr = []
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			aux_arr.append([arr[i], arr[j]])
	return sumPair02(aux_arr, k)
	print aux_arr

#Time Complexity: O(n), Space Complexity: O(n)
def sumPair02(arr, k):
	lookup_arr = {}
	
	found = False
	for i in range(len(arr)):
		if lookup_arr.get(sum(arr[i])):
			temp = arr[lookup_arr[sum(arr[i])]]
			print temp[0], temp[1], arr[i][0], arr[i][1]
			found = True
		else:
			lookup_arr[k-sum(arr[i])] = i
	return found

arr = [10,2,3,4,5,9,7,8]
print tripletSum(arr, 11)
print fourSum(arr, 23)
print fourSum02(arr, 23)
