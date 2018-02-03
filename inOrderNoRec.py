class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

def inOrder2(root):
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

inOrder2(root)
