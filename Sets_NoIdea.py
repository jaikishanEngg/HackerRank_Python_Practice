'''
Problem statement:
https://www.hackerrank.com/challenges/no-idea
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

from collections import Counter

i = 1

A = set()
B = set()
arr = list()

n,m = map(int,stdin.readline().split())
arr = map(int,stdin.readline().split())
arr_c = Counter(arr)

A = set(map(int,stdin.readline().split()))

B = set((map(int,stdin.readline().split())))


happiness = 0

for a in A:
    happiness += arr_c[a]
    

for b in B:
    happiness -= arr_c[b]

print(happiness)
