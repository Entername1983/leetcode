#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
# 2n * 2n matrix, each cell has an integer
# can reverse rows and columns any number of times
# maximize sum of elements in n*n submatrix, upper left corner
# we want to look at each row, if the sum of the first half of the row is larger than teh sum of the second half, do nothing, otherwise reverse them.  
# do the same with the columns
# willw e have to do this several times?  


def flippingMatrix(matrix):
    # Write your code here
    n= len(matrix) // 2
    print("halfway", n)
    total_v = 0
    
    for i in range(n):
        for j in range(n):
            print("i", i, "j", j)
            total_v += max(matrix[i][j], matrix[i][2*n -1 -j], matrix[2*n -1 -i][j], matrix[2*n - 1- i][2*n - 1 - j])
    return total_v
            


if __name__ == '__main__':
    
    result = flippingMatrix([[112, 42, 83, 119], [56, 125, 56, 48], [15, 78, 101, 43], [62, 98, 114, 108]])
    # result = flippingMatrix([[1, 2], [3, 4]])

    print(result)