#With MergeSort, Complexity(nlogn)
def nutBoltMatch(nut,bolt):
	if len(nut)==1 and len(bolt)==1:
		return [nut, bolt]

	mid = len(nut)//2
	left = nutBoltMatch(nut[:mid], bolt[:mid])
	right = nutBoltMatch(nut[mid:], bolt[mid:])

	temp_nut = []
	temp_bolt= []
		
	#Arranging nuts
	while len(left[0]) and len(right[0]):
		if left[0][0] < right[0][0]:
			temp_nut.append(left[0].pop(0))
		else:
			temp_nut.append(right[0].pop(0))
	while len(left[0]):
		temp_nut.append(left[0].pop(0))

	while len(right[0]):
		temp_nut.append(right[0].pop(0))

	#Arranging botls
	while len(left[1]) and len(right[1]):
		if left[1][0] < right[1][0]:
			temp_bolt.append(left[1].pop(0))
		else:
			temp_bolt.append(right[1].pop(0))
	while len(left[1]):
		temp_bolt.append(left[1].pop(0))

	while len(right[1]):
		temp_bolt.append(right[1].pop(0))
	#print bolt
	return [temp_nut, temp_bolt]

#With use of hashmap
def nutBoltHash(nut,bolt):
	lookup = {}

	for i in range(len(nut)):
		lookup[nut[i]] = i
	
	temp_bolt = [-1 for i in range(len(bolt))]
	
	for j in bolt:
		temp_bolt[lookup[j]] = j
	
	del bolt[:]
	bolt += temp_bolt
	
	return

nut = ['@','#','$','%','^','&']
bolt = ['$','%','&','^','@','#']
result = nutBoltMatch(nut,bolt)
print result[0]
print result[1]

nutBoltHash(nut,bolt)
print nut
print bolt
