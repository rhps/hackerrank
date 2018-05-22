#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    a = input()

    b = input()

    a, b = list(a), list(b)
    aitr = list(a)
    for i in aitr:
    	if i in b:
    		a.remove(i)
    		b.remove(i)

    print(len(a) + len(b))