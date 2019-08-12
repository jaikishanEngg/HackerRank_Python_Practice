'''
Problem statement:
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

import sys

line = sys.stdin.readline().strip().split()
w = line[0]
n = int(line[1])

#print(list(combinations_with_replacement(w,n)))
output = []
for i in list(combinations_with_replacement(w,n)):
    output.append(''.join(sorted(i)))

output.sort()
for i in output:
    print(i)