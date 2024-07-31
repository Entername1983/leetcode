#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    mapping = defaultdict(list)
    for row in grid:
        row = list(row)
        row.sort()
        for i, value in enumerate(row):
            mapping[i].append(value)
    for i in range(len(grid[0])):
        print(mapping[i])
        if mapping[i] != sorted(mapping[i]):
            return "NO"
    return "YES"


print(gridChallenge(['abc', 'ade', 'efg']))