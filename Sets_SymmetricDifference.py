'''
Problem statement:
https://www.hackerrank.com/challenges/symmetric-difference
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
m = int(stdin.readline())
M = set(map(int,stdin.readline().split()))
n = int(stdin.readline())
N = set(map(int,stdin.readline().split()))

sym_diff = (M.union(N)).difference( M.intersection(N))
sym_diff = sorted(sym_diff)

for i in sym_diff:
    print(i)

