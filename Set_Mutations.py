'''
Problem statement:
https://www.hackerrank.com/challenges/py-set-mutations
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin

n = int(stdin.readline())   #no.of elements

A = set(map(int,stdin.readline().split()))  #set

n_cmd = int(stdin.readline())   #no.of commands

for i in range(n_cmd):
    cmd, l = stdin.readline().split()
    l = int(l)
    temp = set(map(int,stdin.readline().split()))
    if(cmd == "intersection_update"):
        #intersection_update 
        A.intersection_update(temp)
    
    elif(cmd == "update"):
        #update
        A.update(temp)
    
    elif(cmd == "symmetric_difference_update"):
        #symmetric_difference_update
        A.symmetric_difference_update(temp)

    elif(cmd == "difference_update"):
        #difference_update
        A.difference_update(temp)

print(sum(A))
