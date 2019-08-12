'''
Problem statement:
https://www.hackerrank.com/challenges/designer-door-mat
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n,m = map(int,input().split())

i = 1
while(i<n):
    print((i*'.|.').center(m,'-'))
    i = i + 2

#welcome line
print('WELCOME'.center(m,'-'))
i = i - 2
while(i>0):
    print((i*'.|.').center(m,'-'))
    i = i - 2 
