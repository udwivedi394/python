def sortandRemoveDuplicates(arr):
	temp = sorted(arr)
	del arr[:]

	arr += temp
	i = 0
	while i<len(arr)-1:
		if arr[i] == arr[i+1]:
			arr.pop(i)
		else:
			i += 1
	return arr

#Elements can be repeated
def combinationalSum(arr, k, index=0, new_arr=None):
	if new_arr == None:
		new_arr = []
	
	if index == len(arr) or k==0:
		if k==0:
			print new_arr
		return

	if k-arr[index] >= 0:
		new_arr.append(arr[index])
		combinationalSum(arr, k-arr[index], index, new_arr)
		
		#BackTrack: Excluding the last element
		new_arr.pop()
		#Moving to next index without current element
		combinationalSum(arr, k, index+1, new_arr)
	else:
		combinationalSum(arr, k, index+1, new_arr)
	return

#Sum with distinct elements, No 2 elements repeated again
def combinationalSum02(arr, k, index=0, new_arr=None):
	if new_arr == None:
		new_arr = []
	
	if index == len(arr) or k==0:
		if k==0:
			print new_arr
		return

	if k-arr[index] >= 0:
		new_arr.append(arr[index])
		combinationalSum02(arr, k-arr[index], index+1, new_arr)
		
		#BackTrack: Excluding the last element
		new_arr.pop()
		#Moving to next index without current element
		combinationalSum02(arr, k, index+1, new_arr)
	else:
		combinationalSum02(arr, k, index+1, new_arr)
	return

arr = [2,2,4,5,6,8,8,8,4,6,8]
sortandRemoveDuplicates(arr)
print arr
combinationalSum(arr,10)
print
combinationalSum02(arr,10)
