import convertBT2LL as bT2DLL
#Time Complexity: O(n)
#Space Complexity: O(n)
def findSumPair01(root, k):
	stack = []
	temp = root

	inOrder = []
	#InOrder Traversal of BST and storing all the values in inOrder
	while 1:
		while temp:
			stack.append(temp)
			temp = temp.left

		while temp==None and len(stack):
			temp = stack.pop()
			
			inOrder.append(temp.data)
			temp = temp.right

		if temp==None and len(stack)==0:
			break
	
	#As the inOrder traversal of BST is always sorted, below approach can be used to search pair in O(n) time
	low = 0
	high = len(inOrder)-1

	while low < high:
		curSum = inOrder[low]+inOrder[high]
		if curSum == k:
			print "\nFound:",(inOrder[low],inOrder[high])
			return True
		elif curSum < k:
			low += 1
		else:
			high -= 1
	print "\nNot found!"
	return False

#Time Complexity: O(n)
#Space Complexity: O(1)
#But this approach modifies the original BST into DLL
def findSumPair02(root,k):
	#This function converts the BT into circular DLL inOrder fashion
	#Left Child equals to previous Node and right child points to next Node in DLL
	head = bT2DLL.convertBT2DLL(root)
	temp = head
	tail = head.left

	while temp!=tail:
		curSum = temp.data+tail.data

		if curSum == k:
			print "\nFound:",(temp.data,tail.data)
			return True
		elif curSum < k:
			temp = temp.right
		else:
			tail = tail.left
	print "\nNot found!"
	return False

#Time Complexity: O(n)
#Space Complexity: O(Log n), max size to be stored is the node in height of tree
def findSumPair03(root,k):
	#Reverse inOrder traversal of BST
	revStack = []
	fwdStack = []
	revtemp = root
	fwdtemp = root
	curLow = None
	curHigh = None
	inOrderNext = True
	revInOrderNext = True

	while 1:
		#Next element in InOrder traversal
		while inOrderNext:
			while fwdtemp:
				fwdStack.append(fwdtemp)
				fwdtemp = fwdtemp.left
			if len(fwdStack):
				fwdtemp = fwdStack.pop()
				curLow = fwdtemp.data
				fwdtemp = fwdtemp.right
			inOrderNext = False
		#Next element in Reverse InOrder traversal
		while revInOrderNext:	
			while revtemp:
				revStack.append(revtemp)
				revtemp = revtemp.right
			if len(revStack):
				revtemp = revStack.pop()
				curHigh = revtemp.data
				revtemp = revtemp.left
			revInOrderNext = False

		#If low+high = k, then return found
		if curLow+curHigh == k:
			print "\nFound:",(curLow,curHigh)
			return True
		#if current sum is less than sum required find next in InOrder Traversal
		elif curLow+curHigh < k:
			inOrderNext = True
		#if current sum is greater than sum required find next in revInOrder Traversal
		else:
			revInOrderNext = True
	
		#If any of the traversal is complete then terminate the loop
		if revtemp == None and len(revStack) == 0:
			break

		if fwdtemp == None and len(fwdStack) == 0:
			break
	print "Not found!"
	return False
