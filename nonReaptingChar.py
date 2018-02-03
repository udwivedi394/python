import time

#Return first non-repeating character from string
#Time Complexity O(n) with only one traversal, Space complexity O(1) as fixed size array is being created
def firstNonRepeatingChar(arr):
	lookup_arr = [[0,-1] for i in range(256)]

	for i in range(len(arr)):
		lookup_arr[ord(arr[i])][0] += 1
		if lookup_arr[ord(arr[i])][0] == 1:
			lookup_arr[ord(arr[i])][1] = i
	
	min_index = 9999999999999

	for i in range(256):
		if lookup_arr[i][0] == 1:
			if min_index > lookup_arr[i][1]:
				min_index = lookup_arr[i][1]
	return min_index

#To find the kth nonrepeating character in a array
#O(n) complexity, only one traversal of array.
#Sorting of array is constant time as size of array is fixed
def kNonRepeatingChar(arr, k):
	k -= 1
	n = len(arr)
	lookup_count = [1 for i in range(256)]
	lookup_index = [n for i in range(256)]

	for i in range(len(arr)):
		lookup_count[ord(arr[i])] += 1
		if lookup_count[ord(arr[i])] == 1:
			lookup_index[ord(arr[i])] = i
		elif lookup_count[ord(arr[i])] == 2:		#Extra elif condition instead of else, to avoid redundancy
		#else:
			lookup_index[ord(arr[i])] = n

	#print lookup_index
	lookup_index = sorted(lookup_index)
	#print lookup_index
	
	if lookup_index[k] == n or k > min(n,256):
		return -1
	
	return lookup_index[k]

#Reading from continuous stream
#O(1) complexity, using lookup dictionary 
def firstNonRepeatingfromStream():
	lookup_dict = {}
	ind_ctr = 0			#To count the order in which unique characters were recieved
	cur_ctr = 0			#To mark the current first non Repeating character corresponding to the order of ind_ctr

	try:
		fd = open("textStreamTest.txt", "r")
	except:	
		print "Stream opening failed"
		return -1

	try:
		while 1:
			ch = fd.read(1)
			if len(ch) == 0:
				break
			
			#If character not found in lookup
			if lookup_dict.get(ch)==None:
				#Add the element with [count, current order]
				lookup_dict[ch] = [1, ind_ctr]
				#Inrease the current order
				ind_ctr += 1
			else:
				#If found for first time then increase count by 1, it simply implies character is repeating
				if lookup_dict[ch][0] == 1:
					lookup_dict[ch][0] += 1
				#If found and the order in which the element was entered and current order of unique charactr is equal
				if lookup_dict[ch][1] == cur_ctr:
					#Increment the current order
					cur_ctr += 1

			#print lookup_dict
			#Go through the dictionary
			doagain = 1
			while doagain:
				doagain = 0
				for key, value in lookup_dict.iteritems():
					#If current order is found
					if value[1] == cur_ctr:
					#If count is not 1, i.e., non-repeating
						if value[0] != 1:
							#Increase the cur counter
							cur_ctr += 1
							doagain = 1
							break
						else:
							non_rep_ch = key
							found = 1
							break
					non_rep_ch = "Not Available"
			print "Reading", ch, "from stream", "Cur_ctr", cur_ctr
			print "First Non-Repeating character so far:", non_rep_ch
			#time.sleep(1)
	finally:
		print "Closing Stream"
		fd.close()

arr = "GeeksforGeeks"
arr2 = "GeeksQuiz"
ind = firstNonRepeatingChar(arr)
print "First non-Repeating character is", arr[ind]
ind = kNonRepeatingChar(arr, 1)
print "kth non-Repeating character is", arr[ind] if ind>=0 else "Not Available"

firstNonRepeatingfromStream()
