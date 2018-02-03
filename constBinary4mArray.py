import printBinaryTree as bT

#Time complexity O(n), Space Complexity: O(n)
def convertArrtoBinTree(arr):
	new_arr = [bT.bTree(i) for i in range(len(arr))]
	root = None
	for i in range(len(arr)):
		#If the value of parent is -1, then the current node is root
		if arr[i] == -1:
			root = new_arr[i]
			continue
		#Goto the parent of current node in new_arr, if leftChild is unassigned then connect current node
		if new_arr[arr[i]].left == None:
			new_arr[arr[i]].left = new_arr[i]
		#Otherwise connect to rightchild
		else:
			new_arr[arr[i]].right = new_arr[i]
	return root

arr = [1, 5, 5, 2, 2, -1, 3]
root = convertArrtoBinTree(arr)
bT.levelOrder(root)
