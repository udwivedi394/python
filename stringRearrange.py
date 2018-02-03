def stringRearrange(arr):
	lookup = [0 for i in range(26)]

	for i in arr:
		lookup[ord(i)-ord('a')] += 1
	
	maxi = max(lookup)
	if maxi - (sum(lookup)-maxi) > 1:
		return "Not Possible"

	string =''
	next_index = -1
	while sum(lookup):
		#print next_index,lookup
		maxi = max(lookup)
		max_ind = lookup.index(maxi)
		lookup[max_ind] = 0
		while maxi:
			#print (max_ind, next_index)
			if max_ind != next_index:	
				string+=chr(ord('a')+max_ind)
				maxi -= 1
			next_index = findNext(lookup)
			if next_index!=None:
				string+=chr(ord('a')+next_index)
				lookup[next_index]-=1
			#print string
	return string

def findNext(arr):
	for i in range(len(arr)):
		if arr[i] > 0:
			return i
	return

print stringRearrange("aabbbcdddde")
print stringRearrange("aabbbcddddezzzz")
print stringRearrange("aaaabbbb")
print stringRearrange("aaaabbbbbc")
print stringRearrange("aaa")
