import os
import sys

def simpleArraySum(ar):
	n = len(ar)
	tot = 0
	for x in range(0, n):
		tot = tot + ar[x]
	return tot


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	ar_count = int(input())

	ar = list(map(int, input().rstrip().split()))

	result = simpleArraySum(ar)

	fptr.write(str(result) + '\n')

	fptr.close()