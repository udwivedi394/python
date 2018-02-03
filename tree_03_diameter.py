class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

#determine height of tree
def heightTree(node):
	if node == None:
		return 0
	
	return 1 + max(heightTree(node.left), heightTree(node.right))
	
#determine the diameter of tree, with help of heightTree function
def diameterTree(node):
	if node == None:
		return 0

	lheight = rheight = 0

	lheight = heightTree(node.left)
	rheight = heightTree(node.right)
	
	#print (lheight+rheight+1, lheight, rheight)
	
	ldiameter = diameterTree(node.left)
	rdiameter = diameterTree(node.right)

	return max(lheight+rheight+1, max(ldiameter, rdiameter))

#determine the diameter of tree by determining height of tree in same function
def diameterTree2(root, height):
	if root == None:
		height[0] = 0
		return 0

	lheight = [0]
	rheight = [0]

	ldiameter = diameterTree2(root.left, lheight)
	rdiameter = diameterTree2(root.right, rheight)

	height[0] = max(lheight[0],rheight[0])+1 
	
	return max(lheight[0]+rheight[0]+1, max(ldiameter, rdiameter))

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
#root.left.right.right.right = Node(12)
root.left.right.right.right = Node(13)
root.left.left.right.left.left = Node(14)
root.left.left.right.left.right = Node(15)
root.left.right.right.right.right = Node(16)

#print heightTree(root,0)
#print diameterTree(root, 0)
"""
print heightTree(root)
print heightTree(root.left)
print heightTree(root.right)
"""
print diameterTree(root)

print diameterTree2(root, [0])
