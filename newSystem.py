def call_stringcaseMan(arr, N):
	string = arr.split(' ')
	arr1 = []
	arr2 = []
	arr3 = []

	for i in range(N):
		if string[i] not in arr1:
			arr1.append(string[i])
			arr2.append(1)
			print "Verified",

		else:
			index = arr1.index(string[i])
			print "%s%d" %(string[i],arr2[index]),
			arr2[index] += 1

#call_stringcaseMan()
T = int(input())

inp_arr = []
string_arr = []
for t in range(T):
	N = int(input())
	string = raw_input()
	inp_arr.append(N)
	string_arr.append(string)

for t in range(T):	
	call_stringcaseMan(string_arr[t], inp_arr[i])
	if t < T-1:
		print
