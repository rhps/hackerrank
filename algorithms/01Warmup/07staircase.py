#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    #
    # Write your code here.
    #
    space = n - 1
    for x in range(0, n):
    	out = []
    	for y in range(0,n):
    		if y < space:
    			out.append(' ')
    		else:
    			out.append('#')
    	space = space - 1
    	print(''.join(map(str, out)))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
