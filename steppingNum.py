import time

#Naive Solution
def steppingNum(n,m):
	final_result = []
	for num in range(n,m+1):
		temp = num
		diff = 1
		while num//10 and diff == 1:
			diff = abs(num%10 - (num//10)%10)
			num //= 10
		if diff == 1:
			final_result.append(temp)
	return final_result

#Bottoms-up Approach, works fine for numbers upto 2 digits
def steppingNum02(n,m):
	lookup = [i for i in range(10)]
	final_result = []
	i = 0
	while i < len(lookup) and max(lookup)<=m:
		temp = lookup[i] + (lookup[i]+1)*10
		lookup.append(temp)
		lookup.append(int(str(temp)[::-1],10))
		
		if temp >= n and temp <= m:
			final_result.append(temp)
			temp = int(str(temp)[::-1],10)
			if temp >= n and temp <= m:
				final_result.append(temp)
		i += 1
	#print lookup
	return final_result

#Better Algorithm, building up the tree
def dfs(n,m,stepNum):
	if stepNum >= n and stepNum <= m:
		print stepNum,
	
	if stepNum == 0 or stepNum > m:
		return

	lastDigit = stepNum%10
	
	stepNumA = stepNum*10 + lastDigit - 1
	stepNumB = stepNum*10 + lastDigit + 1

	
	if lastDigit == 0:
		dfs(n,m,stepNumB)
	elif lastDigit == 9:
		dfs(n,m,stepNumA)
	else:
		dfs(n,m,stepNumA)
		dfs(n,m,stepNumB)
	return

def printSteppingNum(n,m):
	if n >= m:
		print "Invalid Range"
	
	for i in range(0,9):
		dfs(n,m,i)

t1 = time.time()
result = steppingNum(10,10000)
t2 = time.time()

if len(result):
	print result
else:
	print "No stepping Number"
print "Time:", t2-t1


result = steppingNum02(10,1000)


if len(result):
	print result
else:
	print "No stepping Number"

print "Better Algorithm"
t1 = time.time()
printSteppingNum(10,10000)
t2 = time.time()
print
print "Time:", t2-t1
