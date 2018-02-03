def sortTrains(arr, dep):
	if len(arr) == 1:
		return [arr, dep]

	mid = len(arr)//2
	left = sortTrains(arr[:mid], dep[:mid])
	right = sortTrains(arr[mid:], dep[mid:])
	
	left_arr = left[0]
	left_dep = left[1]

	right_arr = right[0]
	right_dep = right[1]
	
	temp_arr = []
	temp_dep = []
	while len(left_arr) and len(right_arr):
		if left_arr[0] < right_arr[0]:
			temp_arr.append(left_arr.pop(0))
			temp_dep.append(left_dep.pop(0))
		else:
			temp_arr.append(right_arr.pop(0))
			temp_dep.append(right_dep.pop(0))

	while len(left_arr):
		temp_arr.append(left_arr.pop(0))
		temp_dep.append(left_dep.pop(0))

	while len(right_arr):
		temp_arr.append(right_arr.pop(0))
		temp_dep.append(right_dep.pop(0))
		
	return [temp_arr,temp_dep]

def minPlatforms(arr, dep):
	#Sort the arr and dep according to arr
	sorted_arr = sortTrains(arr, dep)
	
	del arr[:] 
	arr += sorted_arr[0]
	del dep[:] 
	dep += sorted_arr[1]

	#Combine the overlapping intervals, and increase the counter
	i = 0
	min_platforms = 0
	count = 1

	while i < len(arr)-1:
		if dep[i] > arr[i+1]:
			dep[i] = max(dep[i], dep[i+1])
			arr.pop(i+1)
			dep.pop(i+1)
			count += 1
		else:
			min_platforms = max(count, min_platforms)
			count = 1
			i += 1
	
	min_platforms = max(count, min_platforms)
	return min_platforms

arr = [1835, 900,  940,  950, 1100, 1120, 1500, 1800, 1810, 1815, 1830]
dep = [1845, 910, 1200, 1120, 1130, 1150, 1900, 2000, 1820, 1850, 1840 ]

print minPlatforms(arr, dep)
print arr
print dep
