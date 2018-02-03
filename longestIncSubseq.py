import time
#Find the longest subsequence
#arr -> array
#i   -> current counter
#subseq -> this array stores the current subsequence
def longestIncSubseq(arr, i, subseq=None):
	#Base condition, if current counter reaches end of array
	if i == len(arr):
		#print subseq
		#return the length of subseq
		return len(subseq)
	
	#If subseq is NA, then create a new one
	if subseq == None:
		subseq = []

	#Initialize count for two scenarios
	count_01 = -1
	count_02 = -1

	#print "i:", i, "subseq:", subseq
	#if len of subsequence is 0, or current element in arr is greater than max of subsequence
	if len(subseq) == 0 or arr[i] >= max(subseq):
		#add the current element in subsequence
		subseq.append(arr[i])
		count1 = longestIncSubseq(arr, i+1, subseq)

		#Backtrack
		#Exclude the current element from subseq
		subseq.pop()
		count2 = longestIncSubseq(arr, i+1, subseq)
		count_01 = max(count1, count2)
	else:
		#If main condition fails, then move to next element
		count_02 = longestIncSubseq(arr, i+1, subseq)
	
	return max(count_01, count_02)

# A naive Python implementation of LIS problem
 
""" To make use of recursive calls, this function must return
 two things:
 1) Length of LIS ending with element arr[n-1]. We use
 max_ending_here for this purpose
 2) Overall maximum as the LIS may end with an element
 before arr[n-1] max_ref is used this purpose.
 The value of LIS of full array of size n is stored in
 *max_ref which is our final result """
 
# global variable to store the maximum
global maximum
 
def _lis(arr , n ):
 
    # to allow the access of global variable
    global maximum
 
    # Base Case
    if n == 1 :
        return 1
 
    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1
 
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is maller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""
    for i in xrange(1, n):
        res = _lis(arr , i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res +1
 
    # Compare maxEndingHere with overall maximum. And
    # update the overall maximum if needed
    maximum = max(maximum , maxEndingHere)
 
    return maxEndingHere
 
def lis(arr):
 
    # to allow the access of global variable
    global maximum
 
    # lenght of arr
    n = len(arr)
 
    # maximum variable holds the result
    maximum = 1
 
    # The function _lis() stores its result in maximum
    _lis(arr , n)
 
    return maximum

#Dynamic solution, using tabulatioon technique
def findbestSol_03(arr):
	
	#Create a temporary array of same size as arr
	lookup = [1]*len(arr)
	result_arr = [i for i in range(len(arr))]
	
	#Iterate the value of i to len(arr)
	for i in range(1, len(arr)):
		#Initialize j from start of array
		j = 0
		#Compare each value till i
		while j < i:
			if arr[j] < arr[i]:
				#Take max of current lookup and lookup at j + 1
				lookup[i] = max(lookup[i], lookup[j]+1)
				result_arr[i] = j
			j += 1

	print "Result", result_arr
	index = result_arr.index(max(lookup))
	print "Original_arr: ", arr
	print "Arr: ",
	while 1:
		print arr[index],
		if index == result_arr[index]:
			break
		else:
			index = result_arr[index]

	return max(lookup)

def findbestSol_04(arr):
	lookup = []+arr
	result_arr = [i for i in range(len(arr))]

	for i in range(1, len(arr)):
		for j in range(0, i):
			if arr[j] < arr[i]:
				lookup[i] = max(lookup[j]+arr[j], lookup[i])
				result_arr[i] = j
	print lookup
	print result_arr
	return max(lookup)

def findbestSol_05(arr):
	lookup = [1 for i in range(len(arr))]
	result = [i for i in range(len(arr))]

	for i in range(len(arr)):
		for j in range(0,i+1):
			if arr[i] > arr[j]:
				if lookup[j]+1 > lookup[i]:
					result[i] = j
				lookup[i] = max(lookup[j]+1, lookup[i])

	index = lookup.index(max(lookup))
	while 1:
		print arr[index],
		if index == result[index]:
			break
		index = result[index]
	
	return max(lookup)

arr = [10,22,9,33,21,50,41,60,80]
#arr = [10,8,9,20,19]
t1 = time.time()
print longestIncSubseq(arr,0)
t2 = time.time()
print t2-t1

t1 = time.time()
print "Length of lis", lis(arr)
t2 = time.time()
print t2-t1

t1 = time.time()
print "Length of lis", lis(arr)
t2 = time.time()
print t2-t1

t1 = time.time()
print "Length of solution", findbestSol_03(arr)
t2 = time.time()
print t2-t1

t1 = time.time()
print "Length of solution2", findbestSol_04(arr)
t2 = time.time()
print t2-t1


arr = [10,22,9,33,21,50,41,60,80]
arr = [3,4,-1,5,8,2,3,12,7,9,10]
t1 = time.time()
val = findbestSol_05(arr)
print
print "Length of solution05", val
t2 = time.time()
print t2-t1
