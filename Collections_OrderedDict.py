'''
Problem Statement:
https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
'''

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:50:22 2019

@author: Kish
"""

#OrderedDict()

from collections import OrderedDict
import sys
import re

n = int(sys.stdin.readline().strip())

ordered_dict = OrderedDict()

for i in range(n):
    x = sys.stdin.readline().strip()
    price = int(''.join(re.findall('\d+',x)))
    x = x.replace(str(price),'')
    x = x.strip()
    if(x in ordered_dict):
        ordered_dict[x] += price
    else:
        ordered_dict[x] = price        

for i in ordered_dict:
    print(i,ordered_dict[i])
