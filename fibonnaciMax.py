def fibonnaci(N):
	arr = [1,1]

	if N == 1:
		return arr[0]

	if N == 2:
		return arr[1]

	i = 3
	while i <= N:
		e1 = arr[-1]
		e2 = arr[-2]

		arr.append((e1+e2)%100)
		arr.pop(0)
		i+=1
	#print arr
	return arr[-1]

def fibonnaci_02(N):
	N = N%300

	arr = [1, 1]
	if N == 1:
		return arr[0]

	if N == 2:
		return arr[1]

	i = 3
	while i <= N:
		e1 = arr[-1]
		e2 = arr[-2]

		arr.append((e1+e2)%100)
		arr.pop(0)
		i+=1
	#print arr
	return arr[-1]
	

#for i in range(1,9):
#	print fibonnaci(i)

#print fibonnaci(9991)

T = int(input())

inp_arr = []
for i in range(T):
	inp = int(input())
	inp_arr.append(inp)

for j in inp_arr:
	print fibonnaci(j)

print fibonnaci_02(1000000000)
