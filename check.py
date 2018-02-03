
def editDistance(str1, str2):
	m = len(str1)
	n = len(str2)
	
	if m == 0:
		return n

	if m == 0:
		return n
		
	#recur m, n-1
	e1 = editDisArr[m][n-1] 
	if e1 == -1:
		e1 = editDistance(str1, str2[:-1]) + 1
		editDisArr[m][n-1] = e1
	#recur m-1, n
	e2 = editDisArr[m-1][n] 
	if e2 == -1:
		e2 = editDistance(str1[:-1], str2) + 1
		editDisArr[m-1][n] = e2
	#recur m-1, n-1
	e3 = editDisArr[m-1][n-1] 
	if e3 == -1:
		e3 = editDistance(str1[:-1], str2[:-1]) + delta(str1[-1], str2[-1])
		editDisArr[m-1][n-1] = e3

	return min(e1, e2, e3)
