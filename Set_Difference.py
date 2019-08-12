'''
Problem statement:
https://www.hackerrank.com/challenges/py-set-difference-operation
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
a = int(stdin.readline())
A = set(map(int,stdin.readline().split()))

b = int(stdin.readline())
B = set(map(int,stdin.readline().split()))

print(len(A.difference(B)))
