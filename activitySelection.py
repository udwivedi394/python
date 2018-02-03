#Return [[sorted_arr], [index_arr]]
def mergeSort(arr, index_arr=None):
	if len(arr) == 1:
		return [arr, index_arr]

	if index_arr == None:
		#Create an arr with indexes
		index_arr = [i for i in range(len(arr))]

	#left_pack -> [left_arr, left_index]
	left_pack = mergeSort(arr[:len(arr)//2], index_arr[:len(index_arr)//2])

	#right_pack -> [right_arr, right_index]
	right_pack = mergeSort(arr[len(arr)//2:], index_arr[len(index_arr)//2:])

	temp_arr = []
	temp_index = []

	left_arr = left_pack[0]
	left_index = left_pack[1]

	right_arr = right_pack[0]
	right_index = right_pack[1]

	while len(left_arr) and len(right_arr):
		if left_arr[0] <= right_arr[0]:
			temp_arr.append(left_arr.pop(0))
			temp_index.append(left_index.pop(0))
		else:
			temp_arr.append(right_arr.pop(0))
			temp_index.append(right_index.pop(0))
	
	while len(left_arr):
		temp_arr.append(left_arr.pop(0))
		temp_index.append(left_index.pop(0))
	while len(right_arr):
		temp_arr.append(right_arr.pop(0))
		temp_index.append(right_index.pop(0))

	return [temp_arr, temp_index]

#This function requires len(arr1) = len(arr2)
#Sorts arr2 and arranges arr1 in same order as arr2
def mergeSortUtility(arr1, arr2):
	if len(arr1) != len(arr2):
		return

	sort_pack = mergeSort(arr2)
	del arr2[:]
	arr2 += sort_pack[0]

	temp_start = []
	for i in sort_pack[1]:
		temp_start.append(start[i])

	del arr1[:]
	arr1 += temp_start

def activitySel(start, finish):
	#Greedy Approach: Sort the start and finish, in accordance to increasing order of finish time
	mergeSortUtility(start, finish)
	cur_finish = -1

	temp_arr = []
	for i in range(len(finish)):
		#Greedy Choice: If the start time of current activity is greater than or equal to finish time of previous finish time
		if start[i] >= cur_finish:
			cur_finish = finish[i]
			temp_arr.append(i)
	return temp_arr

start =[20,12,10]
finish=[30,25,20]

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
result = activitySel(start, finish)
print "Start time: ", start
print "Finish time:", finish
print "Total activity:", len(result), "Result:", result
