
import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
# loop through the array


def countingSort(arr):
    f_array = [0 for _ in range(100)]
    for i, value in enumerate(arr):
        f_array[value] += 1
    return f_array

if __name__ == '__main__':

    arr = [1,1, 3, 2, 1]
    result = countingSort(arr)
    print(result)
