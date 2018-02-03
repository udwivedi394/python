class Node:
	def __init__(self, coeff, degree):
		self.coeff = coeff
		self.degree = degree
		self.next = None

def createNode(linkedList, coeff, degree):
	new_node = Node(coeff, degree)

	if (linkedList == None):
		return new_node
	
	tempNode = linkedList
	while tempNode.next != None:
		tempNode = tempNode.next
	
	tempNode.next = new_node
	return linkedList

def addPolynomial(linked_list1, linked_list2):
	if linked_list1 == None:
		return linked_list2

	if linked_list2 == None:
		return linked_list1
	
	tempNode1 = linked_list1
	tempNode2 = linked_list2
	newLL = None

	while tempNode1 or tempNode2:
		if tempNode1.degree == tempNode2.degree:
			newLL = createNode(newLL, tempNode1.coeff+tempNode2.coeff, tempNode1.degree)
			tempNode1 = tempNode1.next
			tempNode2 = tempNode2.next

		elif tempNode1.degree > tempNode2.degree:
			newLL = createNode(newLL, tempNode1.coeff, tempNode1.degree)	
			tempNode1 = tempNode1.next

		else:
			newLL = createNode(newLL, tempNode2.coeff, tempNode2.degree)
			tempNode2 = tempNode2.next
	return newLL

def traverseLL(root):
	tempNode = root
	while tempNode != None:
		print tempNode.coeff, tempNode.degree
		tempNode = tempNode.next


ll1 = createNode(None, 5, 3)
createNode(ll1, 4, 2)
createNode(ll1, 2, 0)

ll2 = createNode(None, 5, 1)
#createNode(ll2, 4, 2)
createNode(ll2, 5, 0)

ll3 = addPolynomial(ll1, ll2)
traverseLL(ll3)
