'''
Problem Statement:
https://www.hackerrank.com/challenges/most-commons
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    l = list(s)
    d = {}
    for i in l:
        d[i] = l.count(i)
    sorted_d = dict(sorted(d.items()))
    #print(type(sorted_d))
    #print(d)
    #print(d.items())
    #print(type(d))
    sorted_d = sorted(sorted_d.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_d)
    counter = 0
    output = {}
    for k, v in sorted_d:
        if(counter < 3):
            if(v in output):
                output[v].append(k)
            else:
                dl = []
                dl.append(k)
                output[v] = dl
        else:
            break
        counter += 1
    #print(output)
    #print(type(output))
    k = list(output.keys())
    v = list(output.values())
    for i in range(len(k)):
        val = k[i]
        keys = sorted(list(v[i]))
        #print(keys)
        #print(type(keys))
        for j in keys:
            print(j,val)
