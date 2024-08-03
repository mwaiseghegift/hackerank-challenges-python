#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if(s[-2:].endswith('PM')):
        if(s[:2].startswith('12')):
            return s[:-2]
        time24 = int(s[:2])+12
        if(time24>=24):
            time24 = (time24-24)
            return f'{time24:02}{s[2:-2:]}'
        return f'{time24}{s[2:-2:]}'
    if((s[-2:].endswith('AM')) and (s[:2].startswith('12'))):
        return f'00{s[2:-2:]}'
    return s[:-2]

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
