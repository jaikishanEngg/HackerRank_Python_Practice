'''
Problem statement:
https://www.hackerrank.com/challenges/itertools-combinations
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
import sys

line = sys.stdin.readline().strip().split()
w = line[0]
n = int(line[1])

output = []

for i in range(1,n+1):
    a = list(combinations(w,i))
    for i in a:
        output.append(''.join(sorted(i)))
output.sort()
output.sort(key = lambda output:len(output))

for i in output:
    print(i)

