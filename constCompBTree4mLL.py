import printBinaryTree as bT

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

def constructBTreefromLL(llroot):
	if llroot==None:
		return None
	#Create the first Node of binary Tree from Ist node of LinkedList
	root = bT.bTree(llroot.data)
	temp = llroot.next
	#Initialize the queue with first node of bTree
	queue = [root]

	#While the linked list is exhausted
	while temp:
		#Count number of nodes in current level
		n = len(queue)
		#Max number of children in level can be pow(2,n)
		#However, the loop will go for pow(2,n)/2 or pow(2,n-1)
		#Because, we are assigning the left and right child in 1 iteration
		n = 2**(n-1)
		while n:
			node = queue.pop(0)	
			if temp:
				node.left = bT.bTree(temp.data)
				temp = temp.next
				queue.append(node.left)
			else:
				break
			if temp:
				node.right = bT.bTree(temp.data)
				temp = temp.next
				queue.append(node.right)
			else: 
				break
			n -= 1
	return root

ll = Node(10)
ll.next = Node(12)
ll.next.next = Node(15)
ll.next.next.next = Node(25)
ll.next.next.next.next = Node(30)
ll.next.next.next.next.next = Node(36)
ll.next.next.next.next.next.next = Node(38)
ll.next.next.next.next.next.next.next = Node(40)

root = constructBTreefromLL(ll)
bT.levelOrder(root)
