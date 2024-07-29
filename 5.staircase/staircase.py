#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    initialValue = 0
    for i in range(n):
        spaces = ' '*(n-i-1)
        initialValue += 1
        print(spaces, end='')
        for x in range(initialValue):
            print('#', end='')
        if (initialValue == n):
            pass
        else:
            print('')
            
            

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
