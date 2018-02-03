def upgradeMid(new_num):
	mid = len(new_num)//2
	update = False
	
	even = 0
	if len(new_num)%2 == 0:
		even = 1
	
	i=0
	while new_num[mid-even-i] == 9 or new_num[mid+i] == 9:
		new_num[mid-even-i] = 0
		new_num[mid+i] = 0
		i += 1
		update = True
	if update:
		new_num[mid-even-i] += 1
		new_num[mid+i] += 1
	else:
		if even:
			new_num[mid-1] += 1
			new_num[mid] += 1
		else:
			new_num[mid] += 1

def nextPalindrome03(num):
	if len(num)*9 == sum(num):
		new_num = [0 for i in range(len(num)+1)]
		new_num[0] = new_num[-1] = 1
		return new_num
	
	even = 0
	if len(num)%2:
		even = 1
		
	mid = len(num)//2
	new_num = []+num
	i = mid-1
	j = mid+even

	palindrome = True
	while i>=0 and j<len(num):
		if new_num[i] == new_num[j]:
			i -= 1
			j += 1
		else:
			palindrome = False
			break
	
	if palindrome:
		upgradeMid(new_num)
		return new_num
	
	#Flag to check whether the left digit just after palindrome part is greater than right counter part
	less = False
	if new_num[i] < new_num[j]:
		less = True

	while i>=0 and j<len(num):
		new_num[j] = new_num[i]
		i -= 1
		j += 1

	if less:
		upgradeMid(new_num)
	return new_num

arr1 = [2,3,5,4,5]	#Correct
arr2 = [1,2,3,4]	#Correct now
arr3 = [1,2,2,1]	#Correct
arr4 = [9,9,9,9]	#Correct
arr5 = [9,9,9,9,9]	#Correct
arr6 = [9,4,1,8,7,9,7,8,3,2,2]	#Correct result, odd
arr7 = [9,4,1,8,9,9,7,8,3,2]	#Correct
arr8 = [1,4,5,8,7,6,7,8,3,2,2]	#Correct
arr9 = [1,2,9,2,1]	#Correct now
arr10 = [7,8,3,3,2,2]	#Correct
arr11 = [1,2,5,3,2,2]	#Correct

print nextPalindrome03(arr1)
print nextPalindrome03(arr2)
print nextPalindrome03(arr3)
print nextPalindrome03(arr4)
print nextPalindrome03(arr5)
print "9 4 1 8 8 0 8 8 1 4 9",nextPalindrome03(arr6)
print "9 4 1 8 9 9 8 1 4 9", nextPalindrome03(arr7)
print "1 4 5 8 7 6 7 8 5 4 1,", nextPalindrome03(arr8)
print "1 3 0 3 1,",nextPalindrome03(arr9)
print "7 8 3 3 8 7,",nextPalindrome03(arr10)
print "1 2 5 5 2 1,",nextPalindrome03(arr11)
print "1 4 5 8 7 6 7 8 5 4 1,", nextPalindrome03(arr8)
