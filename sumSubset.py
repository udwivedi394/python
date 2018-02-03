def solveSubset(array, sumi, X):
	if array == None:
		return False

	array_list = []

	solveSubset_Utility(array, [], sumi, array_list, 0, X)

	return False

def isSafe(new_array, val, sumi):
	if sum(new_array)+val <= sumi:
		return True
	return False

def solveSubset_Utility(array, new_array, sumi, array_list, index, X):

	#Limiting condition, if sum of new_array is equal to sum required, print array and return
	if sum(new_array) == sumi:
		print new_array

		#Initialize new_array_sum as list, to get back the result
		new_array_sum = []

		#Call the function to find all values and subset having sum less than or eqaul to X
		solveSubsetLessSum(new_array, [], new_array_sum, X, 0)

		print (new_array_sum)
		return

	#Limiting condition, if index reached length of array, return
	if index == len(array):
		return


	val = array[index]
	
	if isSafe(new_array, val, sumi):
		#If val is safe include it in array
		new_array.append(val)
		solveSubset_Utility(array, new_array, sumi, array_list, index+1, X)
		
		#Backtracking, reversing the previous step, excluding the current element
		new_array.pop()	
		solveSubset_Utility(array, new_array, sumi, array_list, index+1, X)
	else:	
		#If val is not safe, go for next value in main array
		solveSubset_Utility(array, new_array, sumi, array_list, index+1, X)
		

#array: [2, 12, 45], for value of X=70
#append all values with sum less than 70, [0, 2, 12, 14, 47, 57], [0, 2, 14, 59, 47, 12, 57, 45]

def solveSubsetLessSum(array, new_array, new_arr2_sum, sumi, index):
	sum_val = sum(new_array)
	
	#if sum of new_array is less or equal to the requied sum, append it in new_arr2_sum
	if sum_val <= sumi and sum_val not in new_arr2_sum:
		new_arr2_sum.append(sum_val)
	
	#Limiting condition, index reached end of array
	if index == len(array):
		return

	val = array[index]

	if isSafe(new_array, val, sumi):
		#Similar to main problem, if safe, include the current element in new_array
		new_array.append(val)

		#Proceed to the next value including the current element
		solveSubsetLessSum(array, new_array, new_arr2_sum, sumi, index+1)

		#BackTrack, exclude the current element and proceed for next element in array
		new_array.pop()
		solveSubsetLessSum(array, new_array, new_arr2_sum, sumi, index+1)
	else:
		#if not safe, move to next element in array
		solveSubsetLessSum(array, new_array, new_arr2_sum, sumi, index+1)
		

array = [12, 47, 5, 2, 15, 1, 43]
solveSubset(array, 60, 70)

array2 = [2, 12, 45]
new_arr2_sum = []
solveSubsetLessSum(array2, [], new_arr2_sum, 70, 0)
print new_arr2_sum
