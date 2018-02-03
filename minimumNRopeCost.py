#Simple method
def minimumNRopeCost(arr):
	stack = []
	temp = sorted(arr)[::-1]

	while len(temp)!=1:
		r1 = temp.pop()
		r2 = temp.pop()
		temp.append(r1+r2)
		stack.append(r1+r2)
	return sum(stack)

arr=[4,3,2,6]
arr=[6,1,5,3,2,4]
print minimumNRopeCost(arr)
