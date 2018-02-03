def generate_instances(box):
	arr = []
	"""
	arr.append([]+box)
	box.insert(0, box.pop(1))
	arr.append([]+box)
	box = box[::-1]
	arr.append([]+box)	
	"""	
	#[Height, Length, Width]
	#Total combinations can be 3! = 6, we need to take only those where length > width
	i=0
	while i < len(box):
		if box[1] > box[2]:
			arr.append([]+box)
		elif box[2] > box[1]:
			arr.append([box[0], box[2], box[1]])
		i+=1
		if i < len(box):
			box.insert(0, box.pop(i))
	return arr

def merge_sort(arr):
	if len(arr) == 1:
		return arr
	
	left_arr = merge_sort(arr[:len(arr)//2])
	right_arr = merge_sort(arr[len(arr)//2:])

	sorted_arr = []
	while len(left_arr) and len(right_arr):
		#Additional condition to sort according to base area of box, [h, l, b]
		if left_arr[0][1]*left_arr[0][2] >= right_arr[0][1]*right_arr[0][2]:	
		#if left_arr[0] < right_arr[0]:			#Used for normal array sort
			sorted_arr.append(left_arr.pop(0))
		
		#Additional condition to sort according to base area of box, [h, l, b]
		#if left_arr[0][1]*left_arr[0][2] > right_arr[0][1]*right_arr[0][2]:
		else:
		#if left_arr[0] > right_arr[0]:			#Used for normal array sort
			sorted_arr.append(right_arr.pop(0))
	while len(left_arr):
		sorted_arr.append(left_arr.pop(0))
	while len(right_arr):
		sorted_arr.append(right_arr.pop(0))

	return sorted_arr

def boxStacking(arr):
	total_instances = []
	for box in arr:
		total_instances += generate_instances(box)

	#for box in total_instances:
	#	print box
	
	total_instances = merge_sort(total_instances)
	
	#print "After Sort"
	#for box in total_instances:
	#	print box

	height_arr = [box[0] for box in total_instances]
	result_arr = [i for i in range(len(total_instances))]

	#print height_arr
	#print result_arr
	for i in range(1, len(total_instances)):
		for j in range(0, i):
			if total_instances[j][1] > total_instances[i][1] and total_instances[j][2] > total_instances[i][2]:
				#print "(i,j)", (i,j), height_arr
				height_arr[i] = max(height_arr[j]+total_instances[i][0], height_arr[i])
				result_arr[i] = j
			#print "(i,j)", (i,j), height_arr
	print height_arr
	print result_arr

	print "Boxes"
	index = height_arr.index(max(height_arr))
	while 1:
		print total_instances[index]
		if index == result_arr[index]:
			break
		else:
			index = result_arr[index]

	return max(height_arr)

#[height,length,width]
arr =  [[4,6,7],
	[1,2,3],
	[4,5,6],
	[10,12,32]]

arr2 = [10,9,8,7,6,5,4,3,2,1]
#print generate_instances(arr[1])

arr3 = [[4,2,1],
	[5,3,2]]
print boxStacking(arr)

#print merge_sort(arr2)
