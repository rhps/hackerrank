#!/bin/python3

import os
import sys

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(n, ar):
    #
    # Write your code here.
    #
    candle = max(ar)
    count = 0
    for x in range(0,n):
    	if candle == ar[x]:
    		count = count + 1
    return count

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()
