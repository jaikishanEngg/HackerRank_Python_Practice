'''
Problem statement:
https://www.hackerrank.com/challenges/py-set-discard-remove-pop
'''

n = int(input())
s = set(map(int, input().split()))
if(n>0 and n<20):
    N = int(input())
    if(N>0 and N<20):
        for i in range(N):
            cmd = input().split()
            if(cmd[0] == "pop"):
                #pop
                s.pop()
            
            elif(cmd[0] == "remove"):
                #remove
                s.remove(int(cmd[1]))
            
            elif(cmd[0] ==  "discard"):
                s.discard(int(cmd[1]))

        print(sum(s))          
