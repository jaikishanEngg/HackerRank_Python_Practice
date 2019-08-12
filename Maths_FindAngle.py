'''
Problem statement:
https://www.hackerrank.com/challenges/find-angle/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan, degrees, sqrt, acos

ab = float(input())
bc = float(input())

ac = sqrt((ab*ab)+(bc*bc))
mc = ac/2


ang_abc = degrees(acos(ac/bc))

ang_mbc = ang_abc/2

print(ang_mbc)
