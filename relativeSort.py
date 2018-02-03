#Naive Solution
def relativeSort(arr1, arr2):
	temp_arr1 = []+arr1
	new_arr = []

	temp_arr1 = sorted(temp_arr1)
	i = 0
	while i < len(arr2):
		try:
			cur_index = temp_arr1.index(arr2[i])
			new_arr.append(temp_arr1[cur_index])
			temp_arr1.pop(cur_index)
		except ValueError:
			i += 1
	
	if len(temp_arr1) > 0:
		temp_arr1 = sorted(temp_arr1)
		new_arr += temp_arr1
	return new_arr

#Hashing to resolve problem
def relativeSort02(a1, a2):
	lookup_dict = {}
	a1 = []+a1
	for i in a1:
		if lookup_dict.get(i):
			lookup_dict[i] += 1
		else:
			lookup_dict[i] = 1

	new_temp_arr = []
	for i in a2:
		if lookup_dict.get(i):
			new_temp_arr += [i]*lookup_dict.get(i)
			try:
				for j in range(lookup_dict.get(i)):
					a1.remove(i)
				lookup_dict[i] = 0
			except ValueError:
				lookup_dict[i] = 0
	a1 = sorted(a1)
	return new_temp_arr+a1


a1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
a2 = [2, 1, 1, 8, 3, 100, 56, 4, 69, 21, 35, 10, 10]

print relativeSort(a1,a2)
print relativeSort02(a1,a2)
