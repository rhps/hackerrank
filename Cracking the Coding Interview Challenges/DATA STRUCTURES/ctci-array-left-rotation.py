#!/bin/python3

import math
import os
import random
import re
import sys


def ArrayLeftRotation(n, k, a):
	anew = [None] * n

	for x in range(0,n):
		idx = (x + (n - k)) % n
		anew[idx] = a[x]

	return anew


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    a = list(map(int, input().rstrip().split()))

    ans = ArrayLeftRotation(n, k, a)

    print(' '.join(map(str, ans)))
