#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    digSum = 0
    reverseDiagSum = 0
    loopCount=0
    otherCount = len(arr[1])-1
    
    for i in arr:
        digSum += i[loopCount]
        reverseDiagSum+=i[otherCount]
        loopCount +=1
        otherCount -=1
    return abs(digSum - reverseDiagSum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
