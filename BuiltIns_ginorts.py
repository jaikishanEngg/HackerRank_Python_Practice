'''
Problem statement:
https://www.hackerrank.com/domains/python/py-built-ins
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin
inp = stdin.readline()

lower_l = list()
upper_l = list()
odd_l = list()
even_l = list()

for e in list(inp):
    if(e.islower()):
        lower_l.append(e)
    elif(e.isupper()):
        upper_l.append(e)
    elif(e.isdigit()):
        if((int(e)%2) == 0):
            #even
            even_l.append(e)
        else:
            odd_l.append(e)

lower_l.sort()
upper_l.sort()
odd_l.sort()
even_l.sort()

print("".join(lower_l)+("".join(upper_l))+("".join(odd_l))+("".join(even_l)))
