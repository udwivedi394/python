def nonNegativeIntegralSol(n):
	#This can be solved using permutation tool,
	#(n+r-1)C(r-1): To divide n identical things among r people, where any people may get any number of things(including 0)

	return (n+2)*(n+1)//2

print nonNegativeIntegralSol(3)
