class Node:
	def __init__(self,data):
		self.data = data
		self.right = None
		self.down = None

#This solution uses, O(n) space complexity and only provides sorted linkedlist
def flatteningLL(root, n=None):
	if root == None:
		return None

	temp_left = root
	if root.right:
		temp_right = flatteningLL(root.right)
	else:
		return root

	temp_new = None

	#Merging the left and right list in correct order
	while temp_left and temp_right:
		if temp_left.data <= temp_right.data:
			if temp_new == None:
				temp_root = temp_new = Node(temp_left.data)
			else:
				temp_new.down = Node(temp_left.data)
				temp_new = temp_new.down
			temp_left = temp_left.down

		else:
			if temp_new == None:
				temp_root = temp_new = Node(temp_right.data)
			else:
				temp_new.down = Node(temp_right.data)
				temp_new = temp_new.down
			temp_right = temp_right.down
			
	while temp_left:
		if temp_new == None:
			temp_root = temp_new = Node(temp_left.data)
		else:
			temp_new.down = Node(temp_left.data)
			temp_new = temp_new.down
		temp_left = temp_left.down

	while temp_right: 
		if temp_new == None:
			temp_root = temp_new = Node(temp_right.data)
		else:
			temp_new.down = Node(temp_right.data)
			temp_new = temp_new.down
		temp_right = temp_right.down
		
	return temp_root

#Merge the two linked list, such that right one comes after the small one
def mergeLL(leftLL, rightLL):
	if leftLL:
		leftLL.right = None

	if rightLL and leftLL == None:
		return rightLL
	
	if rightLL == None and leftLL:
		return leftLL

	if leftLL.data <= rightLL.data:
		result = leftLL
		leftLL.down = mergeLL(leftLL.down, rightLL)
	else:
		result = rightLL
		rightLL.down = mergeLL(leftLL, rightLL.down)	
	
	return result

#Actual Function, it rearranges the linked list in sorted order.
#No extra space
def flattenLL(root):
	if root == None or root.right == None:
		return root

	return mergeLL(root, flattenLL(root.right))

#if down=True, traverse in downward direction
#if down=False, traverse in right direction
def traverseLL(root, down=False):
	temp = root

	while temp:
		print temp.data,'->',
		if down:
			temp = temp.down
		else:
			temp = temp.right
	print "None"

root = Node(5)
root.down = Node(7)
root.down.down = Node(8)
root.down.down.down = Node(30)

second = root.right = Node(10)
second.down = Node(20)

third = second.right = Node(19)
third.down = Node(22)
third.down.down = Node(50)

fourth = third.right = Node(28)
fourth.down = Node(35)
fourth.down.down = Node(40)
fourth.down.down.down = Node(45)

#flattend = flatteningLL(root)
#traverseLL(flattend,True)
#traverseLL(root)

flattenLL(root)
traverseLL(root, True)
