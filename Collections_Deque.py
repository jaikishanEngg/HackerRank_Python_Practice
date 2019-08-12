'''
Problem Statement:
https://www.hackerrank.com/challenges/py-collections-deque/problem
'''

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:25:24 2019

@author: Kish
"""

#collections deque
from collections import deque
import sys
import re

d = deque()

def action(cmd,value):
    global d
    if(cmd == 'append'):
        d.append(value)
    elif(cmd == 'appendleft'):
        d.appendleft(value)
    elif(cmd == 'clear'):
        d.clear()
    elif(cmd == 'extend'):
        d.extend(value)
    elif(cmd == 'extendleft'):
        d.extendleft(value)
    elif(cmd == 'pop'):
        d.pop()
    elif(cmd == 'popleft'):
        d.popleft()
    elif(cmd == 'count'):
        d.count(value)
    elif(cmd == 'extend'):
        d.extend(value)
    elif(cmd == 'extendleft'):
        d.extendleft(value)
    elif(cmd == 'rotate'):
        d.rotate(value)

n = int(input())

for i in range(n):
    line = input()
    value = re.findall('\d+',line)
    if(not value):
        cmd = line
    else:
        cmd = line[:line.find(''.join(value))-1]
    #print(cmd)
    #print(value)
    value = ''.join(value)
    action(cmd.strip(),value)

for i in d:
    print(i,end=" ")

