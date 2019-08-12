'''
Problem statement:
https://www.hackerrank.com/challenges/maximize-it/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from itertools import product

def evaluateExp(a,m):
    return sum([(x*x) for x in a]) % m

k,m = sys.stdin.readline().strip().split()
k = int(k)
m = int(m)
a = []
for i in range(k):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    temp.pop(0)
    a.append(temp)
 
#print(a)
maximum = 0
for i in product(*a):
    #print(i)
    maximum = max(maximum,evaluateExp(i,m))

print(maximum)