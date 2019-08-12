'''
Problem statement:
https://www.hackerrank.com/challenges/input
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

from sys import stdin

x, k = map(int,stdin.readline().split())

expression = stdin.readline()

print(eval(expression) == k)
