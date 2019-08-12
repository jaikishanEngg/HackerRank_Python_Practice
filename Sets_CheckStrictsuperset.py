'''
Problem statement:
https://www.hackerrank.com/challenges/py-check-subset
'''

# Implement of a strictSuperSet function
from sys import stdin

A = set(map(int,stdin.readline().split()))

n = int(stdin.readline())

isStrictSuperSet = False

for i in range(n):
    temp_set = set(map(int, stdin.readline().split()))
    if(A.issuperset(temp_set)):
        if(A == temp_set):
            break
        else:
            if(i == n-1):
                isStrictSuperSet = True
            continue
    else:
        break

print(isStrictSuperSet)
