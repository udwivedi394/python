#Linear algorithm, Time : O(n), Space: O(1)
def findStartPoint(arr):
	
	min_score = 0
	start_node = -1
	cur_score = 0

	for i in range(len(arr)):
		#at each petrol pump calculate the extra petrol that can be carried out to next
		cur_score = cur_score+arr[i][0]-arr[i][1]

		#Keep record of petrol pump with minimum score
		if cur_score <= min_score:
			min_score=cur_score
			start_node=i

	#If the overall score
	if cur_score < 0:
		return False
	
	return start_node+1

#[fuel_at_petrol_pump, distance_to_next_petrol_pump]
arr1 = [[6,4],
        [3,6],
        [7,3]]


arr2 = [[4,5],
	[4,6],
	[6,5],
	[7,3]]

arr3 = [[6,5],
	[7,3],
	[4,5],
	[4,6]]

print "start:",findStartPoint(arr3)
