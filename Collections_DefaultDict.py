'''
Problem Statement:
https://www.hackerrank.com/challenges/defaultdict-tutorial
'''

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 12:52:37 2019

@author: Kish
"""

from collections import defaultdict
import sys

n,m = sys.stdin.readline().strip().split()
n = int(n)
m = int(m)


n_words = defaultdict(list)

for i in range(1,n+1):
    n_words[input()].append(i)

m_words = []

for i in range(1,m+1):
    m_words.append(input())

for i in m_words:
    if(i in n_words):
        for j in n_words[i]:
            print(j,end=" ")
        print("")
    else:
        print(-1)
    
