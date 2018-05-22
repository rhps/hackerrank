#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def countInversions(arr):
	itr = 0
	n = len(arr)
	for i in range(0,n):
		for j in range(0,n-1):
			if (arr[j] > arr[j+1]):
				arr[j], arr[j+1] = arr[j+1], arr[j]
				itr = itr + 1

	return itr



if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	t = int(input())

	for t_itr in range(t):
		n = int(input())

		arr = list(map(int, input().rstrip().split()))

		result = countInversions(arr)

		fptr.write(str(result) + '\n')

	fptr.close()
