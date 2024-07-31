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
# 0, 0 + 1, 1 + 2, 2
# 0, 2 + 1, 1, + 2, 0
def diagonalDifference(arr):
    bl_tr: int = 0 # bottom left to top right diagonal
    tl_br: int = 0 # top right to bottom left diagonal

    i = 0
    k = len(arr) - 1
    while i < len(arr):
        bl_tr += arr[k][i]
        tl_br += arr[i][i]
        i += 1
        k -= 1
    ## put them in absolute terms
    print(abs(bl_tr - tl_br))
    return abs(bl_tr - tl_br)




if __name__ == '__main__':
    arr = [
    [-1, 2, -3, 4],
    [5, -6, 7, -8],
    [-9, 10, -11, 12],
    [13, -14, 15, -16]
]
    result = diagonalDifference(arr)