import math
import os
import random
import re
import sys
# n towers
# each tower is height m
# players take turns
# each turn a player can choose a tower of height x and reduce its height to y where 1 <= y <= x and y evenly divides x, x modulo y = 0
# alternate turns
# return name of winning player
# construct an array 
#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
# n --> number of towers
# m --> height of towers
# x --> height of tower
# y --> number of bricks they can remove

# # 
# #
# #
# #
# #
# #
## x % y = 0

def towerBreakers(n: int, m: int):

    # Write your code here
    if m == 1:
        return 2
    if m > 1:
        if n%2 == 0:
            return 2
        else:
            return 1

print(towerBreakers(n = 2, m = 6))