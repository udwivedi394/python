#!/bin/python

import sys

def cost(arr):
	n = len(arr)
	dp = [0]*n
	
	for i in range(n):
		#which ever is maximum in i and i-1, maximize it
		if i==n-1:
			dp[i] = arr[i] if max(arr[i],dp[i-1])==arr[i] else 1
		else:
			dp[i] = arr[i] if max(arr[i],arr[i+1])==arr[i] else 1
	print dp
	sumi = 0
	for i in range(n-1):
		sumi += abs(dp[i]-dp[i+1])
	return sumi	
    # Complete this function

def cost03(arr):
	elem,mini,maxi = arr[0],0,0
	n = len(arr)
	new_arr = []

	for i in range(n-1):
		print mini,maxi
		elem = arr[i]
		next_elem = arr[i+1]
		t1 = max(abs(elem-1),abs(elem-next_elem))
		t2 = max(abs(1-1),abs(1-next_elem))

		if maxi+t1 > mini+t2:
			mini = maxi+abs(elem-1)
			maxi = maxi+abs(elem-next_elem)
			new_arr.append(elem)
		else:
			temp = mini+t2
			mini = maxi
			maxi = temp
			new_arr.append(1)

	print new_arr,mini,maxi
	
	sumi = 0
	for i in range(len(new_arr)-1):
		sumi += abs(new_arr[i]-new_arr[i+1])
	print "NewSum:",sumi+max(abs(new_arr[-1]-arr[-1]),abs(new_arr[-1]-1))
	return max(maxi,mini)

def cost02(arr):
	elem,mini,maxi = arr[0],0,0
	n = len(arr)
	new_arr = []

	for i in range(n-1):
		elem = arr[i]
		next_elem = arr[i+1]
		prev_maxi,prev_mini = maxi,mini
		maxi = max(prev_maxi,prev_mini+abs(arr[i]-1))
		mini = max(prev_maxi+abs(arr[i+1]-1),prev_mini+abs(arr[i]-arr[i+1]))

	return max(maxi,mini)


if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = cost02(arr)
        print result
