import sys

def fibonacciUtil(n,lookup):
	if n < 3:
		return lookup[n]
	
	if lookup.get(n-1)==None:
		lookup[n-1] = fibonacciUtil(n-1,lookup)
	
	if lookup.get(n-2)==None:
		lookup[n-2] = fibonacciUtil(n-2,lookup)

	return lookup[n-2] + lookup[n-1]**2


def fibonacciModified(t1, t2, n):
	lookup = {1:t1, 2:t2}
	return fibonacciUtil(n,lookup)
	
if __name__ == "__main__":
    t1, t2, n = raw_input().strip().split(' ')
    t1, t2, n = [int(t1), int(t2), int(n)]
    result = fibonacciModified(t1, t2, n)
    print result
