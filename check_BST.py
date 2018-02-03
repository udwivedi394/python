INT_MAX = 4294967296
INT_MIN =-4294967296

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

def check_bst_01(node, key):
	if node == None:
		return

	if node.left != None and node.left.data >= node.left and node.left >= key:
		return -1

	elif node.left != None:
		return check_bst_01(node.left, key)
	pass

def isBST(root, prev):
	if (root != None):
		if (isBST(root.left, prev) == False):
			return False

		if (prev[0] != None and root.data <= prev[0].data):
			return False
		
		prev = [root]
		return isBST(root.right, prev)
	return True	


#Calls check_bst_02_util for additional arguments
def check_bst_02(node):
	return check_bst_02_util(node, INT_MIN, INT_MAX)


def check_bst_02_util(node, mini, maxi):
	if node is None:
		return True
	
	#if current value greater upper bound and lesset than lower bound return False
	if node.data < mini or node.data > maxi:
		return False

	#apply the constraints
	#upper bound for left subtree should be less than current value
	#similarly for right subtree, the lower bound should be greater than current value 
	return (check_bst_02_util(node.left, mini, node.data-1) and
		check_bst_02_util(node.right, node.data+1, maxi))

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

prev = [None]
print isBST(root, prev)

print check_bst_02(root)
