def longestNRsubstring(arr):
	lookup = [1 for i in range(len(arr))]

	temp_string = []
	final_string = []

	cur_count = 0
	max_count = 0
	
	#O(n) time
	for i in range(len(arr)):
		#O(1) as the max_set_size can be only 256
		if arr[i] not in temp_string:
			temp_string.append(arr[i])
			cur_count += 1
			lookup[i] = cur_count
		else:
			if max_count < cur_count:
				max_count = cur_count
				del final_string[:]
				final_string += temp_string
			cur_count = 0
			del temp_string[:]

	if max_count < cur_count:
		max_count = cur_count
		del final_string[:]
		final_string += temp_string

	print ''.join(final_string)
	return max_count

arr1 = 'ABDEFGABEF'
arr2 = 'ABDEFGABEFUTOYPLRN'
print longestNRsubstring(arr1)
print longestNRsubstring(arr2)
