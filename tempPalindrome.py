def nextPalindrome(num):
	if len(num)*9 == sum(num):
		new_num = [0 for i in range(len(num)+1)]
		new_num[0] = new_num[-1] = 1
		return new_num

	if len(num)%2 == 1:	
		mid = len(num)//2
		new_num = num[:mid+1]+num[:mid][::-1]
		new_num[mid] += 1
	else:
		mid = len(num)//2
		new_num = num[:mid]+num[:mid][::-1]
		new_num[mid] += 1
		new_num[mid-1] += 1
	return new_num

def nextPalindrome02(num):
	if len(num)*9 == sum(num):
		new_num = [0 for i in range(len(num)+1)]
		new_num[0] = new_num[-1] = 1
		return new_num

	if len(num)%2 == 1:	
		mid = len(num)//2
		new_num = num[:mid+1]+num[:mid][::-1]
		temp = [new_num[i]-num[i] for i in range(len(num))]
		#print "New Temprary", temp

		i = 0
		while new_num[mid-i] == 9 or new_num[mid+i] == 9:
			new_num[mid-i] = 0
			new_num[mid+i] = 0
			i += 1

		new_num[mid-i] += 1
		new_num[mid+i] += 1

	else:
		mid = len(num)//2
		new_num = num[:mid]+num[:mid][::-1]
		i = 0
		print
		print "This is me", new_num
		while new_num[mid-1-i] == 9 or new_num[mid+i] == 9:
			print "Going In"
			new_num[mid-1-i] = 0
			new_num[mid+i] = 0
			i += 1
		new_num[mid+i] += 1
		new_num[mid-1-i] += 1
	return new_num

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

	if len(num)%2:	
		mid = len(num)//2
		new_num = []+num
		i = mid-1
		j = mid+1

		#Flag to check whether the left digit just after palindrome part is greater than right counter part
		less = False
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

		if new_num[i] < new_num[j]:
			less = True

		while i>=0 and j<len(num):
			new_num[j] = new_num[i]
			i -= 1
			j += 1

		#print new_num
		if less:
			upgradeMid(new_num)
	#	return new_num
	else:
		mid = len(num)//2
		new_num = []+num
		i = mid-1
		j = mid

		palindrome=True
		while i>=0 and j<len(num):
			if new_num[i] == new_num[j]:
				i -= 1
				j += 1
			else:
				palindrome=False
				break
		
		if palindrome:
			new_num[mid-1] += 1
			new_num[mid] += 1
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
