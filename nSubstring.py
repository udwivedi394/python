def nSubstring(arr):
	
	j=0
	n=len(arr)
	for i in range(1,n):
		if arr[j] == arr[i]:
			j += 1
		else:
			j = 0

	#j will be the last position in the array
	res_len = n-j

	if n % res_len != 0:
		return False
	else:
		return n//res_len

print nSubstring("abcabcabc")
print nSubstring("aabaabaabaab")
print nSubstring("aabaabdabaab")
