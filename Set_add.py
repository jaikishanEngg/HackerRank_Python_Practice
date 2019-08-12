'''
Problem statement:
https://www.hackerrank.com/challenges/py-set-add
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
count = int(stdin.readline())
s = set()
for i in range(count):
    s.add(stdin.readline().strip())

print(len(s))
#print(s)
