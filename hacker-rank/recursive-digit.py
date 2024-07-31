

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
# super digit of an integer x rules
### given integer we need to find the super integer
### if x has only 1 digit then its super digit is x
### Otherwise super digit of x is equal to the super digit of the sum of the digits of x



def superDigit(n: int, k:int):
    print("calling super digit")
    total = 0
    for number in n:
        total += int(number)
    print(total)
    super_digit = total * k 
    
    if super_digit < 10:
        return super_digit
    return superDigit(str(super_digit), 1)
    
print(superDigit('9875', 4))