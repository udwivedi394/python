class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

#this solution requires O(n) space complexity
def addgreatervalue(root):
	if root == None:
		return
	s1 = []
	val_array = []
	current = root
	done = False

	while not done:
		while current != None:
			s1.append(current)
			val_array.append(current.data)
			current = current.left

		if current == None and len(s1) > 0:
			current = s1.pop()
			current = current.right
	
		if current == None and len(s1) == 0:
			done = True

	print val_array
	val_array = sorted(val_array)
	print val_array
	print sum(val_array[val_array.index(60):])

	current = root
	done = False
	s1 = []
	while not done:
		while current != None:
			i = val_array.index(current.data)
			current.data += sum(val_array[i+1:])
			s1.append(current)
			current = current.left

		if current == None and len(s1) > 0:
			current = s1.pop()
			current = current.right

		if current == None and len(s1) == 0:
			done = True

#Make use of property of BST
#i.e., value greater than node lies only in right subtree
#Traverse in reverse manner, visit the rightmost first then keep on adding the value from there 
#add the sum to previous node
#then visit the left subtree
def addgreatervalueBST_02(node, sumi):
	
	if node == None:
		return
	
	addgreatervalueBST_02(node.right, sumi)
	
	sumi[0] += node.data
	node.data = sumi[0]
	
	addgreatervalueBST_02(node.left, sumi)


def inOrder(root):
	if root is None:
		return
	
	stack = []
	curNode = root
	done = 0

	while done==0:
		while curNode != None:
			stack.append(curNode)
			curNode = curNode.left

		if curNode == None and len(stack) > 0:
			curNode = stack.pop()
			print curNode.data,
			curNode = curNode.right
		
		if curNode == None and len(stack) == 0:
			done = 1

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

print
inOrder(root)

print
#addgreatervalue(root)
addgreatervalueBST_02(root, [0])

print
inOrder(root)


