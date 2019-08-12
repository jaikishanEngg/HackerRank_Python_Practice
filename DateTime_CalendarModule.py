'''
Problem Statement:
https://www.hackerrank.com/challenges/calendar-module
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
from sys import stdin
m,d,y = map(int,stdin.readline().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())