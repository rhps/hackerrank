#!/bin/python3

import os
import sys

#
# Complete the countApplesAndOranges function below.
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #
    # Write your code here.
    #
    '''
    ct_ap = 0
    ct_or = 0

    for x in apples:
        if (x + a) >= s and (x + a) <= t:
            ct_ap = ct_ap + 1

    for y in oranges:
        if (y + b) <= t and (y + b) >= s:
            ct_or = ct_or + 1

    print(ct_ap)
    print(ct_or)
    '''
    print(len([1 for app in apple if app >= s-a and app <= t-a]))
    print(len([1 for ora in orange if ora <= t-b and ora >= s-b]))
    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apple = list(map(int, input().rstrip().split()))

    orange = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apple, orange)
