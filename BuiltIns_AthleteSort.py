'''
Problem statement:
https://www.hackerrank.com/challenges/python-sort-sort
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n,m = map(int,input().split())
    arr = []

    for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr.sort(key = lambda arr:arr[k])
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
