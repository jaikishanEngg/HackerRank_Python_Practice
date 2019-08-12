'''
Problem statement:
https://www.hackerrank.com/challenges/itertools-permutations
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

import sys
sys.stdin.readline
line = sys.stdin.readline().strip().split()
w = line[0]
p = int(line[1])

a = list(permutations(w,p))
output = []
for i in a:
    output.append(''.join(i))
output.sort()

for i in output:
    print(i)
#print(output)