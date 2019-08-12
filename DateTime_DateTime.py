'''
Problem Statement:
https://www.hackerrank.com/challenges/python-time-delta
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
import time

# Complete the time_delta function below.
def time_delta(t1, t2):
    timedelta = t2 - t1
    return timedelta.days * 24 * 3600 + timedelta.seconds
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()
        date1 = datetime.strptime(t1)
        date2 = datetime.strptime(t2)

        delta = time_delta(date1, date2)

        fptr.write(delta + '\n')

    fptr.close()
