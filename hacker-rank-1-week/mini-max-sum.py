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
    #loop through the array.  
    # store the min and max values found, keeping them updated
    # add up all the values
    # print min, total addition minus max
    # print max, total addition minus min
    min_v: int = arr[0]
    max_v: int = arr[0]
    total_v: int = 0
    for _, value in enumerate(arr):
        if value < min_v:
            min_v = value
        if value > max_v:
            max_v = value
        total_v += value
    print(f"{total_v - max_v} {total_v - min_v}")
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
