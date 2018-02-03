class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

class QueueNode:
	def __init__(self, node):
		self.node = node
		self.next = None

class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
	
	def enQueue(self, node):
		if self.front is None:
			self.front = QueueNode(node)
			self.rear = self.front
			return
		self.rear.node.next = QueueNode(node)
		self.rear = self.rear.node.next

	def deQueue(self):
		if self.front is None:
			print("Queue Empty!")
			return None


		retNode = self.front.node
		
		if self.front == self.rear:
			self.front = self.rear = None
		else:
			self.front = self.front.node.next

		return retNode

#inOrder(left, root, right)
def inOrder(node):
	if node is None:
		return

	if node.left != None:
		inOrder(node.left)

	print node.data,

	if node.right != None:
		inOrder(node.right)
	return

#LevelOder Traversal
def levelOrder(root):
	tempNode = root

	queue1 = Queue()

	while tempNode != None:
		print tempNode.data,
		
		if tempNode.left != None:
			queue1.enQueue(tempNode.left)

		if tempNode.right != None:
			queue1.enQueue(tempNode.right)

		tempNode = queue1.deQueue()


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

inOrder(root)

print "levelOrder"
levelOrder(root)
