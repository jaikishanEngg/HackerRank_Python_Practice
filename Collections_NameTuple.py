'''
Problem Statement:
https://www.hackerrank.com/challenges/py-collections-namedtuple
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:45:30 2019

@author: Kish
"""
#namedtuple
from collections import namedtuple
import sys
n = int(input())

columns = sys.stdin.readline().strip()
#print(columns)
student = namedtuple('student',columns)
marks = 0
for i in range(n):
    x = sys.stdin.readline().strip().split()
    s = student._make(x)
    #print(s)
    #print(tuple(sys.stdin.readline().strip().split()))
    marks += float(s.MARKS)

print(marks/n)
