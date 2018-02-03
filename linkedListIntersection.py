class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


#Given two linked list
#Naive Solution, Complexity O(mn)
def linkedListIntersection(ll1, ll2):
	#For 1st linked list, traverse through nodes
	while ll1!=None:
		temp = ll2
		#Now tranverse through the second LL, from the beginning
		while temp!=None:
			if temp.next == ll1.next:
				if temp.next == None:
					print "No common link"
					return False
				else:
					print "Found Common link: ", temp.next.data
					return True
			temp = temp.next
		ll1 = ll1.next
	return False

#Using Hash-Map(Dictionary) for storing of address of visited nodes
#Time Complexity: O(m+n)
def linkedListIntersection02(ll1, ll2):
	lookup_dict = {}
	temp1 = ll1
	temp2 = ll2

	while temp1 != None and temp2!=None:
		if lookup_dict.get(temp1):
			print "Link Found at", temp1.data
			return True
		else:
			lookup_dict[temp1] = 1
		temp1 = temp1.next

		if lookup_dict.get(temp2):
			print "Link Found at", temp2.data
			return True
		else:
			lookup_dict[temp2] = 1
		temp2 = temp2.next

	while temp1 != None:
		if lookup_dict.get(temp1):
			print "Link Found at", temp1.data
			return True
		else:
			lookup_dict[temp1] = 1
		temp1 = temp1.next

	while temp2 != None:
		if lookup_dict.get(temp2):
			print "Link Found at", temp2.data
			return True
		else:
			lookup_dict[temp2] = 1
		temp2 = temp2.next
		
	print "No common Link"
	return False

#count the nodes in both linkedList. From bigger LL, tranverse the difference abs(count1-count2)
#Time complexity: O(m+n), Space Complexity: O(1)
def linkedListIntersection03(ll1, ll2):
	temp1 = ll1
	temp2 = ll2
	
	count1 = 0
	count2 = 0

	while temp1!=None:
		count1 += 1
		temp1 = temp1.next

	while temp2!=None:
		count2 += 1
		temp2 = temp2.next

	temp1 = ll1
	temp2 = ll2

	if count1 > count2:
		i = 0
		while i < count1-count2:
			temp1 = temp1.next
			i += 1
	else:
		i = 0
		while i < count2-count1:
			temp2 = temp2.next
			i += 1
	
	while temp1 != None and temp2 != None:
		if temp1.next == temp2.next:
			print "Link found:", temp1.next.data
			return True
		temp1 = temp1.next
		temp2 = temp2.next
	print "Link not found"
	return False

root1 = Node(3)
root1.next = Node(6)
root1.next.next = Node(9)
root1.next.next.next = Node(15)
root1.next.next.next.next = Node(30)

root2 = Node(10)
root2.next = root1.next.next.next

root3 = Node(20)
root3.next = Node(25)
root3.next.next = Node(35)

linkedListIntersection(root1, root2)
linkedListIntersection02(root1, root2)
linkedListIntersection03(root1, root2)
