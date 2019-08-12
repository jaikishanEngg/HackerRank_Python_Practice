'''
Problem statement:
https://www.hackerrank.com/challenges/compress-the-string
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

import sys

n = list(map(int,list(sys.stdin.readline().strip())))
#print(n)

key = []
value = []

for k,v in groupby(n):
    key.append(k)
    value.append(list(v))

for i in value:
    print('('+str(len(i))+', '+str(i[0])+')', end=" ")
