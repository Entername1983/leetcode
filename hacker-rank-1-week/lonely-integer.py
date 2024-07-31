
import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    int_map = defaultdict(int)
    for _, value in enumerate(a):
        int_map[value] += 1

    for i in int_map:
        if int_map[i] == 1:
            return i

if __name__ == '__main__':

    result = lonelyinteger([1, 5, 3, 4, 3, 4, 1])
    print(result)
