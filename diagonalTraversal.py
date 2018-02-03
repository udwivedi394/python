class bTree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def diagonalTraversal(root):
	#Initialize the hashmap with root as initial entry and 0 as slope
	hashmap = {0: [root.data]}

	#Initialize the queue with first node as [slope_val, node]
	queue = [[0, root]]

	#To count the number of levels in the tree, to be used later as.. 
	#..means of printing the diagonals from hashmap
	levels = 0

	while len(queue):
		#gives the number of nodes at current level
		n = len(queue)
		
		while n:
			node = queue.pop(0)
			val = node[0]
			temp = node[1]

			#for left child, the data gets appended to current_slope+1 value in hashmap
			if temp.left:
				if hashmap.get(val+1)==None:
					hashmap[val+1] = [temp.left.data]
				else:
					hashmap[val+1].append(temp.left.data)
				queue.append([val+1, temp.left])

			#for right child, the data is appended to same current_slope value in hashmap
			if temp.right:
				if hashmap.get(val)==None:
					hashmap[val] = [temp.right.data]
				else:
					hashmap[val].append(temp.right.data)
				queue.append([val, temp.right])

			n -= 1
		levels += 1
	
	for i in range(0,level-1):
		print hashmap[i]
	return

root = bTree(8)
root.right = bTree(10)
root.right.right = bTree(14)
root.right.right.left = bTree(3)
root.left = bTree(3)
root.left.right = bTree(6)
root.left.right.right = bTree(7)
root.left.left = bTree(1)

diagonalTraversal(root)
