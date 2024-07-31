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
    s: list = s.split(":")
    if s[2][2:] == "PM":
        s[2] = s[2][0:2] # removing PM
        if s[0] != "12":
            s[0] = str(int(s[0]) + 12)
            if len(s[0]) == 1:
                s[0] = "0" + s[0][0]
    if s[2][2:] == "AM":
        s[2] = s[2][0:2]
        if s[0] == "12":
            s[0] = "00"
    s = (":").join(s)
    return s

if __name__ == '__main__':
    timeConversion("12:45:54PM")
