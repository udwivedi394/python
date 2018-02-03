#Create a Node for tree, it will store the data as well as frequency
class Node:
	def __init__(self, freq):
		self.data = None
		self.freq = freq
		self.left = None
		self.right = None

#LevelOrder traversal of Tree
def levelOrder(root):
	tempNode = root
	queue = []

	while tempNode != None:
		print (tempNode.data,tempNode.freq),

		if tempNode.left != None:
			queue.append(tempNode.left)

		if tempNode.right != None:
			queue.append(tempNode.right)

		if len(queue) > 0:
			tempNode = queue.pop(0)

		else:
			tempNode = None
	print

#Print the Huffman Codes of all the data
def printOrder(node, arr=''):
	if node.left != None:
		printOrder(node.left, arr+'0')
	
	if node.right != None:
		printOrder(node.right, arr+'1')
	
	if node.left == None and node.right == None:
		print (node.data, node.freq, arr)

#Generate the Huffman Tree
def huffmanTree(arr, freq):
	i=1
	#Loop until the no. of elements in Freq array are greater than 1
	while len(freq) > 1:
		#Greedy Approach: Get two elements with minimum frequency
		#Get index of min element in frequency
		index = freq.index(min(freq))

		#Check if the element at arr[index] is an object of Node class
		if isinstance(arr[index], Node):
			#Pop the object at index in arr and assign the reference of the object to node1
			node1 = arr.pop(index)
			#Pop the frequency at index as it is already stored in node1.freq
			freq.pop(index)
		else:
			#Otherwise, create a new leaf node, pop the data at frequency[index] and initialize the Node object
			node1 = Node(freq.pop(index))
			#Populate the leaf data with character at arr[index]
			node1.data = arr.pop(index)

		#Repeat the same process as above for second minimum element
		index = freq.index(min(freq))
		if isinstance(arr[index], Node):
			node2 = arr.pop(index)
			freq.pop(index)
		else:
			node2 = Node(freq.pop(index))
			node2.data = arr.pop(index)

		#Create a new node, initialize with addition of frequency of node1 & node2
		node3 = Node(node1.freq+node2.freq)

		#Populate the data with Ni
		node3.data = 'N'+str(i)

		#Attach 1st min to left of node3 and 2nd min to right of node3
		node3.left = node1
		node3.right = node2
		
		#Insert the node3 frequency in freq arr at 0
		freq.insert(0, node3.freq)

		#Insert the node3 in arr at 0
		arr.insert(0, node3)
		i += 1
	
	return node3

arr = ['a','b','c','d','e','f']
#Frequency of corresponding elements in arr
freq= [5,9,12,13,16,45]

root = huffmanTree(arr, freq)
levelOrder(root)
printOrder(root)
