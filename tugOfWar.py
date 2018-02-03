import time
def solveTugOfWar(array):
	min_diff = [4957954214]
	sol = [False]*len(array)
	solveTugOfWar_Utility(array, [], [], sol, 0, min_diff)
#	print sol
	print "First Subset: ",
	for i in range(len(sol)):
		if sol[i] == True:
			print array[i],

	print
	print "Second Subset: ",
	for i in range(len(sol)):
		if sol[i] == False:
			print array[i],

	return

#array: original array
#arr1: subset 1
#arr2: subset 2
#sol: array with boolean values, True representing the index of success solution in arr1
#index: current index of array
#min_diff: minimum difference between sum of arr1 & arr2
def solveTugOfWar_Utility(array, arr1, arr2, sol, index, min_diff):
	
	if index == len(array):
#		if len(arr1) == len(arr2):
#			print arr1
#			print arr2
		return
#	time.sleep(1)

	val = array[index]
	#include the current element in arr1
	arr1.append(val)
	
	#Creating the complimentry array (arr2), i.e., all the elements not present in arr1 will be in arr2 and vice versa
	del arr2[:]
	for num in array:
		if (num not in arr1) and (num not in arr2):
			arr2.append(num)
	
	#Recursive call, move to next element, including the current in arr1
	solveTugOfWar_Utility(array, arr1, arr2, sol, index+1, min_diff)

	#Check if the difference b/w the half of sum of main array and sum of first array is less than minimum avilable difference,
	#also, length of both the arrays should be equal
	if (abs(sum(array)/2 - sum(arr1)) < min_diff[0] and len(arr1) == len(array)/2):
		#redifine the minimum difference
		min_diff[0] = abs(sum(array)/2 - sum(arr1))
		#clear the solution list
		del sol[:]
		#Reinitialize its values with False
		for k in array:
			sol.append(False)
		#Mark the index of all the elements in the first array as try in solution
		for i in arr1:
			sol[array.index(i)] = True

	#BackTrack: Exclude the current element from arr1
	arr1.pop()
	
	#create the complimentry list arr2
	del arr2[:]
	for num in array:
		if (num not in arr1) and (num not in arr2):
			arr2.append(num)

#	print "Here 02:", arr1, arr2, index
	solveTugOfWar_Utility(array, arr1, arr2, sol, index+1, min_diff)
	return

array1 = [3, 4, 5, -3, 100, 1, 89, 54, 23, 20]
array2 = [1,2,3,4]
array3 = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
solveTugOfWar(array3)
