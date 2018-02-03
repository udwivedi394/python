#/bin/python

import sys

def stockmax(prices):
	n = len(prices)
	maxima = []
	prev_prices = 0
	for i in range(n-1,-1,-1):
		if prices[i] > prev_prices and (i==0 or prices[i] > prices[i-1]):
			maxima.append((prices[i],i))
		prev_prices = prices[i]
	maxima = sorted(maxima, key = lambda item:item[0])[::-1]
	print maxima
	
	profit = 0
	last_index = val = 0
	while maxima:
		maxi = maxima.pop(0)
		if maxi[1] < last_index:
			continue
		print "Here Again:",maxi,last_index,profit
		share_cost = sum(prices[last_index+val:maxi[1]])
		no_of_shares = maxi[1]-(last_index+val)
		profit += no_of_shares*maxi[0]-share_cost
		last_index = maxi[1]
		val = 1
	return profit		

def stockmax02(prices):
	n = len(prices)
	maxima = []
	prev_prices = 0
	for i in range(n):
		if prices[i] > prev_prices and (i==n-1 or prices[i] > prices[i+1]):
			maxima.append((prices[i],i))
		prev_prices = prices[i]
	maxima = sorted(maxima, key = lambda item:item[0])[::-1]
	print maxima
	
	profit = 0
	last_index = val = 0
	while maxima:
		maxi = maxima.pop(0)
		if maxi[1] < last_index:
			continue
		#share_cost = sum(prices[last_index+val:maxi[1]])
		#no_of_shares = maxi[1]-(last_index+val)
		share_cost = no_of_shares = 0
		for i in range(last_index, maxi[1]):
			if prices[i] < maxi[0]:
				share_cost += prices[i]
				no_of_shares += 1
		temp=no_of_shares*maxi[0]-share_cost
		profit += temp
		#print "Maxi,last_index,profit,no_of_shares,share_cost,temp_profit",maxi,last_index,profit,no_of_shares,share_cost,temp
		last_index = maxi[1]
		val = 1
	return profit		
    # Complete this function

#Best Solution, so far O(n)
def stockmax03(prices):
	profit = 0
	maxsofar = 0
	n = len(prices)

	for i in range(n-1,-1,-1):
		if prices[i] >= maxsofar:
			print "Maxima,profit:",(prices[i],i),profit
			maxsofar = prices[i]

		profit += maxsofar-prices[i]
	return profit

"""
f1 = open("stockMax.txt",'r')
if __name__ == "__main__":
    t = int(f1.readline().strip())
    for a0 in xrange(t):
        n = int(f1.readline().strip())
        prices = map(int, f1.readline().strip().split(' '))
        result = stockmax(prices)
        print result
"""
if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        prices = map(int, raw_input().strip().split(' '))
        result = stockmax02(prices)
        print result
#"""
