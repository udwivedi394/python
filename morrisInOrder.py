class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

def morris_inorder_traversal(root):
	current = root

	while current != None:
		#if left subtree NA, print data of current node and visit right subtree
		if current.left == None:
			print current.data, 
			current = current.right

		else:
		#initialise the predecessor as current.left subtree
			predecessor = current.left
		#visit the rightmost node of the right of left subtree, limiting condition whether rightchild of node points to NULL or current itself
			while predecessor.right != None and predecessor.right != current:
				predecessor = predecessor.right

		#if predecessor.right is None, means it has been visited set it to current
			if predecessor.right == None:
				predecessor.right = current
				current = current.left

		#else it has been already visited, break the chain assign it None, print current.data, go to right subtree of current node
			else:
				predecessor.right = None
				print current.data, 
				current = current.right
				#print predecessor.data,

def morris_pre_order_traversal(root):
	current = root
	
	while current != None:

		if current.left == None:
			print current.data,
			current = current.right

		else:
			predecessor = current.left
			
			while predecessor.right != None and predecessor.right != current:
				predecessor = predecessor.right

			if predecessor.right == None:
				print current.data,
				predecessor.right = current
				current = current.left
				
			else:
				predecessor.right = None
				current = current.right

#Not working, replica of inOrder_traversal
def morris_post_order_traversal(root):
	current = root
	while current != None:
		
		if current.left == None:
			print current.data,
			current = current.right

		else:
			predecessor = current.left
			
			while predecessor.right != None and predecessor.right != current:
				predecessor = predecessor.right

			if predecessor.right == None:
				predecessor.right = current
				current = current.left
			else:
				print current.data,
				predecessor.right = None
				current = current.right
#in order traversal without recursion
def inOrder(root):
	s1 = []
	current = root
	done = 0
	#s1.append(root)
	while done == 0:
		
		while current != None:
			s1.append(current)
			current = current.left

		if current == None and len(s1) > 0:
			current = s1.pop()
			print current.data,
			current = current.right

		if current == None and len(s1) == 0:
			done = 1

#preOrder traversal without recursion
def preOrder(root):
	s1 = []
	current = root
	done = 0
	while done == 0:
		while current != None:
			print current.data,
			s1.append(current)
			current = current.left

		if current == None and len(s1) > 0:
			current = s1.pop()
			current = current.right

		if current == None and len(s1)==0:
			done = 1

#postOrder traversal 
def postOrder(root):
	s1 = []
	s2 = []
	current = root
	s1.append(current)

	while len(s1) > 0:
		current = s1.pop()
		s2.append(current)
		
		if (current.left != None):
			s1.append(current.left)

		if (current.right != None):
			s1.append(current.right)

	while len(s2) > 0:
		print s2.pop().data,

def postOrder_iterative(root):
	current = root
	s1 = []
	s2 = []

	s1.append(root)
	
	while len(s1) > 0:
		node = s1.pop()
		s2.append(node)
		
		if (node.left != None):
			s1.append(node.left)
		if (node.right != None):
			s1.append(node.right)
		
	for i in s2[::-1]:
		print i.data,

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(7)
root.left.left.right = Node(8)
root.left.right.right = Node(9)
root.left.left.right.left = Node(10)
root.left.right.right.left = Node(11)
root.left.right.right.right = Node(12)
root.left.right.right.right = Node(13)
root.left.left.right.left.left = Node(14)
root.left.left.right.left.right = Node(15)
root.left.right.right.right.right = Node(16)

morris_inorder_traversal(root)
print
morris_inorder_traversal(root)
print
morris_pre_order_traversal(root)
print
morris_inorder_traversal(root)

print
morris_post_order_traversal(root)

print
#postOrder_iterative(root)

print 
preOrder(root)

print
postOrder(root)
