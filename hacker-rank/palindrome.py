#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
# start from both ends
# as long as both ends match, continue towards the middle.  If there is no match, ignore right letter and continue
# do the same for the left side
# if word is a palindrom without removing any letters return -1, if no solution do the same

def palindromeIndex(s):
    # Write your code here
    start = 0
    end = len(s) - 1
    if end == 0:
        return -1
    letter = None
    while start <= end:
        # print(f"Loop: start={start}, end={end}, letter={letter}, s[start]={s[start]}, s[end]={s[end]}")
        if s[start] == s[end]:
            start += 1
            end -= 1
        elif s[start] == s[end-1]:
            if letter is not None:
                return -1 ## we are removing a second letter which is illegal
            letter = end ## remove letter with index end - 1
            start += 1
            end -= 2
        elif s[start+1] == s[end]:
            if letter is not None:
                return -1
            letter = start
            start +=2
            end -= 1
        else:
            return -1
    if letter is None: ## it is already a palindrom
        return -1
    return letter
    
test_strings = [
    "racecar",        # -1
    "abca",           # 1
    "abcba",          # -1
    "radar",          # -1
    "abccba",         # -1
    "aab",            # 0
    "baab",           # 3
    "abcdefdba",      # -1
    "abc",            # -1
    "abcd",           # -1
    "a",              # -1
    "aa",             # -1
    "ab",             # -1
    "abcdefghgfedcba",# -1
    "abcdefghgfedcbax", # 15
    "abccbaab",       # -1
]

for s in test_strings:
    print(f"String: {s}, Result: {palindromeIndex(s)}")