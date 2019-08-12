'''
Problem Statement:
https://www.hackerrank.com/challenges/piling-up
'''

#collections pile up
from collections import deque
import math

def pileup(l_items):
    left_pileup = 0
    right_pileup = 0
    for i in range(0, len(l_items)-1):
        if(l_items[i] >= l_items[i+1]):
            continue
        else:
            #print("i: ",i)
            left_pileup = 1
            for j in range(len(l_items)-1,i,-1):
                if(l_items[j] >= l_items[j-1]):
                    continue
                else:
                    right_pileup = 1
                    break
    if(left_pileup == 1 and right_pileup ==1):
        return "No"
    else:
        return "Yes"

t = int(input())
output =[]
#parse each test case
for i in range(t):
    c = int(input())
    l = list(map(int,input().split()))
    
    #test pile-up
    #print(l)
    output.append(pileup(l))
    
for i in output:
    print(i)
