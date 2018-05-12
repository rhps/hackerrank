#!/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    #
    # Write your code here.
    #
    alice = 0
    bob = 0
    if a0 > b0:
        alice = alice + 1
    elif a0 < b0:
        bob = bob + 1
    else:
        pass

    if a1 > b1:
        alice = alice + 1
    elif a1 < b1:
        bob = bob + 1
    else:
        pass

    if a2 > b2:
        alice = alice + 1
    elif a2 < b2:
        bob = bob + 1
    else:
        pass

    return alice, bob


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
