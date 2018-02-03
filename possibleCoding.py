import time

#Recursive Solution
def possibleCoding(num):
	#Zero len is also accounted here, as len(0) will occur only if 2nd condition satisfies
	if len(num) <= 1:
		return 1

	count = 0

	if num[-1]!=0:
		count += possibleCoding(num[:-1])
	if num[-2]*10+num[-1] < 27:
		count += possibleCoding(num[:-2])

	return count

#Dynamic Programming, Memoization
def possibleCoding02(num, lookup=None):
	if len(num) <= 1:
		return 1

	if lookup == None:
		lookup = {}

	count = 0
	if num[:-1]!=0:
		if lookup.get(len(num[:-1]))==None:
			lookup[len(num[:-1])] = possibleCoding02(num[:-1], lookup)
		count += lookup[len(num[:-1])]

	if num[-2]*10+num[-1] < 27:
		if lookup.get(len(num[:-2]))==None:
			lookup[len(num[:-2])] = possibleCoding02(num[:-2], lookup)
		count += lookup[len(num[:-2])]
	
	return count

num = [1,2,2,4,9,5,3,4,2,1,4]
num2 = [6,2]

t1 = time.time()
print possibleCoding(num)
t2 = time.time()
print t2-t1


t1 = time.time()
print possibleCoding02(num)
t2 = time.time()
print t2-t1
