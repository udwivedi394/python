#!/bin/python

import sys

def jimOrders(orders):
	new_arr = []
	for i in range(len(orders)):
		new_arr.append([sum(orders[i]),i])
	new_arr=sorted(new_arr, key=lambda item:item[0])

	return [item[1]+1 for item in new_arr]
	
    # Complete this function

if __name__ == "__main__":
    n = int(raw_input().strip())
    orders = []
    for orders_i in xrange(n):
        orders_temp = map(int,raw_input().strip().split(' '))
        orders.append(orders_temp)
    result = jimOrders(orders)
    print " ".join(map(str, result))
