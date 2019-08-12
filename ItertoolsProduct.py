'''
Problem statement:
https://www.hackerrank.com/challenges/itertools-product/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
import sys

a = sys.stdin.readline().strip()
a = list(map(int,(a.split())))

b = sys.stdin.readline().strip()
b = list(map(int,(b.split())))

for i in list(product(a,b)):
    print(i,end=" ")

