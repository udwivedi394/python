#!/bin/python

import sys

def maximumToys(prices, k):
	prices.sort()
	prices.reverse()
	flag = True
	count = 0
	while prices and flag:
		top = prices.pop()
		if k-top>=0:
			count += 1
		else:
			flag = False
	return count
    # Complete this function

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = map(int, raw_input().strip().split(' '))
    result = maximumToys(prices, k)
    print result
