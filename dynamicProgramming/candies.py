#!/bin/python

import sys

def candies02(n, arr):
	prev_cand = 0
	prev_score = 0
	#next_score = arr[1]
	sumi = 0
	
	n = len(arr)
	
	new_arr = [1]*n
	i = 0
	
	while i < n:
		if arr[i] > prev_score:
			new_arr[i] = prev_cand+1

		minima = False
		#find Minima
		#print "i:",i
		if arr[i] < prev_score and (i==n-1 or arr[i] < arr[i+1]):
			#print "Inside",
			minima = True
		
		#print 
		j = i
		while minima and j > 0:
			if arr[j-1] > arr[j]:
				#print "Here:",j
				new_arr[j-1] = max(new_arr[j-1], new_arr[j]+1)
			else:
				minima = False
			j -= 1
	
		prev_cand = new_arr[i]
		prev_score = arr[i]
		i += 1
	
	#print new_arr
	return sum(new_arr)
    # Complete this function

def candies(n, arr):
	prev_cand = 0
	prev_score = 0
	sumi = 0
	
	n = len(arr)
	new_arr = [1]*n

	for i in xrange(n):
		if arr[i] > prev_score:
			new_arr[i] = prev_cand+1
		prev_score = arr[i]
		prev_cand  = new_arr[i]

	for j in xrange(n-1,-1,-1):
		if arr[j] > prev_score:
			new_arr[j] = max(new_arr[j], prev_cand+1)
		prev_score = arr[j]
		prev_cand = new_arr[j]
		
	print new_arr
	return sum(new_arr)

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = []
    arr_i = 0
    for arr_i in xrange(n):
        arr_t = int(raw_input().strip())
        arr.append(arr_t)
    result = candies(n, arr)
    print result
