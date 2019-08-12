'''
Problem statement:
https://www.hackerrank.com/challenges/exceptions/problem
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
for i in range(t):
    a,b = input().split()
    try:
        ans = int(a)/int(b)
        print(int(ans))
    except ZeroDivisionError as e:
        print('Error Code:','integer division or modulo by zero')
    except ValueError as v:
        print('Error Code:',v)
