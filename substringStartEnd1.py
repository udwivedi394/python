def binarySubstring(string):
	n = 0

	for i in string:
		if i == '1':
			n += 1
	
	#return nCr(n,2)
	return n*(n+1)//2

def nCr(n,r):
	
	numerator = 1
	denominator = 1
	for i in range(n, max(n-r, r), -1):
		numerator *= i
	for j in range(1,min(n-r, r)+1):
		denominator *= j
	
	#print (numerator, denominator)

	return numerator//denominator

#print nCr(5,0)
print binarySubstring("001001011")
