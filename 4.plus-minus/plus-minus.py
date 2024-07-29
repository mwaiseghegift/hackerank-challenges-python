#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    lenArray = len(arr)
    negativeCounts = 0
    positiveCounts = 0
    zeroCounts = 0
    
    for n in arr:
        if n <0:
            negativeCounts += 1
        if n > 0:
            positiveCounts += 1
        if n == 0:
            zeroCounts +=1
            
    
    print(round((positiveCounts/lenArray), 6))
    print(round((negativeCounts/lenArray), 6))
    print(round((zeroCounts/lenArray), 6))

        
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
