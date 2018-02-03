#Fibonacci Approach, Dynammic Programming: Bottom-up buildup
#Space Complexity: O(n)
def way2ReachTop(n):
	lookup = []
	lookup.append(1)
	lookup.append(2)

	for i in range(2,n):
		lookup.append(lookup[i-1]+lookup[i-2])

	return lookup.pop()

#Time Complexity: O(n), Space Complexity: O(1)
def way2ReachTop02(n):
	lookup = [1,2]

	for i in range(2,n):
		lookup.append(lookup[0]+lookup[1])
		lookup.pop(0)

	return lookup.pop()


#Dynammic Programming: Generalization
#n->where to go, m->max step can be taken
def way2ReachTop03(n,m,lookup=None):
	if n == 1:
		return 1
	if n == 2:
		return min(2,m)

	if lookup == None:
		lookup = {}

	if lookup.get(n):
		return lookup[n]

	i = 3
	while i <= n:
		j = 1
		sumi = 0
		while j <= m and j < i:
			lookup[i-j] = way2ReachTop03(i-j,m,lookup)
			sumi += lookup[i-j]
			j += 1
		lookup[i] = sumi
		if i == m:
			lookup[i] += 1
		i += 1

	return lookup[n]

n = 25
m = 3
print way2ReachTop(n)	
print way2ReachTop02(n)	
print way2ReachTop03(n,m)	
