'''
Problem statement:
https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
a = sys.stdin.readline()
b = sys.stdin.readline()
c = sys.stdin.readline()
d = sys.stdin.readline()
a = int(a.strip())
b = int(b.strip())
c = int(c.strip())
d = int(d.strip())

print((a**b)+(c**d))
