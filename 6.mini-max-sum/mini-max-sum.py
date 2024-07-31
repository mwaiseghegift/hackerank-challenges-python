#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    max = 0
    min = 0
    counter = 0
    # for minimum
    reverseOrder = sorted(arr, reverse=True)
    ascending = sorted(arr)
    
    for i in reverseOrder:
        max += i
        counter += 1
        if counter == len(arr) -1:
            counter = 0
            break
            
    for i in ascending:
        min += i
        counter += 1
        if counter == len(arr) -1:
            counter = 0
            break
        
    print(f'{min} {max}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
