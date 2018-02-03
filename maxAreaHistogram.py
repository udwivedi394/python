class Stack:
	def __init__(self):
		self.data = []
		self.topi = -1

	def push(self,data):
		self.data.append(data)
		self.topi += 1

	def pop(self):
		if self.topi >= 0:
			temp = self.data.pop()
			self.topi -= 1
			return temp
		else:
			return False

	def top(self):
		return self.data[self.topi]

	def empty(self):
		if self.topi >= 0:
			return False
		else:
			return True

	def __str__(self):
		return ("Stack:%s")%self.data

#Below code is to find Max area under histogram

#Naive Solution, O(n^2)
def findMaxArea(arr):
	cur_max = 0
	final_max = 0

	for i in range(len(arr)):
		for j in range(i,len(arr)):
			cur_max = max(min(arr[i:j+1])*(j-i+1), max(arr[i:j+1]))
			final_max = max(cur_max, final_max)

	return final_max

#Divide and Conquer Method
#In worst case scenario, all min lie to one side
#Therefore, to find minimum O(n) time is used and the overall complexity would become O(n^2)
def findMaxAreaDivideandConquer(arr):
	if len(arr)==1:
		return arr[0]
	if len(arr) == 0:
		return 0

	min_index = arr.index(min(arr))

	left_area = findMaxAreaDivideandConquer(arr[:min_index])
	right_area = findMaxAreaDivideandConquer(arr[min_index+1:])
	min_area = arr[min_index]*len(arr)

	return max(left_area, right_area, min_area)

#Better Solution, Time Complexity: O(n), space complexity: O(n)
def findMaxAreaStack(arr):
	s = Stack()

	max_area = -1
	area_with_top = -1
	i = 0
	n = len(arr)

	#Traverse through histogram
	while i < n:
		#If stack is empty or the arr[top of stack] <= arr[i](current bar in histogram), push current bar index, increment i
		#This way stack will always be in increasing order of bars
		if s.empty() or arr[s.top()] <= arr[i]:
			s.push(i)
			i += 1
		#If current element is lesser than arr[top of stack]
		else:
			#save index of top bar
			tp = s.top()
			#Pop the stack
			s.pop()
			
			#Multiply the current bar with all bars in right side, as the bars in right will be always greater than current bar
			#Taking the new top is important, as if there was a bigger bar between top bar and the previous one,
			#It should also be multiplied with current top bar area
			area_with_top = arr[tp] * (i if s.empty() else i-s.top()-1)
			max_area = max(max_area, area_with_top)

	while s.empty()==False:
		tp = s.top()
		s.pop()
		
		area_with_top = arr[tp] * (i if s.empty() else i-s.top()-1)
		max_area = max(max_area, area_with_top)

	return max_area

arr = [6,1,5,4,5,2,6]
print findMaxArea(arr)
print findMaxAreaDivideandConquer(arr)
print "Max Area:", findMaxAreaStack(arr)
