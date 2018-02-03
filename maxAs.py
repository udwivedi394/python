#Dynammic Approach
def maxA(N):
	if N < 7:
		return N
	
	arr = [0 for i in range(N+1)]
	for i in range(min(7,N+1)):
		arr[i] = i

	max_a = 0
	for i in range(7,N+1):
		for j in range(i):
			#Formula is total A's = [n*(a+1)]
			#Here n -> arr[j], a -> steps remaining = i-j-2
			cur_a = arr[j]*(i-j-2+1)
			max_a = max(max_a, cur_a)
		arr[i]=max_a
	print arr
	return arr.pop()

print maxA(20)
