'''
Problem statement:
https://www.hackerrank.com/challenges/python-power-mod-power
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
a = sys.stdin.readline()
b = sys.stdin.readline()
m = sys.stdin.readline()


a = int(a.strip())
b = int(b.strip())
m = int(m.strip())

print(pow(a,b))
print(pow(a,b,m))
