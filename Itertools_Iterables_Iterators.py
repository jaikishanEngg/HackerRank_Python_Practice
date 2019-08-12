'''
Problem statement:
https://www.hackerrank.com/challenges/iterables-and-iterators/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
import sys
n = sys.stdin.readline().strip()
l = sys.stdin.readline().strip().split()
k = sys.stdin.readline().strip()
n = int(n)
k = int(k)


total_pairs = 0
pairs = 0


com = list(combinations(l,k))
#print(com)

for i in com:
    if ('a' in i):
        pairs += 1

#print(len(com))
#print(pairs)
print(round(pairs/float(len(com)),12))

'''
for i in range(n-1):
    for j in range(i+1,n):
        total_pairs += 1
        if('a' in [l[i],l[j]]):
            pairs += 1

print(total_pairs)            
print(pairs)
print(pairs/total_pairs)
        

print(n)
print(l)
print(k)
'''