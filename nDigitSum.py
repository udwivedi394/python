import time

#A simple solution to get all the n-digit numbers equal to sum given
def nDigitSumUtility(n, sumi, final_count, storage_facility, first=1, cur_num=0):
	#If only one digit is remaining 
	if n==1:
		#Sum required is of 1 digit, then add it with cur_num
		if sumi/10==0:
			return cur_num*10+sumi
		#Otherwise return the current number
		else:
			return cur_num
	
	#For the first time, loop starts from 1 as leading zeroes are not allowed
	for i in range(first, 10):
		if i <= sumi:
			#Recursively call the function, with less digit, substract the current sum, and add it to current num
			cur_sum = nDigitSumUtility(n-1, sumi-i, final_count, storage_facility, 0, cur_num*10+i)
			#As this step is explicitly checking for total number of digits as very initial call, argument first
			#can be ommitted
			if cur_sum//10**(final_count-1):
				storage_facility.append(cur_sum)
				#print cur_sum
	return cur_num

def nDigitSum(n,sumi):
	storage_facility = []
	nDigitSumUtility(n,sumi,n,storage_facility)
	print storage_facility
	return len(storage_facility)

#Recursive Solution, it is not storing numbers
def count_all(n,k):
	#Base-Case, when only 1 digit is available
	if n==1:
		#If sum to be made is of 2 digit
		if k//10:
			return 0
		else:
			return 1
	res = 0
	for i in range(10):
		if k-i>=0:
			res += count_all(n-1,k-i)
	return res

def final_count(n,k):
	res = 0
	for i in range(1,10):
		if k-i >= 0:
			res += count_all(n-1,k-i)
	return res

#Dynamic Solution
#This function counts the zero as digit as well
def count_all_02(n,k,lookup_dict):
	#Base-Case, when only 1 digit is available
	if n==1:
		#If sum to be made is of 2 digit
		if k//10:
			return 0
		else:
			return 1
	res = 0
	for i in range(10):
		if k-i>=0:
			if lookup_dict.get((n-1, k-i)):
				res += lookup_dict[(n-1,k-i)]
			else:
				lookup_dict[(n-1,k-i)] = count_all_02(n-1,k-i,lookup_dict)
				res += count_all_02(n-1,k-i,lookup_dict)
	return res

#Separate function to start the count from 1, as leading zeroes not allowed
def final_count_02(n,k):
	res = 0
	lookup_dict = {}
	for i in range(1,10):
		#Check if current digit is not greater than sum to be made
		if k-i >= 0:
			#Check if the (number of digits, sum to be made) available in lookup dictionary
			if lookup_dict.get((n-1, k-i)):
				#Add in the result
				res += lookup_dict[(n-1,k-i)]
			else:
				#If combination not available then call count_all_02 function and store in the lookup
				lookup_dict[(n-1,k-i)] = count_all_02(n-1,k-i,lookup_dict)
				res += lookup_dict[(n-1,k-i)]
	return res
t1 = time.time()
print nDigitSum(3,6)
t2 = time.time()
print "Time taken", t2-t1

t1 = time.time()
#print final_count(10,18)
t2 = time.time()
print "Time taken", t2-t1

t1 = time.time()
print final_count_02(10,18)
t2 = time.time()
print "Time taken", t2-t1
