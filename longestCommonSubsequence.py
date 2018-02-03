import time

delta = lambda x,y: x if x == y else ''
maxofarr = lambda x,y: x if len(x) > len(y) else y

#consider str1, str2 in the form of (aX, bY), where X and Y are last characters of strings, (a & b) are prefixes
def findLCS(str1, str2):
	if len(str1) == 0 or len(str2) == 0:
		return ''

	#check for (aX, b)
	arr1 = findLCS(str1, str2[:-1])

	#check for (a, bY)
	arr2 = findLCS(str1[:-1], str2)

	#check for (a, b), if x=y then add it existing string
	arr3 = findLCS(str1[:-1], str2[:-1]) + delta(str1[-1], str2[-1])

	return maxofarr(arr1, maxofarr(arr2, arr3))


#Dynamic Programming, (Memoization top to bottom approach)
def findLCS_02(str1, str2, edistDir = None):
	
	#If len of one of the string is zero, then no common substring, return blank
	if len(str1) == 0 or len(str2) == 0:
		return ''
	
	#Create a new directory if not present
	if edistDir == None:
		edistDir = {}

	#If subsolution of (str1, str2) present in lookup table then return the value
	if edistDir.get((str1, str2))!=None:
		return edistDir.get((str1, str2))

	#if last character of both string same then, call recursively for prefixes of str1, str2 and concatenate current character in it
	if str1[-1] == str2[-1]:
		return findLCS_02(str1[:-1], str2[:-1], edistDir) + str1[-1]

	#lookup in (a, bY)
	arr1 = findLCS_02(str1[:-1], str2, edistDir)
	#lookup in (aX, b)
	arr2 = findLCS_02(str1, str2[:-1], edistDir)

	#Save result in lookup table
	edistDir[(str1, str2)] = maxofarr(arr1, arr2)
	return edistDir[(str1, str2)]

#Dynamic Programming, Tabulation Method(Bottom to Top Approach)
#Fill the m*n matrix and find the result, Needs work
def findLCS_03(str1, str2):

	#There is no need to fill the matrix in this case	
	arr = [[0]*(len(str2)+1) for y in range(len(str1)+1)]

	
	lcs = ''
	main_list = []
	prev_j = -1
		
	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			#For the entire range of elements, we just need to check if the str1[i-1] == str2[j-1]
			#The secondary condition is, if current matching j is greater than prev_j
			#If yes, then append the current character to lcs, set prev_j = j
			#If No, then append the current lcs to main_list, set prev_j = j and reinitialize lcs = ''+str2[j-1]
			if str1[i-1] == str2[j-1]:
				arr[i][j] = 1
				if j > prev_j:
					prev_j = j
					lcs += str2[j-1]
				elif j == prev_j:
					pass
				else:
					prev_j = j
					main_list.append(lcs)
					lcs = str2[j-1]
	
	for i in range(len(str1)+1):
		print arr[i]
	
#	print "lcs:", lcs
#	print "main_list:", main_list
	return lcs			#Returns the current LCS
	
	#This part  of program returns all the LCS of same length in form of list
	final_list = [lcs]
	for temp_str in main_list:
		if len(temp_str) >= len(lcs):
			final_list.append(temp_str)
	return final_list
	
#Solution provided on GeeksforGeeks, it just returns the length of LCS
def findLCS_04(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in xrange(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

str1 = "AGGTAB"
str2 = "GXTXAAYB"
str3 = "GTAB"

print "actual:", findLCS(str1, str2), "expected:", str3

str1 = "ABCDGH"
str2 = "AEDFHR"
str3 = "ADH"

print "actual:", findLCS(str1, str2), "expected:", str3

str1 = "ABCDEFG"
str2 = "BCDGK"
str3 = "BCDG"

print "actual:", findLCS(str1, str2), "expected:", str3

str1 = "UTKARSH"
str2 = "SHWETA"
str3 = "SH"


str1 = "XMJYAUZ"
str2 = "MZJAWXU"
str3 = "MJAU"

t1 = time.time()
print "actual:", findLCS(str1, str2), "expected:", str3
t2 = time.time()
print t2-t1

t1 = time.time()
print "actual:", findLCS_02(str1, str2), "expected:", str3
t2 = time.time()
print t2-t1

str1 = "AGGTAAB"
str2 = "GXTXAYB"
str3 = "GTAB"

t1 = time.time()
print "actual:", findLCS_03(str1, str2), "expected:", str3
t2 = time.time()
print t2-t1

str1 = "UTKARSH"
str2 = "SHWETA"
str3 = "SH"

t1 = time.time()
print "actual:", findLCS_03(str1, str2), "expected:", str3
t2 = time.time()
print t2-t1

t1 = time.time()
print "actual:", findLCS_04(str1, str2), "expected:", str3
t2 = time.time()
print t2-t1

str1 = "abcda"
str2 = str1[::-1]
str3 = ''
print "actual:", findLCS_02(str1, str2), "expected:", str3
