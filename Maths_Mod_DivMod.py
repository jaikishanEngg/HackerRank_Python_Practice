'''
Problem statement:
https://www.hackerrank.com/challenges/python-mod-divmod
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = sys.stdin.readline()
d = sys.stdin.readline()

n = int(n.strip())
d = int(d.strip())

res = divmod(n,d)
print(res[0])
print(res[1])
print(res)
