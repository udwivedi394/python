def powerSet(arr):
	n = len(arr)
	n = 1<<n

	for i in range(n):
		str1 = ''
		for j in range(n):
			if i & (1<<j):
				str1 += arr[j]
		print str1
	return

def distinctSet(arr):
	n = 1<<len(arr)
	lookup_dict = {}

	for i in range(n):
		str1 = ''
		for j in range(len(arr)):
			if i & (1<<j):
				str1 += str(arr[j])
		if lookup_dict.get(str1) == None:
			lookup_dict[str1] = 1
			print str1
arr = [1,2,2,9,9]
distinctSet(sorted(arr))

#arr = 'abcdefgh'
#powerSet(arr)
