import time

num = 0
delta = lambda x,y: 1 if x != y else 0

#Naive Solution: Recursive algorithm
def editDistance(str1, str2):
	if len(str1) == 0:
		return len(str2)

	if len(str2) == 0:
		return len(str1)

	#print "(m,n):", (len(str1),len(str2))
	global num
	num += 1
	#recur m, n-1
	e1 = editDistance(str1, str2[:-1]) + 1
	#recur m-1, n
	e2 = editDistance(str1[:-1], str2) + 1
	#recur m-1, n-1
	e3 = editDistance(str1[:-1], str2[:-1]) + delta(str1[-1], str2[-1])
	
	return min(e1, e2, e3)

#Trying to fill the matrix recursively
def editDistance_02(str1, str2):
	m = len(str1)
	n = len(str2)
	
	#if m == 0:
	#	return n

	#if n == 0:
	#	return m
	
	e1 = editDisArr[m][n-1] 
	e2 = editDisArr[m-1][n] 
	e3 = editDisArr[m-1][n-1] 

	print "(m,n)", (m,n), "(e1, e2, e3)", (e1,e2,e3)
	#recur m, n-1 (ax->b) then Insertion of y
	if e1 == -1:
		e1 = editDistance_02(str1, str2[:-1]) + 1
		editDisArr[m][n-1] = e1
	
	#recur m-1, n (a->by) then Deletion of x
	if e2 == -1:
		e2 = editDistance_02(str1[:-1], str2) + 1
		editDisArr[m-1][n] = e2
	
	#recur m-1, n-1, (a->b) then Substitution of x with y if x!=y
	if e3 == -1:
		print "In", delta(str1[-1], str2[-1])
		#e3 = editDistance_02(str1[:-1], str2[:-1]) + delta(str1[-1], str2[-1])
		if str1[:-1] == str2[:-1]:
			e3 = 0
		else:
			e3 = editDistance_02(str1[:-1], str2[:-1]) + delta(str1[-1], str2[-1])	
		editDisArr[m-1][n-1] = e3

	editDisArr[m][n] = min(e1, e2, e3)
	return editDisArr[m][n]

#Trying to make a dictionary with all the calls and use them subsequently
#Memoization(Top Down), lookup into the lookup table before computing the data using recursive approach
#Working Now
def editDistance_03(str1, str2):
	m = len(str1)
	n = len(str2)
	
	if m == 0: return n
	if n == 0: return m
		
	if (m,n) in editDistDir:
		return editDistDir.get((m,n))
	
	#print
	#print "m:", m,"n:", n, editDistDir
	
	#recur m-1, n-1, Diagonal
	#e3 = editDistDir.get((m-1,n-1))
	#if e3 == None:
	e3 = editDistance_03(str1[:-1], str2[:-1]) + delta(str1[-1], str2[-1])
	#editDistDir[(m-1,n-1)] = e3
	
	#recur m-1, n, vertical
	#e2 = editDistDir.get((m-1,n))
	#if e2 == None:
	e2 = editDistance_03(str1[:-1], str2) + 1
	#editDistDir[(m-1,n)] = e2
	
	#recur m, n-1, horizontal
	#e1 = editDistDir.get((m,n-1))
	#if e1 == None:
	e1 = editDistance_03(str1, str2[:-1]) + 1
	#editDistDir[(m,n-1)] = e1
	
	editDistDir[(m,n)] = min(e1, e2, e3)
	#print "(m,n):", (m, n), "(str1, str2):", (str1, str2), "e1,e2,e3:", (e1,e2,e3), "min:", editDistDir[(m,n)]

	return editDistDir[(m,n)]


#Final Solution: Pure Dynamic Programming
#Fill the matrix bottom to top to reach to the result, (Tabulation, bottom up)
def editDistance_04(str1, str2):
	m = len(str1)
	n = len(str2)

	#Create an empty matrix of (m+1)*(n+1)
	dp = [[0 for x in range(n+1)] for y in range(m+1)]

	#Fill the first column with respective row_num
	for i in range(m+1):
		dp[i][0] = i

	#Fill the first row with respective col_num
	for j in range(n+1):
		dp[0][j] = j

	#go for full range of matrix, and filling them using minimum of three possible operations
	for i in range(m+1):
		for j in range(n+1):
			#Insertion, (aX->b)
			distHor = dp[i][j-1] + 1

			#Deletion, (a->bY)
			distVer = dp[i-1][j] + 1

			#Substitution 
			distDiag = dp[i-1][j-1] + delta(str1[i-1], str2[j-1])

			#select the minimum cost of three available option
			dp[i][j] = min(distHor, distVer, distDiag)

	return dp[m][n]

def editDistance_05(str1, str2, memo=None):
	if memo is None: memo = {}

	if len(str1) == 0: return len(str2)
	if len(str2) == 0: return len(str1)

	if (len(str1), len(str2)) in memo:
		return memo[(len(str1), len(str2))]

	horz = editDistance_05(str1, str2[:-1], memo) + 1
	vert = editDistance_05(str1[:-1], str2, memo) + 1
	diag = editDistance_05(str1[:-1], str2[:-1], memo) + delta(str1[-1], str2[-1])
	
	ans = min(horz, vert, diag)
	memo[(len(str1), len(str2))] = ans 
	return ans

str1 = "sunday"
str2 = "saturday"
"""
t1 = time.time()
#print editDistance(str1, str2)
t2 = time.time()
print t2-t1
print num
"""
"""
t1 = time.time()
editDisArr = [[-1 for x in range(len(str2)+1)] for y in range(len(str1)+1)]

for i in range(len(str1)+1):
	editDisArr[i][0] = i

for j in range(len(str2)+1):
	editDisArr[0][j] = j


print editDistance_02(str1, str2)
print ' ',[' ']+list(str2)
for i in range(len(str1)+1):
	if i!=0:
		print str1[i-1], editDisArr[i]
	else:
		print ' ',editDisArr[i]
t2 = time.time()
print t2-t1
#print editDisArr
"""
"""
t1 = time.time()
print editDistance_04(str1, str2)
t2 = time.time()
print editDistDir
print t2-t1
print num
"""
editDistDir = {}
t1 = time.time()
print editDistance_03(str1, str2)
t2 = time.time()
print t2-t1
print editDistDir
