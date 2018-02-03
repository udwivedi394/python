class bTree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		self.nextRight = None

def connectNodeatSameLevel(root):
	queue = [root]

	while len(queue):
		n = len(queue)
		prevNode = None
		while n:
			temp = queue.pop(0)

			if temp.left:
				queue.append(temp.left)
			
			if temp.right:
				queue.append(temp.right)
			
			if prevNode:
				prevNode.nextRight = temp
			prevNode = temp
			n -= 1
	return root

def llTraversal(root):
	temp = root
	while temp:
		print temp.data,"->",
		temp = temp.nextRight
	print "None"

root = bTree('A')
root.left = bTree('B')
root.left.left = bTree('D')
root.left.right = bTree('E')
root.right = bTree('C')
root.right.right = bTree('F')

root2 = bTree(1)
root2.left = bTree(2)
root2.left.left = bTree(4)
root2.left.left.left = bTree(8)
root2.left.left.right = bTree(9)
root2.left.right = bTree(5)
root2.right = bTree(3)
root2.right.left = bTree(6)
root2.right.right = bTree(7)
root2.right.left = bTree(10)
root2.right.right.left = bTree(10)
root2.right.right.right = bTree(11)

connectNodeatSameLevel(root2)
llTraversal(root2.left)
llTraversal(root2.left.left)
llTraversal(root2.left.left.left)
