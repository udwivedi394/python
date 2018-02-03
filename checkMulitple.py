import time

def checkMultipleof3(num):
	even_count = 0
	odd_count = 0
	if num < 0:
		num = -num
	if num == 0:
		return True
	if num == 1:
		return False

	while num:
		if num & 1: 
			odd_count += 1
		num >>= 1
		
		if num & 1:
			even_count += 1
		num >>= 1
	return checkMultipleof3(even_count-odd_count)

for i in range(31):
	print i, checkMultipleof3(i)

t1 = time.time()
if 9999999999999999999999999999999999999%3 == 0:
	print True,
else:
	print False,
t2 = time.time()
first = t2-t1
print "First", first

t1 = time.time()
print checkMultipleof3(9999999999999999999999999999999999999),
t2 = time.time()
second = t2-t1
print "second", second

if first>second:
	print "Success"
else:
	print "Fail"
