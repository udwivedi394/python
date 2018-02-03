class Node:
	def __init__(self, key):
		self.data = key
		self.next = None

#This function merges two already LinkedLists,clean and iterative
#This is a recursive function, there stack size is directly proportional to length of LL
def mergeLL(ll1, ll2):
	if ll1 == None:
		return ll2
	if ll2 == None:
		return ll1

	if ll1.data <= ll2.data:
		ll1.next = mergeLL(ll1.next, ll2)
		cur_node = ll1

	if ll1.data > ll2.data:
		ll2.next = mergeLL(ll1, ll2.next)
		cur_node = ll2

	return cur_node


#Non Recursive Approach, O(n) solution, with O(1) space
def mergeLL2(ll1, ll2):
	if ll1 == None:
		return ll2
	if ll2 == None:
		return ll1
	
	temp_ll1 = ll1
	temp_ll2 = ll2

	while temp_ll1 and temp_ll2:
		if temp_ll1.data <= temp_ll2.data:
			new_ll = temp_ll1.next
			temp_ll1.next = temp_ll2
			temp_ll1 = new_ll

		elif temp_ll1.data > temp_ll2.data:
			new_ll = temp_ll2.next
			temp_ll2.next = temp_ll1
			temp_ll2 = new_ll
	
	if ll1.data < ll2.data:
		return ll1
	return ll2

def traverseLL(root):
	temp = root
	while temp:
		print temp.data,"->",
		temp = temp.next

	print "NULL"

root1 = Node(1)
root1.next = Node(3)
root1.next.next = Node(5)
root1.next.next.next = Node(7)

root2 = Node(2)
root2.next = Node(4)
root2.next.next = Node(6)
root2.next.next.next = Node(8)

traverseLL(root1)
traverseLL(root2)
#new_root = mergeLL(root2,root1)
#new_root = mergeLL(None,root2)
#traverseLL(new_root)
new_root = mergeLL2(root1,root2)
traverseLL(root1)
