def sortarr(arr):
	if len(arr) == 1:
		return arr
	
	mid = len(arr)//2
	left_arr = sortarr(arr[:mid])
	right_arr = sortarr(arr[mid:])

	temp_arr = []
	while len(left_arr) and len(right_arr):
		if left_arr[0][0] <= right_arr[0][0]:
			temp_arr.append(left_arr[0])
			left_arr.pop(0)
		else:
			temp_arr.append(right_arr[0])
			right_arr.pop(0)

	while len(left_arr):
		temp_arr.append(left_arr.pop(0))

	while len(right_arr):
		temp_arr.append(right_arr.pop(0))

	return temp_arr

def mergeOverlap(arr):
	#Sort the arr according to the start time
	arr = sortarr(arr)
	print arr

	i = 0
	while i<len(arr)-1:	
	#Then start from beginning, and check if current end time lies in range of next duration
	#If yes, then pop next, and update the current_end time
		if arr[i][1] >= arr[i+1][0]:
			arr[i][1] = max(arr[i][1], arr[i+1][1])
			arr.pop(i+1)
		else:
			i+=1
	return arr

arr1 = [[6,8],[1,9],[2,4],[4,7]]
arr2 = [[1,3],[2,4],[5,7],[6,8]]
print mergeOverlap(arr2)
