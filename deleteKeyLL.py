class Node:
	def __init__(self,key):
		self.data=key
		self.next=None

def deletekeyLL(root, key):
	temp = root[0]
	prev_node = None

	while temp:
		if temp.data == key:
			if prev_node:
				prev_node.next = temp.next
			else:
				root[0] = temp.next
		else:
			prev_node = temp
		temp = temp.next
	return root[0]

def traverseLL(root):
	temp=root

	while temp:
		print temp.data,
		temp=temp.next
root=Node(2)
root.next=Node(2)
root.next.next=Node(1)
root.next.next.next=Node(8)
new = root.next.next.next.next=Node(2)
new.next=Node(3)
new.next.next=Node(2)
new.next.next.next=Node(7)

traverseLL(root)
check = [root]
deletekeyLL(check,2)
root = check[0]
print
traverseLL(root)
