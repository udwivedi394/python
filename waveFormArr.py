#Naive Solution, sort->take 1 element from last 2 element from beginning
def waveFormArr(arr):
	arr_rev = sorted(arr)

	new_arr = []
	alternate = True
	while len(arr_rev):
		if alternate:
			new_arr.append(arr_rev.pop())
		else:
			new_arr.append(arr_rev.pop(0))
		alternate ^= True
	return new_arr

def waveFormArr02(arr):
	arr = []+arr
	alternate = True
	
	i=0
	while i < len(arr)-1:
		if alternate:
			if arr[i] < arr[i+1]:
				arr[i] ^= arr[i+1]
				arr[i+1] ^= arr[i]
				arr[i] ^= arr[i+1]
		else:
			if arr[i] > arr[i+1]:
				arr[i] ^= arr[i+1]
				arr[i+1] ^= arr[i]
				arr[i] ^= arr[i+1]
		alternate ^= True
		i += 1
	return arr

arr = [10, 5, 6, 3, 2, 20, 100, 80,1]
print waveFormArr(arr)
print waveFormArr02(arr)
