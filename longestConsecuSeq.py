def longestConsSeq(arr):
	lookup_dict = {}

	#Map every element with next consecutive element in array, 
	#key : value
	#element: [element_index, next_element_index]
	#If no next element found in the dictionary till now, next_element_index = None
	for i in range(len(arr)):
		lookup_dict[arr[i]] = [i,None]

		if lookup_dict.get(arr[i]-1):
			lookup_dict[arr[i]-1][1] = i

		if lookup_dict.get(arr[i]+1):
			lookup_dict[arr[i]] = [i,lookup_dict[arr[i]+1][0]]
	
	#Traverse through orig_array
	maxi = 0
	start_elem = i
	for i in arr:
		cur_len = 0
		#To check the current element is start of subsequence, and previous element not present in array
		if lookup_dict.get(i-1)==None:
			cur_elem = i
			#Starting from current element, go on till you find None as cur_elem
			while lookup_dict.get(cur_elem):
				cur_len += 1
				if lookup_dict[cur_elem][1]!=None:
					cur_elem = arr[lookup_dict[cur_elem][1]]
				else:
					break
		#If current length is greater than maxi then store the current element as start element
		if cur_len > maxi:
			start_elem=i
		maxi = max(cur_len, maxi)
	
	#print lookup_dict
	
	print "The longest Sequence is:",

	#Print the largest Subsequence
	cur_elem = start_elem
	while lookup_dict.get(cur_elem):
		print arr[lookup_dict[cur_elem][0]],
		if lookup_dict[cur_elem][1]!=None:
			cur_elem = arr[lookup_dict[cur_elem][1]]
		else:
			break	
	print
	return maxi

arr = [1,9,3,10,4,20,2]
arr2 = [36,41,56,35,44,33,34,92,43,32,42]
print longestConsSeq(arr2)
