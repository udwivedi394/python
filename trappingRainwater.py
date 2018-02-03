#Non Working Solution
def trappingRainWater(arr):
	water = 0
	max_height_index = 0
	min_water = 0
	min_height = 0
	
	i = 1
	n = len(arr)
	while i < n:
		if arr[i] < arr[max_height_index] and arr[i] >= min_height:
			min_water = arr[i]*(i-max_height_index-1)
			min_height = arr[i]
			water += min_water

		if arr[i] >= arr[max_height_index]:
			water += arr[max_height_index]*(i-max_height_index-1)
			max_height_index = i
			water = water-2*(min_water)

		print "i:",i,"arr[i]:",arr[i],"min_water:",min_water,"max_height_index:",max_height_index,"min_height:",min_height,
		print "water:",water
		i += 1

	return water

#Working solution, but complexity is O(n^2)
def trappingRainWater02(arr):
	
	water = 0
	n = len(arr)
	
	for i in range(1,n-1):
		left_max = max(arr[:i])
		right_max = max(arr[i+1:])

		if arr[i] <= left_max and arr[i] <= right_max:
			water += min(left_max,right_max)-arr[i]
		#print "left:",left_max,"right:",right_max,"i:",i,"arr[i]:",arr[i],"water:",water
	return water

#Working solution, Time Complexity: O(n), Space Complexity: O(n)
def trappingRainWater03(arr):
	n = len(arr)
	left_arr = [arr[i] for i in range(n)]
	right_arr = [arr[i] for i in range(n)]

	for i in range(1,n):
		left_arr[i] = max(left_arr[i-1],arr[i])
	
	for i in range(n-2,0,-1):
		right_arr[i] = max(right_arr[i+1], arr[i])


	water = 0

	for i in range(n):
		water += min(left_arr[i], right_arr[i])-arr[i]

	return water

#Working Solution, Time Complexity: O(n), Space Complexity: O(1)
def trappingRainWater04(arr):
	water = 0
	left_max = 0
	right_max = 0

	low = 0
	high = len(arr)-1

	while low < high:

		if arr[low] < arr[high]:
			if arr[low] > left_max:
				left_max = arr[low]

			water += left_max-arr[low]
			low += 1

		else:
			if arr[high] > right_max:
				right_max = arr[high]
			
			water += right_max-arr[high]
			high -= 1

	return water

arr1 = [2,0,2,0,4,0,6,0,2,0,2,0,6]
arr2 = [3, 0, 0, 0, 2, 0, 4]
arr3 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print "Water Trapped:", trappingRainWater02(arr1)
print "New Water Trapped:", trappingRainWater03(arr1)
print "Water Trapped 0.2:", trappingRainWater04(arr1)
