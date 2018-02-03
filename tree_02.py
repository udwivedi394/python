class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

#inOrder Traversal(left, root, right)
def inOrder(node):
	if node == None:
		return

	if node.left != None:
		inOrder(node.left)

	print node.data,

	if node.right != None:
		inOrder(node.right)


#preOrder Traversal(root, left, right)
def preOrder(node):
	if node == None:
		return

	print node.data,

	if node.left != None:
		preOrder(node.left)
	
	if node.right != None:
		preOrder(node.right)

#postOrder Traversal (left, right, root)
def postOrder(node):
	if node == None:
		return

	if node.left != None:
		postOrder(node.left)

	if node.right != None:
		postOrder(node.right)

	print node.data,

#levelOrder Traversal
def levelOrder(root):
	tempNode = root
	
	queue = []

	while tempNode != None:
		print tempNode.data,

		if tempNode.left != None:
			queue.append(tempNode.left)

		if tempNode.right != None:
			queue.append(tempNode.right)

		if len(queue) > 0:
			tempNode = queue.pop(0)

		else:
			tempNode = None

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

print "InOrder"
inOrder(root)

print
print "preOrder"
preOrder(root)

print
print "postOrder"
postOrder(root)

print
print "LevelOrder"

levelOrder(root)
