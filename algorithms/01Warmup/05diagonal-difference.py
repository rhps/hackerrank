#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    # Write your code here.
    #
    n = len(a)
    tot1 = 0
    tot2 = 0

    for x in range(0,n):
        tot1 = tot1 + a[x][x]
        tot2 = tot2 + a[x][n-x-1]

    return abs(tot2-tot1)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
