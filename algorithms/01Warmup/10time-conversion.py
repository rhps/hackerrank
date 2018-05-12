#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hr, mi, sec = map(int, s[:-2].split(':'))
    p = s[-2:]
    hr = hr % 12 + (p.upper() == 'PM') * 12
    return (('%02d:%02d:%02d') % (hr, mi, sec))


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
