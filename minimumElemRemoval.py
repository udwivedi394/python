#Naive Solution 
def minimumRemovals(arr, removals=0):	
	n = len(arr)

	if 2*min(arr) > max(arr):
		return removals

	minimum_removal = 457776344543

	for i in range(n):
		temp = []+arr
		temp.pop(i)
		cur_removal = minimumRemovals(temp, removals+1)
		
		minimum_removal = min(minimum_removal, cur_removal)

	return minimum_removal

def minimumRemovals02(arr):	
	n = len(arr)

	if 2*min(arr) > max(arr):
		return 0

	return min(minimumRemovals02(arr[1:])+1, minimumRemovals02(arr[:-1])+1)

def minimumRemovals03(arr):
	starting_point=0
	ending_point = 0


arr1 = [4, 5, 100, 9, 10, 11, 12, 15, 200]
arr2 = [1,2,3]
print minimumRemovals(arr1)
print minimumRemovals02(arr1)
