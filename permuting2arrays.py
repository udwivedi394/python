#!/bin/python

import sys

def twoArrays(k, A, B):
	A.sort()
	B.sort()
	B.reverse()
	
	for i in range(len(A)):
		if A[i]+B[i]<k:
			return "NO"
	return "YES"
    # Complete this function

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n, k = raw_input().strip().split(' ')
        n, k = [int(n), int(k)]
        A = map(int, raw_input().strip().split(' '))
        B = map(int, raw_input().strip().split(' '))
        result = twoArrays(k, A, B)
        print result

