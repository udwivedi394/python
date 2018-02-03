class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

def deleteNodeWithGreatRight(root):
	prev_node=root
	temp=root

	while temp:
		if temp.next:
			if temp.data < temp.next.data:
				if prev_node == temp:
					if prev_node == root:
						root = temp.next
					prev_node = temp.next
					
				else:
					prev_node.next = temp.next
			else:
				prev_node = temp
		temp = temp.next

	return root

def traverseLL(root):
	temp = root
	while temp:
		print temp.data,"->",
		temp = temp.next
	print "None"


root = Node(12)
root.next = Node(15)
root.next.next = Node(10)
root.next.next.next = Node(11)
root.next.next.next.next = Node(5)
temp =root.next.next.next.next.next = Node(6)
temp.next = Node(2)
temp.next.next = Node(3)

root = Node(10)
root.next = Node(20)
root.next.next = Node(30)
root.next.next.next = Node(40)
root.next.next.next.next = Node(50)
temp =root.next.next.next.next.next = Node(60)
#temp.next = Node(2)
#temp.next.next = Node(3)

root = Node(60)
root.next = Node(50)
root.next.next = Node(40)
root.next.next.next = Node(30)
root.next.next.next.next = Node(20)
temp =root.next.next.next.next.next = Node(10)
temp.next = Node(8)
temp.next.next = Node(5)

print "Before Deleting:",
traverseLL(root)
root = deleteNodeWithGreatRight(root)
print "After Deleting:",
traverseLL(root)
