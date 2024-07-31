import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
# use unicode/ascii value ord(), char()
# track capitalizations

def caesarCipher(s, k):
    cipher = []
    
    for i in (s):
        ## handle non capitalized letters
        ascii_v = ord(i)
        if 96 < ascii_v < 123:
            cyphered_l = chr((((ascii_v + k) - 97) % 26) + 97)
            cipher.append(cyphered_l)
        ## handle capitalized letters\
        elif 64 < ascii_v < 91:
            cyphered_l = chr((((ascii_v + k) - 65) % 26) + 65)
            cipher.append(cyphered_l)
        else:
            cipher.append(chr(ascii_v))
    return "".join(cipher)
        ## ignore the rest, just add it to new array
    # Write your code here
caesarCipher("abcdefghijklmnopqrstuvwxyz", 2)