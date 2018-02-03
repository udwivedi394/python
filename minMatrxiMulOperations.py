lookup = {}

#Naive Solution, Recursive approach
def matrixMul(arr):
	if len(arr)==3:
		return arr[0]*arr[1]*arr[2]

	min_count = 88994654641321313
	cur_count = 0
	for i in range(1, len(arr)-1):
		cur_count = matrixMul(arr[:i]+arr[i+1:]) + (arr[i-1]*arr[i]*arr[i+1])
		if cur_count < min_count:
			min_count = cur_count
	return min_count

#To print paranthesis of correct order
def matrixMul02(arr, arr_alpha):
	if len(arr)==3:
		string = '('+arr_alpha.pop(0)+arr_alpha.pop()+')'
		arr_alpha.append(string)
		return arr[0]*arr[1]*arr[2]

	min_count = 88994654641321313
	cur_count = 0
	for i in range(1, len(arr)-1):
		temp_alpha = []+arr_alpha
		string = '('+arr_alpha[i-1]+arr_alpha[i]+')'
		temp_alpha[i-1] = string
		temp_alpha.pop(i)

		cur_count = matrixMul02(arr[:i]+arr[i+1:], temp_alpha) + (arr[i-1]*arr[i]*arr[i+1])
		if cur_count < min_count:
			min_count = cur_count
			res_arr = temp_alpha

	del arr_alpha[:]
	arr_alpha += res_arr
	return min_count

arr1 = [40,20,30,10,30]
arr2 = [10,20,30,40,30]
arr3 = [10,20,30]
print matrixMul(arr1)

cur_arr = arr2
arr_alpha = [chr(ord('A')+i) for i in range(len(cur_arr)-1)]
result = matrixMul02(cur_arr, arr_alpha)
print "Optimal Parenthesization:", arr_alpha[0]
print "Minimum Cost of Multiplication:", result
