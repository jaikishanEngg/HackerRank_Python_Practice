'''
Problem statement:
https://www.hackerrank.com/challenges/capitalize
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = s.split(" ")   #generate the list of words
    for i in range(len(l)):
        if(l[i] == ""):
            l[i] = ""
        elif(l[i] != ""):
            word = list(l[i])
            word[0] = word[0].upper()
            l[i] = "".join(word)
    return " ".join(l)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
