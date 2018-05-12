#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    plus = 0
    minus = 0
    zero = 0
    n = len(arr)

    for x in range(0,n):
    	if arr[x] >= 1:
    		plus = plus + 1
    	elif arr[x] == 0:
    		zero = zero + 1
    	else:
    		minus = minus + 1

    print('%.6f' %(plus/n))
    print('%.6f' %(minus/n))
    print('%.6f' %(zero/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
