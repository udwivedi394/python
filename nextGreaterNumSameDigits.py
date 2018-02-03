def nextGreaterNum(num):
	num = list(num)
	i = len(num)-1

	while i>0 and num[i-1] > num[i]:
		i -= 1

	if i==0:
		return "Not Possible"

	#Swap the i-1 element with last element in array, which is the smallest
	swap_temp = num[i-1]
	num[i-1] = num[-1]
	num[-1] = swap_temp

	#num = num[:i]+sorted(num[i:])
	#Optimization to better the sort
	high = len(num)-1
	low = i

	while low < high:
		swap(num,low,high)
		low += 1
		high -= 1

	num = ''.join(num)
	return num

def swap(arr, i, j):
	swap = arr[i]
	arr[i] = arr[j]
	arr[j] = swap

	""" This swap method doesnot works on str
	arr[i] ^= arr[j]
	arr[j] ^= arr[i]
	arr[i] ^= arr[j]
	"""
	return arr

num = "534976"
num2 = "4321"
print nextGreaterNum(num)

arr = [1,2,3,4]
