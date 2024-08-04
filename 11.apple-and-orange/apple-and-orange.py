#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesArray = []
    orangesArray = []
    
    applesCount = 0
    orangesCount =0
    
    for i in apples:
        applesArray.append(a+i)
        
    for i in oranges:
        orangesArray.append(b+i)
        
    for x in applesArray:
        if ((x>=s) and (x<=t)):
            applesCount+=1
            
    for x in orangesArray:
        if ((x>=s) and (x<=t)):
            orangesCount+=1
            
    print(applesCount)
    print(orangesCount)
            
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
