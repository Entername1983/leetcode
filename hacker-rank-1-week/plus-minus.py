

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_count: int = 0
    neg_count: int = 0
    zero_count: int = 0
    
    for _, value in enumerate(arr):
        if value > 0:
            pos_count += 1
        elif value < 0:
            neg_count += 1
        else:
            zero_count +=1
    
    print(f"{pos_count/len(arr):6f}\n{neg_count/len(arr):6f}\n{zero_count/len(arr):6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
