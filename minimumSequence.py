#O(n) Complexity, O(1): Space Complexity
def printSeq(arr):
	
	arr = list(arr)
	count_d = 0
	count_i = 0
	max_digit = 0
	last_digit = 0

	while len(arr):
		if arr[0]=='D':
			while len(arr) and arr[0]!='I':
				count_d += 1
				arr.pop(0)
		
			end = max_digit+count_i + (0 if last_digit else 1)
			
			#For printing the increasing sequence
			for i in range(max_digit+1,end):
				print i,
				
				max_digit = max(i,max_digit)
				last_digit = i

			#For printing the decreasing sequence
			for j in range(count_d+max_digit+1, max_digit, -1):	
				print j,
			
			max_digit = max_digit+count_d+1
			last_digit = j
		
			#Clear both the counters, D and I
			count_d = 0
			count_i = 0
		else:
			while len(arr) and arr[0]!='D':
				count_i += 1
				arr.pop(0)

	start = max_digit+1
	end = start+count_i + (0 if max_digit else 1)
	for i in range(start,end):
		print i,
	print
	return
arr = ["" for i in range(10)]
arr[0] = "DDIDDIID"
arr[1] = "D"
arr[2] = "I"
arr[3] = "DD"
arr[4] = "II"
arr[5] = "DIDI"
arr[6] = "IIDDD"
arr[7] = "DDIDDIII"
arr[8] = "IIIIIIID"
arr[9] = "DDDDDDDI"

for i in arr:
	print i
	printSeq(i)
