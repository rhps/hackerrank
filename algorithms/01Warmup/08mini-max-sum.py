#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    #
    # Write your code here.
    #
    n = 0
    ans = []
    for x in range(0,5):
    	sums = 0
    	for y in range(0,5):
    		if y == n:
    			pass
    		else:
    			sums = sums + arr[y]
    	ans.append(sums)
    	n = n + 1
    print(min(ans), max(ans))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
