'''
Problem Statement:
https://www.hackerrank.com/challenges/collections-counter
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:29:26 2019

@author: Kish
"""

#Collections
from collections import Counter
import sys
n_shoes = sys.stdin.readline().strip()
l_size = list(map(int,sys.stdin.readline().strip().split()))
n_customers = int(sys.stdin.readline().strip())
items = dict(Counter(l_size))

total_price = 0

#print(items[4])
for i in range(n_customers):
    size,price = sys.stdin.readline().strip().split()
    size = int(size)
    price = int(price)
    if(size in items):
        if(items[size] == 1):
            items.pop(size)
        else:
            items[size] -= 1
        total_price += price
print(total_price)
            