'''
Problem statement:
https://www.hackerrank.com/challenges/any-or-all
'''

from sys import stdin
n = (stdin.readline()); ele_l = list(map(int,stdin.readline().split()))
print(all(i>0 for i in ele_l) and any(str(i)=="".join(reversed(str(i))) for i in ele_l) )
