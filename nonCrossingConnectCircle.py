import time

#Recursive Solution, Reference of Catalan Numbers
def connectPoints01(n):
	if n%2!=0:
		return False

	if n in (0,2):
		return 1

	count = 0
	for i in range(0,n,2):
		count += connectPoints01(i) * connectPoints01(n-i-2)

	return count

#Dynamic Programming
def connectPoints02(n, lookup=None):
	if n%2!=0:
		return False

	if n in (0,2):
		return 1

	if lookup == None:
		lookup = {}

	count = 0
	for i in range(0,n,2):
		if lookup.get(i)==None:
			lookup[i] = connectPoints02(i)

		if lookup.get(n-i-2)==None:
			lookup[n-i-2] = connectPoints02(n-i-2)

		count += lookup[i]*lookup[n-i-2]

	return count

n = 30
t1 = time.time()
print connectPoints02(n)
t2 = time.time()
print "Time taken:",t2-t1

t1 = time.time()
print connectPoints01(n)
t2 = time.time()
print "Time taken:",t2-t1
